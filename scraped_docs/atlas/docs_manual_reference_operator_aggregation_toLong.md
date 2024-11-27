# $toLong (aggregation) - MongoDB Manual v8.0


Docs Home / MongoDB Manual / Aggregation Operations / Reference / Operators $toLong (aggregation) On this page Definition Behavior Example Definition $toLong Converts a value to a long. If the value cannot be converted
to a long, $toLong errors. If the value is null or
missing, $toLong returns null. $toLong has the following syntax: { $toLong : < expression > } The $toLong takes any valid expression . The $toLong is a shorthand for the following $convert expression: { $convert : { input : < expression > , to : "long" } } Tip See also: $convert Behavior The following table lists the input types that can be converted to a
long: Input Type Behavior Boolean Returns Long(0) for false . Returns Long(1) for true . Double Returns truncated value. The truncated double value must fall within the minimum and
maximum value for a long. You cannot convert a double value whose truncated value is less
than the minimum long value or is greater than the maximum
long value. Decimal Returns truncated value. The truncated decimal value must fall within the minimum and
maximum value for a long. You cannot convert a decimal value whose truncated value is less
than the minimum long value or is greater than the maximum
long value. Integer Returns the int value as a long. Long No-op. Returns the long value. String Returns the numerical value of the string. The string value must be of a base 10 long (e.g. "-5" , "123456" ). You cannot convert a string value of a float or decimal or
non-base 10 number (e.g. "-5.0" , "0x6400" ) Date Converts the Date into the number of milliseconds since the
epoch. The following table lists some conversion to long examples: Example Results { $toLong: true } Long("1") { $toLong: false } Long("0") { $toLong: 1.99999 } Long("1") { $toLong: NumberDecimal("5.5000") } Long("5") { $toLong: NumberDecimal("9223372036854775808.0") } Error { $toLong: NumberInt(8) } Long(8) { $toLong: ISODate("2018-03-26T04:38:28.044Z") } Long("1522039108044") { $toLong: "-2" } Long("-2") { $toLong: "2.5" } Error { $toLong: null } null Example Create a collection orders with the following documents: db. orders . insertMany ( [ { _id : 1 , item : "apple" , qty : NumberInt ( 5 ) } , { _id : 2 , item : "pie" , qty : "100" } , { _id : 3 , item : "ice cream" , qty : NumberLong ( "500" ) } , { _id : 4 , item : "almonds" , qty : "50" } , ] ) The following aggregation operation on the orders collection
converts the qty to long before sorting by the value: // Define stage to add convertedQty field with converted qty value qtyConversionStage = { $addFields : { convertedQty : { $toLong : "$qty" } } } ; // Define stage to sort documents by the converted qty values sortStage = { $sort : { "convertedQty" : - 1 } } ; db. orders . aggregate ( [ qtyConversionStage , sortStage ]) The operation returns the following documents: { _id : 3 , item : 'ice cream' , qty : Long ( "500" ) , convertedQty : Long ( "500" ) } , { _id : 2 , item : 'pie' , qty : '100' , convertedQty : Long ( "100" ) } , { _id : 4 , item : 'almonds' , qty : '50' , convertedQty : Long ( "50" ) } , { _id : 1 , item : 'apple' , qty : 5 , convertedQty : Long ( "5" ) } Note If the conversion operation encounters an error, the aggregation
operation stops and throws an error. To override this behavior, use $convert instead. Back $toInt Next $toObjectId
