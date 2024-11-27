# Transition from Atlas BI Connector to Atlas SQL - MongoDB Atlas


Docs Home / MongoDB Atlas / Create & Connect to Clusters / Connection Methods / BI Connector Transition from Atlas BI Connector to Atlas SQL On this page Atlas SQL Atlas SQL Limitations Atlas SQL Pricing Prepare to Transition to Atlas SQL Transition to Atlas SQL Troubleshoot Atlas SQL MongoDB recommends migrating from the Atlas BI Connector to the newer Atlas SQL Interface . Note The Atlas BI Connector and the on-premise BI Connector
are separate tools. This guide is about migrating from the
Atlas BI Connector, which MongoDB is phasing out. Atlas SQL Similar to the Atlas BI Connector,
Atlas SQL enables you to analyze data from Atlas clusters
using a variety of SQL-based tools, such as Tableau and Power BI. Compared to the Atlas BI Connector, Atlas SQL offers the
following advantages: You can read data from sources other than Atlas clusters
using the Atlas Data Federation infrastructure. You can set your schema. You pay only for your usage; you don't need a subscription. You can use custom MongoDB connectors for Tableau and Power BI. To learn more about Atlas SQL, see Query with Atlas SQL . Atlas SQL Limitations Atlas SQL is read-only. Atlas SQL is compatible only with the SQL 92 dialect;
other SQL dialects are not supported. All Atlas Data Federation limitations apply to Atlas SQL because it's a feature of Atlas Data Federation. Atlas SQL Pricing Atlas SQL incurs only Atlas Data Federation query costs and AWS transfer costs;
the Atlas SQL Interface itself is free to use. To learn more about the
cost of querying your federated database instance, see Data Federation Costs . Note Costs incurred by Atlas SQL queries appear on your invoice under
the federated database instance that you queried, either as "Data Processed" or
"Data Returned and Transferred" charges. Prepare to Transition to Atlas SQL To transition from the Atlas BI Connector to Atlas SQL, make sure your deployment
meets the following prerequisites: Additionally, MongoDB recommends that you generate a Transition Readiness Report to help plan your transition. Prerequisites An federated database instance containing queryable data. A MongoDB database user to connect to your federated database instance. Generate a Transition Readiness Report MongoDB provides an Atlas SQL Transition Readiness Tool to help you
plan your move from the Atlas BI Connector to the Atlas SQL Interface.
The tool generates a report based on your past Atlas BI Connector usage,
providing real-time schema analysis and suggestions and highlighting queries that need
syntax changes to run properly using Atlas SQL. To generate a report, you must provide the tool
with at least one of the following details: Your Atlas BI Connector logs, for query analysis. Your cluster URI , for schema analysis. You can analyze your queries, your schema, or both. 1 Download the Atlas SQL Readiness Report Tool. Select the tab for your operating system below and
download the executable file. MacOS (ARM) MacOS (Intel) Ubuntu Windows Download the MongoDB Atlas SQL Readiness Report Tool . Download the MongoDB Atlas SQL Readiness Report Tool . Download the MongoDB Atlas SQL Readiness Report Tool . Download the MongoDB Atlas SQL Readiness Report Tool . 2 Grant execution permission to the Readiness Report Tool. If the file doesn't have execution permission already, grant it. MacOS (ARM) MacOS (Intel) Ubuntu Windows chmod +x <executable-filename> chmod +x <executable-filename> chmod +x <executable-filename> 3 (Optional) Download and decompress your Atlas BI Connector logs. Providing your Atlas BI Connector logs enables the Readiness Report Tool to
report on the following information: Historical query data, such as volume and frequency. Query syntax that will fail in Atlas SQL. Collection fields with data types
unknown to relational databases. To download your Atlas BI Connector logs: In the Atlas UI, go to the Atlas cluster with the
BI connection that you want to analyze. From your cluster's options ( ),
select Download Logs . Download mongosql.gz . Create a new directory,
then decompress mongosql.gz into it. 4 (Optional) Copy your cluster URI. Providing your Atlas cluster URI enables the Readiness Report Tool
analyze your collection schemas and identify fields that
contain data types unknown to SQL tools. To find your cluster URI : In the Atlas UI, go to the
cluster with the collections that you
want to analyze. Click Connect . Select Shell from the list of connection options. Copy only your connection URI . The connection URI resembles: mongodb+srv://bicluster.example.mongodb.net/ .
Exclude the shell executable, mongosh , and any shell-specific
command line options. 5 Generate a report. In a terminal, run the Readiness Report Tool executable, providing
your downloaded logs or your cluster URI . You must include your database username. You must include either --input , --uri , or both.
If you include your URI , the Readiness Report Tool prompts you
for your database user password. You can specify an --output destination for your generated
report. If you don't, it's generated in your current
directory. You can specify a --resolver to choose a DNS resolver for network requests.
Possible values are: cloudflare , google , and quad9 . You can use --include or --exclude to narrow your list of namespaces.
Glob syntax is supported. By default, all namespaces are included. The --help option returns the full list of
Readiness Report Tool options: <executable-filename> --help Options: -i, --input <INPUT>        Sets the input file or directory to analyze BIC logs (optional). One of `--input` or `--uri` must be provided, or both -o, --output <OUTPUT>      Sets the output directory (optional). If not specified, the current directory is used --uri <URI>            The Atlas cluster URI to analyze schema (optional). One of `--input` or `--uri` must be provided, or both -u, --username <USERNAME>  Username for authentication (optional). This is required if the username and password is not provided in the URI --quiet                Enables quiet mode for less output --resolver <RESOLVER>  The specified resolver (optional) [possible values: cloudflare, google, quad9] --include <INCLUDE>    A list of namespaces to include (optional). If not provided, all namespaces are included. Glob syntax is supported --exclude <EXCLUDE>    A list of namespaces to exclude (optional). If not provided, no namespaces are excluded -h, --help                 Print help (see more with '--help') -V, --version              Print version The Readiness Report Tool organizes the output and generates a clickable index file
so you can easily navigate the report. Transition to Atlas SQL The underlying architecture of Atlas SQL is different from Atlas BI Connector
and you might need to adapt your schema or your queries. To transition to Atlas SQL, identify existing Atlas BI Connector
queries that fail on Atlas SQL and update your schema or their syntax
to fix them. Warning MongoDB recommends testing the full transition process in a sandbox environment
before you make changes to your production environment. Transitioning from the Atlas BI Connector
to Atlas SQL without adapting your schema or your queries
might cause breaking changes. 1 Enable Atlas SQL for your federated database instance. To learn more about enabling and using Atlas SQL,
see Enable the Atlas SQL Interface . 2 Connect to your data with the Atlas SQL Interface. To learn more about connecting with Atlas SQL,
see Connect Using the Atlas SQL Interface . 3 Test your queries. Test your queries with your new Atlas SQL connection to ensure
they run and return the results you expect. To learn more about querying with Atlas SQL,
see Query with Atlas SQL Statements . 4 View your schema and adapt it if necessary. To learn more about schemas in Atlas SQL, see Schema Management . 5 Adapt any failing queries. Some query syntax might need to be changed when you
transition from the Atlas BI Connector to Atlas SQL. To learn more about Atlas SQL query syntax, see Atlas SQL Language Reference . Troubleshoot Atlas SQL The following MongoDB resources can help you
troubleshoot your Atlas SQL configuration: The Community Forum Support Professional Services Your Customer Success team Back BI Connector Next System DSN
