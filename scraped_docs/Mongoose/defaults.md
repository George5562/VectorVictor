# Defaults


# Defaults

[Defaults](#defaults)


## Declaring Defaults in Your Schema

[Declaring Defaults in Your Schema](#declaring-defaults-in-your-schema)


Your schemas can define default values for certain paths. If you create
a new document without that path set, the default will kick in.


Note: Mongoose only applies a default if the value of the path is
strictlyundefined.

`undefined`

```javascript
constschema =newSchema({name:String,role: {type:String,default:'guitarist'}
});constPerson= db.model('Person', schema);constaxl =newPerson({name:'Axl Rose',role:'singer'});
assert.equal(axl.role,'singer');constslash =newPerson({name:'Slash'});
assert.equal(slash.role,'guitarist');constizzy =newPerson({name:'Izzy',role:undefined});
assert.equal(izzy.role,'guitarist');// Defaults do **not** run on `null`, `''`, or value other than `undefined`.constfoo =newPerson({name:'Bar',role:null});
assert.strictEqual(foo.role,null);awaitPerson.create(axl, slash);constdocs =awaitPerson.find({role:'guitarist'});

assert.equal(docs.length,1);
assert.equal(docs[0].name,'Slash');
```


## Default Functions

[Default Functions](#default-functions)


You can also set thedefaultschema option to a function. Mongoose will
execute that function and use the return value as the default.

`default`

```javascript
constschema =newSchema({title:String,date: {type:Date,// `Date.now()` returns the current unix timestamp as a numberdefault:Date.now}
});constBlogPost= db.model('BlogPost', schema);constpost =newBlogPost({title:'5 Best Arnold Schwarzenegger Movies'});// The post has a default Date set to nowassert.ok(post.date.getTime() >=Date.now() -1000);
assert.ok(post.date.getTime() <=Date.now());
```


## ThesetDefaultsOnInsertOption

[ThesetDefaultsOnInsertOption](#the-code>setdefaultsoninsert</code>-option)

`setDefaultsOnInsert`

Mongoose also sets defaults onupdate()andfindOneAndUpdate()when theupsertoption is set by adding your schema's defaults to aMongoDB$setOnInsertoperator.
You can disable this behavior by setting thesetDefaultsOnInsertoption tofalse.

`update()`
`findOneAndUpdate()`
`upsert`
[MongoDB$setOnInsertoperator](https://www.mongodb.com/docs/manual/reference/operator/update/setOnInsert/)

`$setOnInsert`
`setDefaultsOnInsert`
`false`

```javascript
constschema =newSchema({title:String,genre: {type:String,default:'Action'}
});constMovie= db.model('Movie', schema);constquery = {};constupdate = {title:'The Terminator'};constoptions = {// Return the document after updates are appliednew:true,// Create a document if one isn't found.upsert:true};letdoc =awaitMovie.findOneAndUpdate(query, update, options).lean();
doc.genre;// 'Action', Mongoose set a default value.awaitMovie.deleteMany({});

doc =awaitMovie.findOneAndUpdate(query, update, {new:true,upsert:true,setDefaultsOnInsert:false}).lean();
doc.genre;// undefined, Mongoose did not set a default value
```


You can also setsetDefaultsOnInserttofalseglobally:

`setDefaultsOnInsert`
`false`

```javascript
mongoose.set('setDefaultsOnInsert',false);
```


## Default functions andthis

[Default functions andthis](#default-functions-and-code>this</code>)

`this`

Unless it is running on a query withsetDefaultsOnInsert, a default
function'sthisrefers to the document.

`setDefaultsOnInsert`
`this`

```javascript
constschema =newSchema({title:String,released:Boolean,releaseDate: {type:Date,default:function() {if(this.released) {returnDate.now();
      }returnnull;
    }
  }
});constMovie= db.model('Movie', schema);constmovie1 =newMovie({title:'The Terminator',released:true});// The post has a default Date set to nowassert.ok(movie1.releaseDate.getTime() >=Date.now() -1000);
assert.ok(movie1.releaseDate.getTime() <=Date.now());constmovie2 =newMovie({title:'The Legend of Conan',released:false});// Since `released` is false, the default function will return nullassert.strictEqual(movie2.releaseDate,null);
```


[Source](https://mongoosejs.com/docs/defaults.html)