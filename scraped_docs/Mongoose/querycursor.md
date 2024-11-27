# QueryCursor


# QueryCursor

[Mongoose](mongoose.html)

[Schema](schema.html)

[Connection](connection.html)

[Document](document.html)

[Model](model.html)

[Query](query.html)

[QueryCursor](querycursor.html)


QueryCursor()QueryCursor.prototype.addCursorFlag()QueryCursor.prototype.close()QueryCursor.prototype.eachAsync()QueryCursor.prototype.getDriverCursor()QueryCursor.prototype.map()QueryCursor.prototype.next()QueryCursor.prototype.optionsQueryCursor.prototype.rewind()QueryCursor.prototype[Symbol.asyncIterator]()

- QueryCursor()

`QueryCursor()`
- QueryCursor.prototype.addCursorFlag()

`QueryCursor.prototype.addCursorFlag()`
- QueryCursor.prototype.close()

`QueryCursor.prototype.close()`
- QueryCursor.prototype.eachAsync()

`QueryCursor.prototype.eachAsync()`
- QueryCursor.prototype.getDriverCursor()

`QueryCursor.prototype.getDriverCursor()`
- QueryCursor.prototype.map()

`QueryCursor.prototype.map()`
- QueryCursor.prototype.next()

`QueryCursor.prototype.next()`
- QueryCursor.prototype.options

`QueryCursor.prototype.options`
- QueryCursor.prototype.rewind()

`QueryCursor.prototype.rewind()`
- QueryCursor.prototype[Symbol.asyncIterator]()

`QueryCursor.prototype[Symbol.asyncIterator]()`
[Aggregate](aggregate.html)

[AggregationCursor](aggregationcursor.html)

[SchemaType](schematype.html)

[VirtualType](virtualtype.html)

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


QueryCursor()QueryCursor.prototype.addCursorFlag()QueryCursor.prototype.close()QueryCursor.prototype.eachAsync()QueryCursor.prototype.getDriverCursor()QueryCursor.prototype.map()QueryCursor.prototype.next()QueryCursor.prototype.optionsQueryCursor.prototype.rewind()QueryCursor.prototype[Symbol.asyncIterator]()

- QueryCursor()

`QueryCursor()`
- QueryCursor.prototype.addCursorFlag()

`QueryCursor.prototype.addCursorFlag()`
- QueryCursor.prototype.close()

`QueryCursor.prototype.close()`
- QueryCursor.prototype.eachAsync()

`QueryCursor.prototype.eachAsync()`
- QueryCursor.prototype.getDriverCursor()

`QueryCursor.prototype.getDriverCursor()`
- QueryCursor.prototype.map()

`QueryCursor.prototype.map()`
- QueryCursor.prototype.next()

`QueryCursor.prototype.next()`
- QueryCursor.prototype.options

`QueryCursor.prototype.options`
- QueryCursor.prototype.rewind()

`QueryCursor.prototype.rewind()`
- QueryCursor.prototype[Symbol.asyncIterator]()

`QueryCursor.prototype[Symbol.asyncIterator]()`

### QueryCursor()

