# $asinh (aggregation) - MongoDB Manual v8.0


Docs Home / MongoDB Manual / Aggregation Operations / Reference / Operators $asinh (aggregation) On this page Behavior Example $asinh Returns the inverse hyperbolic sine (hyperbolic arc sine) of
a value. $asinh has the following syntax: { $asinh : < expression > } $asinh takes any valid expression that resolves to a number. $asinh returns values in radians. Use $radiansToDegrees operator to convert the output value
from radians to degrees. By default $asinh returns values as a double . $asinh can also return values as a 128-bit decimal as long as the <expression> resolves to a 128-bit decimal value. For more information on expressions, see Expression Operators . Behavior null , NaN , and +/- Infinity If the argument resolves to a value of null or refers to a field
that is missing, $asinh returns null . If the
argument resolves to NaN , $asinh returns NaN .
If the argument resolves to negative or positive infinity, $asinh returns negative or positive infinity respectively. Example Results { $asinh: NaN } NaN { $asinh: null } null { $asinh : Infinity} Infinity { $asinh : -Infinity } -Infinity Example Inverse Hyperbolic Sine in Degrees Inverse Hyperbolic Sine in Radians The trigonometry collection contains a document that
stores a value along the x axis of a 2-D graph: { "_id" : ObjectId( "5c50782193f833234ba90d85" ), "x-coordinate" : NumberDecimal( "1" ) } The following aggregation operation uses the $asinh expression to calculate inverse hyperbolic
sine of x-coordinate and add it to the input document using
the $addFields pipeline stage. db.trigonometry.aggregate([ { $addFields : { "y-coordinate" : { $radiansToDegrees : { $asinh : " $x -coordinate" } } } } ]) The $radiansToDegrees expression converts the
radian value returned by $asinh to the equivalent
value in degrees. The command returns the following output: { "_id" : ObjectId( "5c50782193f833234ba90d85" ), "x-coordinate" : NumberDecimal( "1" ), "y-coordinate" : NumberDecimal( "50.49898671052621144221476300417157" ) } Since x-coordinate is stored as a 128-bit decimal , the output of $asinh is a 128-bit decimal. The trigonometry collection contains a document that
stores a value along the x axis of a 2-D graph: { "_id" : ObjectId( "5c50782193f833234ba90d85" ), "x-coordinate" : NumberDecimal( "1" ) } The following aggregation operation uses the $asinh expression to calculate inverse hyperbolic
sine of x-coordinate and add it to the input document using
the $addFields pipeline stage. db.trigonometry.aggregate([ { $addFields : { "y-coordinate" : { $asinh : " $x -coordinate" } } } ]) The command returns the following output: { "_id" : ObjectId( "5c50782193f833234ba90d85" ), "x-coordinate" : NumberDecimal( "1" ), "y-coordinate" : NumberDecimal( "1.818446459232066823483698963560709" ) } Since x-coordinate is stored as a 128-bit decimal , the output of $asinh is a 128-bit decimal. Back $asin Next $atan
