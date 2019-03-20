#%%

""" Importing necessary modules: NetworkX to generate DAG, MatPlotLib to view DAG """
import networkx as nx
from networkx.drawing import nx_pydot
from networkx.drawing.nx_pydot import write_dot
import matplotlib.pyplot as plt
import graphviz as gv
from graphviz import render
import pandas as pd
import pyodbc

""" Initiating the DiGraph and assigning it to the variable G """
""" I believe this line is actually pointless since nx.from_pandas_edgelist cleares this graphs contents
        I could omit this and instead use create_using=nx.DiGraph() in from_pandas_edgelist function """
G = nx.DiGraph()


""" SQL used to generate data for Relationship CSV File """
    # SELECT RTRIM(LTRIM(IA.InvestorID)) as InvestorID, RTRIM(LTRIM(IA.InvestmentID)) as InvestmentID, RTRIM(LTRIM(IA.OwnershipPct)) as label
    # FROM BKUSLP.HARMONY_IMPL.DBO.IA_RELATIONSHIP2 IA, BKUSLP.HARMONY_IMPL.DBO.ENTITY EN
    # WHERE IA.InvestorID = EN.ENTITYID AND EN.LEDGCODE <> 'CA'

""" Connection string to be used by pyodbc to connect directly to the SQL database via linked server
        pyodbc will be used to connect to database and execute raw SQL statements """
conn_str = (
     r'DRIVER={SQL Server};'
     r'SERVER=BT4SQL11QA\sqlcol;'
     r'Trusted_Connection=Yes;'
     r'DATABASE=MRI_Source;'
)
""" Establishes a connection to above database """
conn = pyodbc.connect(conn_str)

""" Loads SQL query into pandas dataframe """
edges = pd.read_sql("SELECT RTRIM(LTRIM(IA.InvestorID)) as InvestorID, RTRIM(LTRIM(IA.InvestmentID)) as InvestmentID, RTRIM(LTRIM(IA.OwnershipPct)) as label FROM BKUSLP.HARMONY_IMPL.DBO.IA_RELATIONSHIP2 IA, BKUSLP.HARMONY_IMPL.DBO.ENTITY EN WHERE IA.InvestorID = EN.ENTITYID AND EN.LEDGCODE = 'BK'", conn)


""" The below two lines have been commented out because this script now connects directly to
        the database instead of dumping data into csv file via seperate query. """
# csv_path = 'IA_RELATIONSHIP.csv'
# edges = pd.read_csv(csv_path)

""" Added create_using parameter because graph wasn't rendering as directional """
G = nx.from_pandas_edgelist(edges, source='InvestorID', target='InvestmentID', edge_attr='label' , create_using=G)

""" I finally got this to work thanks to:
        https://stackoverflow.com/questions/20885986/how-to-add-dots-graph-attribute-into-final-dot-output """
""" This lines updates the aspect-ratio to make the rendered svg longer rather than wider """
G.graph['graph']={'ratio':.25}

""" Writing a dot file to be, later, rendered using GraphViz in a later iteration """
write_dot(G, 'IA_RELATIONSHIP.dot')

""" Switched output from png to scalable vector graphics (svg) because svg files are clear at any scale
        and svg files are searchable 
        This should also help later on because each node is explicitly ID'd in rendered HTML which will 
        help when making drag 'n' drop application. """
render('dot', 'svg', 'IA_RELATIONSHIP.dot', renderer= None, formatter= None, quiet= False)

#%%