[QueryCursor()](#QueryCursor())

`QueryCursor()`

query«Query»options«Object»query options passed to.find()

- query«Query»

`query`
- options«Object»query options passed to.find()

`options`
`.find()`

«Readable»

- «Readable»

[«Readable»](https://nodejs.org/api/stream.html#class-streamreadable)


A QueryCursor is a concurrency primitive for processing query results
one document at a time. A QueryCursor fulfills the Node.js streams3 API,
in addition to several other mechanisms for loading documents from MongoDB
one at a time.


QueryCursors execute the model's prefindhooks before loading any documents
from MongoDB, and the model's postfindhooks after loading each document.

`find`
`find`

Unless you're an advanced user, donotinstantiate this class directly.
UseQuery#cursor()instead.

[Query#cursor()](/docs/api/query.html#Query.prototype.cursor())

`Query#cursor()`

### QueryCursor.prototype.addCursorFlag()

[QueryCursor.prototype.addCursorFlag()](#QueryCursor.prototype.addCursorFlag())

`QueryCursor.prototype.addCursorFlag()`

flag«String»value«Boolean»

- flag«String»

`flag`
- value«Boolean»

`value`

«AggregationCursor»this

- «AggregationCursor»this


Adds acursor flag.
Useful for setting thenoCursorTimeoutandtailableflags.

[cursor flag](https://mongodb.github.io/node-mongodb-native/4.9/classes/FindCursor.html#addCursorFlag)

`noCursorTimeout`
`tailable`

### QueryCursor.prototype.close()

[QueryCursor.prototype.close()](#QueryCursor.prototype.close())

`QueryCursor.prototype.close()`

«Promise»

- «Promise»


AggregationCursor.close

- AggregationCursor.close

[AggregationCursor.close](https://mongodb.github.io/node-mongodb-native/4.9/classes/AggregationCursor.html#close)


Marks this cursor as closed. Will stop streaming and subsequent calls tonext()will error.

`next()`

### QueryCursor.prototype.eachAsync()

[QueryCursor.prototype.eachAsync()](#QueryCursor.prototype.eachAsync())

`QueryCursor.prototype.eachAsync()`

fn«Function»[options]«Object»[options.parallel]«Number»the number of promises to execute in parallel. Defaults to 1.[options.batchSize]«Number»if set, will callfn()with arrays of documents with length at mostbatchSize[options.continueOnError=false]«Boolean»if true,eachAsync()iterates through all docs even iffnthrows an error. If false,eachAsync()throws an error immediately if the given functionfn()throws an error.

- fn«Function»

`fn`
- [options]«Object»

`[options]`

[options.parallel]«Number»the number of promises to execute in parallel. Defaults to 1.

- [options.parallel]«Number»the number of promises to execute in parallel. Defaults to 1.

`[options.parallel]`

[options.batchSize]«Number»if set, will callfn()with arrays of documents with length at mostbatchSize

- [options.batchSize]«Number»if set, will callfn()with arrays of documents with length at mostbatchSize

`[options.batchSize]`
`fn()`
`batchSize`

[options.continueOnError=false]«Boolean»if true,eachAsync()iterates through all docs even iffnthrows an error. If false,eachAsync()throws an error immediately if the given functionfn()throws an error.

- [options.continueOnError=false]«Boolean»if true,eachAsync()iterates through all docs even iffnthrows an error. If false,eachAsync()throws an error immediately if the given functionfn()throws an error.

`[options.continueOnError=false]`
`eachAsync()`
`fn`
`eachAsync()`
`fn()`

«Promise»

- «Promise»


Executefnfor every document in the cursor. Iffnreturns a promise,
will wait for the promise to resolve before iterating on to the next one.
Returns a promise that resolves when done.

`fn`
`fn`

#### Example:

[Example:](#example)


```javascript
// Iterate over documents asynchronouslyThing.find({name:/^hello/}).cursor().eachAsync(asyncfunction(doc, i) {
    doc.foo= doc.bar+ i;awaitdoc.save();
  })
```


### QueryCursor.prototype.getDriverCursor()

[QueryCursor.prototype.getDriverCursor()](#QueryCursor.prototype.getDriverCursor())

`QueryCursor.prototype.getDriverCursor()`

Returns the underlying cursor from the MongoDB Node driver that this cursor uses.


### QueryCursor.prototype.map()

[QueryCursor.prototype.map()](#QueryCursor.prototype.map())

`QueryCursor.prototype.map()`

fn«Function»

- fn«Function»

`fn`

«QueryCursor»

- «QueryCursor»


Registers a transform function which subsequently maps documents retrieved
via the streams interface or.next()

`.next()`

#### Example:

[Example:](#example)


```javascript
// Map documents returned by `data` eventsThing.find({name:/^hello/}).cursor().map(function(doc) {
   doc.foo="bar";returndoc;
  })on('data',function(doc) {console.log(doc.foo); });// Or map documents returned by `.next()`constcursor =Thing.find({name:/^hello/}).cursor().map(function(doc) {
    doc.foo="bar";returndoc;
  });
cursor.next(function(error, doc) {console.log(doc.foo);
});
```


### QueryCursor.prototype.next()

[QueryCursor.prototype.next()](#QueryCursor.prototype.next())

`QueryCursor.prototype.next()`

«Promise»

- «Promise»


Get the next document from this cursor. Will returnnullwhen there are
no documents left.

`null`

### QueryCursor.prototype.options

[QueryCursor.prototype.options](#QueryCursor.prototype.options)

`QueryCursor.prototype.options`

«property»

- «property»


Theoptionspassed in to theQueryCursorconstructor.

`options`
`QueryCursor`

### QueryCursor.prototype.rewind()

[QueryCursor.prototype.rewind()](#QueryCursor.prototype.rewind())

`QueryCursor.prototype.rewind()`

«AggregationCursor»this

- «AggregationCursor»this


Rewind this cursor to its uninitialized state. Any options that are present on the cursor will
remain in effect. Iterating this cursor will cause new queries to be sent to the server, even
if the resultant data has already been retrieved by this cursor.


### QueryCursor.prototype[Symbol.asyncIterator]()

[QueryCursor.prototype[Symbol.asyncIterator]()](#QueryCursor.prototype[Symbol.asyncIterator]())

`QueryCursor.prototype[Symbol.asyncIterator]()`

Returns an asyncIterator for use withfor/await/ofloops.
You do not need to call this function explicitly, the JavaScript runtime
will call it for you.

[for/await/ofloops](https://thecodebarbarian.com/getting-started-with-async-iterators-in-node-js)

`for/await/of`

#### Example:

[Example:](#example)


```javascript
// Works without using `cursor()`forawait(constdocofModel.find([{$sort: {name:1} }])) {console.log(doc.name);
}// Can also use `cursor()`forawait(constdocofModel.find([{$sort: {name:1} }]).cursor()) {console.log(doc.name);
}
```


Node.js 10.x supports async iterators natively without any flags. You can
enable async iterators in Node.js 8.x using the--harmony_async_iterationflag.

[--harmony_async_iterationflag](https://github.com/tc39/proposal-async-iteration/issues/117#issuecomment-346695187)

`--harmony_async_iteration`

Note:This function is not ifSymbol.asyncIteratoris undefined. IfSymbol.asyncIteratoris undefined, that means your Node.js version does not
support async iterators.

`Symbol.asyncIterator`
`Symbol.asyncIterator`

[Source](https://mongoosejs.com/docs/api/querycursor.html)