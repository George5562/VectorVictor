# Multikey Index Bounds - MongoDB Manual v8.0


Docs Home / MongoDB Manual / Indexes / Types / Multikey Multikey Index Bounds On this page Bounds Intersection for a Multikey Index Example: Bounds Intersection Query without $elemMatch Compound Bounds for a Multikey Index Example: Compound Bounds of Non-array Field and Array Field Example: Compound Bounds of Non-array Field and Multiple Array Fields Compound Bounds of Multiple Fields from the Same Array Example: $elemMatch on Diverging Field Paths Index bounds define the range of index values that MongoDB searches
when using an index to fulfill a query. When you specify multiple query
predicates on an indexed field, MongoDB attempts to combine the bounds
for those predicates to produce an index scan with smaller bounds.
Smaller index bounds result in faster queries and reduced resource use. MongoDB combines bounds by either intersecting or compounding bounds. Bounds Intersection for a Multikey Index Bounds intersection refers to the point where multiple bounds overlap.
For example, given the bounds [ [ 3, Infinity ] ] and [ [
-Infinity, 6 ] ] , the intersection of the bounds results in [ [ 3, 6
] ] . Given an indexed array field, consider a query that specifies multiple
query predicates on the array and uses a multikey index to fulfill the query. MongoDB can intersect the
multikey index bounds if an $elemMatch operator joins the query
predicates. Example: Bounds Intersection The following example shows how MongoDB uses bounds intersection to
define a smaller range of values to query, resulting in improved query
performance. 1 Populate a sample collection Create a students collection that contains documents with a
field name and an array field grades : db. students . insertMany ( [ { _id : 1 , name : "Shawn" , grades : [ 70 , 85 ] } , { _id : 2 , item : "Elena" , grades : [ 92 , 84 ] } ] ) 2 Create a multikey index Create a multikey index on the grades array: db. students . createIndex ( { grades : 1 } ) 3 Query the collection Run the following query: db. students . find ( { grades : { $elemMatch : { $gte : 90 , $lte : 99 } } } ) The preceding query uses $elemMatch to return documents where
the grades array contains at least one element that matches both of the specified conditions. Taking the query predicates separately: The bounds for the greater than or equal to 90 predicate ( $gte: 90 )
are [ [ 90, Infinity ] ] . The bounds for the less than or equal to 99 predicate ( $lte:
99 ) are [ [ -Infinity, 99 ] ] . Because the query uses $elemMatch to join these predicates,
MongoDB intersects the bounds to: ratings : [ [ 90 , 99 ] ] Query without $elemMatch If the query does not join the conditions on the array field with $elemMatch , MongoDB cannot intersect the multikey index bounds. Consider this query: db. students . find ( { grades : { $gte : 90 , $lte : 99 } } ) The query searches the grades array for: At least one element greater than or equal to 90 At least one element less than or equal to 99 The same element can satisfy both criteria. Because the preceding query does not use $elemMatch , MongoDB does
not intersect the bounds. Instead, MongoDB uses either of the following
bounds: [ [ 90, Infinity ] ] [ [ -Infinity, 99 ] ] MongoDB makes no guarantee as to which of the two bounds it chooses. Compound Bounds for a Multikey Index Compound bounds combine bounds for multiple keys of a compound
index . Using bounds from multiple keys reduces
the time it takes to process a query because MongoDB does not need to
compute results for each bound individually. For example, consider a compound index { temperature: 1, humidity: 1
} with the following bounds: temperature has a bound of [ [ 80, Infinity ] ] . humidity has a bound of [ [ -Infinity, 20 ] ] . Compounding the bounds results in the use of both bounds: { temperature : [ [ 80 , Infinity ] ] , humidity : [ [ - Infinity , 20 ] ] } If MongoDB cannot compound the two bounds, MongoDB constrains the index
scan by the bound on the leading field. In this example, the leading
field is temperature , resulting in a constraint of temperature: [
[ 80, Infinity ] ] . Example: Compound Bounds of Non-array Field and Array Field The following example shows how MongoDB uses compound bounds to define a
more efficient query constraint, resulting in improved query
performance. 1 Populate a sample collection Create a survey collection that contains documents with a field item and an array field ratings : db. survey . insertMany ( [ { _id : 1 , item : "ABC" , ratings : [ 2 , 9 ] } , { _id : 2 , item : "XYZ" , ratings : [ 4 , 3 ] } ] ) 2 Create a compound multikey index Create a compound multikey index on the item and ratings fields: db. survey . createIndex ( { item : 1 , ratings : 1 } ) 3 Query the collection Run the following query: db. survey . find ( { item : "XYZ" , ratings : { $gte : 3 } } ) The preceding query specifies a condition on both keys of the index
( item and ratings ). Taking the predicates separately: The bounds for the item: "XYZ" predicate are [ [ "XYZ", "XYZ" ]] . The bounds for the ratings: { $gte: 3 } predicate are [ [ 3, Infinity ] ] . MongoDB uses the combined bounds of: { item : [ [ "XYZ" , "XYZ" ] ] , ratings : [ [ 3 , Infinity ] ] } Example: Compound Bounds of Non-array Field and Multiple Array Fields The following example shows how MongoDB uses compound bounds when an
index includes a non-array field and multiple array fields. 1 Populate a sample collection Create a survey2 collection that contains documents with a
string field item and an array field ratings : db. survey2 . insertMany ( [ { _id : 1 , item : "ABC" , ratings : [ { score : 2 , by : "mn" } , { score : 9 , by : "anon" } ] } , { _id : 2 , item : "XYZ" , ratings : [ { score : 5 , by : "anon" } , { score : 7 , by : "wv" } ] } ] ) 2 Create a compound multikey index Create a compound index on the following fields: item (non-array) ratings.score (array) ratings.by (array) db. survey2 . createIndex ( { "item" : 1 , "ratings.score" : 1 , "ratings.by" : 1 } ) 3 Query the collection Run the following query: db. survey2 . find ( { item : "XYZ" , "ratings.score" : { $lte : 5 } , "ratings.by" : "anon" } ) Taking the predicates separately: The bounds for the item: "XYZ" predicate are [ [ "XYZ", "XYZ" ] ] . The bounds for the score: { $lte: 5 } predicate are [ [ -Infinity, 5] ] . The bounds for the by: "anon" predicate are [ "anon", "anon" ] . MongoDB compounds the bounds for the item key with either the bounds
for "ratings.score" or the bounds for "ratings.by" , depending
upon the query predicates and the index key values. MongoDB does not
guarantee which bounds it compounds with the item field. MongoDB fulfills the query in one of the following ways: MongoDB compounds the item bounds with the "ratings.score" bounds: { "item" : [ [ "XYZ" , "XYZ" ] ] , "ratings.score" : [ [ - Infinity , 5 ] ] , "ratings.by" : [ [ MinKey , MaxKey ] ] } MongoDB compounds the item bounds with the "ratings.by" bounds: { "item" : [ [ "XYZ" , "XYZ" ] ] , "ratings.score" : [ [ MinKey , MaxKey ] ] , "ratings.by" : [ [ "anon" , "anon" ] ] } To compound the bounds for "ratings.score" with the bounds for "ratings.by" , the query must use $elemMatch . Compound Bounds of Multiple Fields from the Same Array To compound the bounds for index keys from the same array, both of the
following must be true: The index keys must share the same field path up to but excluding the
field names. The query must specify predicates on the fields using $elemMatch on that path. For a field in an embedded document, the dotted field name , such as "a.b.c.d" , is the field path for d . To compound the bounds for index keys from the same array, the $elemMatch must be on the path up to but excluding the field
name itself (meaning "a.b.c" ). Example The following example shows how MongoDB combines bounds for index keys
from the same array. This example uses the survey2 collection used
in the previous example . 1 Create a compound multikey index Create a compound index on the ratings.score and the ratings.by fields: db. survey2 . createIndex ( { "ratings.score" : 1 , "ratings.by" : 1 } ) The fields "ratings.score" and "ratings.by" share the
field path ratings . 2 Query the collection Run the following query: db. survey2 . find ( { ratings : { $elemMatch : { score : { $lte : 5 } , by : "anon" } } } ) The preceding query uses $elemMatch on the ratings field to
require that the array contains at least one single element that
matches both conditions. Taking the predicates separately: The bounds for the score: { $lte: 5 } predicate are [ [ -Infinity, 5 ] ] . The bounds for the by: "anon" predicate are [ [ "anon", "anon" ] ] . MongoDB compounds the two bounds to the following bounds: { "ratings.score" : [ [ - Infinity , 5 ] ] , "ratings.by" : [ [ "anon" , "anon" ] ] } Example: $elemMatch on Diverging Field Paths If your query specifies $elemMatch on fields that diverge from
a common path, MongoDB cannot compound the bounds of index keys from
the same array. The following example demonstrates $elemMatch on diverging field
paths. 1 Populate a sample collection Create a collection survey3 contains documents with a string
field item and an array field ratings : db. survey3 . insertMany ( [ { _id : 1 , item : "ABC" , ratings : [ { scores : [ { q1 : 2 , q2 : 4 } , { q1 : 3 , q2 : 8 } ] , loc : "A" } , { scores : [ { q1 : 2 , q2 : 5 } ] , loc : "B" } ] } , { _id : 2 , item : "XYZ" , ratings : [ { scores : [ { q1 : 7 } , { q1 : 2 , q2 : 8 } ] , loc : "B" } ] } ] ) 2 Create a compound multikey index Create a compound index on the ratings.scores.q1 and the ratings.scores.q2 fields: db. survey3 . createIndex ( { "ratings.scores.q1" : 1 , "ratings.scores.q2" : 1 } ) The fields "ratings.scores.q1" and "ratings.scores.q2" share the field path "ratings.scores" . In order to compound
index bounds, a query must use $elemMatch on the common field
path. 3 Query the collection The following query uses an $elemMatch not on the
required path: db. survey3 . find ( { ratings : { $elemMatch : { 'scores.q1' : 2 , 'scores.q2' : 8 } } } ) MongoDB cannot compound the index bounds and the "ratings.scores.q2" field is unconstrained during the index
scan. To compound the bounds, the query must use $elemMatch on
the common path "ratings.scores" : db. survey3 . find ( { 'ratings.scores' : { $elemMatch : { 'q1' : 2 , 'q2' : 8 } } } ) Back Embedded Array Field Next Wildcard
