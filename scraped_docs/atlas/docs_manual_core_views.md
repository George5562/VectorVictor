# Views - MongoDB Manual v8.0


Docs Home / MongoDB Manual / Introduction / Databases & Collections Views On this page Use Cases Create and Manage Views Comparison with On-Demand Materialized Views Behavior Access Control A MongoDB view is a read-only queryable object whose contents are
defined by an aggregation pipeline on
other collections or views. MongoDB does not persist the view contents to disk. A view's content is
computed on-demand when a client queries the view. Note Disambiguation This page discusses standard views. For discussion of on-demand
materialized views, see On-Demand Materialized Views . To understand the differences between the view types, see Comparison with On-Demand Materialized Views . You can create materialized views in the UI for deployments hosted in MongoDB Atlas . Use Cases You can use views to: Create a view on a collection of employee data to exclude any
personally identifiable information (PII). Your application can query
the view for employee data that does not contain any PII . Create a view on a collection of sensor data to add computed fields
and metrics. Your application can use find operations to query the computed data. Create a view that joins two collections containing inventory and
order history. Your application can query the view without managing or
understanding the underlying pipeline. Create and Manage Views To learn how to create and manage views, see the following resources: Create a Materialized View in the MongoDB Atlas UI Create and Query a View Use a View to Join Two Collections Create a View with Default Collation Modify a View Remove a View Comparison with On-Demand Materialized Views MongoDB provides two different view types: standard views and on-demand materialized views . Both view types return the results
from an aggregation pipeline. Standard views are computed when you read the view, and are not stored
to disk. On-demand materialized views are stored on and read from disk. They
use a $merge or $out stage to update the saved
data. Note When using $merge , you can use change streams to watch for changes on the materialized view.
When using $out , you can't watch for changes on the
materialized view. Indexes Standard views use the indexes of the underlying collection. As a
result, you cannot create, drop or re-build indexes on a standard view
directly, nor get a list of indexes on the view. You can create indexes directly on on-demand materialized views because
they are stored on disk. Performance On-demand materialized views provide better read performance than
standard views because they are read from disk instead of computed as
part of the query. This performance benefit increases based on the
complexity of the pipeline and size of the data being aggregated. Behavior The following sections describe behavior specific to views. Read Only Views are read-only. Write operations on views return an error. Snapshot Isolation Views do not maintain timestamps of collection changes and do not
support point-in-time or snapshot read isolation. View Pipelines The view's underlying aggregation pipeline is subject to the 100
megabyte memory limit for blocking sort and blocking group
operations. Starting in MongoDB 6.0, pipeline stages that require more than 100
megabytes of memory to execute write temporary files to disk by
default. These temporary files last for the duration of the pipeline
execution and can influence storage space on your instance. In earlier
versions of MongoDB, you must pass { allowDiskUse: true } to
individual find and aggregate commands to enable this
behavior. Individual find and aggregate commands can override the allowDiskUseByDefault parameter by either: Using { allowDiskUse: true } to allow writing temporary files out
to disk when allowDiskUseByDefault is set to false Using { allowDiskUse: false } to prohibit writing temporary files
out to disk when allowDiskUseByDefault is set to true Note For MongoDB Atlas, it is recommended to configure storage auto-scaling to prevent
long-running queries from filling up storage with temporary files. If your Atlas cluster uses storage auto-scaling, the temporary files
may cause your cluster to scale to the next storage tier. Time Series Collections Time series collections are
writable non-materialized views. Limitations for views apply to time
series collections. For more information, see Time Series
Collection Limitations . You cannot create a view from a time series bucket collection
namespace (namely, a collection prefixed with system.buckets ). Warning Do not attempt to create a time series collection or view with the
name system.profile . MongoDB 6.3 and later versions return an IllegalOperation error if you attempt to do so. Earlier MongoDB
versions crash. Access Control If the deployment enforces authentication : To create a view, you must have the createCollection privilege on the database that the view is created. Additionally, if
you have the find privilege on the namespace of the
view you want to create, you must also have the find privilege on the
following resources: The source collection or view from which the new view is created. Any collections or views referenced in the view pipeline . To query a view, you must have the find privilege on the view
namespace. You don't need the find privilege on the source
collection or any namespaces referenced in the view pipeline. A user with the built-in readWrite role on the database
has the required privileges to run the listed operations. To grant the
required permissions, either: Create a user with the required role. Grant the role to an existing user . Back Databases & Collections Next Create & Query
