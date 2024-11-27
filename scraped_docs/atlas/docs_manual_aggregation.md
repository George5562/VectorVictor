# Aggregation Operations - MongoDB Manual v8.0


Docs Home / MongoDB Manual Aggregation Operations On this page Aggregation Pipelines Single Purpose Aggregation Methods Aggregation operations process multiple documents and return computed
results. You can use aggregation operations to: Group values from multiple documents together. Perform operations on the grouped data to return a single result. Analyze data changes over time. To perform aggregation operations, you can use: Aggregation pipelines , which are
the preferred method for performing aggregations. Single purpose aggregation methods , which are simple but lack the
capabilities of an aggregation pipeline. You can run aggregation pipelines in the UI for deployments hosted in MongoDB Atlas . Aggregation Pipelines An aggregation pipeline consists of one or more stages that process documents: Each stage performs an operation on the input documents.
For example, a stage can filter documents, group documents, and
calculate values. The documents that are output from a stage are passed to the next
stage. An aggregation pipeline can return results for groups of documents.
For example, return the total, average, maximum, and minimum values. You can update documents with an aggregation pipeline if you use the stages
shown in Updates with Aggregation Pipeline . Note Aggregation pipelines run with the db.collection.aggregate() method do not modify documents in
a collection, unless the pipeline contains a $merge or $out stage. Aggregation Pipeline Example The following aggregation pipeline example contains two stages and returns the total
order quantity of medium size pizzas grouped by pizza name: db. orders . aggregate ( [ // Stage 1: Filter pizza order documents by pizza size { $match : { size : "medium" } } , // Stage 2: Group remaining documents by pizza name and calculate total quantity { $group : { _id : "$name" , totalQuantity : { $sum : "$quantity" } } } ] ) The $match stage: Filters the pizza order documents to pizzas with a size of medium . Passes the remaining documents to the $group stage. The $group stage: Groups the remaining documents by pizza name . Uses $sum to calculate the total order quantity for each
pizza name . The total is stored in the totalQuantity field
returned by the aggregation pipeline. For runnable examples containing sample input documents, see Complete Aggregation Pipeline Examples . Learn More About Aggregation Pipelines To learn more about aggregation pipelines, see Aggregation Pipeline . Single Purpose Aggregation Methods The single purpose aggregation methods aggregate documents from a single
collection. The methods are simple but lack the capabilities of an
aggregation pipeline. Method Description db.collection.estimatedDocumentCount() Returns an approximate count of the documents in a collection or
a view. db.collection.count() Returns a count of the number of documents in a collection or a
view. db.collection.distinct() Returns an array of documents that have distinct values for the
specified field. Back Tailable Cursors Next Aggregation Pipeline
