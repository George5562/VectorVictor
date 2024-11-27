# Atlas User Roles - MongoDB Atlas


Docs Home / MongoDB Atlas / Configure UI Access / Authorization Atlas User Roles On this page Organization Roles Project Roles Atlas user roles define the actions Atlas users can perform in
organizations, projects, or both. Organization and project Owners can manage Atlas users and their roles within their respective
organizations and projects. You can apply these permissions only on the the
organization level or the project level . So,
you should carefully plan the hierarchy of your
organizations and projects. To learn more, see Cluster Management . Organization Roles Organization Role (UI) Organization Role (API) Description Organization Owner ORG_OWNER Grants root access to the organization, including: Project Owner access to all projects in
the organization, which grants database access, even if
added to a project with a non-Owner role. Privileges to administer organization settings. Privileges to add, modify, or delete Atlas users and database users within the organization. Privileges to delete the organization. Privileges to add, modify, or delete resource tags . All the privileges granted by the other organization roles
combined. Organization Project Creator ORG_GROUP_CREATOR Grants the following access: Privileges to create projects in the organization. Privileges granted by the Organization Member role. Organization Billing Admin ORG_BILLING_ADMIN Grants the following access: Privileges to administer billing information for the organization. Privileges granted by the Organization Member role. Privileges to create, edit, delete, acknowledge, and
unacknowledge billing alerts. Organization Billing Viewer ORG_BILLING_READ_ONLY Grants the following access: Privileges to view billing information for the organization. Privileges granted by the Organization Member role. Organization Read Only ORG_READ_ONLY Provides read-only access to the settings, users, and projects
in the organization. Organization Member ORG_MEMBER Provides read-only access to the settings and users
in the organization and the projects they belong to. Unlike Organization Read Only ,
an Organization Member can only access projects
they have been explicitly added to. For an Organization Member , within a project, the
user has the privileges as determined by the user's project role . If a user's project role is Project Owner , then the user can
add a new user to the project, which results in adding the
newly-added user to the organization as well (if the newly added
user is not already in the organization). Project Roles The following roles grant privileges within a project. Project Role (UI) Project Role (API) Description Project Owner GROUP_OWNER Grants the privileges to perform the following actions: Cluster Types . Manage project access and project settings . Manage IP Access List entries. Manage programmatic access to a project . You can grant API Keys access to a project with either an
organization or a project role. If your key has both the Organization Owner and Project Owner roles, it can access all projects in the organization. Manage database access for clusters within
the project. Retrieve process and audit logs for all clusters in the project. Manage backups for and restore data to all clusters in the project. Launch MongoDB Charts . Connect or disconnect Charts data sources . Create App Services apps . Add, modify, or delete resource tags . Project Cluster Manager GROUP_CLUSTER_MANAGER A user with the Project Cluster Manager role can
perform the following tasks: Grants access to edit, pause ,
and resume Atlas clusters. Test failover . The Project Cluster Manager role doesn't allow users
to: Create Atlas clusters. Access the Data Explorer . Retrieve process and audit logs. Project Stream Processing Owner GROUP_STREAM_PROCESSING_OWNER A user with the Project Stream Processing Owner role can perform the following tasks: Edit, pause ,
and resume Atlas clusters. Manage database access for
clusters within the project. Test failover . Access the Data Explorer . View stream processing instances Create a stream processing instance Delete a stream processing instance Edit a stream processing instance View Connections in the Connection Registry Add a Connection to the Connection Registry Modify a Connection from the Connection Registry Delete a Connection from the Connection Registry Download and manage stream processing instance audit logs. The Project Stream Processing Owner role doesn't
allow users to: Create Atlas clusters. Retrieve process and database audit logs. Project Data Access Admin GROUP_DATA_ACCESS_ADMIN Grants access to the Data Explorer . This
role also grants privileges of Project Read Only . Allows the user to perform the following Data Explorer actions: View, create, and drop databases, collections, and indexes. UI only : View, modify, and delete documents. You can't
read or write data using the Atlas Administration API. Retrieve process and audit logs for all clusters in the project. View the sample query field values in the Performance Advisor . View collection-level query latency with Namespace Insights . View query performance in the Query Profiler . View real-time performance in the Real-Time Performance Panel . View documents using the Search Tester . Launch MongoDB Charts . The Project Data Access Admin role does not grant
privileges to initiate backup or restore jobs. Project Data Access Read/Write GROUP_DATA_ACCESS_READ_WRITE Grants access to the Data Explorer ;
specifically, the privileges to perform the following through the Atlas UI : View and create databases and collections. UI only : View, modify, and delete documents.  You can't
read or write data using the Atlas Administration API. View indexes. Retrieve process and audit logs for all clusters in the
project. View the sample query field values in the Performance Advisor . View collection-level query latency with Namespace Insights . View query performance in the Query Profiler . View real-time performance in the Real-Time Performance Panel . View documents using the Search Tester . Launch MongoDB Charts . Project Data Access Read Only GROUP_DATA_ACCESS_READ_ONLY Grants access to the Data Explorer ;
specifically, to perform the following actions through the Atlas UI : View databases and collections. UI only : View documents. You can't read or write data
using the Atlas Administration API. View indexes. Retrieve process and audit logs for all clusters in the
project. View the sample query field values in the Performance Advisor . View collection-level query latency with Namespace Insights . View query performance in the Query Profiler . View real-time performance in the Real-Time Performance Panel . View documents using the Search Tester . Launch MongoDB Charts . Project Read Only GROUP_READ_ONLY Grants metadata view-only access to the project control pane for
all of the projects in the organization, including: all activity,
operational data, users, and user roles.
The user, however, cannot access the Data Explorer or retrieve process and audit logs. The user can view
cluster metric charts . Grants access to MongoDB Charts only if invited to the project by a Project Owner . The user, however,
cannot access data from Charts , unless the Project Owner also grants them data source access . Project Search Index Editor GROUP_SEARCH_INDEX_EDITOR Grants the privileges to perform the following actions: Create an Atlas Search Index . View an Atlas Search Index . Edit an Atlas Search Index . Delete an Atlas Search Index . Back Authorization Next Organization Access
