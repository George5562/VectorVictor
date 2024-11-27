# Aggregation Pipeline Limits - MongoDB Manual v8.0


Docs Home / MongoDB Manual / Aggregation Operations / Aggregation Pipeline Aggregation Pipeline Limits On this page Result Size Restrictions Number of Stages Restrictions Memory Restrictions Aggregation operations with the aggregate command have the
following limitations. Result Size Restrictions The aggregate command can either return a cursor or store
the results in a collection. Each document in the result set is subject
to the 16 megabyte BSON Document Size limit . If any single document exceeds the BSON Document Size
limit , the aggregation produces an error. The
limit only applies to the returned documents. During the pipeline
processing, the documents may exceed this size. The db.collection.aggregate() method returns a cursor by default. Number of Stages Restrictions MongoDB limits the number of aggregation pipeline stages allowed in a single
pipeline to 1000. If an aggregation pipeline exceeds the stage limit before or after being parsed,
you receive an error. Memory Restrictions Starting in MongoDB 6.0, the allowDiskUseByDefault parameter controls whether pipeline stages that require more than 100
megabytes of memory to execute write temporary files to disk by
default. If allowDiskUseByDefault is set to true , pipeline
stages that require more than 100 megabytes of memory to execute
write temporary files to disk by default. You can disable writing
temporary files to disk for specific find or aggregate commands using the { allowDiskUse: false } option. If allowDiskUseByDefault is set to false , pipeline
stages that require more than 100 megabytes of memory to execute
raise an error by default. You can enable writing temporary files to
disk for specific find or aggregate using
the { allowDiskUse: true } option. The $search aggregation stage is not restricted to
100 megabytes of RAM because it runs in a separate process. Examples of stages that can write temporary files to disk when allowDiskUse is true are: $bucket $bucketAuto $group $setWindowFields $sort when the sort operation is not supported by an
index $sortByCount Note Pipeline stages operate on streams of documents with each pipeline
stage taking in documents, processing them, and then outputting the
resulting documents. Some stages can't output any documents until they have processed all
incoming documents. These pipeline stages must keep their stage
output in RAM until all incoming documents are processed. As a
result, these pipeline stages may require more space than the 100 MB
limit. If the results of one of your $sort pipeline stages exceed
the limit, consider adding a $limit stage . The profiler log messages and diagnostic log
messages includes a usedDisk indicator if any aggregation stage wrote data to temporary files due
to memory restrictions . Back Optimization Next Sharded Collections
