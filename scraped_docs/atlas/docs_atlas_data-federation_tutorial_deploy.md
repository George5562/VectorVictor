# Deploy a Federated Database Instance - MongoDB Atlas


Docs Home / MongoDB Atlas / Query Federated Data / Get Started Deploy a Federated Database Instance On this page Required Access Prerequisites Use the Feed Downstream Systems Wizard Use the Explore with Sample Data Wizard Use the Query Data Across Clusters Wizard Next Steps Estimated completion time: 15 minutes This part of the tutorial guides you through deploying a federated database instance using the following quickstart wizards in the Atlas UI: The Feed Downstream Systems wizard
helps you set up a federated database instance that exports data from your Atlas cluster, transforms the data into Parquet , CSV , BSON , or MongoDB Extended JSON , and copies the data to your AWS S3 buckets at specified intervals using Atlas Triggers . The Explore with Sample Data wizard helps
you set up a federated database instance loaded with sample data to demonstrate  how to
connect to the federated database instance and run queries. The Query Data Across Clusters wizard
helps you set up a federated database instance that accesses data from multiple Atlas clusters so you can run federated queries across collections from
all of them. To learn more about the storage configuration options, see Define Data Stores for a Federated Database Instance . Required Access To deploy a federated database instance, you must have Project Owner access to the project.
Users with Organization Owner access must add themselves as a Project Owner to the project before deploying a federated database instance. Prerequisites To complete this part of the tutorial, make sure you meet the following prerequisites: Create a MongoDB Atlas account, if you don't have one already. For the Feed Downstream Systems wizard, you need: The AWS CLI , configured to access your AWS account . Alternatively, you must have access to the AWS Management Console with permission to create IAM roles . An S3 bucket to store extracted data. At least one Atlas cluster with a database. For the Query Data Across Clusters wizard, you need: At least one Atlas cluster deployed in the same project you'll use for your federated database instance. At least one database collection. You can load sample data if you don't have collections already. Use the Feed Downstream Systems Wizard The Feed Downstream Systems wizard helps you set up a federated database instance that writes data from your Atlas cluster to your AWS S3 bucket continuously on a schedule. 1 Log in to MongoDB Atlas. 2 Select the Data Federation option on the left-hand navigation. 3 Create a federated database instance. Click the Create New Federated Database dropdown. Select Feed Downstream Systems . 4 Click Get Started . 5 Type a name for your federated database instance in the Federated Database Instance Name field and click Continue . Defaults to FederatedDatabaseInstance[n] . Once your federated database instance is
created, you can't change its name. 6 Specify your data sources. Select an Atlas cluster to use as a data source from the dropdown. By default, Atlas Data Federation adds all collections in this cluster. To use a subset of the data, click Specific Collections , expand the databases, and then select the collections that you want to add to your federated database instance. Tip To filter the databases and collections, enter text into
the Specific Collections field. The
dialog box displays only databases and collections with names
that match your search criteria. Click Continue . 7 Select an AWS IAM role for Atlas . You can select an existing AWS IAM role that Atlas is
authorized for from the role selection dropdown list or choose Authorize an AWS IAM Role to authorize a new role. If you selected an existing role that Atlas is authorized for,
proceed to the next step to list your AWS S3 buckets. If you are authorizing Atlas for an existing role or are creating
a new role, complete the following steps before proceeding to the
next step: From the dropdown, select Authorize an AWS IAM Role to authorize a new role or select an existing role. Use the AWS ARN and unique
External ID in the Role Authorization section to add Atlas to the trust
relationships of an existing or new AWS IAM role. In the Atlas UI, click one of the following: The Create new AWS IAM role shows how to
use the ARN and the unique External ID to add Atlas to the
trust relationships of a new AWS IAM role. Follow the steps
in the Atlas UI for creating a new role. To learn more, see Create New Role with the AWS CLI . When authorizing a new role, if you quit the workflow: Before validating the role, Atlas will not create the
federated database instance. You can go to the Atlas Integrations page to authorize a new role, then start
the procedure for deploying a federated database instance again when you have
the AWS IAM role ARN . After validating the role, Atlas will not create the
federated database instance. However, the role is available in the role selection
dropdown and can be used to create a federated database instance. You do not need
to authorize the role again. The Use existing AWS IAM role shows how to use the ARN and the unique External ID to add Atlas to the trust relationships of an existing AWS IAM role. Follow the steps in the Atlas UI for adding Atlas to the trust relationship to an existing role. To learn more,
see Add Trust Relationships to an Existing Role . Important If you modify your custom AWS role ARN in the future,
ensure that the access policy of the role includes the
appropriate access to the S3 resources for the federated database instance. To learn more, see Set Up Unified AWS Access and Create a Cloud Provider Access Role . Click Validate AWS IAM role . 8 Assign an access policy to your AWS IAM role. Enter the name of your S3 bucket. Follow the steps in the Atlas UI to assign an access policy to your AWS IAM role. Click Validate AWS S3 bucket access . Click Continue . 9 Schedule your data extractions. Schedule a trigger to continuously copy data from your Atlas cluster into your S3 bucket using $out in the Schedule Queries section. Specify how often you want to extract data from your Atlas cluster using the Repeat Once By dropdowns. Optional . Specify whether Atlas Data Federation must re-run the same query if it missed it for any reason. By default, this is disabled to allow Atlas Data Federation to re-run missed queries. Alternatively, to skip missed queries and not catch up, toggle on Skip Catch Up Events . Optional . Choose the format you want for your data when Atlas Data Federation writes it to your S3 bucket. Atlas Data Federation supports Parquet , CSV , BSON , and MongoDB Extended JSON . Specify the Max File Size to limit how large each file that Atlas Data Federation writes to your S3 bucket can be. For example, if you set Max File Size to 100 MB and a query returns 1 GB of data, Atlas Data Federation writes the query to your S3 bucket in 10 files, each 100 MBs. Enter the AWS prefix for your destination S3 bucket. Enter the name of the indexed date field in Date Field and specify the format of its value using the dropdown. Every collection that you want to copy downstream must have an indexed field that stores a timestamp as its value. Click Continue . 10 Click Create . Use the Explore with Sample Data Wizard The Explore with Sample Data wizard helps you set up a federated database instance loaded with sample data. 1 Log in to MongoDB Atlas. 2 Select the Data Federation option on the left-hand navigation. 3 Create a federated database instance. Click the Create New Federated Database dropdown. Select Explore with Sample Data . 4 Click Get Started . 5 Click Create . This federated database instance includes the following sample datasets that you can use to practice running queries : /airbnb/listingsAndReviews/{bedrooms int}/{review_scores.review_scores_rating int}/ This path references the airbnb dataset, which contains the
vacation home listing details and customer reviews. To learn more
about this dataset, see Sample AirBnB Listings Dataset . For this path, the federated database instance uses partitions optimized for queries on
the bedrooms field and review_scores.review_score_ratings fields. /analytics/accounts/{limit int}/ This path references the analytics dataset, which contains data
for a typical financial services application. To learn more about
this dataset, see Sample Analytics Dataset . For this path, the federated database instance uses partitions optimized for queries on
the limit field. /analytics/customers/{birthdate isodate}/ This data references the analytics dataset, which contains
collections for a typical financial services application. To learn
more about this dataset, see Sample Analytics Dataset . For this path, the federated database instance uses partitions optimized for queries on
the birthdate field. /analytics/transactions/{account_id int}/ This path references the analytics dataset, which contains
data for a typical finanacial services application. To learn more
about this dataset, see Sample Analytics Dataset . For this path, the federated database instance uses partitions optimized for queries on
the account_id field. /mflix/movies/{type string}/{year int}/ This path references the mflix dataset, which contains data on
movies and movie theaters. To learn more about this dataset, see Sample Mflix Dataset . For this path, the federated database instance uses partitions optimized for queries on
the type and year fields. /mflix/sessions.json This path references the mflix dataset, which contains data on
movies and movie theaters. To learn more about this dataset, see Sample Mflix Dataset . This path does not contain any partition attributes and so, for
queries against data in the collection, Data Federation searches all the
files in the collection. /mflix/theaters/{theaterId string}/{location.address.zipcode string}/ This path references the mflix dataset, which contains data on
movies and movie theaters. To learn more about this dataset, see Sample Mflix Dataset . For this path, the federated database instance uses partitions optimized for queries on
the theaterId and location.address.zipcode fields. /mflix/users.json This path references the mflix collection, which contains data
on movies and movie theaters. To learn more about this dataset, see Sample Mflix Dataset . This path does not contain any partition attributes and so, for
queries against data in the collection, the federated database instance searches all the
files in the collection. /nyc-yellow-cab-trips/{trip_start_isodate isodate}/{passenger_count int}/{fare_type string}/ This path references the nyc-yellow-cab-trips dataset, which
contains data on the trips, including trip date, fare, and number
of passengers. For this path, the federated database instance uses partitions optimized for queries on
the trip_start_isodate , passenger_count , and fare_type fields. Use the Query Data Across Clusters Wizard The Query Data Across Clusters wizard helps you set up a federated database instance that accesses data from multiple Atlas clusters. 1 Log in to MongoDB Atlas. 2 Select the Data Federation option on the left-hand navigation. 3 Create a federated database instance. Click the Create New Federated Database dropdown. Select Query Data Across Clusters . 4 Click Get Started . 5 Type a name for your federated database instance in the Federated Database Instance Name field and click Continue . Defaults to FederatedDatabaseInstance[n] . Once your federated database instance is
created, you can't change its name. 6 Specify the Atlas clusters to use as data sources. Select an Atlas cluster to use as a data source from the dropdown. Atlas only displays
clusters in your current Atlas project in this dropdown. Expand the databases and select the collections that you want to add to your federated database instance. Tip To filter the databases and collections, enter text into
the Specific collections field. The
dialog box displays only databases and collections with names
that match your search criteria. Optional . Expand the Cluster Read Preference settings to configure the following fields. Field Name Description Read Preference Mode Specifies the replica set member to which you want to
route the read requests. You can choose one of the
following from the dropdown: primary - to route all read requests to the replica set primary primaryPreferred - to route all read requests the replica set primary and to secondary members
only if primary is unavailable secondary - to route all read requests to the secondary members of the replica set secondaryPreferred - to route all read requests to the secondary members of
the replica set and the primary on sharded clusters only if secondary members are unavailable nearest - to route all read requests to random eligible replica
set member, irrespective of whether that member is a primary or secondary If you add an Atlas cluster as a store, the
default value is secondary . If you don't set anything in your federated database instance storage
configuration, the default value is nearest . To
learn more, see Read preference mode . TagSets Specifies the list of tags or tag
specification documents that contain name and value
pairs for the replica set member to which you want to
route read requests. To learn more, see Read
Preference Tag Sets . Maxstaleness Seconds Specifies the maximum replication lag, or
"staleness", for reads from secondaries. To learn
more, see Read Preference
maxStalenessSeconds . Click Add Atlas cluster and collection and repeat these steps for all the Atlas clusters that you want to use as data sources. Once you're done adding clusters, click Continue . 7 Click Create . Next Steps Now that your federated database instance is deployed, proceed to Configure Connection for Your Federated Database Instance .
