# Create a Compound Index - MongoDB Manual v8.0


Docs Home / MongoDB Manual / Indexes / Types / Compound Create a Compound Index On this page Restriction Before You Begin Procedure Results Learn More Compound indexes are indexes that contain references to multiple
fields. Compound indexes improve performance for queries on exactly the
fields in the index or fields in the index prefix . Indexing commonly queried fields increases the
chances of covering those queries,
meaning MongoDB can satisfy the query entirely with the index,
without examining documents. To create a compound index, use the db.collection.createIndex() method: db. < collection > . createIndex ( { < field1 > : < sortOrder > , < field2 > : < sortOrder > , ... < fieldN > : < sortOrder > } ) Restriction You can specify up to 32 fields in a single compound index. Before You Begin Create a students collection that contains these documents: db. students . insertMany ( [ { "name" : "Alice" , "gpa" : 3.6 , "location" : { city : "Sacramento" , state : "California" } } , { "name" : "Bob" , "gpa" : 3.2 , "location" : { city : "Albany" , state : "New York" } } ]) Procedure The following operation creates a compound index containing the name and gpa fields: db. students . createIndex ( { name : 1 , gpa : - 1 } ) In this example: The index on name is ascending ( 1 ). The index on gpa is descending ( -1 ). Results The created index supports queries that select on: Both name and gpa fields. Only the name field, because name is a prefix of the compound index. For example, the index supports these queries: db. students . find ( { name : "Alice" , gpa : 3.6 } ) db. students . find ( { name : "Bob" } ) The index does not support queries on only the gpa field,
because gpa is not part of the index prefix. For example, the index
does not support this query: db. students . find ( { gpa : { $gt : 3.5 } } ) Learn More To learn how to create efficient compound indexes, see The ESR (Equality, Sort, Range) Rule . To learn how sort order (ascending or descending) impacts performance
of compound indexes, see Use Indexes to Sort Query Results . To learn about other index types, see Index Types . To learn what properties you can specify for indexes, see Index Properties . Back Compound Next Sort Order
