#!/opt/local/bin/python
# Physics Equation Graph
# Ben Payne <ben.is.located@gmail.com>
# 
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

connectionsDB=physgraf.parse_XML_file(db_path+'/connections_database.xml')
statementsDB=physgraf.parse_XML_file(db_path+'/statements_database.xml')

statement_punid_ary=[]
for these_statements in connectionsDB.getElementsByTagName('statement_punid'):
  statement_punid=physgraf.remove_tags(these_statements.toxml(encoding="ascii"),'statement_punid')
  statement_punid_ary.append(statement_punid)

#http://stackoverflow.com/questions/2870466/python-histogram-one-liner
hist = {}
for x in statement_punid_ary: hist[x] = hist.pop(x,0) + 1  # x=statement_punid

#http://stackoverflow.com/questions/613183/python-sort-a-dictionary-by-value
for w in sorted(hist, key=hist.get, reverse=True): # w=statement_punid
  latex=physgraf.convert_tpunid_to_latex(w,statementsDB,'statement')
  print (str(hist[w])+" "+w+" "+latex)
  
sys.exit("done")