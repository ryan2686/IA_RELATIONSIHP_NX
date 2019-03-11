

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
G = nx.DiGraph()


# SQL used to generate data for Relationship CSV File
    # SELECT RTRIM(LTRIM(IA.InvestorID)) as InvestorID, RTRIM(LTRIM(IA.InvestmentID)) as InvestmentID, RTRIM(LTRIM(IA.OwnershipPct)) as OwnershipPct
    # BKUSLP.HARMONY_TEST.DBO.IA_RELATIONSHIP IA, BKUSLP.HARMONY_TEST.DBO.ENTITY EN
    # WHERE IA.InvestorID = EN.ENTITYID AND EN.LEDGCODE <> 'CA'


csv_path = 'IA_RELATIONSHIP.csv'
edges = pd.read_csv(csv_path)

# added create_using parameter because graph wasn't rendering as directional
G = nx.from_pandas_edgelist(edges, source='InvestorID', target='InvestmentID', create_using=G)

# writing a dot file to be, later, rendered using GraphViz in a later iteration
write_dot(G, 'IA_RELATIONSHIP.dot')

# switched output from png to scalable vector graphics (svg) because svg files are clear at any scale
    # and svg files are searchable 
render('dot', 'svg', 'IA_RELATIONSHIP.dot', renderer= None, formatter= None, quiet= False)

#%%