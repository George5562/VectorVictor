# $atanh (aggregation) - MongoDB Manual v8.0


Docs Home / MongoDB Manual / Aggregation Operations / Reference / Operators $atanh (aggregation) On this page Behavior Example $atanh Returns the inverse hyperbolic tangent (hyperbolic arc tangent) of
a value. $atanh has the following syntax: { $atanh : < expression > } $atanh takes any valid expression that resolves to a number  between -1 and 1 , e.g. -1 <= value <= 1 . $atanh returns values in radians. Use $radiansToDegrees operator to convert the output value
from radians to degrees. By default $atanh returns values as a double . $atanh can also return values as a 128-bit decimal as long as the <expression> resolves to a 128-bit decimal value. For more information on expressions, see Expression Operators . Behavior null , NaN , and +/- Infinity If the argument resolves to a value of null or refers to a field
that is missing, $atanh returns null . If the
argument resolves to NaN , $atanh returns NaN .
If the argument resolves to negative or positive infinity, $atanh throws an error. If the argument resolves to +1 or -1 , $atanh returns Infinity and -Infinity respectively. Example Results { $atanh: NaN } NaN { $atanh: null } null { $atanh: 1 } Infinity { $atanh: -1} -Infinity { $atanh : Infinity} or { $atanh : -Infinity } Throws an error message resembling the following formatted
output: "errmsg" : "Failed to optimize pipeline :: caused by :: cannot apply $atanh to -inf, value must in (-inf,inf)" Example Inverse Hyperbolic Tangent in Degrees Inverse Hyperbolic Tangent in Radians The trigonometry collection contains a document that
stores a value along the x axis of a 2-D graph: { "_id" : ObjectId( "5c50782193f833234ba90d85" ), "x-coordinate" : NumberDecimal( "0.5" ) } The following aggregation operation uses the $atanh expression to calculate inverse hyperbolic
tangent of x-coordinate and add it to the input document using
the $addFields pipeline stage. db.trigonometry.aggregate([ { $addFields : { "y-coordinate" : { $radiansToDegrees : { $atanh : " $x -coordinate" } } } } ]) The $radiansToDegrees expression converts the
radian value returned by $atanh to the equivalent
value in degrees. The command returns the following output: { "_id" : ObjectId( "5c50782193f833234ba90d85" ), "x-coordinate" : NumberDecimal( "0.5" ), "y-coordinate" : NumberDecimal( "31.47292373094538001977241539068589" ) } Since x-coordinate is stored as a 128-bit decimal , the output of $atanh is a 128-bit decimal. The trigonometry collection contains a document that
stores a value along the x axis of a 2-D graph: { "_id" : ObjectId( "5c50782193f833234ba90d85" ), "x-coordinate" : NumberDecimal( "0.5" ) } The following aggregation operation uses the $atanh expression to calculate inverse hyperbolic
tangent of x-coordinate and add it to the input document using
the $addFields pipeline stage. db.trigonometry.aggregate([ { $addFields : { "y-coordinate" : { $atanh : " $x -coordinate" } } } ]) The command returns the following output: { "_id" : ObjectId( "5c50782193f833234ba90d85" ), "x-coordinate" : NumberDecimal( "0.5" ), "y-coordinate" : NumberDecimal( "0.5493061443340548456976226184612628" ) } Since x-coordinate is stored as a 128-bit decimal , the output of $asin is a 128-bit decimal. Back $atan2 Next $avg
