# $sortByCount (aggregation) - MongoDB Manual v8.0


Docs Home / MongoDB Manual / Aggregation Operations / Reference / Stages $sortByCount (aggregation) On this page Definition Considerations Behavior Example Definition $sortByCount Groups incoming documents based on the value of a specified
expression, then computes the count of documents in each distinct
group. Each output document contains two fields: an _id field
containing the distinct grouping value, and a count field
containing the number of documents belonging to that grouping or
category. The documents are sorted by count in descending order. The $sortByCount stage has the following prototype form: { $sortByCount :  < expression > } Field Description expression Expression to group by. You
can specify any expression except for a document literal. To specify a field path ,
prefix the field name with a dollar sign $ and enclose it
in quotes. For example, to group by the field employee ,
specify "$employee" as the expression. { $sortByCount : "$employee" } Although you cannot specify a document literal for the group
by expression, you can, however, specify a field or an
expression that evaluates to a document. For example, if employee and business fields are document fields,
then the following $mergeObjects expression,
which evaluates to a document, is a valid argument to $sortByCount : { $sortByCount : { $mergeObjects : [ "$employee" , "$business" ] } } However, the following example with the document literal
expression is invalid: { $sortByCount : { lname : "$employee.last" , fname : "$employee.first" } } Tip See also: Comparison/Sort Order Considerations $sortByCount and Memory Restrictions Starting in MongoDB 6.0, pipeline stages that require more than 100
megabytes of memory to execute write temporary files to disk by
default. These temporary files last for the duration of the pipeline
execution and can influence storage space on your instance. In earlier
versions of MongoDB, you must pass { allowDiskUse: true } to
individual find and aggregate commands to enable this
behavior. Individual find and aggregate commands can override the allowDiskUseByDefault parameter by either: Using { allowDiskUse: true } to allow writing temporary files out
to disk when allowDiskUseByDefault is set to false Using { allowDiskUse: false } to prohibit writing temporary files
out to disk when allowDiskUseByDefault is set to true Note For MongoDB Atlas, it is recommended to configure storage auto-scaling to prevent
long-running queries from filling up storage with temporary files. If your Atlas cluster uses storage auto-scaling, the temporary files
may cause your cluster to scale to the next storage tier. For additional details, see Aggregation Pipeline Limits . Behavior The $sortByCount stage is equivalent to the
following $group + $sort sequence: { $group : { _id : < expression > , count : { $sum : 1 } } } , { $sort : { count : - 1 } } Example Consider a collection exhibits with the following documents: { "_id" : 1 , "title" : "The Pillars of Society" , "artist" : "Grosz" , "year" : 1926 , "tags" : [ "painting" , "satire" , "Expressionism" , "caricature" ] } { "_id" : 2 , "title" : "Melancholy III" , "artist" : "Munch" , "year" : 1902 , "tags" : [ "woodcut" , "Expressionism" ] } { "_id" : 3 , "title" : "Dancer" , "artist" : "Miro" , "year" : 1925 , "tags" : [ "oil" , "Surrealism" , "painting" ] } { "_id" : 4 , "title" : "The Great Wave off Kanagawa" , "artist" : "Hokusai" , "tags" : [ "woodblock" , "ukiyo-e" ] } { "_id" : 5 , "title" : "The Persistence of Memory" , "artist" : "Dali" , "year" : 1931 , "tags" : [ "Surrealism" , "painting" , "oil" ] } { "_id" : 6 , "title" : "Composition VII" , "artist" : "Kandinsky" , "year" : 1913 , "tags" : [ "oil" , "painting" , "abstract" ] } { "_id" : 7 , "title" : "The Scream" , "artist" : "Munch" , "year" : 1893 , "tags" : [ "Expressionism" , "painting" , "oil" ] } { "_id" : 8 , "title" : "Blue Flower" , "artist" : "O'Keefe" , "year" : 1918 , "tags" : [ "abstract" , "painting" ] } The following operation unwinds the tags array and uses the $sortByCount stage to count the
number of documents associated with each tag: db. exhibits . aggregate ( [ { $unwind : "$tags" } , { $sortByCount : "$tags" } ] ) The operation returns the following documents, sorted in descending
order by count: { "_id" : "painting" , "count" : 6 } { "_id" : "oil" , "count" : 4 } { "_id" : "Expressionism" , "count" : 3 } { "_id" : "Surrealism" , "count" : 2 } { "_id" : "abstract" , "count" : 2 } { "_id" : "woodblock" , "count" : 1 } { "_id" : "woodcut" , "count" : 1 } { "_id" : "ukiyo-e" , "count" : 1 } { "_id" : "satire" , "count" : 1 } { "_id" : "caricature" , "count" : 1 } Back $sort Next $unionWith
