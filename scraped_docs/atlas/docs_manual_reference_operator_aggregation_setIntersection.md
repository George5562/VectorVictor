# $setIntersection (aggregation) - MongoDB Manual v8.0


Docs Home / MongoDB Manual / Aggregation Operations / Reference / Operators $setIntersection (aggregation) On this page Definition Behavior Examples Definition $setIntersection Takes two or more arrays and returns an array that contains the
elements that appear in every input array. $setIntersection has the following syntax: { $setIntersection : [ < array1 > , < array2 > , ... ] } The arguments can be any valid expression as long as they each resolve to an array.
For more information on expressions, see Expression Operators . Behavior $setIntersection performs set operation on arrays, treating arrays
as sets. If an array contains duplicate entries, $setIntersection ignores the duplicate entries. $setIntersection ignores the order of
the elements. $setIntersection filters out duplicates in its result to output an
array that contain only unique entries. The order of the elements in
the output array is unspecified. If no intersections are found (i.e. the input arrays contain no common
elements), $setIntersection returns an empty array. If a set contains a nested array element, $setIntersection does not descend
into the nested array but evaluates the array at top-level. Example Result { $setIntersection : [ [ "a" , "b" , "a" ] , [ "b" , "a" ] ] } [ "b" , "a" ] { $setIntersection : [ [ "a" , "b" ] , [ [ "a" , "b" ] ] ] } [ ] Examples This section contains examples that show the use of $setIntersection with collections. Elements Array Example Consider an flowers collection with the following documents: db. flowers . insertMany ( [ { "_id" : 1 , "flowerFieldA" : [ "rose" , "orchid" ] , "flowerFieldB" : [ "rose" , "orchid" ] } , { "_id" : 2 , "flowerFieldA" : [ "rose" , "orchid" ] , "flowerFieldB" : [ "orchid" , "rose" , "orchid" ] } , { "_id" : 3 , "flowerFieldA" : [ "rose" , "orchid" ] , "flowerFieldB" : [ "rose" , "orchid" , "jasmine" ] } , { "_id" : 4 , "flowerFieldA" : [ "rose" , "orchid" ] , "flowerFieldB" : [ "jasmine" , "rose" ] } , { "_id" : 5 , "flowerFieldA" : [ "rose" , "orchid" ] , "flowerFieldB" : [ ] } , { "_id" : 6 , "flowerFieldA" : [ "rose" , "orchid" ] , "flowerFieldB" : [ [ "rose" ] , [ "orchid" ] ] } , { "_id" : 7 , "flowerFieldA" : [ "rose" , "orchid" ] , "flowerFieldB" : [ [ "rose" , "orchid" ] ] } , { "_id" : 8 , "flowerFieldA" : [ ] , "flowerFieldB" : [ ] } , { "_id" : 9 , "flowerFieldA" : [ ] , "flowerFieldB" : [ "rose" ] } ] ) The following operation uses the $setIntersection operator to return an array of elements common to both the flowerFieldA array and the flowerFieldB array: db. flowers . aggregate ( [ { $project : { flowerFieldA : 1 , flowerFieldB : 1 , commonToBoth : { $setIntersection : [ "$flowerFieldA" , "$flowerFieldB" ] } , _id : 0 } } ] ) The operation returns the following results: { "flowerFieldA" : [ "rose" , "orchid" ] , "flowerFieldB" : [ "rose" , "orchid" ] , "commonToBoth" : [ "orchid" , "rose" ] } { "flowerFieldA" : [ "rose" , "orchid" ] , "flowerFieldB" : [ "orchid" , "rose" , "orchid" ] , "commonToBoth" : [ "orchid" , "rose" ] } { "flowerFieldA" : [ "rose" , "orchid" ] , "flowerFieldB" : [ "rose" , "orchid" , "jasmine" ] , "commonToBoth" : [ "orchid" , "rose" ] } { "flowerFieldA" : [ "rose" , "orchid" ] , "flowerFieldB" : [ "jasmine" , "rose" ] , "commonToBoth" : [ "rose" ] } { "flowerFieldA" : [ "rose" , "orchid" ] , "flowerFieldB" : [ ] , "commonToBoth" : [ ] } { "flowerFieldA" : [ "rose" , "orchid" ] , "flowerFieldB" : [ [ "rose" ] , [ "orchid" ] ] , "commonToBoth" : [ ] } { "flowerFieldA" : [ "rose" , "orchid" ] , "flowerFieldB" : [ [ "rose" , "orchid" ] ] , "commonToBoth" : [ ] } { "flowerFieldA" : [ ] , "flowerFieldB" : [ ] , "commonToBoth" : [ ] } { "flowerFieldA" : [ ] , "flowerFieldB" : [ "rose" ] , "commonToBoth" : [ ] } Retrieve Documents for Roles Granted to the Current User Starting in MongoDB 7.0, you can use the new USER_ROLES system variable to return user roles . The scenario in this section shows users with various roles who have
limited access to documents in a collection containing budget
information. The scenario shows one possible use of USER_ROLES . The budget collection contains documents with a field named allowedRoles . As
you'll see in the following scenario, you can write queries that compare
the user roles found in the allowedRoles field with the roles
returned by the USER_ROLES system variable. Note For another USER_ROLES example scenario, see Retrieve Medical Information for Roles Granted to the Current User . That
example doesn't store the user roles in the document fields, as is
done in the following example. For the budget scenario in this section, perform the following steps to
create the roles, users, and budget collection: 1 Create the roles Run: db. createRole ( { role : "Marketing" , roles : [ ] , privileges : [ ] } ) db. createRole ( { role : "Sales" , roles : [ ] , privileges : [ ] } ) db. createRole ( { role : "Development" , roles : [ ] , privileges : [ ] } ) db. createRole ( { role : "Operations" , roles : [ ] , privileges : [ ] } ) 2 Create the users Create users named John and Jane with the required roles.
Replace the test database with your database name. db. createUser ( { user : "John" , pwd : "jn008" , roles : [ { role : "Marketing" , db : "test" } , { role : "Development" , db : "test" } , { role : "Operations" , db : "test" } , { role : "read" , db : "test" } ] } ) db. createUser ( { user : "Jane" , pwd : "je009" , roles : [ { role : "Sales" , db : "test" } , { role : "Operations" , db : "test" } , { role : "read" , db : "test" } ] } ) 3 Create the collection Run: db. budget . insertMany ( [ { _id : 0 , allowedRoles : [ "Marketing" ] , comment : "For marketing team" , yearlyBudget : 15000 } , { _id : 1 , allowedRoles : [ "Sales" ] , comment : "For sales team" , yearlyBudget : 17000 , salesEventsBudget : 1000 } , { _id : 2 , allowedRoles : [ "Operations" ] , comment : "For operations team" , yearlyBudget : 19000 , cloudBudget : 12000 } , { _id : 3 , allowedRoles : [ "Development" ] , comment : "For development team" , yearlyBudget : 27000 } ] ) Perform the following steps to retrieve the documents accessible to John : 1 Log in as John Run: db. auth ( "John" , "jn008" ) 2 Retrieve the documents To use a system variable, add $$ to the start of the variable name.
Specify the USER_ROLES system variable as $$USER_ROLES . Run: db. budget . aggregate ( [ { $match : { $expr : { $not : { $eq : [ { $setIntersection : [ "$allowedRoles" , "$$USER_ROLES.role" ] } , [ ] ] } } } } ] ) The previous example returns the documents from the budget collection that match at least one of the roles that the user who runs
the example has. To do that, the example uses $setIntersection to return documents where the
intersection between the budget document allowedRoles field and
the set of user roles from $$USER_ROLES is not empty. 3 Examine the documents John has the Marketing , Operations , and Development roles, and sees these documents: [ { _id : 0 , allowedRoles : [ 'Marketing' ] , comment : 'For marketing team' , yearlyBudget : 15000 } , { _id : 2 , allowedRoles : [ 'Operations' ] , comment : 'For operations team' , yearlyBudget : 19000 , cloudBudget : 12000 } , { _id : 3 , allowedRoles : [ 'Development' ] , comment : 'For development team' , yearlyBudget : 27000 } ] Perform the following steps to retrieve the documents accessible to Jane : 1 Log in as Jane Run: db. auth ( "Jane" , "je009" ) 2 Retrieve the documents To use a system variable, add $$ to the start of the variable name.
Specify the USER_ROLES system variable as $$USER_ROLES . Run: db. budget . aggregate ( [ { $match : { $expr : { $not : { $eq : [ { $setIntersection : [ "$allowedRoles" , "$$USER_ROLES.role" ] } , [ ] ] } } } } ] ) 3 Examine the documents Jane has the Sales and Operations roles, and sees these
documents: [ { _id : 1 , allowedRoles : [ 'Sales' ] , comment : 'For sales team' , yearlyBudget : 17000 , salesEventsBudget : 1000 } , { _id : 2 , allowedRoles : [ 'Operations' ] , comment : 'For operations team' , yearlyBudget : 19000 , cloudBudget : 12000 } ] Note On a sharded cluster, a query can be run on a shard by another server
node on behalf of the user. In those queries, USER_ROLES is still
populated with the roles for the user. Back $setField Next $setIsSubset