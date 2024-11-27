# Configure MongoDB Support Access to Atlas Backend Infrastructure - MongoDB Atlas


Docs Home / MongoDB Atlas / Configure UI Access Configure MongoDB Support Access to Atlas Backend Infrastructure On this page Block Access at the Organization Level Grant Infrastructure Access to MongoDB Support for 24 hours Grant Access to MongoDB Support Only for Database Logs Grant Sync Data Access to MongoDB Support for 24 hours Revoke Temporary Infrastructure Access to MongoDB Support As an organization owner, you can set up your Atlas organization
so that MongoDB Production Support Employees, including Technical
Service Engineers, can only access your production servers with your
explicit permission. If an issue that requires MongoDB Support arises
and you want to grant 24-hour temporary infrastructure access to
MongoDB Support, you can grant access at the clusters
level. Granting temporary access doesn't give MongoDB Support access to
read your database, only the underlying MongoDB and Atlas Search
infrastructure, which should exclude sensitive information . You can also revoke temporary infrastructure access
at any time prior to the automatic 24-hour expiration. Important Blocking infrastructure access from MongoDB Support
may increase support issue response and resolution
time and negatively impact your cluster's availability. Block Access at the Organization Level You must be an organization owner to adjust this setting. 1 In Atlas , go to the Organization Settings page. If it's not already displayed, select your desired organization
from the Organizations menu in the
navigation bar. Click the Organization Settings icon next to the Organizations menu. The Organization Settings page displays. 2 Toggle the setting. Toggle the switch marked Block MongoDB Production
Support Employee Access to Atlas Infrastructure to the On position. Grant Infrastructure Access to MongoDB Support for 24 hours If an issue that requires MongoDB Support arises and you want to allow
MongoDB support
staff limited-time access to a cluster
within your organization,
you can do so with the following procedure. Atlas Administration API Atlas UI To grant limited-time access to MongoDB support staff to a cluster through
the Atlas Administration API, see Grant MongoDB employee cluster access for one cluster . You can specify CLUSTER_INFRASTRUCTURE for the grantType field in the request body schema. 1 In Atlas , go to the Clusters page for your project. If it's not already displayed, select the organization that
contains your desired project from the Organizations menu in the
navigation bar. If it's not already displayed, select your desired project
from the Projects menu in the navigation bar. If it's not already displayed, click Clusters in the
sidebar. The Clusters page displays. 2 Grant temporary access. Locate the cluster to which to grant access
from the list of clusters. Select the ellipsis icon ( ... ) to the right of the
cluster. Select Grant Temporary Infrastructure Access to MongoDB Support . Select Atlas cluster infrastructure and all cluster logs . Click Grant Access . Grant Access to MongoDB Support Only for Database Logs If an issue that requires MongoDB Support arises and you want to allow
MongoDB support staff limited-time access only to database logs within
your organization, you can do so with the following procedure. Atlas Administration API Atlas UI To grant access to MongoDB support staff to database logs through
the Atlas Administration API, see Grant MongoDB employee cluster access for one cluster . You can specify CLUSTER_DATABASE_LOGS for the grantType field in the request body schema. 1 Block MongoDB Support Access to Atlas Cluster Infrastructure and Logs. Select the organization that contains your desired project from the Organizations menu in the navigation bar. Select General Settings from the Settings menu in the navigation bar. Toggle Block MongoDB Support Access to Atlas Cluster Infrastructure and Logs to Yes . 2 Grant Temporary Infrastructure Access to MongoDB Support. Select your desired project from the Projects menu in the navigation bar. If the Clusters page is not already displayed, click Database in the sidebar. Select the ellipsis icon ( ... ) to the right of the cluster. Select Grant Temporary Infrastructure Access to MongoDB Support . Select Only database logs . Click Grant Access . IMPORTANT: You can grant MongoDB Support staff access only to database logs for 24 hours.
Any downloads in progress won't be interrupted if you revoke this access. Database audit logs are
not included in this access grant. Grant Sync Data Access to MongoDB Support for 24 hours The procedure you follow to grant sync data access to MongoDB Support
for 24 hours through the Atlas UI depends on whether your organization
owner has enabled Block MongoDB Support Access to Atlas Infrastructure . Select the tab applicable to your organization. Support Access Blocked Support Access Enabled If App Services sync is enabled and an issue that requires
MongoDB Support arises, you can
allow MongoDB support staff limited-time access to
App Services sync data in a cluster
within your organization with the following procedure. 1 In Atlas , go to the Clusters page for your project. If it's not already displayed, select the organization that
contains your desired project from the Organizations menu in the
navigation bar. If it's not already displayed, select your desired project
from the Projects menu in the navigation bar. If it's not already displayed, click Clusters in the
sidebar. The Clusters page displays. 2 Grant temporary access. Locate the cluster to which to grant access
from the list of clusters. Select the ellipsis icon ( ... ) to the right of the
cluster. Select Grant Temporary Infrastructure Access to MongoDB Support . A Grant Infrastructure Access to MongoDB Support for 24 hours modal appears. Select Grant Infrastructure and App Services Sync Data to
grant temporary infrastructure and sync data access to MongoDB
Support. When you successfully grant temporary access to MongoDB
Support, a new item appears in the dropdown that informs you
when your access expires. If App Services sync is enabled and an issue that requires
MongoDB Support arises, you can
allow MongoDB support staff limited-time access to
App Services sync data in a cluster
within your organization with the following procedure. 1 In Atlas , go to the Clusters page for your project. If it's not already displayed, select the organization that
contains your desired project from the Organizations menu in the
navigation bar. If it's not already displayed, select your desired project
from the Projects menu in the navigation bar. If it's not already displayed, click Clusters in the
sidebar. The Clusters page displays. 2 Grant temporary access. Locate the cluster to which to grant access
from the list of clusters. Select the ellipsis icon ( ... ) to the right of the
cluster. Select Grant Temporary Sync Data Access to MongoDB Support . When you successfully grant temporary access to MongoDB
Support, a new item appears in the dropdown that informs you
when your access expires. To grant access to MongoDB support staff to sync data through the
Atlas Administration API, see Grant MongoDB employee cluster
access for one cluster . You can specify CLUSTER_INFRASTRUCTURE_AND_APP_SERVICES_SYNC_DATA for
the grantType field in the request body schema. Revoke Temporary Infrastructure Access to MongoDB Support If you want to revoke access to a cluster
within your organization that has been granted
24-hour temporary infrastructure access,
you can do so with the following procedure. Important Temporary infrastructure access that is not revoked will automatically
expire at the end of 24 hours. Atlas displays a timer indicating
the amount of time left before 24-hour temporary infrastructure access expires. 1 In Atlas , go to the Clusters page for your project. If it's not already displayed, select the organization that
contains your desired project from the Organizations menu in the
navigation bar. If it's not already displayed, select your desired project
from the Projects menu in the navigation bar. If it's not already displayed, click Clusters in the
sidebar. The Clusters page displays. 2 Locate the cluster to which to grant access from the list of clusters. 3 Select the ellipsis icon ( ... ) to the right of the cluster. 4 Select Revoke Temporary Infrastructure Access to MongoDB Support . Important Ensure that all issues requiring MongoDB Support have been
addressed before revoking access. 5 Click Revoke Access . Click Revoke Access to revoke temporary
infrastructure access. To revoke 24-hour temporary infrastructure access from MongoDB support staff
through the Atlas Administration API, see Revoke granted MongoDB employee
cluster access for one cluster . Back Personalize the UI Next Migrate or Import Data
