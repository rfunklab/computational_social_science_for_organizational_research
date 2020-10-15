# -*- coding: utf-8 -*-

"""download_sotu_data.py: Download State of the Union communications."""

__author__ = "Russell J. Funk"
__date__ = "March 25, 2020"

# built in modules
import re
import os
import sys
import datetime
import time

# other modules
import requests
from bs4 import BeautifulSoup
import pandas as pd

# configuration parameters
BASE_URL = "https://www.presidency.ucsb.edu"
SOTU_MESSAGES_INDEX_URL =  "/documents/app-categories/written-messages/presidential/state-the-union-messages?items_per_page=200"
SOTU_ADDRESSES_INDEX_URL = "/documents/app-categories/spoken-addresses-and-remarks/presidential/state-the-union-addresses?items_per_page=100"
OUTPUT_FOLDER = "sotu_data"
SLEEP_TIME = 1

def pull_index_content(index_url):
  """Pull content from index pages of SOTU communications (messages or addresses)."""

  # initialize a list to store the communications
  communications_list = []

  # open the index of communications
  communications_index_request = requests.get(index_url)

  # read the html for the index of communications
  communications_index_html = BeautifulSoup(communications_index_request.text, features="lxml")

  # loop over communications
  for communication_container in communications_index_html.find_all("div", typeof="sioc:Item foaf:Document"):
  
    # sanity checks
    assert len(communication_container.select("a")) == 2
    assert len(communication_container.select("span")) == 1
    
    # extract communication title
    communication_title = communication_container.select("a")[0].text

    # extract communication url
    communication_url = communication_container.select("a")[0]["href"]
    
    # extract communication president
    communication_president = communication_container.select("a")[1].text
    
    # extract communication date
    communication_date = communication_container.select("span")[0]["content"]
    communication_date = datetime.datetime.strptime(communication_date, "%Y-%m-%dT%H:%M:%S%z").date()
    
    communications_list.append({"title": communication_title,
                               "url": communication_url,
                               "president": communication_president,
                               "date": communication_date})
    
  # return the results
  return communications_list

def extract_communication_text(communication_url):
  """Pull the raw text of a SOTU communication (message or address)."""

  # open the communication page
  communication_request = requests.get(communication_url)

  # read the html for the communication page
  communication_html = BeautifulSoup(communication_request.text, features="lxml")

  # extract the container
  communication_container = communication_html.find_all("div", class_="field-docs-content")
  
  # sanity check
  assert len(communication_container) == 1
  
  # return the results
  return communication_container[0].text
  

def main():
 
  # initialize list of dictionaries to hold the combined results
  results = []
 
  # pull index data for messages  
  messages = pull_index_content(BASE_URL + SOTU_MESSAGES_INDEX_URL)
  
  # loop over messages
  for i, message in enumerate(messages):

    # pull message text
    message_text = extract_communication_text(BASE_URL + message["url"])
    
    # add message text to message data
    message["text"] = message_text
    
    # add message type to message data
    message["type"] = "message"
    
    # sleep to avoid overloading the server
    time.sleep(SLEEP_TIME)
    
    # print results
    print(message["title"],
          message["url"],
          message["president"],
          message["date"],
          message["type"],
          len(message["text"]))    
          
    # add message to combined results list
    results.append(message)

  # pull index data for addresses
  addresses = pull_index_content(BASE_URL + SOTU_ADDRESSES_INDEX_URL)
  
  # loop over addresses
  for i, address in enumerate(addresses):

    # pull address text
    address_text = extract_communication_text(BASE_URL + address["url"])
    
    # add address text to address data
    address["text"] = address_text
    
    # add address type to address data
    address["type"] = "address"
    
    # sleep to avoid overloading the server
    time.sleep(SLEEP_TIME)
    
    # print results
    print(address["title"],
          address["url"],
          address["president"],
          address["date"],
          address["type"],
          len(address["text"]))    
  
    # add address to combined results list
    results.append(address)

  # convert results to a pandas DataFrame
  results_df = pd.DataFrame(results)

  # save results as pickle
  results_df.to_pickle(OUTPUT_FOLDER + "/sotu_df.pickle")
  
  # save results as csv
  results_df.to_csv(OUTPUT_FOLDER + "/sotu_df.csv")

if __name__ == "__main__":
  main()