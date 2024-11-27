# $let (aggregation) - MongoDB Manual v8.0


Docs Home / MongoDB Manual / Aggregation Operations / Reference / Operators $let (aggregation) On this page Definition Behavior Example Definition $let Binds variables for use in
the specified expression, and returns the result of the expression. The $let expression has the following syntax: { $let: { vars: { <var1>: <expression>, ... }, in: <expression> } } Field Specification vars Assignment block for the variables accessible in the in expression. To assign a variable, specify a string for the
variable name and assign a valid expression for the value. The variable assignments have no meaning outside the in expression, not even within the vars block itself. in The expression to evaluate. To access variables in aggregation expressions, prefix the variable
name with double dollar signs ( $$ ) and enclose in quotes. For
more information on expressions, see Expression Operators . For information on use of
variables in the aggregation pipeline, see Variables in Aggregation Expressions . Behavior $let can access variables defined outside its expression
block, including system variables . If you modify the values of externally defined variables in the vars block, the new values take effect only in the in expression. Outside of the in expression, the variables retain
their previous values. In the vars assignment block, the order of the assignment does not matter, and the variable assignments only have meaning inside
the in expression. As such, accessing a variable's value in the vars assignment block refers to the value of the variable defined
outside the vars block and not inside the same vars block. For example, consider the following $let expression: { $let: { vars: { low: 1, high: "$$low" }, in: { $gt: [ "$$low", "$$high" ] } } } In the vars assignment block, "$$low" refers to the value of an
externally defined variable low and not the variable defined in the
same vars block. If low is not defined outside this $let expression block, the expression is invalid. Example A sales collection has the following documents: { _id : 1 , price : 10 , tax : 0.50 , applyDiscount : true } { _id : 2 , price : 10 , tax : 0.25 , applyDiscount : false } The following aggregation uses $let in the $project pipeline stage to calculate and return the finalTotal for each document: db.sales.aggregate( [ { $project: { finalTotal: { $let: { vars: { total: { $add: [ '$price', '$tax' ] }, discounted: { $cond: { if: '$applyDiscount', then: 0.9, else: 1 } } }, in: { $multiply: [ "$$total", "$$discounted" ] } } } } } ] ) The aggregation returns the following results: { "_id" : 1 , "finalTotal" : 9.450000000000001 } { "_id" : 2 , "finalTotal" : 10.25 } Tip See also: $map Back $lastN Next $linearFill
