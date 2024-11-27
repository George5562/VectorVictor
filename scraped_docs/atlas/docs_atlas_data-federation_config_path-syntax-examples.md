# Define Path for S3 Data - MongoDB Atlas


Docs Home / MongoDB Atlas / Query Federated Data / Define Data Stores / AWS S3 Bucket Define Path for S3 Data On this page Overview Supported Parsing Functions Parsing Null Values from Filenames Parsing Padded Numbers from Filenames Unsupported Parsing Functions Examples Parse Single Field from Filename Parse Multiple Fields from Filename Use Regular Expression to Parse Fields from Filename Identify Ranges of Queryable Data from Filename Identify Nested Fields from Filename Create Partitions from ObjectIds Create Partitions from File Path Create Partitions from ISODate Generate Dynamic Collection Names from File Path Overview When you query documents in your S3 buckets, the Atlas Data Federation path value allows Data Federation to map the data inside your document to the
filename of the document. path supports parsing filenames in S3 buckets into computed fields.
Data Federation can add the computed fields to each document
generated from the parsed file. Data Federation can target
queries on those computed field values to only those files with
a matching file name. See Supported Parsing Functions and Examples for more information. path also supports creating partitions using partition attributes in the
path to the file. Data Federation can target queries on the
parameter defined in the partition attribute to only those files
that contain the query in the filename or partition prefix. Example Consider the following files in your S3 bucket: /users/26/1234.json /users/26/5678.json The JSON document 1234.json contains the following: { "name" : "jane doe" , "age" : 26 , "userID" : "1234" } your federated database instance configuration for the files in your S3 bucket defines
the following path : "path": "/users/{age int}/{userID string}" The following shows how Data Federation maps a query to the
partitions created from the path definition: db.users.findOne(                /users { / 40 "age" : 26 ----------------->   / 26 "userID" : "1234" ---------->     / 1234. json } / 5678. json ) If the computed field for the partition attribute already exists
in your document, Data Federation maps your query to the appropriate file.
If the computed field does not exist, Data Federation adds the computed
field to the document. For example, if the age field does not
exist in 1234.json , Data Federation adds the age field and value to 1234.json . Supported Parsing Functions You can specify a single parsing function on the filename. /path/to/files/{<fieldA> <data-type>} You can specify multiple parsing functions on the filename. /path/to/files/{<fieldA> <data-type>}-{<fieldB> <data-type>} You can specify parsing functions alongside static strings in
the filename: /path/to/files/prefix-{<fieldA> <data-type>}-suffix You can specify dot (i.e. . ) along the path to the filename. /path/to/files/{<fieldA>.<fieldB> <data-type>} You can specify ObjectIds in the path to the files to create
partitions. /path/to/files/{objid objectid} You can specify a range of ObjectIds in the path to the
files to create partitions. /path/to/files/{min(obj) objectid}-{max(obj) objectid} You can specify parsing functions along the path to the filename. /path/{<fieldA> <data-type>}/{<fieldB> <data-type>}/{<fieldC> <data-type>}/* You can specify regex for ISODate along the path to the
filename. /path/to/files/{<field-name> isodate("<date-format>"):\\<regex>} Note When specifying the path : Specify the data type for the partition attribute. Ensure that the partition attribute type matches the data type to parse. Use the delimiter specified in delimiter . When specifying attributes of the same type, do any of the following: Add a constant separator between the attributes. Use regular expressions to describe the search pattern. To learn more,
see Unsupported Parsing Functions . Parsing Null Values from Filenames Data Federation automatically parses an empty string ( "" ) in the place of an
attribute in the file path as the BSON null value for all the Atlas Data Federation
attribute types except string . With a string , empty string
could either represent a BSON null value or a BSON empty string value.
Atlas Data Federation does not parse any BSON value for string attribute type.
This avoids adding a BSON value with a conflicting type to documents
read from S3 . Example Consider the following S3 federated database instance store: /records/january/1.json /records/february/1.json /records//1.json For the path ``/records/{month string}/*``, Data Federation does not add any computed fields for the ``month`` attribute to documents generated from the third record in the above store. Note When writing files to S3 , write BSON null values as empty
strings in filenames for all Atlas Data Federation attribute types. Parsing Padded Numbers from Filenames File path can include numeric values that are padded with leading
zeros. For Data Federation to correctly parse padded numeric values for
attribute types like int , epoch_millis , and epoch_secs ,
specify the number of digits in the value using regular expressions. Example Consider a S3 store with the following files: |--users |--001.json |--002.json ... The following path syntax uses a regular expression to specify
the number of digits in the filename. Data Federation identifies the portion
of the path that corresponds to the partition attribute and then
maps that partition attribute to a type int : /users/{user_id int:\\d{3}} Unsupported Parsing Functions Specifying consecutive parsing functions on the same filename with
no way of differentiating them could lead to inconsistent results. Example Consider a S3 store with the following files: |--food |--icecream |--peanutbutter Now consider the following path to the files in the food directory: /food/{first string}{second string}/ There is no way to determine which part of the filename substring
should match the first versus second string attributes.
Therefore, Atlas Data Federation matches everything to first . Consider using attributes with regex similar to the following
instead: /food/{first string:\\D{3}}{second string:\\D{5}} The preceding path specifies that first matches 3 non-digit
characters and second matches the next 5 non-digit characters. /food/{first string:[A-Z]{3}}{second string:[a-z]{5}} The preceding path matches first to 3 uppercase letters and second to 5 lowercase letters. Examples The following examples demonstrate how to parse filenames into
computed fields: Parse Single Field from Filename Parse Multiple Fields from Filename Use Regular Expression to Parse Fields from Filename Identify Ranges of Queryable Data from Filename Identify Nested Fields from Filename Create Partitions from ObjectIds Create Partitions from File Path Create Partitions from ISODate Generate Dynamic Collection Names from File Path Parse Single Field from Filename Consider a federated database instance store accountingArchive containing files
where the filename describes an invoice date. For  example, the filename /invoices/1564671291998.json contains the invoices for the UNIX
timestamp 1564671291998 . The following databases object generates a
field invoiceDate by parsing the filename as a UNIX timestamp: "databases" : [ { "name" : "accounting", "collections" : [ { "name" : "invoices", "dataSources" : [ { "storeName" : "accountingArchive", "path" : "/invoices/{invoiceDate epoch_millis}" } ] } ] } ] Data Federation adds the computed field and value to each
document generated from the filename. Documents generated from the
example filename includes a field invoiceDate: ISODate("2019-08-01T14:54:51Z") . Queries on the invoiceDate field can be targeted to only those files
that match the specified value. Parse Multiple Fields from Filename Consider a federated database instance store accountingArchive containing files
where the filename describes an invoice number and invoice date. For
example, the filename /invoices/MONGO12345-1564671291998.json contains the invoice MONGODB12345 for the UNIX timestamp 1564671291998 . The following databases object
generates: A field invoiceNumber by parsing the first segment of the filename
as a string. A field invoiceDate by parsing the second segment of the filename
as a UNIX timestamp. "databases" : [ { "name": "accounting", "collections" : [ { "name" : "invoices", "dataSources" : [ { "storeName" : "accountingArchive", "path" : "/invoices/{invoiceNumber string}-{invoiceDate epoch_millis}" } ] } ] } ] Data Federation adds the computed fields and values to each
document generated from the filename. Documents generated from the
example filename include the following fields: invoiceNumber : "MONGODB12345" invoiceDate : ISODate("2019-08-01T14:54:51Z") Queries that include both the invoiceNumber and invoiceDate fields can be targeted to only those files that match the
specified values. Use Regular Expression to Parse Fields from Filename Consider a federated database instance store accountingArchive containing files
where the filename describes an invoice number and invoice date. For
example, the filename /invoices/MONGODB12345-20190102.json contains
the invoice MONGODB12345 for the date 20190102 . The following databases object
generates: A field invoiceNumber by parsing the first segment of the filename
as a string A field year by using a regular expression to parse only the
first 4 digits of the second segment of the filename as an int. A field month by using a regular expression to parse only the
next 2 digits of the second segment of the filename as an int. A field day by using a regular expression to parse only the
next 2 digits of the second segment of the filename as an int. "databases" : [ { "name" : "accounting", "collections" : [ { "name" : "invoices", "dataSources" : [ { "storeName" : "accountingArchive", "path" : "/invoices/{invoiceNumber string}-{year int:\\d{4}}{month int:\\d{2}}{day int:\\d{2}}" } ] } ] } ] Data Federation adds the computed fields and values to each
document generated from the filename. Documents generated from the
example filename include the following fields: invoiceNumber : "MONGODB12345" year : 2019 month: 01 day: 02 Important You must escape the regex string specified in the path . For
example, if the regex string includes double quotes, you must
escape those values. Data Federation supports the Package Syntax for regular expressions
in the storage configuration. Queries that include all generated fields can be targeted to only
those files that match the specified values. Tip See also: Parsing Padded Numbers from Filenames Identify Ranges of Queryable Data from Filename Consider a federated database instance store accountingArchive containing files
where the filename describes the range of data contained in the file.
For example, the filename /invoices/1546367712000-1549046112000.json contains invoices for
the time period between 2019-01-01 and 2019-01-02 with the date range
represented as milliseconds elapsed since the UNIX epoch. The following databases object identifies
the minimum time range as the first segment of the filename and the
maximum time range as the second segment of the filename: "databases" : [ { "name: "accounting", "collections" : [ { "name: "invoices", "dataSources" : [ { "storeName" : "accountingArchive", "path" : "/invoices/{min(invoiceDate) epoch_millis}-{max(invoiceDate) epoch_millis}" } ] } ] } ] When Data Federation receives a query on the "invoiceDate" field, it uses
the specified path to identify which files contain the data that
matches the query. Queries on the invoiceDate field can be targeted to only those
files whose range captures the specified value, including the min and max date. Important The field specified for the min and max ranges must exist in
every document contained in the file to avoid unexpected or
undesired behavior. Data Federation does not perform any
validation that the underlying data conforms to this constraint. Tip See also: Parsing Padded Numbers from Filenames Identify Nested Fields from Filename Data Federation supports querying nested data when the nested data
value is also the filename. You can use the dot operator (i.e. . )
in your path to map the partitions attributes in your storage configuration to
nested fields in your documents. Consider a federated database instance store accountingArchive . The federated database instance store
contains files with names that match values of nested fields in the
documents. For example: accountingArchive |--invoices |--January.json |--February.json ... Suppose the January.json file contains a document with the
following fields: { "invoice": { "invoiceNumber" : "MONGODB12345", "year" : 2019, "month": "January", //value matches filename "date": 02 }, "vendor": "MONGODB", ... } The following databases object identifies month as a nested field inside a document. The databases object also identifies the value of month as the name of the file that contains the document. "databases" : [ { "name" : "accounting", "collections" : [ { "name" : "invoices", "dataSources" : [ { "storeName" : "accountingArchive", "path" : "/invoices/{invoice.month string}" } ] } ] } ] When Atlas Data Federation receives a query on a specific month such as January , it uses the specified path to identify which file
contains the data that matches the query. Create Partitions from ObjectIds You can specify ObjectIds in the path to the files. For files that contain ObjectId in the
filename, Atlas Data Federation creates partitions for each ObjectId . Consider the following federated database instance store, accountingArchive . This data
store contains files that include ObjectId in the filename: accountingArchive |--invoices |--507f1f77bcf86cd799439011.json |--507f1f77bcf86cd799439012.json |--507f1f77bcf86cd799439013.json |--507f1f77bcf86cd799439014.json |--507f1f77bcf86cd799439015.json The following databases object creates
partitions for the ObjectIds . "databases" : [ { "name" : "accounting", "collections" : [ { "name" : "invoices", "dataSources" : [ { "storeName" : "accountingArchive", "path" : "/invoices/{objid objectid}" } ] } ] } ] Or, suppose the federated database instance store accountingArchive contains
files that include a range of ObjectIds in the filename. For
example: accountingArchive |--invoices |--507f1f77bcf86cd799439011-507f1f77bcf86cd799439020.json |--507f1f77bcf86cd799439021-507f1f77bcf86cd799439030.json |--507f1f77bcf86cd799439031-507f1f77bcf86cd799439040.json The following databases object creates
partitions for the given range of ObjectIds . "databases" : [ { "name" : "accounting", "collections" : [ { "name" : "invoices", "dataSources" : [ { "storeName" : "accountingArchive", "path" : "/invoices/{min(obj) objectid}-{max(obj) objectid}" } ] } ] } ] When Data Federation receives a query on the ObjectId , it uses the
specified path to identify which file contains the data that matches
the query. Create Partitions from File Path You can specify parsing functions on any path leading up to the
filename. Each computed field is based on a parsing function along the
path. When querying the data, Atlas Data Federation converts each computed field to a
partition. Partitions, which are synonymous with subdirectories, are
then used to filter files with increasing precision. Consider a federated database instance store accountingArchive with the following
directory structure: invoices |--MONGO12345 |--2019 |--01 |--02 The following databases object creates the invoiceNumber , year , month , and day partitions with
a small set of filtered files: "databases" : [ { "name" : "accounting", "collections" : [ { "name" : "invoices", "dataSources" : [ { "storeName" : "accountingArchive", "path" : "/invoices/{invoiceNumber string}/{year int}/{month int:\\d{2}}/{day int:\\d{2}}/*" } ] } ] } } Tip See also: Parsing Padded Numbers from Filenames Create Partitions from ISODate You can specify ISODate in the path to the files. For files that contain ISODate in the
filename, Atlas Data Federation creates partitions for each ISODate . Consider the following federated database instance store, accountingArchive . This data
store contains files that include ISODate in the filename: accountingArchive |--invoices |--01_02_2022_2301.json |--02_02_2022_2301.json |--03_02_2022_2301.json |--04_02_2022_2301.json |--05_02_2022_2301.json The following databases object creates
partitions for the ISODate . The path demonstrates how to use
regex for the date format if the date is not in RFC 3339 format. "databases" : [ { "name" : "accounting", "collections" : [ { "name" : "invoices", "dataSources" : [ { "storeName" : "accountingArchive", "path" : "/invoices/creationDate isodate('01_02_2006_1504'):\\d{2}_\\d{2}_\\d{4}_\\d{4}.json" } ] } ] } ] To learn more about other supported formats, see Use Partition Attribute Types . Generate Dynamic Collection Names from File Path Consider a federated database instance store accountingArchive with the
following directory structure: invoices |--SuperSoftware |--UltraSoftware |--MegaSoftware The following databases object
generates a dynamic collection name from the file path: "databases" : [ { "name" : "invoices" , "collections" : [ { "name" : "*" , "dataSources" : [ { "storeName" : "accountingArchive" , "path" : "/invoices/{collectionName()}/" } ] } ] } ] When applied to the example directory structure, the path
results in the following collections: SuperSoftware UltraSoftware MegaSoftware Or, consider a federated database instance store accountingArchive with the
following files: /orders/MONGODB/invoices/January.json /orders/MONGODB/purchaseOrders/January.json /orders/MONGODB/invoices/February.json ... The following databases object
generates a dynamic collection name from the file path: "databases" : [ { "name" : "invoices" , "collections" : [ { "name" : "*" , "dataSources" : [ { "storeName" : "accountingArchive" , "path" : "/orders/MONGODB/{collectionName()}/{invoiceMonth string}.json/" } ] } ] } ] When applied to the example filenames, the path
results in the following collections: invoices purchaseOrders Note When you dynamically generate collections from filenames,
the number of collections is not accurately reported in the Data Federation view. Back Generate Collections Next Optimize Queries
