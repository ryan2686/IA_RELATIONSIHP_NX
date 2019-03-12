

#%%

# Importing necessary modules: NetworkX to generate DAG, MatPlotLib to view DAG
import networkx as nx
from networkx.drawing import nx_pydot
from networkx.drawing.nx_pydot import write_dot
import matplotlib.pyplot as plt
import graphviz as gv
from graphviz import render
import pandas as pd


# Initiating the DiGraph and assigning it to the variable G
# I believe this line is actually pointless since nx.from_pandas_edgelist cleares this graphs contents
    # I could omit this and instead use create_using=nx.DiGraph() in from_pandas_edgelist function
G = nx.DiGraph()


# SQL used to generate data for Relationship CSV File
    # SELECT RTRIM(LTRIM(IA.InvestorID)) as InvestorID, RTRIM(LTRIM(IA.InvestmentID)) as InvestmentID, RTRIM(LTRIM(IA.OwnershipPct)) as label
    # BKUSLP.HARMONY_TEST.DBO.IA_RELATIONSHIP IA, BKUSLP.HARMONY_TEST.DBO.ENTITY EN
    # WHERE IA.InvestorID = EN.ENTITYID AND EN.LEDGCODE <> 'CA'


csv_path = 'IA_RELATIONSHIP.csv'
edges = pd.read_csv(csv_path)

# added create_using parameter because graph wasn't rendering as directional
G = nx.from_pandas_edgelist(edges, source='InvestorID', target='InvestmentID', edge_attr='label' , create_using=G)

# I finally got this to work thanks to:
    # https://stackoverflow.com/questions/20885986/how-to-add-dots-graph-attribute-into-final-dot-output
# This lines updates the aspect-ratio to make the rendered svg longer rather than wider
G.graph['graph']={'ratio':.25}

# writing a dot file to be, later, rendered using GraphViz in a later iteration
write_dot(G, 'IA_RELATIONSHIP.dot')

# switched output from png to scalable vector graphics (svg) because svg files are clear at any scale
    # and svg files are searchable 
    # This should also help later on because each node is explicitly ID'd in rendered HTML which will 
    # help when making drag 'n' drop application.
render('dot', 'svg', 'IA_RELATIONSHIP.dot', renderer= None, formatter= None, quiet= False)

#%%