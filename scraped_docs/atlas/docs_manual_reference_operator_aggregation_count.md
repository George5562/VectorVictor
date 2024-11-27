# $count (aggregation) - MongoDB Manual v8.0


Docs Home / MongoDB Manual / Aggregation Operations / Reference / Stages $count (aggregation) On this page Definition Compatibility Syntax Behavior Examples Learn More Definition $count Passes a document to the next stage that contains a count of the
number of documents input to the stage. Note Disambiguation This page describes the $count aggregation pipeline stage.
For the $count aggregation accumulator, see $count
(aggregation accumulator) . Compatibility You can use $count for deployments hosted in the following
environments: MongoDB Atlas : The fully
managed service for MongoDB deployments in the cloud MongoDB Enterprise : The
subscription-based, self-managed version of MongoDB MongoDB Community : The
source-available, free-to-use, and self-managed version of MongoDB Syntax $count has the following syntax: { $count : < string > } <string> is the name of the output field which has the count
as its value. <string> must be a non-empty string, must not
start with $ and must not contain the . character. Behavior The return type is represented by the smallest type that can store
the final value of count: integer â long â double The $count stage is equivalent to the following $group and $project sequence: db. collection . aggregate ( [ { $group : { _id : null , myCount : { $sum : 1 } } } , { $project : { _id : 0 } } ] ) myCount is the output field that stores the count.
You can specify another name for the output field. If the input dataset is empty, $count doesn't return a result. Tip See also: db.collection.countDocuments() which wraps the $group aggregation stage with a $sum expression. Examples Create a collection named scores with these documents: db. scores . insertMany ( [ { "_id" : 1 , "subject" : "History" , "score" : 88 } , { "_id" : 2 , "subject" : "History" , "score" : 92 } , { "_id" : 3 , "subject" : "History" , "score" : 97 } , { "_id" : 4 , "subject" : "History" , "score" : 71 } , { "_id" : 5 , "subject" : "History" , "score" : 79 } , { "_id" : 6 , "subject" : "History" , "score" : 83 } ] ) The following aggregation operation has two stages: The $match stage excludes documents that have a score value of less than or equal to 80 to pass along the
documents with score greater than 80 to the next
stage. The $count stage returns a count of the remaining documents
in the aggregation pipeline and assigns the value to a field called passing_scores . db. scores . aggregate ( [ { $match : { score : { $gt : 80 } } } , { $count : "passing_scores" } ] ) The operation returns this result: { "passing_scores" : 4 } If the input dataset is empty, $count doesn't return a result. The
following example doesn't return a result because there are no documents
with scores greater than 99 : db. scores . aggregate ( [ { $match : { score : { $gt : 99 } } } , { $count : "high_scores" } ] ) Learn More db.collection.countDocuments() $collStats db.collection.estimatedDocumentCount() count db.collection.count() Back $collStats Next $currentOp
