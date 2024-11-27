# Query with Atlas SQL - MongoDB Atlas


Docs Home / MongoDB Atlas / Query Federated Data Query with Atlas SQL You can run SQL-style queries to search data on your federated database instances using the
Atlas SQL Interface. This capability allows you to visualize, graph, and
report on your Atlas data using relational business intelligence
tools such as Power BI and Tableau . Note Considerations Atlas SQL Interface only supports read operations. You cannot write
data to your Atlas cluster with the Atlas SQL Interface. Important MongoDB Minimum Version If some or all of your data comes from an Atlas cluster, you must
use MongoDB version 5.0 or greater for that cluster to
take advantage of Atlas SQL. The Atlas SQL Interface is available by default when you create a
federated database instance. Atlas Data Federation automatically creates collection schemas for Atlas SQL query
compilation and type inference. To learn more about the
schema, see Schema Management . To use the Atlas SQL Interface to run SQL queries, connect to your data
using a MongoDB SQL Driver or one of the BI tool custom connectors. To
learn more about the different connection options, see Connect . Components The Atlas SQL interface includes the following components: Federated Database Instance A federated database instance is a deployment of Atlas Data Federation. Each federated database instance contains virtual
databases and collections that map to data in your data stores. This
also provides a SQL schema and translates Atlas SQL queries between
your BI tool and your Atlas data. Custom Connector or SQL Driver A custom connector or a SQL driver provides a standard method to connect to a BI tool.
If you are using a BI tool, check which connections it supports. BI Tool A visualization and reporting tool, such as Power BI or Tableau. Pricing Querying your federated database instance with Atlas SQL incurs data transfer charges. See Data Federation Costs to
learn more about the costs associated with Atlas Data Federation. Get Started To start querying your Atlas data with Atlas SQL, enable the Atlas SQL Interface and connect to your data with a driver or BI tool of your choice. Back MQL Next Enable the Interface
