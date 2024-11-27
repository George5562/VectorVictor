# $replaceOne (aggregation) - MongoDB Manual v8.0


Docs Home / MongoDB Manual / Aggregation Operations / Reference / Operators $replaceOne (aggregation) On this page Definition Syntax Behavior Example Definition $replaceOne Replaces the first instance of a search string in an input string
with a replacement string. If no occurrences are found, $replaceOne evaluates to
the input string. $replaceOne is both case-sensitive and
diacritic-sensitive, and ignores any collation present on a
collection. Syntax The $replaceOne operator has the following operator expression syntax : { $replaceOne : { input : < expression > , find : < expression > , replacement : < expression > } } Operator Fields Field Description input The string on which you wish to apply the find . Can be any valid expression that resolves to a
string or a null . If input refers to a field that is
missing, $replaceOne returns null . find The string to search for within the given input . Can be any valid expression that resolves to a
string or a null . If find refers to a field that is
missing, $replaceOne returns null . replacement The string to use to replace the first matched instance of find in input .
Can be any valid expression that
resolves to a string or a null . Behavior If no occurrences of find are found in input , $replaceOne evaluates to
the input string. The input , find , and replacement expressions must evaluate to
a string or a null , or $replaceOne fails with an
error. $replaceOne and Null Values If input or find refer to a field that is missing, they return null . If any one of input , find , or replacement evaluates to a null , the
entire $replaceOne expression evaluates to null : Example Result { $replaceOne: { input: null, find: "abc", replacement: "ABC" } } null { $replaceOne: { input: "abc", find: null, replacement: "ABC" } } null { $replaceOne: { input: "abc", find: "abc", replacement: null } } null $replaceOne and Collation String matching for all $replaceOne expressions is always
case-sensitive and diacritic-sensitive. Any collation configured is ignored when performing string comparisons with $replaceOne . For example, create a sample collection with collation strength 1 : db. createCollection ( "myColl" , { collation : { locale : "fr" , strength : 1 } } ) A collation strength of 1 compares base character only and ignores
other differences such as case and diacritics. Next, insert three example documents: db. myColl . insertMany ( [ { _id : 1 , name : "cafe" } , { _id : 2 , name : "Cafe" } , { _id : 3 , name : "cafÃ©" } ]) The following $replaceOne operation tries to find and
replace the first instance of "Cafe" in the name field: db. myColl . aggregate ( [ { $addFields : { resultObject : { $replaceOne : { input : "$name" , find : "Cafe" , replacement : "CAFE" } } } } ]) Because $replaceOne ignores the collation configured for
this collection, the operation only matches the instance of "Cafe" in
document 2 : { "_id" : 1 , "name" : "cafe" , "resultObject" : "cafe" } { "_id" : 2 , "name" : "Cafe" , "resultObject" : "CAFE" } { "_id" : 3 , "name" : "cafÃ©" , "resultObject" : "cafÃ©" } Operators which respect collation, such as $match , would
match all three documents when performing a string comparison against
"Cafe" due to this collection's collation strength of 1 . $replaceOne and Unicode Normalization The $replaceOne aggregation expression does not perform
any unicode normalization. This means that string matching for all $replaceOne expressions will consider the number of code points used
to represent a character in unicode when attempting a match. For example, the character Ã© can be represented in unicode using
either one code point or two: Unicode Displays as Code points \xe9 Ã© 1 ( \xe9 ) e\u0301 Ã© 2 ( e + \u0301 ) Using $replaceOne with a find string where the character Ã© is represented in unicode with one code
point will not match any instance of Ã© that uses two code points in
the input string. The following table shows whether a match occurs for a find string of "cafÃ©" when compared to input strings where Ã© is represented
by either one code point or two. The find string in this example uses one code point to represent the Ã© character: Example Match { $replaceOne: { input: "caf\xe9", find: "cafÃ©", replacement: "CAFE" } } yes { $replaceOne: { input: "cafe\u0301", find: "cafÃ©", replacement: "CAFE" } } no Because $replaceOne does not perform any unicode
normalization, only the first string comparison matches, where both the find and input strings use one code point to represent Ã© . Example Create an inventory collection with the following documents: db. inventory . insertMany ( [ { "_id" : 1 , "item" : "blue paint" } , { "_id" : 2 , "item" : "blue and green paint" } , { "_id" : 3 , "item" : "blue paint with blue paintbrush" } , { "_id" : 4 , "item" : "blue paint with green paintbrush" } , ]) The following example replaces the first instance of "blue paint" in the item field with "red paint": db. inventory . aggregate ( [ { $project : { item : { $replaceOne : { input : "$item" , find : "blue paint" , replacement : "red paint" } } } } ]) The operation returns the following results: { "_id" : 1 , "item" : "red paint" } { "_id" : 2 , "item" : "blue and green paint" } { "_id" : 3 , "item" : "red paint with blue paintbrush" } { "_id" : 4 , "item" : "red paint with green paintbrush" } Note that with document 3 , only the first matched instance of
"blue paint" is replaced. Back $regexMatch Next $replaceAll
