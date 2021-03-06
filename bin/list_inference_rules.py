#!/opt/local/bin/python
# Physics Equation Graph
# Ben Payne <ben.is.located@gmail.com>
# 
# use: python sandbox/list_connection_sets.py
# input: 
# output: 

# current bugs:

import sys
import os
lib_path = os.path.abspath('lib')
sys.path.append(lib_path) # this has to proceed use of physgraph
db_path = os.path.abspath('databases')
sys.path.append(lib_path) # this has to proceed use of physgraph
import lib_physics_graph as physgraf
from xml.dom.minidom import parseString

inference_rulesDB=physgraf.parse_XML_file(db_path+'/inference_rules_database.xml')

for these_rules in inference_rulesDB.getElementsByTagName('infrule_name'):
  print(physgraf.remove_tags(these_rules.toxml(),'infrule_name'))
  
sys.exit("done")  