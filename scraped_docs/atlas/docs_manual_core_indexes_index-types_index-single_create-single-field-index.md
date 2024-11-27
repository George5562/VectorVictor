# Create an Index on a Single Field - MongoDB Manual v8.0


Docs Home / MongoDB Manual / Indexes / Types / Single Field Create an Index on a Single Field On this page Before You Begin Procedures Create an Index on a Single Field Create an Index on an Embedded Field Learn More You can create an index on a single field to improve performance for
queries on that field. Indexing commonly queried fields increases the
chances of covering those queries,
meaning MongoDB can satisfy the query entirely with the index,
without examining documents. To create a single-field index, use the db.collection.createIndex() method: db. < collection > . createIndex ( { < field > : 1 } ) Note Index Sort Order Using a descending single-field index may negatively impact index
performance. For best performance, only use ascending single-field
indexes. Before You Begin Create a students collection that contains the following documents: db. students . insertMany ( [ { "name" : "Alice" , "gpa" : 3.6 , "location" : { city : "Sacramento" , state : "California" } } , { "name" : "Bob" , "gpa" : 3.2 , "location" : { city : "Albany" , state : "New York" } } ] ) Procedures The following examples show you how to: Create an Index on a Single Field Create an Index on an Embedded Field Create an Index on a Single Field Consider a school administrator who frequently looks up students by
their GPA . You can create an index on the gpa field to improve performance for those queries: db. students . createIndex ( { gpa : 1 } ) Results The index supports queries that select on the field gpa , such as the
following: db. students . find ( { gpa : 3.6 } ) db. students . find ( { gpa : { $lt : 3.4 } } ) Create an Index on an Embedded Field You can create indexes on fields within embedded documents. Indexes on
embedded fields can fulfill queries that use dot notation . The location field is an embedded document that contains the
embedded fields city and state . Create an index on the location.state field: db. students . createIndex ( { "location.state" : 1 } ) Results The index supports queries on the field location.state , such as the
following: db. students . find ( { "location.state" : "California" } ) db. students . find ( { "location.city" : "Albany" , "location.state" : "New York" } ) Learn More Create an Index on an Embedded Document Create an Index on an Embedded Field in an Array Check if a query uses an index Learn about other types of index types Back Single Field Next Embedded Documents
