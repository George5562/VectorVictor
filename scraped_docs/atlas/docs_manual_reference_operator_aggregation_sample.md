# $sample (aggregation) - MongoDB Manual v8.0


Docs Home / MongoDB Manual / Aggregation Operations / Reference / Stages $sample (aggregation) On this page Definition Behavior Example Definition $sample Randomly selects the specified number of documents from the
input documents. $sample stage syntax: { $sample : { size : < positive integer N > } } N is the number of documents to randomly select.
Set N to an integer greater than or equal to 1 . Behavior If all of the following conditions are true, $sample uses a
pseudo-random cursor to select the N documents: $sample is the first stage of the pipeline. N is less than 5% of the total documents in the collection. Note You can't configure the threshold that $sample uses to
determine when to scan the entire collection. The thresholds is 5%.
If the size is greater than 5% of the total number of documents in
the collection, $sample performs a top-k sort by a generated random value.
The top-k sort could spill to disk if the sample documents are
larger than 100MB. The collection contains more than 100 documents. If any of the previous conditions are false, $sample : Reads all documents that are output from a preceding aggregation
stage or a collection scan. Performs a random sort to select N documents. Random sorts are
subject to the sort memory restrictions . Note Views are the result of aggregation
pipelines. When you use $sample on a view, MongoDB appends the stage
to the end of the view's aggregation pipeline syntax. Therefore, the $sample stage on a view is never the first stage and always
results in a collection scan. If you use $sample in a sharded cluster , each shard performs
the sample operation independently. mongos samples
the merged result of each shard's sample operation and returns the
requested number of documents. Example This section shows an aggregation pipeline example that uses the
following users collection: db. users . insertMany ( [ { _id : 1 , name : "dave123" , q1 : true , q2 : true } , { _id : 2 , name : "dave2" , q1 : false , q2 : false } , { _id : 3 , name : "ahn" , q1 : true , q2 : true } , { _id : 4 , name : "li" , q1 : true , q2 : false } , { _id : 5 , name : "annT" , q1 : false , q2 : true } , { _id : 6 , name : "li" , q1 : true , q2 : true } , { _id : 7 , name : "ty" , q1 : false , q2 : true } ] ) The following aggregation operation randomly selects 3 documents from the
collection: db. users . aggregate ( [ { $sample : { size : 3 } } ] ) The operation returns three random documents. Tip See also: $rand (aggregation) Back $replaceWith Next $search
