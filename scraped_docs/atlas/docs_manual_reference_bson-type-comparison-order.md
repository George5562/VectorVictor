# Comparison/Sort Order - MongoDB Manual v8.0


Docs Home / MongoDB Manual / Introduction / BSON Types Comparison/Sort Order On this page Numeric Types Strings Arrays Objects Dates and Timestamps Non-existent Fields BinData When comparing values of different BSON types in
sort operations, MongoDB uses the following comparison order, from
lowest to highest: MinKey (internal type) Null Numbers (ints, longs, doubles, decimals) Symbol, String Object Array BinData ObjectId Boolean Date Timestamp Regular Expression JavaScript Code MaxKey (internal type) Note Range query operators perform
comparisons only on fields where the BSON type matches the query value's type. MongoDB enforces
comparisons with Comparison Query Operators only on documents where the BSON type of the target field
matches the query operand type through Type Bracketing . Numeric Types MongoDB treats some types as equivalent for comparison purposes. For
instance, numeric types undergo conversion before comparison. Strings Binary Comparison By default, MongoDB uses the simple binary comparison to compare
strings. Collation Collation allows users to specify
language-specific rules for string comparison, such as rules for
lettercase and accent marks. Collation specification has the following syntax: { locale: <string>, caseLevel: <boolean>, caseFirst: <string>, strength: <int>, numericOrdering: <boolean>, alternate: <string>, maxVariable: <string>, backwards: <boolean> } When specifying collation, the locale field is mandatory; all
other collation fields are optional. For descriptions of the fields,
see Collation Document . If no collation is specified for the collection or for the
operations, MongoDB uses the simple binary comparison used in prior
versions for string comparisons. Arrays In array comparisons: An ascending sort compares the smallest
elements of the array according to the BSON type sort order. A descending sort compares the largest elements of the array according
to the reverse BSON type sort order. Comparison Query Operators , such as $lt and $gt ,
perform comparisons on arrays lexicographically. When comparing a field whose value is a one element array (for example, [ 1 ] ) with non-array fields (for example, 2 ), the comparison is
for 1 and 2 . A comparison of an empty array (for example, [ ] ) considers the empty
array as less than a null value or a missing field value. A comparison of a nested array (for example, [[1, 2], [3, 4]] ) compares
any array after the outmost array lexicographically. Note Comparison Query Operators enforce type-bracketing when
the query is an array. If the indexed value is an array,
the operator performs a type-bracketed comparison
element-wise over the indexed array. Objects MongoDB's comparison of BSON objects uses the following order: Recursively compare key-value pairs in the order that they appear
within the BSON object. Compare the field types. MongoDB uses the following comparison
order for field types, from lowest to highest: MinKey (internal type) Null Numbers (ints, longs, doubles, decimals) Symbol, String Object Array BinData ObjectId Boolean Date Timestamp Regular Expression JavaScript Code MaxKey (internal type) If the field types are equal, compare the key field names . If the key field names are equal, compare the field values. If the field values are equal, compare the next key/value pair
(return to step 1). An object without further pairs is less than an
object with further pairs. Dates and Timestamps Date objects sort before Timestamp objects. Non-existent Fields The comparison treats a non-existent field as if it were null. A
sort on the a field in documents { } and { a: null } would treat the documents as equivalent in sort order. BinData MongoDB sorts BinData in the following order: First, the length or size of the data. Then, by the BSON one-byte subtype. Finally, by the data, performing a byte-by-byte comparison on unsigned bytes. Back BSON Types Next Migrate Undefined Data and Queries
