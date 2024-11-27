# Set Up Database Auditing - MongoDB Atlas


Docs Home / MongoDB Atlas / Configure Security Features Set Up Database Auditing On this page Required Access Procedure Configure a Custom Auditing Filter Example Auditing Filters Note This feature is not available for any of the following deployments: Serverless instances M0 clusters M2/M5 clusters Flex clusters To learn more, see Limits . Database auditing lets administrators track system activity for
deployments with multiple users. Atlas administrators can select
the actions, database users, Atlas roles, and LDAP groups that they
want to audit. Atlas supports auditing most of the documented system event actions , with the following limitation: The Atlas audit logs don't track user creation or modification
events because Atlas performs these operations directly in the admin database. Important Performing a Full Database Audit Due to this limitation, you must use a combination of audit logs,
the mongodb.log , and the Project Activity Feed to perform a full audit. The authCheck event action logs authorization attempts by users
trying to read from and write to databases in the clusters in your
project. Atlas audits the following specific commands: authCheck Reads authCheck Writes aggregate aggregate mapReduce mapReduce distinct delete count findAndModify geoNear insert geoSearch update group resetError find getLastError getMore getPrevError Atlas implements the authCheck event action as the following
four separate actions: Event Action Description authChecksReadFailures authCheck event action for all failed reads with the auditAuthorizationSuccess parameter set to false. This event action is the default for
read-related event actions. authChecksReadAll authCheck event action for all reads, both sucesses and
failures.
This event action is the same as authChecksReadFailures , but
with the auditAuthorizationSuccess parameter set to true. WARNING: If you enable auditAuthorizationSuccess ,
you might severely impact cluster performance. Enable
this option with caution. authChecksWriteFailures authCheck event action for all failed writes with the auditAuthorizationSuccess parameter set to false. This event action is the default for
write-related event actions. authChecksWriteAll authCheck event action for all writes, both successes and
failures. This event action is the same as authChecksWriteFailures , but with the auditAuthorizationSuccess parameter set to true. WARNING: If you enable auditAuthorizationSuccess ,
you might severely impact cluster performance. Enable
this option with caution. To learn about how MongoDB writes audit events to disk, see Audit Guarantee in the MongoDB Manual. Required Access To configure audit logs, you must have Project Owner access to the project that
you want to update or Organization Owner access
to the organization that contains the project that you want to update. Procedure Note To learn about best practices for auditing the actions of temporary
database users, see Audit Temporary Database Users . Use the following procedure to set up database auditing: 1 In Atlas , go to the Advanced page for your project. If it's not already displayed, select the
organization that contains your project from the Organizations menu in the navigation bar. If it's not already displayed, select your project
from the Projects menu in the navigation bar. In the sidebar, click Advanced under
the Security heading. The Advanced page displays. 2 Toggle the button next to Database Auditing to On . 3 Confirm that you want to audit authentication failures. By default, Atlas logs the failed authentication attempts of both
known and unknown users in the audit log of the primary node. 4 Select the database users, Atlas roles, and LDAP groups whose actions you want to audit in Select users and roles . Alternatively, click Use Custom JSON Filter to manually
enter an audit filter as a JSON string. For more information on configuring custom audit
filters in Atlas , see Configure a Custom Auditing Filter . 5 Select the event actions that you want to audit in Select actions to audit . Note Deselecting the authenticate action prevents Atlas from
auditing authentication failures. Note When selecting the authorization success granularity of auditing for the authCheck event action, Atlas does
not support different selections for reads and writes. For example,
you may not select Successes and Failures for authCheck Reads and Failures for authCheck Writes . If you
select both authCheck Reads and authCheck Writes , Atlas automatically applies your selected granularity to both. 6 Click Save . To retrieve the audit logs in Atlas , see MongoDB Logs . To retrieve the audit logs using the API, see Logs . Configure a Custom Auditing Filter Note This feature is not available for any of the following deployments: Serverless instances M0 clusters M2/M5 clusters Flex clusters To learn more, see Limits . Atlas supports specifying a JSON-formatted audit filter
for customizing MongoDB Auditing . Custom audit filters let users forgo the managed
Atlas UI auditing filter builder in favor of hand-tailored granular control of event auditing. Atlas checks only that the custom filter uses valid
JSON syntax, and doesn't validate or test the filter's functionality. The audit filter document must resolve to a query that matches one or
more fields in the audit event message .
The filter document can use combinations of query operators and equality
conditions to match the desired audit messages. To view example auditing filters, see Example Auditing Filters . To learn more about configuring MongoDB
auditing filters, see Configure Audit Filter . Important Atlas uses a rolling upgrade strategy
for enabling or updating audit configuration settings across all
clusters in the Atlas project. Rolling upgrades require at least
one election per replica set. To learn more about testing application resilience to replica set
elections, see Test Primary Failover . To learn more
about how Atlas provides high availability, see Atlas High Availability . Procedure 1 In Atlas , go to the Advanced page for your project. If it's not already displayed, select the
organization that contains your project from the Organizations menu in the navigation bar. If it's not already displayed, select your project
from the Projects menu in the navigation bar. In the sidebar, click Advanced under
the Security heading. The Advanced page displays. 2 Toggle the button next to Database Auditing to On . 3 Select Use Custom JSON Filter . 4 Enter your audit filter into the text box. 5 Toggle Audit authorization successes . Warning Enabling Audit authorization successes can severely
impact cluster performance. Enable this option with caution. For audit filters specifying the authCheck action type ,
by default the
auditing system logs only authorization
failures for any specified param.command . Enabling Audit authorization successes directs the auditing
system to also log authorization successes. For more information,
see auditAuthorizationSuccess 6 Click Save . Edit a Custom Auditing Filter You can edit your filter at any time: 1 In Atlas , go to the Advanced page for your project. If it's not already displayed, select the
organization that contains your project from the Organizations menu in the navigation bar. If it's not already displayed, select your project
from the Projects menu in the navigation bar. In the sidebar, click Advanced under
the Security heading. The Advanced page displays. 2 Edit the filter. Under Database Auditing Configure Your Auditing Filter , click Use Custom JSON Filter . Make the required changes. Click Save . View Your Custom Auditing Filter Atlas CLI Atlas UI To return the auditing configuration for the specified project using the
Atlas CLI, run the following command: atlas auditing describe [options] To learn more about the command syntax and parameters, see the
Atlas CLI documentation for atlas auditing describe . Tip See: Related Links Install the Atlas CLI Connect to the Atlas CLI To view your custom auditing filter in the Atlas UI: 1 In Atlas , go to the Advanced page for your project. If it's not already displayed, select the
organization that contains your project from the Organizations menu in the navigation bar. If it's not already displayed, select your project
from the Projects menu in the navigation bar. In the sidebar, click Advanced under
the Security heading. The Advanced page displays. 2 View your filter. Your custom auditing filter displays under Database Auditing . Example Auditing Filters Use the following example auditing filters for guidance in constructing
your own filters. Important These examples are not intended for use in
production environments, nor are they a replacement for familiarity
with the MongoDB Auditing Documentation . Audit all authentication events for known users { "atype" : "authenticate" } Audit all authentication events for known users and authentication failures for unknown users { "$or" : [ { "users" : [ ] } , { "atype" : "authenticate" } ] } Note The authenticate action is required to log authentication
failures from known and unknown users. Audit authentication events for the "myClusterAdministrator" user { "atype" : "authenticate" , "param" : { "user" : "myClusterAdministrator" , "db" : "admin" , "mechanism" : "SCRAM-SHA-256" } } Audit unauthorized attempts at executing the selected commands { "atype" : "authCheck" , "param.command" : { "$in" : [ "insert" , "update" , "delete" ] } } Back Google Cloud KMS Next Access History
