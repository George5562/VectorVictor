# Documents - MongoDB Manual v8.0


Docs Home / MongoDB Manual / Introduction Documents On this page Compatibility Document Structure Dot Notation Document Limitations Other Uses of the Document Structure Further Reading MongoDB stores data records as BSON documents. BSON is a binary
representation of JSON documents, though it contains more data
types than JSON. For the BSON spec, see bsonspec.org . See also BSON Types . Compatibility MongoDB stores records as documents for deployments hosted in the
following environments: MongoDB Atlas : The fully
managed service for MongoDB deployments in the cloud MongoDB Enterprise : The
subscription-based, self-managed version of MongoDB MongoDB Community : The
source-available, free-to-use, and self-managed version of MongoDB Document Structure MongoDB documents are composed of field-and-value pairs and have the
following structure: { field1 : value1 , field2 : value2 , field3 : value3 , ... fieldN : valueN } The value of a field can be any of the BSON data types , including other documents, arrays, and arrays
of documents. For example, the following document contains values of varying types: var mydoc = { _id : ObjectId ( "5099803df3f4948bd2f98391" ) , name : { first : "Alan" , last : "Turing" } , birth : new Date ( 'Jun 23, 1912' ) , death : new Date ( 'Jun 07, 1954' ) , contribs : [ "Turing machine" , "Turing test" , "Turingery" ] , views : NumberLong ( 1250000 ) } The above fields have the following data types: _id holds an ObjectId . name holds an embedded document that contains the fields first and last . birth and death hold values of the Date type. contribs holds an array of strings . views holds a value of the NumberLong type. Field Names Field names are strings. Documents have the following restrictions on field
names: The field name _id is reserved for use as a primary key; its value
must be unique in the collection, is immutable, and may be of any type
other than an array or regex. If the _id contains subfields, the
subfield names cannot begin with a ( $ ) symbol. Field names cannot contain the null character. The server permits storage of field names that contain dots ( . )
and dollar signs ( $ ). MongodB 5.0 adds improved support for the use of ( $ ) and ( . )
in field names. There are some restrictions. See Field Name Considerations for more details. Each field name must be unique within the document. You must not store
documents with duplicate fields because MongoDB CRUD operations might behave unexpectedly if a document has duplicate
fields. The MongoDB Query Language does not support documents with duplicate
field names. While some BSON builders may support creating a BSON document with
duplicate field names, inserting these documents into MongoDB is not supported even if the insert succeeds, or appears to succeed. For example, inserting a
BSON document with duplicate field names through a MongoDB driver may result in
the driver silently dropping the duplicate values prior to insertion, or may
result in an invalid document being inserted that contains duplicate fields. Querying against any such documents would lead to arbitrary and inconsistent results. Dot Notation MongoDB uses the dot notation to access the elements of an array and
to access the fields of an embedded document. Arrays To specify or access an element of an array by the zero-based index
position, concatenate the array name with the dot ( . ) and
zero-based index position, and enclose in quotes: "<array>.<index>" For example, given the following field in a document: { ... contribs : [ "Turing machine" , "Turing test" , "Turingery" ] , ... } To specify the third element in the contribs array, use the dot
notation "contribs.2" . For examples querying arrays, see: Query an Array Query an Array of Embedded Documents Tip See also: $[] all positional operator for update operations, $[<identifier>] filtered positional operator for update operations, $ positional operator for update operations, $ projection operator when array index position is
unknown Query an Array for dot notation examples with arrays. Embedded Documents To specify or access a field of an embedded document with dot notation,
concatenate the embedded document name with the dot ( . ) and
the field name, and enclose in quotes: "<embedded document>.<field>" For example, given the following field in a document: { ... name : { first : "Alan" , last : "Turing" } , contact : { phone : { type : "cell" , number : "111-222-3333" } } , ... } To specify the field named last in the name field, use the
dot notation "name.last" . To specify the number in the phone document in the contact field, use the dot notation "contact.phone.number" . Warning Partition fields cannot use field names that contain a dot ( . ). For examples querying embedded documents, see: Query on Embedded/Nested Documents Query an Array of Embedded Documents Document Limitations Documents have the following attributes: Document Size Limit The maximum BSON document size is 16 megabytes. The maximum document size helps ensure that a single document cannot
use excessive amount of RAM or, during transmission, excessive amount
of bandwidth. To store documents larger than the maximum size, MongoDB
provides the GridFS API. See mongofiles and the
documentation for your driver for more
information about GridFS. Document Field Order Unlike JavaScript objects, the fields in a BSON document are ordered. Field Order in Queries For queries, the field order behavior is as follows: When comparing documents, field ordering is significant. For
example, when comparing documents with fields a and b in a
query: {a: 1, b: 1} is equal to {a: 1, b: 1} {a: 1, b: 1} is not equal to {b: 1, a: 1} For efficient query execution, the query engine may reorder fields
during query processing. Among other cases, reordering fields may
occur when processing these projection operators: $project , $addFields , $set , and $unset . Field reordering may occur in intermediate results as well as the
final results returned by a query. Because some operations may reorder fields, you should not rely on
specific field ordering in the results returned by a query that
uses the projection operators listed earlier. Field Order in Write Operations For write operations, MongoDB preserves the order of the document fields except for the following cases: The _id field is always the first field in the document. Updates that include renaming of field names may
result in the reordering of fields in the document. The _id Field In MongoDB, each document stored in a collection requires a unique _id field that acts as a primary key . If an inserted
document omits the _id field, the MongoDB driver automatically
generates an ObjectId for the _id field. This also applies to documents inserted through update
operations with upsert: true . The _id field has the following behavior and constraints: By default, MongoDB creates a unique index on the _id field
during the creation of a collection. The _id field is always the first field in the documents. If the
server receives a document that does not have the _id field
first, then the server will move the field to the beginning. If the _id contains subfields, the subfield names cannot begin
with a ( $ ) symbol. The _id field may contain values of any BSON data type , other than an array, regex, or undefined. Warning To ensure functioning replication, do not store values
that are of the BSON regular expression type in the _id field. The following are common options for storing values for _id : Use an ObjectId . Use a natural unique identifier, if available. This saves space and
avoids an additional index. Generate an auto-incrementing number. Generate a UUID in your application code. For a more efficient
storage of the UUID values in the collection and in the _id index, store the UUID as a value of the BSON BinData type. Index keys that are of the BinData type are more efficiently stored
in the index if: the binary subtype value is in the range of 0-7 or 128-135, and the length of the byte array is: 0, 1, 2, 3, 4, 5, 6, 7, 8, 10, 12,
14, 16, 20, 24, or 32. Use your driver's BSON UUID facility to generate UUIDs. Be aware
that driver implementations may implement UUID serialization and
deserialization logic differently, which may not be fully compatible
with other drivers. See your driver documentation for
information concerning UUID interoperability. Note Most MongoDB driver clients include the _id field and
generate an ObjectId before sending the insert operation to
MongoDB. However, if the client sends a document without an _id field, the mongod adds the _id field and generates
the ObjectId . Other Uses of the Document Structure In addition to defining data records, MongoDB uses the document
structure throughout, including but not limited to: query filters , update specifications documents , and index specification
documents Query Filter Documents Query filter documents specify the conditions that determine which
records to select for read, update, and delete operations. You can use <field>:<value> expressions to specify the equality
condition and query operator expressions. { < field1 > : < value1 > , < field2 > : { < operator > : < value > } , ... } For examples, see: Query Documents Query on Embedded/Nested Documents Query an Array Query an Array of Embedded Documents Update Specification Documents Update specification documents use update operators to specify the data modifications to perform on
specific fields during an update operation. { < operator1 > : { < field1 > : < value1 > , ... } , < operator2 > : { < field2 > : < value2 > , ... } , ... } For examples, see Update specifications . Index Specification Documents Index specification documents define the field to index and the index
type: { < field1 > : < type1 > , < field2 > : < type2 > , ... } Further Reading For more information on the MongoDB document model, download the MongoDB Application Modernization Guide . The download includes the following resources: Presentation on the methodology of data modeling with MongoDB White paper covering best practices and considerations for
migrating to MongoDB from an RDBMS data model Reference MongoDB schema with its RDBMS equivalent Application Modernization scorecard Back Clustered Collections Next Query API
