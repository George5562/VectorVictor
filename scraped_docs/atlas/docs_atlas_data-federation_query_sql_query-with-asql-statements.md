# Query with Atlas SQL Statements - MongoDB Atlas


Docs Home / MongoDB Atlas / Query Federated Data / SQL Query with Atlas SQL Statements On this page Example Queries SELECT Statement LIMIT Statement WHERE Statement FLATTEN and UNWIND FLATTEN Flatten Example UNWIND Unwind Example Combined FLATTEN and UNWIND Example The page gives example Atlas SQL queries.
You'll find basic examples that use SQL syntax to query collections,
as well more advanced ones that use FLATTEN and UNWIND to work with nested data. Example Queries Try running the following Atlas SQL queries against the Advanced Configuration sample federated database instance, or modify them to read your
own data. Note These examples use short-form syntax . SELECT Statement SELECT * FROM sessions; Atlas SQL returns all documents from the Sessions collection. LIMIT Statement SELECT * FROM users LIMIT 2; Atlas SQL returns two documents from the Users collection. WHERE Statement SELECT * FROM users WHERE name = 'Jon Snow'; Atlas SQL returns documents from the Users collection where the user's name is Jon Snow . FLATTEN and UNWIND This section covers two Atlas SQL capabilities that make it easier to interact with document structures.
These are unique to Atlas SQL. FLATTEN FLATTEN flattens semi-structured data (name-value pairs in
JSON) into separate columns. Field names become column names that hold
all of the values for that field in rows. The syntax for flattening nested documents is a FLATTEN function
that can be used in the FROM clause in conjunction with a data
source and options. SELECT * FROM FLATTEN(<data source> WITH DEPTH => <integer>, SEPARATOR => <string> ) Variable Necessity Description <data source> Required Data source to flatten. DEPTH Optional Positive integer indicating how many levels of subdocuments to
flatten. Defaults to flattening every level of subdocuments. SEPARATOR Optional String to use as the delimiter when concatenating
field names. Defaults to _ . Flatten Example In an example scenario, a customerInfo collection contains
documents that are structured as follows: { id : 1 , location : "New York" , customer : { age : 50 , email : "customer@email.com" , satisfaction : 5 } } If you run the query SELECT * FROM customerInfo ,
Atlas SQL returns documents with the following top-level fields: id 1 location "New York" customer { age: 50, email: "customer@email.com", satisfaction: 5 } If you run the query SELECT * FROM FLATTEN(customerInfo) ,
Atlas SQL returns documents with the following top-level fields: id 1 location "New York" customer_age 50 customer_email "customer@email.com" customer_satisfaction 5 When you use FLATTEN , each flattened field from the original
document becomes a top-level field in the result set. Nested fields are
concatenated with their parent field names and separated by the default
delimiter, _ . UNWIND UNWIND deconstructs an array field from the input data source to
output one row for each item in that array. To learn more about
unwinding, see the $unwind aggregation
stage documentation. The syntax for unwinding array fields is an UNWIND function that
can be used in the FROM clause in conjunction with a data source
and options. SELECT * FROM UNWIND(<data source> WITH PATH => <array_path>, INDEX => <identifier>, OUTER => <bool> ) Variable Necessity Description <data source> Required Source of the array field to unwind. PATH Required Path to the field in the data source to
unwind. INDEX Optional Name to assign the index column. If omitted, Atlas SQL does
not create an index field. OUTER Optional Flag that indicates whether documents with null, missing, or
empty array values are preserved. If true , documents with
null, missing, or empty array values are preserved. Defaults to false . Unwind Example In an example scenario, a customerInfo collection contains
documents that are structured as follows: { id : 1 , location : "New York" , customer : { age : 50 , email : "customer@email.com" , satisfaction : 5 } , visits : [ { year : 2020 , score : 10 } , { year : 2021 , score : 8 } , { year : 2022 score : 7 } ] } If you run the query SELECT * FROM customerInfo ,
Atlas SQL returns documents with the following top-level fields: id 1 location "New York" customer { age: 50, email: "customer@email.com", satisfaction: 5 } visits [ { year: 2020, score: 10 }, { year: 2021, score: 8 }, { year: 2022, score: 7 } ] If you run the query SELECT * FROM UNWIND(customerInfo WITH PATH => visits, INDEX => idx) ,
Atlas SQL returns documents with the following top-level fields: id 1 1 1 location "New York" "New York" "New York" customer { age: 50, email: "customer@email.com", satisfaction: 5 } { age: 50, email: "customer@email.com", satisfaction: 5 } { age: 50, email: "customer@email.com", satisfaction: 5 } idx 0 1 2 visits { year: 2020, score: 10 } { year: 2021, score: 8 } { year: 2022, score: 7 } When you use UNWIND with PATH => visits , each visits object
becomes a table row. Combined FLATTEN and UNWIND Example The following example combines the FLATTEN and UNWIND functions. In an example scenario, a customerInfo collection contains
documents that are structured as follows: { id : 1 , location : "New York" , customer : { age : 50 , email : "customer@email.com" , satisfaction : 5 } , visits : [ { year : 2020 , score : 10 } , { year : 2021 , score : 8 } , { year : 2022 score : 7 } ] } If you run the query SELECT * FROM customerInfo ,
Atlas SQL returns documents with the following top-level fields: id 1 location "New York" satisfaction 5 customer { age: 50, email: "customer@email.com", satisfaction: 5 } visits [ { year: 2020, score: 10 }, { year: 2021, score: 8 }, { year: 2022, score: 7 } ] If you run the query Select * from FLATTEN(UNWIND(customerInfo WITH PATH => visits, INDEX => idx)) ,
Atlas SQL returns documents with the following top-level fields: id 1 1 1 location "New York" "New York" "New York" satisfaction 5 5 5 customer_age 50 50 50 customer_email "customer@email.com" "customer@email.com" "customer@email.com" idx 0 1 2 visits_year 2020 2021 2022 visits_score 10 8 7 When you use both the FLATTEN and UNWIND functions,
the visits array is unwound, and the resulting document is then flattened. Back Private Endpoint Next Manage Schemas