# $bucketAuto (aggregation) - MongoDB Manual v8.0


Docs Home / MongoDB Manual / Aggregation Operations / Reference / Stages $bucketAuto (aggregation) On this page Definition Considerations Behavior Example Definition $bucketAuto Categorizes incoming documents into a specific number of groups,
called buckets, based on a specified expression. Bucket boundaries
are automatically determined in an attempt to evenly distribute the
documents into the specified number of buckets. Each bucket is represented as a document in the output. The document
for each bucket contains: An _id object that specifies the bounds of the bucket. The _id.min field specifies the inclusive lower bound for the
bucket. The _id.max field specifies the upper bound for the bucket.
This bound is exclusive for all buckets except the final
bucket in the series, where it is inclusive. A count field that contains the number of documents in the
bucket. The count field is included by default when the output document is not specified. The $bucketAuto stage has the following form: { $bucketAuto : { groupBy : < expression > , buckets : < number > , output : { < output1 > : { < $accumulator expression > } , ... } granularity : < string > } } Field Type Description groupBy expression An expression to group documents
by. To specify a field path ,
prefix the field name with a dollar sign $ and enclose it in
quotes. buckets integer A positive 32-bit integer that specifies the number of buckets into
which input documents are grouped. output document Optional. A document that specifies the fields to include in
the output documents in addition to the _id field. To
specify the field to include, you must use accumulator
expressions : < outputfield1 > : { < accumulator > : < expression1 > } , ... The default count field is not included in the output document
when output is specified. Explicitly specify the count expression as part of the output document to include it: output : { < outputfield1 > : { < accumulator > : < expression1 > } , ... count : { $sum : 1 } } granularity string Optional. A string that specifies the preferred number series to use to
ensure that the calculated boundary edges end on preferred
round numbers or their powers of 10. Available only if the all groupBy values are numeric and
none of them are NaN . The supported values of granularity are: "R5" "R10" "R20" "R40" "R80" "1-2-5" "E6" "E12" "E24" "E48" "E96" "E192" "POWERSOF2" Considerations $bucketAuto and Memory Restrictions The $bucketAuto stage has a limit of 100 megabytes of RAM.
By default, if the stage exceeds this limit, $bucketAuto returns an error. To allow more space for stage processing, use the allowDiskUse option to enable aggregation
pipeline stages to write data to temporary files. Tip See also: Aggregation Pipeline Limits Behavior There may be less than the specified number of buckets if: The number of input documents is less than the specified number of
buckets. The number of unique values of the groupBy expression is less
than the specified number of buckets . The granularity has fewer intervals than the number of buckets . The granularity is not fine enough to evenly distribute documents
into the specified number of buckets . If the groupBy expression refers to an array or document, the
values are arranged using the same ordering as in $sort before determining the bucket boundaries. The even distribution of documents across buckets depends on the
cardinality, or the number of unique values, of the groupBy field. If
the cardinality is not high enough, the $bucketAuto stage may not evenly
distribute the results across buckets. Granularity The $bucketAuto accepts an optional granularity parameter which
ensures that the boundaries of all buckets adhere to a specified preferred number series .
Using a preferred number series provides more control on where the
bucket boundaries are set among the range of values in the groupBy expression. They may also be used to help logarithmically and evenly
set bucket boundaries when the range of the groupBy expression
scales exponentially. Renard Series The Renard number series are sets of numbers derived by taking either
the 5 th , 10 th , 20 th ,
40 th , or 80 th root of 10, then including
various powers of the root that equate to values between 1.0 to 10.0
(10.3 in the case of R80 ). Set granularity to R5 , R10 , R20 , R40 , or R80 to
restrict bucket boundaries to values in the series. The values of the
series are multiplied by a power of 10 when the groupBy values are
outside of the 1.0 to 10.0 (10.3 for R80 ) range. Example The R5 series is based off of the fifth root of 10, which is
1.58, and includes various powers of this root (rounded) until 10 is
reached. The R5 series is derived as follows: 10 0/5 = 1 10 1/5 = 1.584 ~ 1.6 10 2/5 = 2.511 ~ 2.5 10 3/5 = 3.981 ~ 4.0 10 4/5 = 6.309 ~ 6.3 10 5/5 = 10 The same approach is applied to the other Renard series to offer finer
granularity, i.e., more intervals between 1.0 and 10.0 (10.3 for R80 ). E Series The E number series are similar to the Renard series in that they subdivide the
interval from 1.0 to 10.0 by the 6 th ,
12 th , 24 th , 48 th ,
96 th , or 192 nd root of ten with a
particular relative error. Set granularity to E6 , E12 , E24 , E48 , E96 , or E192 to restrict bucket boundaries to values in the series. The
values of the series are multiplied by a power of 10 when the groupBy values are outside of the 1.0 to 10.0 range. To learn more
about the E-series and their respective relative errors, see preferred number series . 1-2-5 Series The 1-2-5 series behaves like a three-value Renard series , if such a series existed. Set granularity to 1-2-5 to restrict bucket boundaries to
various powers of the third root of 10, rounded to one significant
digit. Example The following values are part of the 1-2-5 series:
0.1, 0.2, 0.5, 1, 2, 5, 10, 20, 50, 100, 200, 500, 1000, and so
on... Powers of Two Series Set granularity to POWERSOF2 to restrict bucket boundaries to
numbers that are a power of two. Example The following numbers adhere to the power of two Series: 2 0 = 1 2 1 = 2 2 2 = 4 2 3 = 8 2 4 = 16 2 5 = 32 and so on... A common implementation is how various computer components, like
memory, often adhere to the POWERSOF2 set of preferred numbers: 1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, and so on.... Comparing Different Granularities The following operation demonstrates how specifying different values
for granularity affects how $bucketAuto determines bucket
boundaries.  A collection of things have an _id numbered from
0 to 99: { _id : 0 } { _id : 1 } ... { _id : 99 } Different values for granularity are substituted into the following
operation: db. things . aggregate ( [ { $bucketAuto : { groupBy : "$_id" , buckets : 5 , granularity : < granularity > } } ] ) The results in the following table demonstrate how different values for granularity yield different bucket boundaries: Granularity Results Notes No granularity { "_id" : { "min" : 0, "max" : 20 }, "count" : 20 } { "_id" : { "min" : 20, "max" : 40 }, "count" : 20 } { "_id" : { "min" : 40, "max" : 60 }, "count" : 20 } { "_id" : { "min" : 60, "max" : 80 }, "count" : 20 } { "_id" : { "min" : 80, "max" : 99 }, "count" : 20 } R20 { "_id" : { "min" : 0, "max" : 20 }, "count" : 20 } { "_id" : { "min" : 20, "max" : 40 }, "count" : 20 } { "_id" : { "min" : 40, "max" : 63 }, "count" : 23 } { "_id" : { "min" : 63, "max" : 90 }, "count" : 27 } { "_id" : { "min" : 90, "max" : 100 }, "count" : 10 } E24 { "_id" : { "min" : 0, "max" : 20 }, "count" : 20 } { "_id" : { "min" : 20, "max" : 43 }, "count" : 23 } { "_id" : { "min" : 43, "max" : 68 }, "count" : 25 } { "_id" : { "min" : 68, "max" : 91 }, "count" : 23 } { "_id" : { "min" : 91, "max" : 100 }, "count" : 9 } 1-2-5 { "_id" : { "min" : 0, "max" : 20 }, "count" : 20 } { "_id" : { "min" : 20, "max" : 50 }, "count" : 30 } { "_id" : { "min" : 50, "max" : 100 }, "count" : 50 } The specified number of buckets exceeds the number of intervals
in the series. POWERSOF2 { "_id" : { "min" : 0, "max" : 32 }, "count" : 32 } { "_id" : { "min" : 32, "max" : 64 }, "count" : 32 } { "_id" : { "min" : 64, "max" : 128 }, "count" : 36 } The specified number of buckets exceeds the number of intervals
in the series. Example Consider a collection artwork with the following documents: { "_id" : 1 , "title" : "The Pillars of Society" , "artist" : "Grosz" , "year" : 1926 , "price" : NumberDecimal ( "199.99" ) , "dimensions" : { "height" : 39 , "width" : 21 , "units" : "in" } } { "_id" : 2 , "title" : "Melancholy III" , "artist" : "Munch" , "year" : 1902 , "price" : NumberDecimal ( "280.00" ) , "dimensions" : { "height" : 49 , "width" : 32 , "units" : "in" } } { "_id" : 3 , "title" : "Dancer" , "artist" : "Miro" , "year" : 1925 , "price" : NumberDecimal ( "76.04" ) , "dimensions" : { "height" : 25 , "width" : 20 , "units" : "in" } } { "_id" : 4 , "title" : "The Great Wave off Kanagawa" , "artist" : "Hokusai" , "price" : NumberDecimal ( "167.30" ) , "dimensions" : { "height" : 24 , "width" : 36 , "units" : "in" } } { "_id" : 5 , "title" : "The Persistence of Memory" , "artist" : "Dali" , "year" : 1931 , "price" : NumberDecimal ( "483.00" ) , "dimensions" : { "height" : 20 , "width" : 24 , "units" : "in" } } { "_id" : 6 , "title" : "Composition VII" , "artist" : "Kandinsky" , "year" : 1913 , "price" : NumberDecimal ( "385.00" ) , "dimensions" : { "height" : 30 , "width" : 46 , "units" : "in" } } { "_id" : 7 , "title" : "The Scream" , "artist" : "Munch" , "price" : NumberDecimal ( "159.00" ) , "dimensions" : { "height" : 24 , "width" : 18 , "units" : "in" } } { "_id" : 8 , "title" : "Blue Flower" , "artist" : "O'Keefe" , "year" : 1918 , "price" : NumberDecimal ( "118.42" ) , "dimensions" : { "height" : 24 , "width" : 20 , "units" : "in" } } Single Facet Aggregation In the following operation, input documents are grouped into four
buckets according to the values in the price field: db. artwork . aggregate ( [ { $bucketAuto : { groupBy : "$price" , buckets : 4 } } ] ) The operation returns the following documents: { "_id" : { "min" : NumberDecimal ( "76.04" ) , "max" : NumberDecimal ( "159.00" ) } , "count" : 2 } { "_id" : { "min" : NumberDecimal ( "159.00" ) , "max" : NumberDecimal ( "199.99" ) } , "count" : 2 } { "_id" : { "min" : NumberDecimal ( "199.99" ) , "max" : NumberDecimal ( "385.00" ) } , "count" : 2 } { "_id" : { "min" : NumberDecimal ( "385.00" ) , "max" : NumberDecimal ( "483.00" ) } , "count" : 2 } Multi-Faceted Aggregation The $bucketAuto stage can be used within the $facet stage to process multiple aggregation pipelines on
the same set of input documents from artwork . The following aggregation pipeline groups the documents from the artwork collection into buckets based on price , year , and
the calculated area : db. artwork . aggregate ( [ { $facet : { "price" : [ { $bucketAuto : { groupBy : "$price" , buckets : 4 } } ] , "year" : [ { $bucketAuto : { groupBy : "$year" , buckets : 3 , output : { "count" : { $sum : 1 } , "years" : { $push : "$year" } } } } ] , "area" : [ { $bucketAuto : { groupBy : { $multiply : [ "$dimensions.height" , "$dimensions.width" ] } , buckets : 4 , output : { "count" : { $sum : 1 } , "titles" : { $push : "$title" } } } } ] } } ] ) The operation returns the following document: { "area" : [ { "_id" : { "min" : 432 , "max" : 500 } , "count" : 3 , "titles" : [ "The Scream" , "The Persistence of Memory" , "Blue Flower" ] } , { "_id" : { "min" : 500 , "max" : 864 } , "count" : 2 , "titles" : [ "Dancer" , "The Pillars of Society" ] } , { "_id" : { "min" : 864 , "max" : 1568 } , "count" : 2 , "titles" : [ "The Great Wave off Kanagawa" , "Composition VII" ] } , { "_id" : { "min" : 1568 , "max" : 1568 } , "count" : 1 , "titles" : [ "Melancholy III" ] } ] , "price" : [ { "_id" : { "min" : NumberDecimal ( "76.04" ) , "max" : NumberDecimal ( "159.00" ) } , "count" : 2 } , { "_id" : { "min" : NumberDecimal ( "159.00" ) , "max" : NumberDecimal ( "199.99" ) } , "count" : 2 } , { "_id" : { "min" : NumberDecimal ( "199.99" ) , "max" : NumberDecimal ( "385.00" ) } , "count" : 2 } , { "_id" : { "min" : NumberDecimal ( "385.00" ) , "max" : NumberDecimal ( "483.00" ) } , "count" : 2 } ] , "year" : [ { "_id" : { "min" : null , "max" : 1913 } , "count" : 3 , "years" : [ 1902 ] } , { "_id" : { "min" : 1913 , "max" : 1926 } , "count" : 3 , "years" : [ 1913 , 1918 , 1925 ] } , { "_id" : { "min" : 1926 , "max" : 1931 } , "count" : 2 , "years" : [ 1926 , 1931 ] } ] } Back $bucket Next $changeStream