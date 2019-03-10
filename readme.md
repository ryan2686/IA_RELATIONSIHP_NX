# First GitHub Repository - NetworkX

This repository is my first attempt at using GitHub, as well as one of my first foray into Python.  I've chosen to work with NetworkX since I'm interested in making a Directed Acyclic Graph (DAG) representing an ownership structure.  My final product, for this repository, will probably be an application that will create a DAG directly from a MSSQL server with no manual data pre-processing.  Later, I may attempt to build a web application that will be able to, interactively, modify the structure of the underlying data set by simply dragging and dropping nodes in the network.

I expect to have multiple iterations of this code.
     1.   Hard code ownership structure into my application.

     2.   Read my ownership structure into my application using a csv file.
          a.   I will initially prep my data in Excel to remove any leading or trailing spaces, then load in my code with the CSV module

          b.   I may, later, attempt to prep my data using a module such as Pandas
     
     3.   Read my ownership structure into my applicatoin directly from a MSSQL Server without the need for manual data pre-processing in Excel.