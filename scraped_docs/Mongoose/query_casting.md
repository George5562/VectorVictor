# Query Casting


# Query Casting

[Query Casting](#query-casting)


The first parameter toModel.find(),Query#find(),Model.findOne(), etc. is calledfilter.
In older content this parameter is sometimes calledqueryorconditions. For example:

[Model.find()](../api/model.html#model_Model-find)

`Model.find()`
[Query#find()](../api/query.html#query_Query-find)

`Query#find()`
[Model.findOne()](../api/model.html#model_Model-findOne)

`Model.findOne()`
`filter`
`query`
`conditions`

```javascript
constquery =Character.find({name:'Jean-Luc Picard'});
query.getFilter();// `{ name: 'Jean-Luc Picard' }`// Subsequent chained calls merge new properties into the filterquery.find({age: {$gt:50} });
query.getFilter();// `{ name: 'Jean-Luc Picard', age: { $gt: 50 } }`
```


When you execute the query usingQuery#exec()orQuery#then(), Mongoosecaststhe filter to match your schema.

[Query#exec()](../api/query.html#query_Query-exec)

`Query#exec()`
[Query#then()](../api/query.html#query_Query-then)

`Query#then()`

```javascript
// Note that `_id` and `age` are strings. Mongoose will cast `_id` to// a MongoDB ObjectId and `age.$gt` to a number.constquery =Character.findOne({_id:'5cdc267dd56b5662b7b7cc0c',age: {$gt:'50'}
});// `{ _id: '5cdc267dd56b5662b7b7cc0c', age: { $gt: '50' } }`// Query hasn't been executed yet, so Mongoose hasn't casted the filter.query.getFilter();constdoc =awaitquery.exec();
doc.name;// "Jean-Luc Picard"// Mongoose casted the filter, so `_id` became an ObjectId and `age.$gt`// became a number.query.getFilter()._idinstanceofmongoose.Types.ObjectId;// truetypeofquery.getFilter().age.$gt==='number';// true
```


If Mongoose fails to cast the filter to your schema, your query will throw aCastError.

`CastError`

```javascript
constquery =Character.findOne({age: {$lt:'not a number'} });consterr =awaitquery.exec().then(() =>null,err=>err);
errinstanceofmongoose.CastError;// true// Cast to number failed for value "not a number" at path "age" for// model "Character"err.message;
```


## ThestrictQueryOption

[ThestrictQueryOption](#the-code>strictquery</code>-option)

`strictQuery`

By default, Mongoose doesnotcast filter properties that aren't in your schema.


```javascript
constquery =Character.findOne({notInSchema: {$lt:'not a number'} });// No error because `notInSchema` is not defined in the schemaawaitquery.exec();
```


You can configure this behavior using thestrictQueryoption for schemas. This option is analogous to thestrictoption. SettingstrictQuerytotrueremoves non-schema properties from the filter:

[strictQueryoption for schemas](../guide.html#strictQuery)

`strictQuery`
[strictoption](../guide.html#strict)

`strict`
`strictQuery`
`true`

```javascript
mongoose.deleteModel('Character');constschema =newmongoose.Schema({name:String,age:Number}, {strictQuery:true});Character= mongoose.model('Character', schema);constquery =Character.findOne({notInSchema: {$lt:'not a number'} });awaitquery.exec();
query.getFilter();// Empty object `{}`, Mongoose removes `notInSchema`
```


To make Mongoose throw an error if yourfilterhas a property that isn't in the schema, setstrictQueryto'throw':

`filter`
`strictQuery`
`'throw'`

```javascript
mongoose.deleteModel('Character');constschema =newmongoose.Schema({name:String,age:Number}, {strictQuery:'throw'});Character= mongoose.model('Character', schema);constquery =Character.findOne({notInSchema: {$lt:'not a number'} });consterr =awaitquery.exec().then(() =>null,err=>err);
err.name;// 'StrictModeError'// Path "notInSchema" is not in schema and strictQuery is 'throw'.err.message;
```


## Implicit$in

[Implicit$in](#implicit-code>$in</code>)

`$in`

Because of schemas, Mongoose knows what types fields should be, so it can provide some neat syntactic sugar. For example, if you forget to put$inon a non-array field, Mongoose will add$infor you.

[$in](https://www.mongodb.com/docs/manual/reference/operator/query/in/)

`$in`
`$in`

```javascript
// Normally wouldn't find anything because `name` is a string, but// Mongoose automatically inserts `$in`constquery =Character.findOne({name: ['Jean-Luc Picard','Will Riker'] });constdoc =awaitquery.exec();
doc.name;// "Jean-Luc Picard"// `{ name: { $in: ['Jean-Luc Picard', 'Will Riker'] } }`query.getFilter();
```


[Source](https://mongoosejs.com/docs/tutorials/query_casting.html)