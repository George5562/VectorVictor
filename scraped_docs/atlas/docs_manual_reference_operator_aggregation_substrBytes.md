# $substrBytes (aggregation) - MongoDB Manual v8.0


Docs Home / MongoDB Manual / Aggregation Operations / Reference / Operators $substrBytes (aggregation) On this page Definition Behavior Example Definition $substrBytes Returns the substring of a string. The substring starts with the
character at the specified UTF-8 byte index (zero-based) in the
string and continues for the number of bytes specified. $substrBytes has the following operator
expression syntax : { $substrBytes : [ <string expression>, <byte index>, <byte count> ] } Field Type Description string expression string The string from which the substring will be extracted. string expression can be any valid expression as
long as it resolves to a string. For more information on
expressions, see Expression Operators . If the argument resolves to a value of null or refers to a field
that is missing, $substrBytes returns an empty string. If the argument does not resolve to a string or null nor
refers to a missing field, $substrBytes returns an error. byte index number Indicates the starting point of the substring. byte index can be
any valid expression as long as
it resolves to a non-negative integer or number that can be
represented as an integer (such as 2.0). byte index cannot refer
to a starting index located in the middle of a multi-byte UTF-8
character. byte count number Can be any valid expression as long as it resolves to a non-negative integer or number that can be
represented as an integer (such as 2.0). byte count can not
result in an ending index that is in the middle of a UTF-8 character. Behavior The $substrBytes operator uses the indexes of UTF-8
encoded bytes where each code point, or character, may use between one
and four bytes to encode. For example, US-ASCII characters are encoded using one byte. Characters
with diacritic markings and additional Latin alphabetical characters
(Latin characters outside of the English alphabet) are encoded
using two bytes. Chinese, Japanese and Korean characters typically
require three bytes, and other planes of unicode (emoji, mathematical
symbols, etc.) require four bytes. It is important to be mindful of the content in the string expression because providing a byte index or byte count located in the middle of a UTF-8 character will result
in an error. $substrBytes differs from $substrCP in that $substrBytes counts the bytes of each character, whereas $substrCP counts the code points, or characters,
regardless of how many bytes a character uses. Example Results { $substrBytes : [ "abcde" , 1 , 2 ] } "bc" { $substrBytes : [ "Hello World!" , 6 , 5 ] } "World" { $substrBytes : [ "cafÃ©tÃ©ria" , 0 , 5 ] } "cafÃ©" { $substrBytes : [ "cafÃ©tÃ©ria" , 5 , 4 ] } "tÃ©r" { $substrBytes : [ "cafÃ©tÃ©ria" , 7 , 3 ] } Errors with message: "Error: Invalid range, starting index is a UTF-8 continuation byte." { $substrBytes : [ "cafÃ©tÃ©ria" , 3 , 1 ] } Errors with message: "Error: Invalid range, ending index is in the middle of a UTF-8 character." Example Single-Byte Character Set Consider an inventory collection with the following documents: { "_id" : 1 , "item" : "ABC1" , quarter : "13Q1" , "description" : "product 1" } { "_id" : 2 , "item" : "ABC2" , quarter : "13Q4" , "description" : "product 2" } { "_id" : 3 , "item" : "XYZ1" , quarter : "14Q2" , "description" : null } The following operation uses the $substrBytes operator
separate the quarter value (containing only single byte US-ASCII
characters) into a yearSubstring and a quarterSubstring . The quarterSubstring field represents the rest of the string from the
specified byte index following the yearSubstring . It is
calculated by subtracting the byte index from the length of the
string using $strLenBytes . db. inventory . aggregate ( [ { $project : { item : 1 , yearSubstring : { $substrBytes : [ "$quarter" , 0 , 2 ] } , quarterSubtring : { $substrBytes : [ "$quarter" , 2 , { $subtract : [ { $strLenBytes : "$quarter" } , 2 ] } ] } } } ] ) The operation returns the following results: { "_id" : 1 , "item" : "ABC1" , "yearSubstring" : "13" , "quarterSubtring" : "Q1" } { "_id" : 2 , "item" : "ABC2" , "yearSubstring" : "13" , "quarterSubtring" : "Q4" } { "_id" : 3 , "item" : "XYZ1" , "yearSubstring" : "14" , "quarterSubtring" : "Q2" } Single-Byte and Multibyte Character Set Create a food collection with the following documents: db. food . insertMany ( [ { "_id" : 1 , "name" : "apple" } , { "_id" : 2 , "name" : "banana" } , { "_id" : 3 , "name" : "Ã©clair" } , { "_id" : 4 , "name" : "hamburger" } , { "_id" : 5 , "name" : "jalapeÃ±o" } , { "_id" : 6 , "name" : "pizza" } , { "_id" : 7 , "name" : "tacos" } , { "_id" : 8 , "name" : "å¯¿å¸sushi" } ] ) The following operation uses the $substrBytes operator to create a three
byte menuCode from the name value: db. food . aggregate ( [ { $project : { "name" : 1 , "menuCode" : { $substrBytes : [ "$name" , 0 , 3 ] } } } ] ) The operation returns the following results: { "_id" : 1 , "name" : "apple" , "menuCode" : "app" } { "_id" : 2 , "name" : "banana" , "menuCode" : "ban" } { "_id" : 3 , "name" : "Ã©clair" , "menuCode" : "Ã©c" } { "_id" : 4 , "name" : "hamburger" , "menuCode" : "ham" } { "_id" : 5 , "name" : "jalapeÃ±o" , "menuCode" : "jal" } { "_id" : 6 , "name" : "pizza" , "menuCode" : "piz" } { "_id" : 7 , "name" : "tacos" , "menuCode" : "tac" } { "_id" : 8 , "name" : "å¯¿å¸sushi" , "menuCode" : "å¯¿" } Tip See also: $substrCP Back $substr Next $substrCP
