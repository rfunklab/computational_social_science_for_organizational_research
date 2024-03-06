# MGMT 8404, Computational Social Science for Organizational Research

Russell J. Funk, rfunk@umn.edu

This seminar will provide a general introduction to the field of computational social science, with an emphasis on applications for research on  organizations and management. The course will begin with an examination of the benefits of computational methods and their relationship to other, more established research approaches. Subsequently, we will consider several broad categories of topics, theories, and tools, including, for example, social network analysis, simulation, and natural language processing. In addition to providing an overview of the emerging field of computational social science, the course will help you gain hands on experience with using the methods discussed through lab demonstrations and a research project.

Check out the sessions folder for course content. 

To install required python packages, run:

```
pip install -r requirements.txt
```
After installing, you may also need to run
```
python -m spacy download en_core_web_lg
```
for some of the language-based notebooks to work. 

Note: Could not get Maximum Likelihood model with spreg to work in geography.ipynb notebook.
Removed pygraphviz requirement in networks notebook as it can be difficult to install on windows and machines without proper C++ compilers.
