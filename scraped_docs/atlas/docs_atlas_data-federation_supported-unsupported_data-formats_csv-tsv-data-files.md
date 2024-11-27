# CSV and TSV - MongoDB Atlas


Docs Home / MongoDB Atlas / Query Federated Data / Define Data Stores / AWS S3 Bucket / Data Formats CSV and TSV Your CSV or TSV file must start with a header row. Atlas Data Federation utilizes the
header row as field names. The dot-delimited field names in the header
row become nested fields or objects in JSON format. For each dot in
the field name, Data Federation creates another level of nesting. Example Suppose your federated database instance is reading a CSV file with content
similar to the following: company,location.state,location.city.name,location.city.street "MongoDB", "California", "Palo Alto", "Forest Ave" For the data fields in the above example CSV file, Data Federation
creates the following JSON document: { "company" : "MongoDB" , "location" : { "state" : "California" , "city" : { "name" : "Palo Alto" , "street" : "Forest Ave" , } } Data Federation requires all field names at the same level of nesting
to be unique. The following are examples of invalid field names
in the header row: One field duplicates another field at the same level of nesting. Example Consider the following: company,location,company In the header, company is included twice at the same level of
nesting. One dot-delimited field duplicates another field at the same level
of nesting. Example Consider the following: company,location,location.city In the header, location is both a stand-alone field
and dot-delimited field at the same level of nesting. Back Parquet Next Limitations
