# VirtualType


# VirtualType

[Mongoose](mongoose.html)

[Schema](schema.html)

[Connection](connection.html)

[Document](document.html)

[Model](model.html)

[Query](query.html)

[QueryCursor](querycursor.html)

[Aggregate](aggregate.html)

[AggregationCursor](aggregationcursor.html)

[SchemaType](schematype.html)

[VirtualType](virtualtype.html)


VirtualType()VirtualType.prototype.applyGetters()VirtualType.prototype.applySetters()VirtualType.prototype.get()VirtualType.prototype.set()

- VirtualType()

`VirtualType()`
- VirtualType.prototype.applyGetters()

`VirtualType.prototype.applyGetters()`
- VirtualType.prototype.applySetters()

`VirtualType.prototype.applySetters()`
- VirtualType.prototype.get()

`VirtualType.prototype.get()`
- VirtualType.prototype.set()

`VirtualType.prototype.set()`
[Error](error.html)

[SchemaArray](schemaarray.html)

[SchemaDocumentArray](schemadocumentarray.html)

[SchemaSubdocument](schemasubdocument.html)

[SchemaBoolean](schemaboolean.html)

[SchemaBuffer](schemabuffer.html)

[SchemaNumber](schemanumber.html)

[SchemaObjectId](schemaobjectid.html)

[SchemaString](schemastring.html)

[DocumentArray](documentarray.html)

[Subdocument](subdocument.html)

[ArraySubdocument](arraysubdocument.html)

[Buffer](buffer.html)

[Decimal128](decimal128.html)

[Map](map.html)

[Array](array.html)


VirtualType()VirtualType.prototype.applyGetters()VirtualType.prototype.applySetters()VirtualType.prototype.get()VirtualType.prototype.set()

- VirtualType()

`VirtualType()`
- VirtualType.prototype.applyGetters()

`VirtualType.prototype.applyGetters()`
- VirtualType.prototype.applySetters()

`VirtualType.prototype.applySetters()`
- VirtualType.prototype.get()

`VirtualType.prototype.get()`
- VirtualType.prototype.set()

`VirtualType.prototype.set()`

### VirtualType()

