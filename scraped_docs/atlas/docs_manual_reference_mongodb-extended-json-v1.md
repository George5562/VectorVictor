# MongoDB Extended JSON (v1) - MongoDB Manual v8.0


Docs Home / MongoDB Manual / Introduction / BSON Types MongoDB Extended JSON (v1) On this page MongoDB Extended JSON v1 and MongoDB Drivers Parsers and Supported Format BSON Data Types and Associated Representations Important Disambiguation The following page discusses MongoDB Extended JSON v1 (Legacy
extended JSON). For discussion on MongoDB Extended JSON v2, see MongoDB Extended JSON (v2) . For supported data types in mongo , see mongosh Data Types . JSON can only represent a subset of the types supported by BSON . To preserve type information, MongoDB adds the following
extensions to the JSON format: Strict mode . Strict mode representations of BSON types conform to
the JSON RFC . Any JSON parser can parse
these strict mode representations as key/value pairs; however, only
the MongoDB internal JSON parser recognizes the type
information conveyed by the format. mongo Shell mode . The MongoDB internal JSON parser and the mongo shell can parse this mode. The representation used for the various data types depends on the
context in which the JSON is parsed. MongoDB Extended JSON v1 and MongoDB Drivers The following drivers use the Extended JSON v1.0 (Legacy) C# Ruby For the other drivers, refer to MongoDB Extended JSON (v2) . Parsers and Supported Format Input in Strict Mode The following can parse representations in strict mode with recognition of the type information. mongoimport version 4.0 and earlier --query option of various MongoDB tools MongoDB Compass Other JSON parsers, including mongo shell, can parse
strict mode representations as key/value pairs, but without recognition of the type information. Input in mongo Shell Mode The following can parse representations in mongo shell mode with recognition of the type information. mongoimport version 4.0 and earlier --query option of various MongoDB tools mongo shell Output in Strict mode Before version 4.2, mongoexport outputs data in Strict mode of MongoDB Extended JSON v1. Output in mongo Shell Mode Before version 4.2, bsondump outputs in mongo Shell
mode . BSON Data Types and Associated Representations The following presents the BSON data types and the associated
representations in Strict mode and mongo Shell mode . Binary data_binary Strict Mode mongo Shell Mode { "$binary": "<bindata>", "$type": "<t>" } BinData ( <t>, <bindata> ) Where the values are as follows: <bindata> is the base64 representation of a binary string. <t> is a representation of a single byte indicating the data type. In Strict mode it is a hexadecimal string, and in Shell mode it is an integer.
See the extended bson documentation. http://bsonspec.org/spec.html Date data_date Strict Mode mongo Shell Mode { "$date": "<date>" } new Date ( <date> ) In Strict mode , <date> is an ISO-8601 date format with a mandatory time
zone field following the template YYYY-MM-DDTHH:mm:ss.mmm<+/-Offset> . In Shell mode , <date> is the JSON representation of a 64-bit signed
integer giving the number of milliseconds since epoch UTC. Timestamp data_timestamp Strict Mode mongo Shell Mode { "$timestamp": { "t": <t>, "i": <i> } } Timestamp( <t>, <i> ) Where the values are as follows: <t> is the JSON representation of a 32-bit unsigned integer for
seconds since epoch. <i> is a 32-bit unsigned integer for the increment. Regular Expression data_regex Strict Mode mongo Shell Mode { "$regex": "<sRegex>", "$options": "<sOptions>" } /<jRegex>/<jOptions> Where the values are as follows: <sRegex> is a string of valid JSON characters. <jRegex> is a string that may contain valid JSON characters and
unescaped double quote ( " ) characters, but may not contain
unescaped forward slash ( / ) characters. <sOptions> is a string containing the regex options represented
by the letters of the alphabet. <jOptions> is a string that may contain only the characters 'g',
'i', 'm' and 's' (added in v1.9). Because the JavaScript and mongo Shell representations support a limited range of options,
any nonconforming options will be dropped when converting to this
representation. OID data_oid Strict Mode mongo Shell Mode { "$oid": "<id>" } ObjectId( "<id>" ) Where the values are as follows: <id> is a 24-character hexadecimal string. DB Reference data_ref Strict Mode mongo Shell Mode { "$ref": "<name>", "$id": "<id>" } DBRef("<name>", "<id>") Where the values are as follows: <name> is a string of valid JSON characters. <id> is any valid extended JSON type. Undefined Type data_undefined Strict Mode mongo Shell Mode { "$undefined": true } undefined The representation for the JavaScript/BSON undefined type. You cannot use undefined in query documents.
Consider the following document inserted into the people collection using the legacy mongo shell: db.people.insertOne( { name : "Sally" , age : undefined } ) The following queries return an error: db.people.find( { age : undefined } ) db.people.find( { age : { $gte : undefined } } ) However, you can query for undefined values using $type , as
in: db.people.find( { age : { $type : 6 } } ) This query returns all documents for which the age field has
value undefined . Important The undefined BSON type is deprecated . mongosh stores
a null value instead. For example, use the same code to insert a document in mongosh and in the legacy mongo shell: db. people . insertOne ( { name : "Sally" , age : undefined } ) The resulting documents are different: { "name" : "Sally", "age" : null } { "name" : "Sally", "age" : undefined } MinKey data_minkey Strict Mode mongo Shell Mode { "$minKey": 1 } MinKey The representation of the MinKey BSON data type that compares lower
than all other types. See Comparison/Sort Order for more information on
comparison order for BSON types. MaxKey data_maxkey Strict Mode mongo Shell Mode { "$maxKey": 1 } MaxKey The representation of the MaxKey BSON data type that compares higher
than all other types. See Comparison/Sort Order for more information on
comparison order for BSON types. NumberLong data_numberlong Strict Mode mongo Shell Mode { "$numberLong": "<number>" } NumberLong( "<number>" ) NumberLong is a 64 bit signed integer. In the legacy mongo shell, you must use quotation marks to insert a NumberLong or the operation will produce an error. For example, the following commands attempt to insert 9223372036854775807 as a NumberLong with and without
quotation marks around the integer value: db.json.insertOne( { longQuoted : NumberLong( "9223372036854775807" ) } ) db.json.insertOne( { longUnQuoted : NumberLong(9223372036854775807) } ) The highlighted line produces an error in the legacy mongo shell. The insert succeeds in mongosh . NumberDecimal data_numberdecimal Strict Mode mongo Shell Mode { "$numberDecimal": "<number>" } NumberDecimal( "<number>" ) NumberDecimal is a high-precision decimal . You must include quotation marks, or the
input number will be treated as a double, resulting in data loss. For example, the following commands insert 123.40 as a NumberDecimal with and without quotation marks around the value: db.json.insertOne( { decimalQuoted : NumberDecimal( "123.40" ) } ) db.json.insertOne( { decimalUnQuoted : NumberDecimal(123.40) } ) When you retrieve the documents, the value of decimalUnQuoted has
changed, while decimalQuoted retains its specified precision: db.json. find () { "_id" : ObjectId( "596f88b7b613bb04f80a1ea9" ), "decimalQuoted" : NumberDecimal( "123.40" ) } { "_id" : ObjectId( "596f88c9b613bb04f80a1eaa" ), "decimalUnQuoted" : NumberDecimal( "123.400000000000" ) } Important This insert behavior is different in mongosh . The quoted string format, NumberDecimal("123.40") , is
deprecated. The insert succeeds, but also produces a warning. The unquoted string format, NumberDecimal(123.40) ,
stores the value as 123.4 . The trailing 0 is dropped. Back Extended JSON (v2) Next CRUD Operations