# -*- coding: utf-8 -*-

"""download_patentsview_b10aa_network_data.py: Download patent collaboration network data
from patentsview for Big 10 Academic Alliance universities."""

__author__ = "Russell J. Funk"
__date__ = "January 15, 2020"

# built in modules
import re
import os
import sys
import json
import random

# other modules
import requests
import networkx as nx
from networkx.algorithms import bipartite
import probablepeople as pp
import gender_guesser.detector as gender

# configuration parameters
DATE_START = "2007-01-01"
DATE_END = "2012-12-31"
PER_PAGE = 9999
BASE_URL = "https://www.patentsview.org/api/patents/query"
OUTPUT_FOLDER = "network_data"
UNIVERSITIES = ({"assignee_id": "org_bc6lUv5STJ8mpLZRh4yW", "name": "MICHIGAN"},
                {"assignee_id": "org_RWqhrlYbdCwoizZdLB7H", "name": "RUTGERS"},
                {"assignee_id": "org_OcawIS6TgLu0is1l9KyA", "name": "OHIO_STATE"},
                {"assignee_id": "org_8179W6jy5dO8wP9aiWVg", "name": "IOWA"},
                {"assignee_id": "org_gCHgholcypwXAN387I44", "name": "INDIANA"},
                {"assignee_id": "org_Y0wfV2542ecBUzEQdRZu", "name": "UIUC"},
                {"assignee_id": "org_yCDhSk1vYQ6qDtcA0cg1", "name": "MARYLAND"},
                {"assignee_id": "org_q57vGQ9Wmc7mdlqv153r", "name": "MINNESOTA"},
                {"assignee_id": "org_MQgh8MW8okCbGstcb8HD", "name": "PENN_STATE"},
                {"assignee_id": "org_mAyELP7MbXqcUgR2h6rO", "name": "PURDUE"},
                {"assignee_id": "org_E5kQ39riXJrINxYNWeko", "name": "MICHIGAN_STATE"},
                {"assignee_id": "org_ead7SNUziKyKxgAS3wT2", "name": "NORTHWESTERN"},
                {"assignee_id": "org_hdlPV7lIsDdFQuYRkEPI", "name": "WISCONSIN"},
                {"assignee_id": "org_Q7lMwr3Yijk4x4uuqILo", "name": "NEBRASKA"}) 

def main():

  # initialize gender detector
  gender_detector = gender.Detector()

  # loop over universities
  for university in UNIVERSITIES:
  
    # format query
    params = {'q': '{"_and":[{"_gte":{"patent_date":"%s"}},{"_lt":{"patent_date":"%s"}},{"assignee_id":"%s"}]}' % (DATE_START, DATE_END, university["assignee_id"]),
              'f': '["patent_number","patent_date","patent_title","inventor_id","inventor_first_name","inventor_last_name", "assignee_organization", "cited_patent_number", "citedby_patent_number"]',
              'o': '{"per_page":%s}' % (PER_PAGE,) }

    # make api request
    request = requests.get(
      BASE_URL,
      params=params)

    # save response as dict
    data = json.loads(request.text)

    # pull patent data
    patent_data = data["patents"]
  
    # pull response information
    page_count = data["count"]
    total_patent_count = data["total_patent_count"]
  
    # initialize containers to hold data
    INVENTORS = {}
    EDGES_2MODE = set()
  
    # loop over patents to pull network data
    for d in patent_data:
  
      # extract data for each patent
      patent_number = d["patent_number"]
      patent_date = d["patent_date"]
      patent_title = d["patent_title"]
      inventors = d["inventors"]
      assignees = d["assignees"]
      cited_patents = d["cited_patents"]
      citedby_patents = d["citedby_patents"]
    
      # loop over inventors
      for inventor in inventors:
      
        # save inventor data
        if inventor["inventor_id"] not in INVENTORS:
        
          # get full name
          inventor_full_name = "%s %s" % (inventor["inventor_first_name"],
                                          inventor["inventor_last_name"])
         
          # get gender
          inventor_gender = None
          for inventor_first_name_token in inventor["inventor_first_name"].split():       
            if gender_detector.get_gender(inventor_first_name_token) in ("male", "mostly_male", "female", "mostly_female") and inventor_gender is None:
              inventor_gender = gender_detector.get_gender(inventor_first_name_token).replace("mostly_", "")
          if inventor_gender is None:
            inventor_gender = "UNKNOWN"                   
          assert inventor_gender in ("male", "female", "UNKNOWN")
          
          # add to dictionary
          INVENTORS[inventor["inventor_id"]] = {"inventor_first_name": inventor["inventor_first_name"], 
                                                "inventor_last_name": inventor["inventor_last_name"],
                                                "inventor_full_name": inventor_full_name,
                                                "inventor_gender": inventor_gender}
      
        # save edge data
        EDGES_2MODE.add((inventor["inventor_id"],
                              patent_number))

    # create a bipartite graph in networkx
    B = nx.Graph()
    B.add_nodes_from([n[0] for n in EDGES_2MODE], bipartite=0)
    B.add_nodes_from([n[1] for n in EDGES_2MODE], bipartite=1)
    B.add_edges_from(EDGES_2MODE)
  
    # project the network to a unipartite representation
    G = bipartite.generic_weighted_projected_graph(B, [n[0] for n in EDGES_2MODE])
  
    # add inventor attributes
    nx.set_node_attributes(G, INVENTORS)
    
    # set some graph attributes
    G.graph["assignee_id"] = university["assignee_id"]
    G.graph["name"]= university["name"]

    # get rid of node attributes we don't need
    for node in G.nodes:
      del G.nodes[node]["bipartite"]

    # impute gender randomly in proportion to distribution in the network
    nmale = len([i for i in G.nodes.data("inventor_gender") if i[1] == "male"])*["male"]
    nfemale = len([i for i in G.nodes.data("inventor_gender") if i[1] == "female"])*["female"]
    gender_distribution = nmale + nfemale
    for node in G.nodes(data=True):
      if G.nodes[node[0]]["inventor_gender"] == "UNKNOWN":
        G.nodes[node[0]]["inventor_gender"] = random.choice(gender_distribution)
    
    # export the graph
    path = os.path.join(os.path.realpath('.'), OUTPUT_FOLDER, "%s.graphml" % (G.graph["name"],))
    nx.write_graphml(G, path)

    # print
    for node in G.nodes(data=True):
      print(G.graph["assignee_id"], G.graph["name"], node)
      assert node[1]["inventor_gender"] in ("male","female")
    
if __name__ == "__main__":
  main()  
  
  