[VirtualType()](#VirtualType())

`VirtualType()`

options«Object»[options.ref]«String|Function»ifrefis not nullish, this becomes apopulated virtual[options.localField]«String|Function»the local field to populate on if this is a populated virtual.[options.foreignField]«String|Function»the foreign field to populate on if this is a populated virtual.[options.justOne=false]«Boolean»by default, a populated virtual is an array. If you setjustOne, the populated virtual will be a single doc ornull.[options.getters=false]«Boolean»if you set this totrue, Mongoose will call any custom getters you defined on this virtual[options.count=false]«Boolean»if you set this totrue,populate()will set this virtual to the number of populated documents, as opposed to the documents themselves, usingQuery#countDocuments()[options.match=null]«Object|Function»add an extra match condition topopulate()[options.limit=null]«Number»add a defaultlimitto thepopulate()query[options.skip=null]«Number»add a defaultskipto thepopulate()query[options.perDocumentLimit=null]«Number»For legacy reasons,limitwithpopulate()may give incorrect results because it only executes a single query for every document being populated. If you setperDocumentLimit, Mongoose will ensure correctlimitper document by executing a separate query for each document topopulate(). For example,.find().populate({ path: 'test', perDocumentLimit: 2 })will execute 2 additional queries if.find()returns 2 documents.[options.options=null]«Object»Additional options likelimitandlean.name«String»

- options«Object»

`options`

[options.ref]«String|Function»ifrefis not nullish, this becomes apopulated virtual

- [options.ref]«String|Function»ifrefis not nullish, this becomes apopulated virtual

`[options.ref]`
`ref`

[options.localField]«String|Function»the local field to populate on if this is a populated virtual.

- [options.localField]«String|Function»the local field to populate on if this is a populated virtual.

`[options.localField]`

[options.foreignField]«String|Function»the foreign field to populate on if this is a populated virtual.

- [options.foreignField]«String|Function»the foreign field to populate on if this is a populated virtual.

`[options.foreignField]`

[options.justOne=false]«Boolean»by default, a populated virtual is an array. If you setjustOne, the populated virtual will be a single doc ornull.

- [options.justOne=false]«Boolean»by default, a populated virtual is an array. If you setjustOne, the populated virtual will be a single doc ornull.

`[options.justOne=false]`
`justOne`
`null`

[options.getters=false]«Boolean»if you set this totrue, Mongoose will call any custom getters you defined on this virtual

- [options.getters=false]«Boolean»if you set this totrue, Mongoose will call any custom getters you defined on this virtual

`[options.getters=false]`
`true`

[options.count=false]«Boolean»if you set this totrue,populate()will set this virtual to the number of populated documents, as opposed to the documents themselves, usingQuery#countDocuments()

- [options.count=false]«Boolean»if you set this totrue,populate()will set this virtual to the number of populated documents, as opposed to the documents themselves, usingQuery#countDocuments()

`[options.count=false]`
`true`
`populate()`
`Query#countDocuments()`

[options.match=null]«Object|Function»add an extra match condition topopulate()

- [options.match=null]«Object|Function»add an extra match condition topopulate()

`[options.match=null]`
`populate()`

[options.limit=null]«Number»add a defaultlimitto thepopulate()query

- [options.limit=null]«Number»add a defaultlimitto thepopulate()query

`[options.limit=null]`
`limit`
`populate()`

[options.skip=null]«Number»add a defaultskipto thepopulate()query

- [options.skip=null]«Number»add a defaultskipto thepopulate()query

`[options.skip=null]`
`skip`
`populate()`

[options.perDocumentLimit=null]«Number»For legacy reasons,limitwithpopulate()may give incorrect results because it only executes a single query for every document being populated. If you setperDocumentLimit, Mongoose will ensure correctlimitper document by executing a separate query for each document topopulate(). For example,.find().populate({ path: 'test', perDocumentLimit: 2 })will execute 2 additional queries if.find()returns 2 documents.

- [options.perDocumentLimit=null]«Number»For legacy reasons,limitwithpopulate()may give incorrect results because it only executes a single query for every document being populated. If you setperDocumentLimit, Mongoose will ensure correctlimitper document by executing a separate query for each document topopulate(). For example,.find().populate({ path: 'test', perDocumentLimit: 2 })will execute 2 additional queries if.find()returns 2 documents.

`[options.perDocumentLimit=null]`
`limit`
`populate()`
`perDocumentLimit`
`limit`
`populate()`
`.find().populate({ path: 'test', perDocumentLimit: 2 })`
`.find()`

[options.options=null]«Object»Additional options likelimitandlean.

- [options.options=null]«Object»Additional options likelimitandlean.

`[options.options=null]`
`limit`
`lean`
- name«String»

`name`

VirtualType constructor


This is what mongoose uses to define virtual attributes viaSchema.prototype.virtual.

`Schema.prototype.virtual`

#### Example:

[Example:](#example)


```javascript
constfullname = schema.virtual('fullname');
fullnameinstanceofmongoose.VirtualType// true
```


### VirtualType.prototype.applyGetters()

[VirtualType.prototype.applyGetters()](#VirtualType.prototype.applyGetters())

`VirtualType.prototype.applyGetters()`

value«Object»doc«Document»The document this virtual is attached to

- value«Object»

`value`
- doc«Document»The document this virtual is attached to

`doc`

«Any»the value after applying all getters

- «Any»the value after applying all getters


Applies getters tovalue.

`value`

### VirtualType.prototype.applySetters()

[VirtualType.prototype.applySetters()](#VirtualType.prototype.applySetters())

`VirtualType.prototype.applySetters()`

value«Object»doc«Document»

- value«Object»

`value`
- doc«Document»

`doc`

«Any»the value after applying all setters

- «Any»the value after applying all setters


Applies setters tovalue.

`value`

### VirtualType.prototype.get()

[VirtualType.prototype.get()](#VirtualType.prototype.get())

`VirtualType.prototype.get()`

fn«Function»

- fn«Function»

`fn`

«VirtualType»this

- «VirtualType»this


Adds a custom getter to this virtual.


Mongoose calls the getter function with the below 3 parameters.


value: the value returned by the previous getter. If there is only one getter,valuewill beundefined.virtual: the virtual object you called.get()on.doc: the document this virtual is attached to. Equivalent tothis.

- value: the value returned by the previous getter. If there is only one getter,valuewill beundefined.

`value`
`value`
`undefined`
- virtual: the virtual object you called.get()on.

`virtual`
`.get()`
- doc: the document this virtual is attached to. Equivalent tothis.

`doc`
`this`

#### Example:

[Example:](#example)


```javascript
constvirtual = schema.virtual('fullname');
virtual.get(function(value, virtual, doc) {returnthis.name.first+' '+this.name.last;
});
```


### VirtualType.prototype.set()

[VirtualType.prototype.set()](#VirtualType.prototype.set())

`VirtualType.prototype.set()`

fn«Function»

- fn«Function»

`fn`

«VirtualType»this

- «VirtualType»this


Adds a custom setter to this virtual.


Mongoose calls the setter function with the below 3 parameters.


value: the value being set.virtual: the virtual object you're calling.set()on.doc: the document this virtual is attached to. Equivalent tothis.

- value: the value being set.

`value`
- virtual: the virtual object you're calling.set()on.

`virtual`
`.set()`
- doc: the document this virtual is attached to. Equivalent tothis.

`doc`
`this`

#### Example:

[Example:](#example)


```javascript
constvirtual = schema.virtual('fullname');
virtual.set(function(value, virtual, doc) {constparts = value.split(' ');this.name.first= parts[0];this.name.last= parts[1];
});constModel= mongoose.model('Test', schema);constdoc =newModel();// Calls the setter with `value = 'Jean-Luc Picard'`doc.fullname='Jean-Luc Picard';
doc.name.first;// 'Jean-Luc'doc.name.last;// 'Picard'
```


[Source](https://mongoosejs.com/docs/api/virtualtype.html#VirtualType())