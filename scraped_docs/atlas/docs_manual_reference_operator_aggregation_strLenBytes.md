# $strLenBytes (aggregation) - MongoDB Manual v8.0


Docs Home / MongoDB Manual / Aggregation Operations / Reference / Operators $strLenBytes (aggregation) On this page Definition Behavior Example Definition $strLenBytes Returns the number of UTF-8 encoded bytes in the specified string. $strLenBytes has the following operator
expression syntax : { $strLenBytes : < string expression > } The argument can be any valid expression as long as it resolves to a string. For
more information on expressions, see Expression Operators . If the argument resolves to a value of null or refers to a
missing field, $strLenBytes returns an error. Behavior The $strLenBytes operator counts the number of UTF-8
encoded bytes in a string where each character may use between one
and four bytes. For example, US-ASCII characters are encoded using one byte. Characters
with diacritic markings and additional Latin alphabetical characters
(Latin characters outside of the English alphabet) are encoded
using two bytes. Chinese, Japanese and Korean characters typically
require three bytes, and other planes of unicode (emoji, mathematical
symbols, etc.) require four bytes. The $strLenBytes operator differs from $strLenCP operator which counts the code points in the specified string regardless of how many bytes each character
uses. Example Results Notes { $strLenBytes : "abcde" } 5 Each character is encoded using one byte. { $strLenBytes : "Hello World!" } 12 Each character is encoded using one byte. { $strLenBytes : "cafeteria" } 9 Each character is encoded using one byte. { $strLenBytes : "cafÃ©tÃ©ria" } 11 Ã© is encoded using two bytes. { $strLenBytes : "" } 0 Empty strings return 0. { $strLenBytes : "$â¬Î»G" } 7 â¬ is encoded using three bytes. Î» is encoded using two bytes. { $strLenBytes : "å¯¿å¸" } 6 Each character is encoded using three bytes. Example Single-Byte and Multibyte Character Set Create a food collection with the following documents: db. food . insertMany ( [ { "_id" : 1 , "name" : "apple" } , { "_id" : 2 , "name" : "banana" } , { "_id" : 3 , "name" : "Ã©clair" } , { "_id" : 4 , "name" : "hamburger" } , { "_id" : 5 , "name" : "jalapeÃ±o" } , { "_id" : 6 , "name" : "pizza" } , { "_id" : 7 , "name" : "tacos" } , { "_id" : 8 , "name" : "å¯¿å¸" } ] ) The following operation uses the $strLenBytes operator to calculate
the length of each name value: db. food . aggregate ( [ { $project : { "name" : 1 , "length" : { $strLenBytes : "$name" } } } ] ) The operation returns the following results: { "_id" : 1 , "name" : "apple" , "length" : 5 } { "_id" : 2 , "name" : "banana" , "length" : 6 } { "_id" : 3 , "name" : "Ã©clair" , "length" : 7 } { "_id" : 4 , "name" : "hamburger" , "length" : 9 } { "_id" : 5 , "name" : "jalapeÃ±o" , "length" : 9 } { "_id" : 6 , "name" : "pizza" , "length" : 5 } { "_id" : 7 , "name" : "tacos" , "length" : 5 } { "_id" : 8 , "name" : "å¯¿å¸" , "length" : 6 } The documents with _id: 3 and _id: 5 each contain a diacritic
character ( Ã© and Ã± respectively) that requires two bytes to
encode. The document with _id: 8 contains two Japanese characters
that are encoded using three bytes each.  This makes the length greater than the number of characters in name for the documents
with _id: 3 , _id: 5 and _id: 8 . Tip See also: $strLenCP $binarySize Back $strcasecmp Next $strLenCP
