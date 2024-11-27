# View Database Access History - MongoDB Atlas


Docs Home / MongoDB Atlas / Configure Security Features View Database Access History On this page Overview Required Access Procedure Note This feature is not available for any of the following deployments: Serverless instances M0 clusters M2/M5 clusters Flex clusters To learn more, see Limits . Overview Atlas parses the MongoDB database logs to collect a list of
authentication requests made against your clusters through the
following methods: mongosh Compass Drivers Authentication requests made with API Keys through the
Atlas Administration API are not logged. Atlas logs the following information for each authentication
request within the last 7 days: Field Description Timestamp The date and time of the authentication request. Username The username associated with the database user who made the
authentication request. For LDAP usernames, the UI displays the
resolved LDAP name. Hover over the name to see the full LDAP
username. IP Address The IP address of the machine that sent the authentication
request. Host The target server that processed the authentication request. Authentication Source The database that the authentication request was made against. admin is the authentication source for SCRAM-SHA users and $external for LDAP users. Authentication Result The success or failure of the authentication request. A reason
code is displayed for the failed authentication requests. Authentication requests are pre-sorted by descending timestamp with 25 entries per page. Logging Limitations If a cluster experiences an activity spike and generates an extremely large
quantity of log messages, Atlas may stop collecting and storing new logs
for a period of time. Note Log analysis rate limits apply only to the Performance Advisor UI,
the Query Insights UI, the Access Tracking UI, and the Atlas Search Query
Analytics UI. Downloadable log files are always
complete. If authentication requests occur during a period when logs are not
collected, they will not appear in the database access history. Required Access To view database access history, you must have Project Owner or Organization Owner access to Atlas . Procedure Atlas CLI Atlas Administration API Atlas UI To return the access logs for a cluster using the
Atlas CLI, run the following command: atlas accessLogs list [options] To learn more about the command syntax and parameters, see the
Atlas CLI documentation for atlas accessLogs list . Tip See: Related Links Install the Atlas CLI Connect to the Atlas CLI To view the database access history using the API, see Access Tracking . Use the following procedure to view your database access history
using the Atlas UI: 1 In Atlas , go to the Clusters page for your project. If it's not already displayed, select the organization that
contains your desired project from the Organizations menu in the
navigation bar. If it's not already displayed, select your desired project
from the Projects menu in the navigation bar. If it's not already displayed, click Clusters in the
sidebar. The Clusters page displays. 2 View the cluster's database access history. On the cluster card, click . Select View Database Access
History . or Click the cluster name. Click . Select View Database Access History . Back Auditing Next Configure UI Access
