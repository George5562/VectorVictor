# $accumulator (aggregation) - MongoDB Manual v8.0


Docs Home / MongoDB Manual / Aggregation Operations / Reference / Operators $accumulator (aggregation) On this page Definition Syntax Behavior Examples Definition $accumulator Important Server-side JavaScript Deprecated Starting in MongoDB 8.0, server-side JavaScript functions
( $accumulator , $function , $where ) are
deprecated. MongoDB logs a warning when you run these functions. Defines a custom accumulator operator . Accumulators are operators that
maintain their state (e.g. totals, maximums, minimums, and related
data) as documents progress through the pipeline. Use the $accumulator operator to execute your own JavaScript
functions to implement behavior not supported by the MongoDB Query
Language. See also $function . $accumulator is available in these stages: $bucket $bucketAuto $group Important Executing JavaScript inside of an aggregation operator may
decrease performance. Only use the $accumulator operator
if the provided pipeline operators cannot fulfill your
application's needs. Syntax The $accumulator operator has this syntax: { $accumulator : { init : < code > , initArgs : <array expression>,        // Optional accumulate: <code>, accumulateArgs: <array expression>, merge: <code>, finalize: <code>,                    // Optional lang: <string> } } Field Type Description init String or Code Function used to initialize the state. The init function
receives its arguments from the initArgs array expression. You can specify the
function definition as either BSON type Code or String. The init function has the following form: function ( <initArg1>, <initArg2>, ... ) { ... return < initialState > } Spilling to disk or running a query on a sharded cluster can cause the
accumulator to be computed as a merge of multiple sub-accumulations, each
of which begins by calling init() . Ensure that your init() , accumulate() , and merge() functions are compatible with this
execution model. initArgs Array Optional. Arguments passed to the init function. initArgs has the following form: [ < initArg1 > , < initArg2 > , ... ] IMPORTANT: When used in a $bucketAuto stage, initArgs cannot refer to the group key (i.e., you cannot use the $<fieldName> syntax). Instead, in a $bucketAuto stage,
you can only specify constant values in initArgs . accumulate String or Code Function used to accumulate documents. The accumulate function receives its arguments from the current state and accumulateArgs array
expression. The result of the accumulate function becomes
the new state. You can specify the function definition as
either BSON type Code or String. The accumulate function has the following form: function ( state, <accumArg1>, <accumArg2>, ... ) { ... return < newState > } accumulateArgs Array Arguments passed to the accumulate function. You can use accumulateArgs to specify what field value(s) to pass to
the accumulate function. accumulateArgs has the following form: [ < accumArg1 > , < accumArg2 > , ... ] merge String or Code Function used to merge two internal states. merge must be
either a String or Code BSON type. merge returns the
combined result of the two merged states. For information on
when the merge function is called, see Merge Two States with $merge . The merge function has the following form: function ( <state1>, <state2> ) { <logic to merge state1 and state2> return <newState> } finalize String or Code Optional. Function used to update the result of the accumulation. The finalize function has the following form: function ( state ) { ... return < finalState > } lang String The language used in the $accumulator code. IMPORTANT: Currently, the only supported value for lang is js . Behavior The following steps outline how the $accumulator operator
processes documents: The operator begins at an initial state, defined by the init function. For each document, the operator updates
the state based on the accumulate function. The accumulate function's
first argument is the current state, and additional arguments are be
specified in the accumulateArgs array. When the operator needs to merge multiple intermediate states, it
executes the merge function. For more
information on when the merge function is
called, see Merge Two States with $merge . If a finalize function has been
defined, once all documents have been processed and the state has
been updated accordingly, finalize converts the state to a final output. Merge Two States with $merge As part of its internal operations, the $accumulator operator
may need to merge two separate, intermediate states. The merge function specifies how the operator should merge
two states. The merge function always merges two
states at a time. In the event that more than two states must be merged,
the resulting merge of two states is merged with a single state. This
process repeats until all states are merged. For example, $accumulator may need to combine two states in the
following scenarios: $accumulator is run on a sharded cluster. The operator
needs to merge the results from each shard to obtain the final
result. A single $accumulator operation exceeds its specified
memory limit. If you specify the allowDiskUse option, the operator stores the
in-progress operation on disk and finishes the operation in memory.
Once the operation finishes, the results from disk and memory are
merged together using the merge function. Document Processing Order The order that MongoDB processes documents for the init() , accumulate() , and merge() functions can vary, and might differ
from the order that those documents are specified to the $accumulator function. For example, consider a series of documents where the _id fields are
the letters of the alphabet: { _id: 'a' }, { _id: 'b' }, { _id: 'c' } ... { _id: 'z' } Next, consider an aggregation pipeline that sorts the documents by the _id field and then uses an $accumulator function to concatenate
the _id field values: [ { $sort : { _id : 1 } } , { $group : { _id : null , alphabet : { $accumulator : { init : function ( ) { return "" } , accumulate : function ( state, letter ) { return ( state + letter) } , accumulateArgs : [ "$_id" ] , merge : function ( state1, state2 ) { return ( state1 + state2) } , lang : "js" } } } } ] MongoDB does not guarantee that the documents are processed in the
sorted order, meaning the alphabet field does not necessarily get
set to abc...z . Due to this behavior, ensure that your $accumulator function does
not need to process and return documents in a specific order. Javascript Enabled To use $accumulator , you must have server-side scripting
enabled. If you do not use $accumulator (or $function , $where , or mapReduce ), disable server-side
scripting: For a mongod instance, see security.javascriptEnabled configuration option or --noscripting command-line option. For a mongos instance, see security.javascriptEnabled configuration option or the --noscripting command-line option. In earlier versions, MongoDB does not allow JavaScript execution on mongos instances. See also â¤ Run MongoDB with Secure Configuration Options . Unsupported Array and String Functions MongoDB 6.0 upgrades the internal JavaScript engine used for server-side JavaScript , $accumulator , $function , and $where expressions and from MozJS-60 to MozJS-91. Several deprecated,
non-standard array and string functions that existed in MozJS-60 are
removed in MozJS-91. For the complete list of removed array and string functions, see the 6.0 compatibility notes . Examples Use $accumulator to Implement the $avg Operator Note This example walks through using the $accumulator operator
to implement the $avg operator, which is already supported
by MongoDB. The goal of this example is not to implement new
functionality, but to illustrate the behavior and syntax of the $accumulator operator with familiar logic. In mongosh , create a sample collection named books with the following documents: db. books . insertMany ( [ { "_id" : 8751 , "title" : "The Banquet" , "author" : "Dante" , "copies" : 2 } , { "_id" : 8752 , "title" : "Divine Comedy" , "author" : "Dante" , "copies" : 1 } , { "_id" : 8645 , "title" : "Eclogues" , "author" : "Dante" , "copies" : 2 } , { "_id" : 7000 , "title" : "The Odyssey" , "author" : "Homer" , "copies" : 10 } , { "_id" : 7020 , "title" : "Iliad" , "author" : "Homer" , "copies" : 10 } ]) The following operation groups the documents by author , and uses $accumulator to compute the average
number of copies across books for each author: db. books . aggregate ( [ { $group : { _id : "$author" , avgCopies : { $accumulator : { init : function ( ) { // Set the initial state return { count : 0 , sum : 0 } } , accumulate : function ( state, numCopies ) { // Define how to update the state return { count : state. count + 1 , sum : state. sum + numCopies } } , accumulateArgs : [ "$copies" ] , // Argument required by the accumulate function merge : function ( state1, state2 ) { // When the operator performs a merge, return { // add the fields from the two states count : state1. count + state2. count , sum : state1. sum + state2. sum } } , finalize : function ( state ) { // After collecting the results from all documents, return ( state. sum / state. count ) // calculate the average } , lang : "js" } } } } ]) Result This operation returns the following result: { "_id" : "Dante" , "avgCopies" : 1.6666666666666667 } { "_id" : "Homer" , "avgCopies" : 10 } Behavior The $accumulator defines an initial state where count and sum are both set to 0 . For each document that the $accumulator processes, it updates the state by: Incrementing the count by 1 and Adding the values of the document's copies field to the sum .
The accumulate function can access the copies field because it is passed in the accumulateArgs field. With each document that is processed, the accumulate function returns the updated
state. Once all documents have been processed, the finalize function divides the sum of
the copies by the count of documents to obtain the average. This
removes the need to keep a running computed average, since the finalize function receives the cumulative sum and count of all documents. Comparison with $avg This operation is equivalent to the following pipeline, which uses the $avg operator: db. books . aggregate ( [ { $group : { _id : "$author" , avgCopies : { $avg : "$copies" } } } ]) Use initArgs to Vary the Initial State by Group You can use the initArgs option in
to vary the initial state of $accumulator . This can be
useful if you want to, for example: Use the value of a field which is not in your state to affect your
state, or Set the initial state to a different value based on the group being
processed. In mongosh , create a sample collection named restaurants with the following documents: db. restaurants . insertMany ( [ { "_id" : 1 , "name" : "Food Fury" , "city" : "Bettles" , "cuisine" : "American" } , { "_id" : 2 , "name" : "Meal Macro" , "city" : "Bettles" , "cuisine" : "Chinese" } , { "_id" : 3 , "name" : "Big Crisp" , "city" : "Bettles" , "cuisine" : "Latin" } , { "_id" : 4 , "name" : "The Wrap" , "city" : "Onida" , "cuisine" : "American" } , { "_id" : 5 , "name" : "Spice Attack" , "city" : "Onida" , "cuisine" : "Latin" } , { "_id" : 6 , "name" : "Soup City" , "city" : "Onida" , "cuisine" : "Chinese" } , { "_id" : 7 , "name" : "Crave" , "city" : "Pyote" , "cuisine" : "American" } , { "_id" : 8 , "name" : "The Gala" , "city" : "Pyote" , "cuisine" : "Chinese" } ]) Suppose an application allows users to query this data to find
restaurants. It may be useful to show more results for
the city where the user lives. For this example, we assume that the
user's city is called in a variable called userProfileCity . The following aggregation pipeline groups the
documents by city . The operation uses the $accumulator to display a different number of results from each city depending on
whether the restaurant's city matches the city in the user's profile: Note To execute this example in mongosh , replace <userProfileCity> in the initArgs with a string containing an actual city value, such as Bettles . 1 db. restaurants . aggregate ( [ 2 { 3 $group : 4 { 5 _id : { city : "$city" } , 6 restaurants : 7 { 8 $accumulator : 9 { 10 init : function ( city, userProfileCity ) { // Set the initial state 11 return { 12 max : city === userProfileCity ? 3 : 1 , // If the group matches the user's city, return 3 restaurants 13 restaurants : [ ] // else, return 1 restaurant 14 } 15 } , 16 17 initArgs : [ "$city" , < userProfileCity > ] , // Argument to pass to the init function 18 19 accumulate : function ( state, restaurantName ) { // Define how to update the state 20 if ( state. restaurants . length < state. max ) { 21 state. restaurants . push ( restaurantName) ; 22 } 23 return state ; 24 } , 25 26 accumulateArgs : [ "$name" ] , // Argument required by the accumulate function 27 28 merge : function ( state1, state2 ) { 29 return { 30 max : state1. max , 31 restaurants : state1. restaurants . concat ( state2. restaurants ). slice ( 0 , state1. max ) 32 } 33 } , 34 35 finalize : function ( state ) { // Adjust the state to only return field we need 36 return state. restaurants 37 } 38 39 lang : "js" 40 } 41 } 42 } 43 } 44 ]) Results If the value of userProfileCity is Bettles , this operation
returns the following result: { "_id" : { "city" : "Bettles" } , "restaurants" : { "restaurants" : [ "Food Fury" , "Meal Macro" , "Big Crisp" ] } } { "_id" : { "city" : "Onida" } , "restaurants" : { "restaurants" : [ "The Wrap" ] } } { "_id" : { "city" : "Pyote" } , "restaurants" : { "restaurants" : [ "Crave" ] } } If the value of userProfileCity is Onida , this operation
returns the following result: { "_id" : { "city" : "Bettles" } , "restaurants" : { "restaurants" : [ "Food Fury" ] } } { "_id" : { "city" : "Onida" } , "restaurants" : { "restaurants" : [ "The Wrap" , "Spice Attack" , "Soup City" ] } } { "_id" : { "city" : "Pyote" } , "restaurants" : { "restaurants" : [ "Crave" ] } } If the value of userProfileCity is Pyote , this operation
returns the following result: { "_id" : { "city" : "Bettles" } , "restaurants" : { "restaurants" : [ "Food Fury" ] } } { "_id" : { "city" : "Onida" } , "restaurants" : { "restaurants" : [ "The Wrap" ] } } { "_id" : { "city" : "Pyote" } , "restaurants" : { "restaurants" : [ "Crave" , "The Gala" ] } } If the value of userProfileCity is any other value, this operation
returns the following result: { "_id" : { "city" : "Bettles" } , "restaurants" : { "restaurants" : [ "Food Fury" ] } } { "_id" : { "city" : "Onida" } , "restaurants" : { "restaurants" : [ "The Wrap" ] } } { "_id" : { "city" : "Pyote" } , "restaurants" : { "restaurants" : [ "Crave" ] } } Behavior The init function defines an initial state
containing max and restaurants fields. The max field sets
the maximum number of restaurants for that particular group. If the
document's city field matches userProfileCity , that group
contains a maximum of 3 restaurants. Otherwise, if the document _id does not match userProfileCity , the group contains at most a single
restaurant. The init function receives both
the city userProfileCity arguments from the initArgs array. For each document that the $accumulator processes, it pushes
the name of the restaurant to the restaurants array, provided
that name would not put the length of restaurants over the max value. With each document that is processed, the accumulate function returns the updated state. The merge function defines how to merge two
states. The function concatenates the restaurant arrays from each
state together, and the length of the resulting array is limited using
the slice() method to ensure that it does not exceed the max value. Once all documents have been processed, the finalize function modifies the resulting state to only
return the names of the restaurants.  Without this function, the max field would also be included in the output, which does not fulfill any
needs for the application. Back $abs Next $acos
