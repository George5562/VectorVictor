# Subdocuments


# Subdocuments

[Subdocuments](#subdocuments)


Subdocuments are documents embedded in other documents. In Mongoose, this
means you can nest schemas in other schemas. Mongoose has two
distinct notions of subdocuments:arrays of subdocumentsand single nested
subdocuments.

[arrays of subdocuments](https://masteringjs.io/tutorials/mongoose/array#document-arrays)


```javascript
constchildSchema =newSchema({name:'string'});constparentSchema =newSchema({// Array of subdocumentschildren: [childSchema],// Single nested subdocumentschild: childSchema
});
```


Note that populated documents arenotsubdocuments in Mongoose.
Subdocument data is embedded in the top-level document.
Referenced documents are separate top-level documents.


```javascript
constchildSchema =newSchema({name:'string'});constChild= mongoose.model('Child', childSchema);constparentSchema =newSchema({child: {type: mongoose.ObjectId,ref:'Child'}
});constParent= mongoose.model('Parent', parentSchema);constdoc =awaitParent.findOne().populate('child');// NOT a subdocument. `doc.child` is a separate top-level document.doc.child;
```


What is a Subdocument?Subdocuments versus Nested PathsSubdocument DefaultsFinding a SubdocumentAdding Subdocs to ArraysRemoving SubdocsParents of SubdocsAlternate declaration syntax for arrays

- What is a Subdocument?

- Subdocuments versus Nested Paths

- Subdocument Defaults

- Finding a Subdocument

- Adding Subdocs to Arrays

- Removing Subdocs

- Parents of Subdocs

- Alternate declaration syntax for arrays


## What is a Subdocument?

[What is a Subdocument?](#what-is-a-subdocument)


Subdocuments are similar to normal documents. Nested schemas can havemiddleware,custom validation logic,
virtuals, and any other feature top-level schemas can use. The major
difference is that subdocuments are
not saved individually, they are saved whenever their top-level parent
document is saved.

[middleware](middleware.html)

[custom validation logic](validation.html)


```javascript
constParent= mongoose.model('Parent', parentSchema);constparent =newParent({children: [{name:'Matt'}, {name:'Sarah'}] });
parent.children[0].name='Matthew';// `parent.children[0].save()` is a no-op, it triggers middleware but// does **not** actually save the subdocument. You need to save the parent// doc.awaitparent.save();
```


Subdocuments havesaveandvalidatemiddlewarejust like top-level documents. Callingsave()on the parent document triggers
thesave()middleware for all its subdocuments, and the same forvalidate()middleware.

`save`
`validate`
[middleware](middleware.html)

`save()`
`save()`
`validate()`

```javascript
childSchema.pre('save',function(next) {if('invalid'==this.name) {returnnext(newError('#sadpanda'));
  }next();
});constparent =newParent({children: [{name:'invalid'}] });try{awaitparent.save();
}catch(err) {
  err.message;// '#sadpanda'}
```


Subdocuments'pre('save')andpre('validate')middleware executebeforethe top-level document'spre('save')butafterthe
top-level document'spre('validate')middleware. This is because validating
beforesave()is actually a piece of built-in middleware.

`pre('save')`
`pre('validate')`
`pre('save')`
`pre('validate')`
`save()`

```javascript
// Below code will print out 1-4 in orderconstchildSchema =newmongoose.Schema({name:'string'});

childSchema.pre('validate',function(next) {console.log('2');next();
});

childSchema.pre('save',function(next) {console.log('3');next();
});constparentSchema =newmongoose.Schema({child: childSchema
});

parentSchema.pre('validate',function(next) {console.log('1');next();
});

parentSchema.pre('save',function(next) {console.log('4');next();
});
```


## Subdocuments versus Nested Paths

[Subdocuments versus Nested Paths](#subdocuments-versus-nested-paths)


In Mongoose, nested paths are subtly different from subdocuments.
For example, below are two schemas: one withchildas a subdocument,
and one withchildas a nested path.

`child`
`child`

```javascript
// SubdocumentconstsubdocumentSchema =newmongoose.Schema({child:newmongoose.Schema({name:String,age:Number})
});constSubdoc= mongoose.model('Subdoc', subdocumentSchema);// Nested pathconstnestedSchema =newmongoose.Schema({child: {name:String,age:Number}
});constNested= mongoose.model('Nested', nestedSchema);
```


These two schemas look similar, and the documents in MongoDB will
have the same structure with both schemas. But there are a few
Mongoose-specific differences:


First, instances ofNestednever havechild === undefined.
You can always set subproperties ofchild, even if you don't set
thechildproperty. But instances ofSubdoccan havechild === undefined.

`Nested`
`child === undefined`
`child`
`child`
`Subdoc`
`child === undefined`

```javascript
constdoc1 =newSubdoc({});
doc1.child===undefined;// truedoc1.child.name='test';// Throws TypeError: cannot read property...constdoc2 =newNested({});
doc2.child===undefined;// falseconsole.log(doc2.child);// Prints 'MongooseDocument { undefined }'doc2.child.name='test';// Works
```


## Subdocument Defaults

[Subdocument Defaults](#subdocument-defaults)


Subdocument paths are undefined by default, and Mongoose does
not apply subdocument defaults unless you set the subdocument
path to a non-nullish value.


```javascript
constsubdocumentSchema =newmongoose.Schema({child:newmongoose.Schema({name:String,age: {type:Number,default:0}
  })
});constSubdoc= mongoose.model('Subdoc', subdocumentSchema);// Note that the `age` default has no effect, because `child`// is `undefined`.constdoc =newSubdoc();
doc.child;// undefined
```


However, if you setdoc.childto any object, Mongoose will apply
theagedefault if necessary.

`doc.child`
`age`

```javascript
doc.child= {};// Mongoose applies the `age` default:doc.child.age;// 0
```


Mongoose applies defaults recursively, which means there's a nice
workaround if you want to make sure Mongoose applies subdocument
defaults: make the subdocument path default to an empty object.


```javascript
constchildSchema =newmongoose.Schema({name:String,age: {type:Number,default:0}
});constsubdocumentSchema =newmongoose.Schema({child: {type: childSchema,default:() =>({})
  }
});constSubdoc= mongoose.model('Subdoc', subdocumentSchema);// Note that Mongoose sets `age` to its default value 0, because// `child` defaults to an empty object and Mongoose applies// defaults to that empty object.constdoc =newSubdoc();
doc.child;// { age: 0 }
```


## Finding a Subdocument

[Finding a Subdocument](#finding-a-subdocument)


Each subdocument has an_idby default. Mongoose document arrays have a
specialidmethod
for searching a document array to find a document with a given_id.

`_id`
[id](api/mongoosedocumentarray.html#mongoosedocumentarray_MongooseDocumentArray-id)

`_id`

```javascript
constdoc = parent.children.id(_id);
```


## Adding Subdocs to Arrays

[Adding Subdocs to Arrays](#adding-subdocs-to-arrays)


MongooseArray methods such aspush,unshift,addToSet, and others cast arguments to their proper types transparently:

`push`
`unshift`
`addToSet`

```javascript
constParent= mongoose.model('Parent');constparent =newParent();// create a commentparent.children.push({name:'Liesl'});constsubdoc = parent.children[0];console.log(subdoc);// { _id: '501d86090d371bab2c0341c5', name: 'Liesl' }subdoc.isNew;// trueawaitparent.save();console.log('Success!');
```


You can also create a subdocument without adding it to an array by using thecreate()methodof Document Arrays.

[create()method](api/mongoosedocumentarray.html#mongoosedocumentarray_MongooseDocumentArray-create)

`create()`

```javascript
constnewdoc = parent.children.create({name:'Aaron'});
```


## Removing Subdocs

[Removing Subdocs](#removing-subdocs)


Each subdocument has its owndeleteOnemethod.
For an array subdocument, this is equivalent to calling.pull()on the subdocument.
For a single nested subdocument,deleteOne()is equivalent to setting the subdocument tonull.

[deleteOne](api/subdocument.html#Subdocument.prototype.deleteOne())

`.pull()`
`deleteOne()`
[null](https://masteringjs.io/tutorials/fundamentals/null)

`null`

```javascript
// Equivalent to `parent.children.pull(_id)`parent.children.id(_id).deleteOne();// Equivalent to `parent.child = null`parent.child.deleteOne();awaitparent.save();console.log('the subdocs were removed');
```


## Parents of Subdocs

[Parents of Subdocs](#subdoc-parents)


Sometimes, you need to get the parent of a subdoc. You can access the
parent using theparent()function.

`parent()`

```javascript
constschema =newSchema({docArr: [{name:String}],singleNested:newSchema({name:String})
});constModel= mongoose.model('Test', schema);constdoc =newModel({docArr: [{name:'foo'}],singleNested: {name:'bar'}
});

doc.singleNested.parent() === doc;// truedoc.docArr[0].parent() === doc;// true
```


If you have a deeply nested subdoc, you can access the top-level document
using theownerDocument()function.

`ownerDocument()`

```javascript
constschema =newSchema({level1:newSchema({level2:newSchema({test:String})
  })
});constModel= mongoose.model('Test', schema);constdoc =newModel({level1: {level2:'test'} });

doc.level1.level2.parent() === doc;// falsedoc.level1.level2.parent() === doc.level1;// truedoc.level1.level2.ownerDocument() === doc;// true
```


### Alternate declaration syntax for arrays

[Alternate declaration syntax for arrays](#altsyntaxarrays)


If you create a schema with an array of objects, Mongoose will automatically convert the object to a schema for you:


```javascript
constparentSchema =newSchema({children: [{name:'string'}]
});// EquivalentconstparentSchema =newSchema({children: [newSchema({name:'string'})]
});
```


### Next Up

[Next Up](#next-up)


Now that we've covered Subdocuments, let's take a look atquerying.

[querying](queries.html)


[Source](https://mongoosejs.com/docs/subdocs.html#subdocuments-versus-nested-paths)