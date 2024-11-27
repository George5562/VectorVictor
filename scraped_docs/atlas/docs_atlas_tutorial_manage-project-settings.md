# Manage Project Settings - MongoDB Atlas


Docs Home / MongoDB Atlas / Configure UI Access / Authorization / Project Access Manage Project Settings On this page Required Access Manage Project Settings Required Access To view project settings, you must have Project Owner access to the project. Manage Project Settings Project settings apply to all the users in the project [ 1 ] . The Project ID displayed at the top of
the page is used by the Atlas Administration API and the Atlas CLI. Atlas CLI Atlas UI Update Project Settings To update settings for the project you specify using the
Atlas CLI, run the following command: atlas projects settings update [options] To learn more about the command syntax and parameters, see the
Atlas CLI documentation for atlas projects settings update . Tip See: Related Links Install the Atlas CLI Connect to the Atlas CLI View Project Settings To return the settings details for the project you specify using the
Atlas CLI, run the following command: atlas projects settings describe [options] To learn more about the command syntax and parameters, see the
Atlas CLI documentation for atlas projects settings describe . Tip See: Related Links Install the Atlas CLI Connect to the Atlas CLI Configure Custom DNS on AWS Use the following commands to configure custom DNS settings on AWS . Enable Custom DNS on AWS To enable custom DNS configuration for an Atlas cluster deployed to AWS using the
Atlas CLI, run the following command: atlas customDns aws enable [options] To learn more about the command syntax and parameters, see the
Atlas CLI documentation for atlas customDns aws enable . Tip See: Related Links Install the Atlas CLI Connect to the Atlas CLI Disable Custom DNS on AWS To disable custom DNS configuration for an Atlas cluster deployed to AWS using the
Atlas CLI, run the following command: atlas customDns aws disable [options] To learn more about the command syntax and parameters, see the
Atlas CLI documentation for atlas customDns aws disable . Tip See: Related Links Install the Atlas CLI Connect to the Atlas CLI Return the Details for Your Custom DNS on AWS To return the custom DNS configuration of an Atlas cluster deployed to AWS using the
Atlas CLI, run the following command: atlas customDns aws describe [options] To learn more about the command syntax and parameters, see the
Atlas CLI documentation for atlas customDns aws describe . Tip See: Related Links Install the Atlas CLI Connect to the Atlas CLI 1 In Atlas , go to the Project Settings page. If it's not already displayed, select the organization that
contains your desired project from the Organizations menu in the
navigation bar. If it's not already displayed, select your desired project
from the Projects menu in the navigation bar. Next to the Projects menu, expand the Options menu, then click Project Settings . The Project Settings page
displays. 2 View or modify project settings. You can set the following in the Atlas UI: Setting Description Project Name Sets your project's name. You must have the Project Owner role for the
project or the Organization Owner role for the
project's organization to edit the project name. Project Time Zone Sets your project's time zone. This affects the maintenance window
timezone and alerts, but not the timezone set for individual user
accounts. [ 1 ] There is also a User Preferences timezone, which
only affects the activity feed. Tags Allows you to label and organize your projects with key-value
pairs. To learn more, see Tags on Projects . Connect via Peering Only (GCP and Azure) Allows you to enable or disable connections between MongoDB
Atlas dedicated clusters and public IP addresses outside
of the peered VPC /VNet. You can only enable or disable this
setting when there are no active dedicated GCP or Azure clusters
in your project. IMPORTANT: This feature has been deprecated. Existing clusters can
continue to use this feature. Use both Standard and Private
IP for Peering connection strings to connect to your project.
These connection strings allow you to connect using both VPC /VNet Peering and allowed public IP addresses. To
learn more about support for multiple connection strings, see this FAQ . Using Custom DNS on AWS with VPC peering Allows you to expose a second connection string for your
dedicated Atlas clusters on AWS that resolves to private IPs. Enable this setting if you use custom DNS that cannot take
advantage of AWS built-in split-horizon DNS across a VPC peering
connection. service| displays this setting only when you enable network peering on AWS . Multiple Regionalized Private Endpoints Allows you to create more than one Private Endpoint in more than one region for multi-region and
global sharded clusters. Enable this setting if you want to connect to multi-region or
global sharded clusters using private endpoints. WARNING: Your connection strings to existing
multi-region and global sharded clusters change when you enable this
setting. You must update your applications to use the new connection strings.
This might cause downtime. You can enable this setting only if your Atlas project contains no non-sharded replica sets. You can't disable this setting if you have: More than one private endpoint in more than one region, or More than one private endpoint in one region and one private
endpoint in one or more regions. You can create only sharded clusters when you enable the regionalized
private endpoint setting. You can't create replica sets. Collect Database Specific Statistics Allows you to enable or disable the collection of database
statistics in cluster metrics . Set Preferred Cluster Maintenance Start Time Set which hour of the day that Atlas should start weekly
maintenance on your cluster. To learn more about cluster maintenance windows, see Configure Maintenance Window . Project Overview Sets the project landing page to Overview . Overview is a home page for Atlas that displays
modules for common Atlas actions. Atlas enables the Overview page by default. To
enable or disable the Overview page, you must have the Project Owner role. Real Time Performance Panel Allows you to see real time metrics from your MongoDB database. Data Explorer Allows you to query your database with an easy-to-use interface. IMPORTANT: When Data Explorer is disabled, you cannot: Terminate slow operations from the Real-Time Performance Panel . Create indexes from the Performance Advisor . You
can still view Performance Advisor recommendations, but you must
create those indexes from mongosh . Performance Advisor and Profiler Allows you to analyze database logs and receive performance
improvement recommendations. Schema Advisor Allows you to receive customized recommendations to optimize your
data model and enhance performance. Disable this setting to disable schema suggestions in the Performance Advisor and the Atlas UI . You can't access the Schema Advisor for
Serverless instances. Managed Slow Operations Dynamically sets the Slow Query Threshold based on execution times of operations across your cluster. Disable this feature to set a fixed, user-specified slow query
threshold. Enable Extended Storage Sizes Allows you to configure M40+ clusters with greater maximum
storage than the standard limit. Only clusters which meet the
following criteria support extended storage: The cluster is on Azure , AWS , or Google Cloud If the cluster is on Azure , it is configured in one of the
following regions that support extended storage The cluster is either General or Low-CPU class The cluster is single-region. Extended storage is a temporary solution for clusters that might
require additional storage capacity in the future. We recommend that
you enable sharding for long-term expanded
storage capacity. Delete Charts IMPORTANT: Deleting a MongoDB Charts instance deletes all data associated with
that instance including dashboards, data sources, and metadata. Once
the MongoDB Charts instance is deleted, this data cannot be recovered. Allows Project Owners to delete the MongoDB Charts instance associated with your project. This setting is
only visible if you have created a Charts instance for your
project. If you delete your linked MongoDB Charts instance, you can create a new MongoDB Charts instance for your project at any time. The newly created
instance does not retain any data from previously deleted instances. Delete Project The DELETE button allows you to delete a project. You can delete a project only if there are no Online
Archives for the clusters in the
project. [ 1 ] ( 1 , 2 ) To modify your user settings, click on your user name in the
upper-right hand corner and select Account . Back Projects Next Overview Landing Page
