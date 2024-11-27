# $sampleRate (aggregation) - MongoDB Manual v8.0


Docs Home / MongoDB Manual / Aggregation Operations / Reference / Operators $sampleRate (aggregation) On this page Definition Behavior Examples Definition $sampleRate Matches a random selection of input documents. The number of
documents selected approximates the sample rate expressed as a
percentage of the total number of documents. The $sampleRate operator has the following syntax: { $sampleRate : < non-negative float > } Behavior The selection process uses a uniform random distribution. The sample
rate is a floating point number between 0 and 1, inclusive, which
represents the probability that a given document will be selected as it
passes through the pipeline. For example, a sample rate of 0.33 selects roughly one document in
three. This expression: { $match : { $sampleRate : 0.33 } } is equivalent to using the $rand operator as follows: { $match : { $expr : { $lt : [ { $rand : { } } , 0.33 ] } } } Repeated runs on the same data will produce different outcomes since
the selection process is non-deterministic. In general, smaller
datasets will show more variability in the number of documents
selected on each run. As collection size increases, the number of
documents chosen will approach the expected value for a uniform random
distribution. Note If an exact number of documents is required from each run, the $sample operator should be used instead of $sampleRate . Examples This code creates a small collection with 100 documents. N = 100 bulk = db. collection . initializeUnorderedBulkOp ( ) for ( i = 0 ; i < N ; i + + ) { bulk. insert ( { _id : i , r : 0 } ) } bulk. execute ( ) The $sampleRate operator can be used in a pipeline to select random
documents from the collection. In this example we use $sampleRate to select about one third of the documents. db. collection . aggregate ( [ { $match : { $sampleRate : 0.33 } } , { $count : "numMatches" } ] ) This is the output from 5 runs on the sample collection: { "numMatches" : 38 } { "numMatches" : 36 } { "numMatches" : 29 } { "numMatches" : 29 } { "numMatches" : 28 } Tip See also: $sample $rand Back $rtrim Next $second
