# $zip (aggregation) - MongoDB Manual v8.0


Docs Home / MongoDB Manual / Aggregation Operations / Reference / Operators $zip (aggregation) On this page Definition Behavior Example Definition $zip Transposes an array of input arrays so that the first element of
the output array would be an array containing, the first element of
the first input array, the first element of the second input array,
etc. For example, $zip would transform [ [ 1, 2, 3 ], [ "a", "b", "c" ] ] into [ [ 1, "a" ], [ 2, "b" ], [ 3, "c" ] ] . $zip has the following syntax: { $zip : { inputs : [ <array expression1>,  ... ], useLongestLength: <boolean>, defaults:  <array expression> } } Operand Description inputs An array of expressions that
resolve to arrays. The elements of these input arrays combine
to form the arrays of the output array. If  any of the inputs arrays resolves to a value of null or refers to a
missing field, $zip returns null . If any of the inputs arrays does not resolve to an array or null nor refers
to a missing field, $zip returns an error. useLongestLength A boolean which specifies whether the length of the longest
array determines the number of arrays in the output array. The default value is false : the shortest array length
determines the number of arrays in the output array. defaults An array of default element values to use if the input arrays
have different lengths. You must specify useLongestLength: true along with this field, or else $zip will return an error. If useLongestLength: true but defaults is empty or not
specified, $zip uses null as the default
value. If specifying a non-empty defaults , you must specify a
default for each input array or else $zip will return an error. Behavior The input arrays do not need to be of the same length. By default,
the output array has the length of the shortest input array, but the useLongestLength option instructs $zip to output
an array as long as the longest input array. Example Results { $zip : { inputs : [ [ "a" ] , [ "b" ] , [ "c" ] ] } [ [ "a" , "b" , "c" ] ] { $zip : { inputs : [ [ "a" ] , [ "b" , "c" ] ] } } [ [ "a" , "b" ] ] { $zip : { inputs : [ [ 1 ] , [ 2 , 3 ] ] , useLongestLength : true } } [ [ 1 , 2 ] , [ null , 3 ] ] { $zip : { inputs : [ [ 1 ] , [ 2 , 3 ] , [ 4 ] ] , useLongestLength : true , defaults : [ "a" , "b" , "c" ] } } Because useLongestLength: true , $zip will pad the shorter
input arrays with the corresponding defaults elements. This yields [ [ 1, 2, 4 ], [ "a", 3, "c" ] ] . Example Matrix Transposition A collection called matrices contains the following documents: db. matrices . insertMany ( [ { matrix : [ [ 1 , 2 ] , [ 2 , 3 ] , [ 3 , 4 ]] } , { matrix : [ [ 8 , 7 ] , [ 7 , 6 ] , [ 5 , 4 ]] } , ]) To compute the transpose of each 3x2 matrix in this collection, you can
use the following aggregation operation: db. matrices . aggregate ( [ { $project : { _id : false , transposed : { $zip : { inputs : [ { $arrayElemAt : [ "$matrix" , 0 ] } , { $arrayElemAt : [ "$matrix" , 1 ] } , { $arrayElemAt : [ "$matrix" , 2 ] } , ] } } } }]) This will return the following 2x3 matrices: { "transposed" : [ [ 1 , 2 , 3 ] , [ 2 , 3 , 4 ] ] } { "transposed" : [ [ 8 , 7 , 5 ] , [ 7 , 6 , 4 ] ] } Filtering and Preserving Indexes You can use $zip with $filter to obtain a subset of
elements in an array, saving the original index alongside each
retained element. A collection called pages contains the following document: db. pages . insertOne ( { "category" : "unix" , "pages" : [ { "title" : "awk for beginners" , reviews : 5 } , { "title" : "sed for newbies" , reviews : 0 } , { "title" : "grep made simple" , reviews : 2 } , ] } ) The following aggregation pipeline will first zip the elements of the pages array together with their index, and then filter out only the
pages with at least one review: db. pages . aggregate ( [ { $project : { _id : false , pages : { $filter : { input : { $zip : { inputs : [ "$pages" , { $range : [ 0 , { $size : "$pages" }] } ] } } , as : "pageWithIndex" , cond : { $let : { vars : { page : { $arrayElemAt : [ "$$pageWithIndex" , 0 ] } } , in : { $gte : [ "$$page.reviews" , 1 ] } } } } } } }]) This will return the following document: { "pages" : [ [ { "title" : "awk for beginners" , "reviews" : 5 } , 0 ] , [ { "title" : "grep made simple" , "reviews" : 2 } , 2 ] ] } Back $year Next Commands Comparison
