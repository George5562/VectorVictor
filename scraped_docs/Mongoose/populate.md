# Populate


# Populate

[Populate](#populate)


MongoDB has the join-like$lookupaggregation operator in versions >= 3.2. Mongoose has a more powerful alternative calledpopulate(), which lets you reference documents in other collections.

[$lookup](https://www.mongodb.com/docs/manual/reference/operator/aggregation/lookup/)

`populate()`

Population is the process of automatically replacing the specified paths in the document with document(s) from other collection(s). We may populate a single document, multiple documents, a plain object, multiple plain objects, or all objects returned from a query. Let's look at some examples.


```javascript
constmongoose =require('mongoose');const{Schema} = mongoose;constpersonSchema =Schema({_id:Schema.Types.ObjectId,name:String,age:Number,stories: [{type:Schema.Types.ObjectId,ref:'Story'}]
});conststorySchema =Schema({author: {type:Schema.Types.ObjectId,ref:'Person'},title:String,fans: [{type:Schema.Types.ObjectId,ref:'Person'}]
});constStory= mongoose.model('Story', storySchema);constPerson= mongoose.model('Person', personSchema);
```


So far we've created twoModels. OurPersonmodel has
itsstoriesfield set to an array ofObjectIds. Therefoption is
what tells Mongoose which model to use during population, in our case
theStorymodel. All_ids we store here must be document_ids from
theStorymodel.

[Models](models.html)

`Person`
`stories`
`ObjectId`
`ref`
`Story`
`_id`
`_id`
`Story`

Saving RefsPopulationChecking Whether a Field is PopulatedSetting Populated FieldsWhat If There's No Foreign Document?Field SelectionPopulating Multiple PathsQuery conditions and other optionslimitvs.perDocumentLimitRefs to childrenPopulating an existing documentPopulating multiple existing documentsPopulating across multiple levelsPopulating across DatabasesDynamic References viarefPathDynamic References viarefPopulate VirtualsPopulate Virtuals: The Count OptionPopulate Virtuals: The Match OptionPopulating MapsPopulate in MiddlewarePopulating Multiple Paths in MiddlewareTransform populated documents

- Saving Refs

- Population

- Checking Whether a Field is Populated

- Setting Populated Fields

- What If There's No Foreign Document?

- Field Selection

- Populating Multiple Paths

- Query conditions and other options

- limitvs.perDocumentLimit

`limit`
`perDocumentLimit`
- Refs to children

- Populating an existing document

- Populating multiple existing documents

- Populating across multiple levels

- Populating across Databases

- Dynamic References viarefPath

`refPath`
- Dynamic References viaref

`ref`
- Populate Virtuals

- Populate Virtuals: The Count Option

- Populate Virtuals: The Match Option

- Populating Maps

- Populate in Middleware

- Populating Multiple Paths in Middleware

- Transform populated documents


## Saving refs

[Saving refs](#saving-refs)


Saving refs to other documents works the same way you normally save
properties, just assign the_idvalue:

`_id`

```javascript
constauthor =newPerson({_id:newmongoose.Types.ObjectId(),name:'Ian Fleming',age:50});awaitauthor.save();conststory1 =newStory({title:'Casino Royale',author: author._id// assign the _id from the person});awaitstory1.save();// that's it!
```


You can set therefoption onObjectId,Number,String, andBufferpaths.populate()works with ObjectIds, numbers, strings, and buffers.
However, we recommend using ObjectIds as_idproperties (and thus ObjectIds forrefproperties) unless you have a good reason not to.
That is because MongoDB will set_idto an ObjectId if you create a new document without an_idproperty, so if you make your_idproperty a Number, you need to be extra careful not to insert a document without a numeric_id.

`ref`
`ObjectId`
`Number`
`String`
`Buffer`
`populate()`
`_id`
`ref`
`_id`
`_id`
`_id`
`_id`

## Population

[Population](#population)


So far we haven't done anything much different. We've merely created aPersonand aStory. Now let's take a look at populating our story'sauthorusing the query builder:

`Person`
`Story`
`author`

```javascript
conststory =awaitStory.findOne({title:'Casino Royale'}).populate('author').exec();// prints "The author is Ian Fleming"console.log('The author is %s', story.author.name);
```


Populated paths are no longer set to their original_id, their value
is replaced with the mongoose document returned from the database by
performing a separate query before returning the results.

`_id`

Arrays of refs work the same way. Just call thepopulatemethod on the query and an
array of documents will be returnedin placeof the original_ids.

[populate](api/query.html#query_Query-populate)

`_id`

## Setting Populated Fields

[Setting Populated Fields](#setting-populated-fields)


You can manually populate a property by setting it to a document. The document
must be an instance of the model yourrefproperty refers to.

`ref`

```javascript
conststory =awaitStory.findOne({title:'Casino Royale'});
story.author= author;console.log(story.author.name);// prints "Ian Fleming"
```


You can also push documents or POJOs onto a populated array, and Mongoose will add those documents if theirrefmatches.

`ref`

```javascript
constfan1 =awaitPerson.create({name:'Sean'});awaitStory.updateOne({title:'Casino Royale'}, {$push: {fans: {$each: [fan1._id] } } });conststory =awaitStory.findOne({title:'Casino Royale'}).populate('fans');
story.fans[0].name;// 'Sean'constfan2 =awaitPerson.create({name:'George'});
story.fans.push(fan2);
story.fans[1].name;// 'George'story.fans.push({name:'Roger'});
story.fans[2].name;// 'Roger'
```


If you push a non-POJO and non-document value, like an ObjectId, Mongoose>= 8.7.0will depopulate the entire array.

`>= 8.7.0`

```javascript
constfan4 =awaitPerson.create({name:'Timothy'});
story.fans.push(fan4._id);// Push the `_id`, not the full documentstory.fans[0].name;// undefined, `fans[0]` is now an ObjectIdstory.fans[0].toString() === fan1._id.toString();// true
```


## Checking Whether a Field is Populated

[Checking Whether a Field is Populated](#checking-populated)


You can call thepopulated()function to check whether a field is populated.
Ifpopulated()returns atruthy value,
you can assume the field is populated.

`populated()`
`populated()`
[truthy value](https://masteringjs.io/tutorials/fundamentals/truthy)


```javascript
story.populated('author');// truthystory.depopulate('author');// Make `author` not populated anymorestory.populated('author');// undefined
```


A common reason for checking whether a path is populated is getting theauthorid. However, for your convenience, Mongoose adds a_idgetter to ObjectId instancesso you can usestory.author._idregardless of whetherauthoris populated.

`author`
[_idgetter to ObjectId instances](api/mongoose.html#mongoose_Mongoose-set)

`_id`
`story.author._id`
`author`

```javascript
story.populated('author');// truthystory.author._id;// ObjectIdstory.depopulate('author');// Make `author` not populated anymorestory.populated('author');// undefinedstory.authorinstanceofObjectId;// truestory.author._id;// ObjectId, because Mongoose adds a special getter
```


## What If There's No Foreign Document?

[What If There's No Foreign Document?](#doc-not-found)


Mongoose populate doesn't behave like conventionalSQL joins. When there's no
document,story.authorwill benull. This is analogous to aleft joinin SQL.

[SQL joins](https://www.w3schools.com/sql/sql_join.asp)

`story.author`
`null`
[left join](https://www.w3schools.com/sql/sql_join_left.asp)


```javascript
awaitPerson.deleteMany({name:'Ian Fleming'});conststory =awaitStory.findOne({title:'Casino Royale'}).populate('author');
story.author;// `null`
```


If you have an array ofauthorsin yourstorySchema,populate()will
give you an empty array instead.

`authors`
`storySchema`
`populate()`

```javascript
conststorySchema =Schema({authors: [{type:Schema.Types.ObjectId,ref:'Person'}],title:String});// Laterconststory =awaitStory.findOne({title:'Casino Royale'}).populate('authors');
story.authors;// `[]`
```


## Field Selection

[Field Selection](#field-selection)


What if we only want a few specific fields returned for the populated
documents? This can be accomplished by passing the usualfield name syntaxas the second argument
to the populate method:

[field name syntax](api/query.html#query_Query-select)


```javascript
conststory =awaitStory.findOne({title:/casino royale/i}).populate('author','name').exec();// only return the Persons name// prints "The author is Ian Fleming"console.log('The author is %s', story.author.name);// prints "The authors age is null"console.log('The authors age is %s', story.author.age);
```


## Populating Multiple Paths

[Populating Multiple Paths](#populating-multiple-paths)


What if we wanted to populate multiple paths at the same time?


```javascript
awaitStory.find({/* ... */}).populate('fans').populate('author').exec();
```


If you callpopulate()multiple times with the same path, only the last
one will take effect.

`populate()`

```javascript
// The 2nd `populate()` call below overwrites the first because they// both populate 'fans'.awaitStory.find().populate({path:'fans',select:'name'}).populate({path:'fans',select:'email'});// The above is equivalent to:awaitStory.find().populate({path:'fans',select:'email'});
```


## Query conditions and other options

[Query conditions and other options](#query-conditions)


What if we wanted to populate our fans array based on their age and
select just their names?


```javascript
awaitStory.find().populate({path:'fans',match: {age: {$gte:21} },// Explicitly exclude `_id`, see http://bit.ly/2aEfTdBselect:'name -_id'}).exec();
```


Thematchoption doesn't filter outStorydocuments. If there are no documents that satisfymatch,
you'll get aStorydocument with an emptyfansarray.

`match`
`Story`
`match`
`Story`
`fans`

For example, suppose youpopulate()a story'sauthorand theauthordoesn't satisfymatch. Then
the story'sauthorwill benull.

`populate()`
`author`
`author`
`match`
`author`
`null`

```javascript
conststory =awaitStory.findOne({title:'Casino Royale'}).populate({path:'author',match: {name: {$ne:'Ian Fleming'} } }).exec();
story.author;// `null`
```


In general, there is no way to makepopulate()filter stories based on properties of the story'sauthor.
For example, the below query won't return any results, even thoughauthoris populated.

`populate()`
`author`
`author`

```javascript
conststory =awaitStory.findOne({'author.name':'Ian Fleming'}).populate('author').exec();
story;// null
```


If you want to filter stories by their author's name, you should usedenormalization.

[denormalization](https://www.mongodb.com/blog/post/6-rules-of-thumb-for-mongodb-schema-design-part-3)


## limitvs.perDocumentLimit

[limitvs.perDocumentLimit](#limit-vs-perDocumentLimit)

`limit`
`perDocumentLimit`

Populate does support alimitoption, however, it currently
doesnotlimit on a per-document basis for backwards compatibility. For example,
suppose you have 2 stories:

`limit`

```javascript
awaitStory.create([
  {title:'Casino Royale',fans: [1,2,3,4,5,6,7,8] },
  {title:'Live and Let Die',fans: [9,10] }
]);
```


If you were topopulate()using thelimitoption, you
would find that the 2nd story has 0 fans:

`populate()`
`limit`

```javascript
conststories =awaitStory.find().populate({path:'fans',options: {limit:2}
});

stories[0].name;// 'Casino Royale'stories[0].fans.length;// 2// 2nd story has 0 fans!stories[1].name;// 'Live and Let Die'stories[1].fans.length;// 0
```


That's because, in order to avoid executing a separate query
for each document, Mongoose instead queries for fans usingnumDocuments * limitas the limit. If you need the correctlimit, you should use theperDocumentLimitoption (new in Mongoose 5.9.0).
Just keep in mind thatpopulate()will execute a separate query
for each story, which may causepopulate()to be slower.

`numDocuments * limit`
`limit`
`perDocumentLimit`
`populate()`
`populate()`

```javascript
conststories =awaitStory.find().populate({path:'fans',// Special option that tells Mongoose to execute a separate query// for each `story` to make sure we get 2 fans for each story.perDocumentLimit:2});

stories[0].name;// 'Casino Royale'stories[0].fans.length;// 2stories[1].name;// 'Live and Let Die'stories[1].fans.length;// 2
```


## Refs to children

[Refs to children](#refs-to-children)


We may find however, if we use theauthorobject, we are unable to get a
list of the stories. This is because nostoryobjects were ever 'pushed'
ontoauthor.stories.

`author`
`story`
`author.stories`

There are two perspectives here. First, you may want theauthorto know
which stories are theirs. Usually, your schema should resolve
one-to-many relationships by having a parent pointer in the 'many' side.
But, if you have a good reason to want an array of child pointers, you
canpush()documents onto the array as shown below.

`author`
`push()`

```javascript
awaitstory1.save();

author.stories.push(story1);awaitauthor.save();
```


This allows us to perform afindandpopulatecombo:

`find`
`populate`

```javascript
constperson =awaitPerson.findOne({name:'Ian Fleming'}).populate('stories').exec();// only works if we pushed refs to childrenconsole.log(person);
```


It is debatable that we really want two sets of pointers as they may get
out of sync. Instead we could skip populating and directlyfind()the
stories we are interested in.

`find()`

```javascript
conststories =awaitStory.find({author: author._id}).exec();console.log('The stories are an array: ', stories);
```


The documents returned fromquery populationbecome fully
functional,removeable,saveable documents unless theleanoption is specified. Do not confuse
them withsub docs. Take caution when calling its
remove method because you'll be removing it from the database, not just
the array.

[query population](api/query.html#query_Query-populate)

`remove`
`save`
[lean](api/query.html#query_Query-lean)

[sub docs](subdocs.html)


## Populating an existing document

[Populating an existing document](#populate_an_existing_mongoose_document)


If you have an existing mongoose document and want to populate some of its
paths, you can use theDocument#populate()method.

[Document#populate()](api/document.html#document_Document-populate)


```javascript
constperson =awaitPerson.findOne({name:'Ian Fleming'});

person.populated('stories');// null// Call the `populate()` method on a document to populate a path.awaitperson.populate('stories');

person.populated('stories');// Array of ObjectIdsperson.stories[0].name;// 'Casino Royale'
```


TheDocument#populate()method does not support chaining.
You need to callpopulate()multiple times, or with an array of paths, to populate multiple paths

`Document#populate()`
`populate()`

```javascript
awaitperson.populate(['stories','fans']);
person.populated('fans');// Array of ObjectIds
```


## Populating multiple existing documents

[Populating multiple existing documents](#populate_multiple_documents)


If we have one or many mongoose documents or even plain objects
(likemapReduceoutput), we may
populate them using theModel.populate()method. This is whatDocument#populate()andQuery#populate()use to populate documents.

[mapReduce](api/model.html#model_Model-mapReduce)

[Model.populate()](api/model.html#model_Model-populate)

`Document#populate()`
`Query#populate()`

## Populating across multiple levels

[Populating across multiple levels](#deep-populate)


Say you have a user schema which keeps track of the user's friends.


```javascript
constuserSchema =newSchema({name:String,friends: [{type:ObjectId,ref:'User'}]
});
```


Populate lets you get a list of a user's friends, but what if you also
wanted a user's friends of friends? Specify thepopulateoption to tell
mongoose to populate thefriendsarray of all the user's friends:

`populate`
`friends`

```javascript
awaitUser.findOne({name:'Val'}).populate({path:'friends',// Get friends of friends - populate the 'friends' array for every friendpopulate: {path:'friends'}
  });
```


## Cross Database Populate

[Cross Database Populate](#cross-db-populate)


Let's say you have a schema representing events, and a schema representing
conversations. Each event has a corresponding conversation thread.


```javascript
constdb1 = mongoose.createConnection('mongodb://127.0.0.1:27000/db1');constdb2 = mongoose.createConnection('mongodb://127.0.0.1:27001/db2');constconversationSchema =newSchema({numMessages:Number});constConversation= db2.model('Conversation', conversationSchema);consteventSchema =newSchema({name:String,conversation: {type:ObjectId,ref:Conversation// `ref` is a **Model class**, not a string}
});constEvent= db1.model('Event', eventSchema);
```


In the above example, events and conversations are stored in separate MongoDB
databases. Stringrefwill not work in this situation, because Mongoose
assumes a stringrefrefers to a model name on the same connection. In
the above example, the conversation model is registered ondb2, notdb1.

`ref`
`ref`
`db2`
`db1`

```javascript
// Worksconstevents =awaitEvent.find().populate('conversation');
```


This is known as a "cross-database populate," because it enables you to
populate across MongoDB databases and even across MongoDB instances.


If you don't have access to the model instance when defining youreventSchema,
you can also passthe model instance as an option topopulate().

`eventSchema`
[the model instance as an option topopulate()](api/model.html#model_Model-populate)

`populate()`

```javascript
constevents =awaitEvent.find().// The `model` option specifies the model to use for populating.populate({path:'conversation',model:Conversation});
```


## Dynamic References viarefPath

[Dynamic References viarefPath](#dynamic-refpath)

`refPath`

Mongoose can also populate from multiple collections based on the value
of a property in the document. Let's say you're building a schema for
storing comments. A user may comment on either a blog post or a product.


```javascript
constcommentSchema =newSchema({body: {type:String,required:true},doc: {type:Schema.Types.ObjectId,required:true,// Instead of a hardcoded model name in `ref`, `refPath` means Mongoose// will look at the `docModel` property to find the right model.refPath:'docModel'},docModel: {type:String,required:true,enum: ['BlogPost','Product']
  }
});constProduct= mongoose.model('Product',newSchema({name:String}));constBlogPost= mongoose.model('BlogPost',newSchema({title:String}));constComment= mongoose.model('Comment', commentSchema);
```


TherefPathoption is a more sophisticated alternative toref.
Ifrefis a string, Mongoose will always query the same model to find the populated subdocs.
WithrefPath, you can configure what model Mongoose uses for each document.

`refPath`
`ref`
`ref`
`refPath`

```javascript
constbook =awaitProduct.create({name:'The Count of Monte Cristo'});constpost =awaitBlogPost.create({title:'Top 10 French Novels'});constcommentOnBook =awaitComment.create({body:'Great read',doc: book._id,docModel:'Product'});constcommentOnPost =awaitComment.create({body:'Very informative',doc: post._id,docModel:'BlogPost'});// The below `populate()` works even though one comment references the// 'Product' collection and the other references the 'BlogPost' collection.constcomments =awaitComment.find().populate('doc').sort({body:1});
comments[0].doc.name;// "The Count of Monte Cristo"comments[1].doc.title;// "Top 10 French Novels"
```


An alternative approach is to define separateblogPostandproductproperties oncommentSchema, and thenpopulate()on both properties.

`blogPost`
`product`
`commentSchema`
`populate()`

```javascript
constcommentSchema =newSchema({body: {type:String,required:true},product: {type:Schema.Types.ObjectId,required:true,ref:'Product'},blogPost: {type:Schema.Types.ObjectId,required:true,ref:'BlogPost'}
});// ...// The below `populate()` is equivalent to the `refPath` approach, you// just need to make sure you `populate()` both `product` and `blogPost`.constcomments =awaitComment.find().populate('product').populate('blogPost').sort({body:1});
comments[0].product.name;// "The Count of Monte Cristo"comments[1].blogPost.title;// "Top 10 French Novels"
```


Defining separateblogPostandproductproperties works for this simple
example. But, if you decide to allow users to also comment on articles or
other comments, you'll need to add more properties to your schema. You'll
also need an extrapopulate()call for every property, unless you usemongoose-autopopulate.
UsingrefPathmeans you only need 2 schema paths and onepopulate()call
regardless of how many models yourcommentSchemacan point to.

`blogPost`
`product`
`populate()`
[mongoose-autopopulate](https://www.npmjs.com/package/mongoose-autopopulate)

`refPath`
`populate()`
`commentSchema`

You could also assign a function torefPath, which means Mongoose selects a refPath depending on a value on the document being populated.

`refPath`

```javascript
constcommentSchema =newSchema({body: {type:String,required:true},commentType: {type:String,enum: ['comment','review']
  },entityId: {type:Schema.Types.ObjectId,required:true,refPath:function() {returnthis.commentType==='review'?this.reviewEntityModel:this.commentEntityModel;// 'this' refers to the document being populated}
  },commentEntityModel: {type:String,required:true,enum: ['BlogPost','Review']
  },reviewEntityModel: {type:String,required:true,enum: ['Vendor','Product']
  }
});
```


## Dynamic References viaref

[Dynamic References viaref](#dynamic-ref)

`ref`

Just likerefPath,refcan also be assigned a function.

`refPath`
`ref`

```javascript
constcommentSchema =newSchema({body: {type:String,required:true},verifiedBuyer:Booleandoc: {type:Schema.Types.ObjectId,required:true,ref:function() {returnthis.verifiedBuyer?'Product':'BlogPost';// 'this' refers to the document being populated}
  },
});
```


## Populate Virtuals

[Populate Virtuals](#populate-virtuals)


So far you've only populated based on the_idfield.
However, that's sometimes not the right choice.
For example, suppose you have 2 models:AuthorandBlogPost.

`_id`
`Author`
`BlogPost`

```javascript
constAuthorSchema=newSchema({name:String,posts: [{type: mongoose.Schema.Types.ObjectId,ref:'BlogPost'}]
});constBlogPostSchema=newSchema({title:String,comments: [{author: {type: mongoose.Schema.Types.ObjectId,ref:'Author'},content:String}]
});constAuthor= mongoose.model('Author',AuthorSchema,'Author');constBlogPost= mongoose.model('BlogPost',BlogPostSchema,'BlogPost');
```


The above is an example ofbad schema design. Why?
Suppose you have an extremely prolific author that writes over 10k blog posts.
Thatauthordocument will be huge, over 12kb, and large documents lead to performance issues on both server and client.
ThePrinciple of Least Cardinalitystates that one-to-many relationships, like author to blog post, should be stored on the "many" side.
In other words, blog posts should store theirauthor, authors shouldnotstore all theirposts.

`author`
[Principle of Least Cardinality](https://dev.to/swyx/4-things-i-learned-from-mastering-mongoose-js-25e#4-principle-of-least-cardinality)

`author`
`posts`

```javascript
constAuthorSchema=newSchema({name:String});constBlogPostSchema=newSchema({title:String,author: {type: mongoose.Schema.Types.ObjectId,ref:'Author'},comments: [{author: {type: mongoose.Schema.Types.ObjectId,ref:'Author'},content:String}]
});
```


Unfortunately, these two schemas, as written, don't support populating an author's list of blog posts.
That's wherevirtual populatecomes in.
Virtual populate means callingpopulate()on a virtual property that has arefoption as shown below.

`populate()`
`ref`

```javascript
// Specifying a virtual with a `ref` property is how you enable virtual// populationAuthorSchema.virtual('posts', {ref:'BlogPost',localField:'_id',foreignField:'author'});constAuthor= mongoose.model('Author',AuthorSchema,'Author');constBlogPost= mongoose.model('BlogPost',BlogPostSchema,'BlogPost');
```


You can thenpopulate()the author'spostsas shown below.

`populate()`
`posts`

```javascript
constauthor =awaitAuthor.findOne().populate('posts');

author.posts[0].title;// Title of the first blog post
```


Keep in mind that virtuals arenotincluded intoJSON()andtoObject()output by default.
If you want populate virtuals to show up when using functions like Express'res.json()functionorconsole.log(), set thevirtuals: trueoption on your schema'stoJSONandtoObject()options.

`toJSON()`
`toObject()`
[res.json()function](https://masteringjs.io/tutorials/express/json)

`res.json()`
`console.log()`
`virtuals: true`
`toJSON`
`toObject()`

```javascript
constauthorSchema =newSchema({name:String}, {toJSON: {virtuals:true},// So `res.json()` and other `JSON.stringify()` functions include virtualstoObject: {virtuals:true}// So `console.log()` and other functions that use `toObject()` include virtuals});
```


If you're using populate projections, make sureforeignFieldis included
in the projection.

`foreignField`

```javascript
letauthors =awaitAuthor.find({}).// Won't work because the foreign field `author` is not selectedpopulate({path:'posts',select:'title'}).exec();

authors =awaitAuthor.find({}).// Works, foreign field `author` is selectedpopulate({path:'posts',select:'title author'}).exec();
```


## Populate Virtuals: The Count Option

[Populate Virtuals: The Count Option](#count)


Populate virtuals also support counting the number of documents with
matchingforeignFieldas opposed to the documents themselves. Set thecountoption on your virtual:

`foreignField`
`count`

```javascript
constPersonSchema=newSchema({name:String,band:String});constBandSchema=newSchema({name:String});BandSchema.virtual('numMembers', {ref:'Person',// The model to uselocalField:'name',// Find people where `localField`foreignField:'band',// is equal to `foreignField`count:true// And only get the number of docs});// Laterconstdoc =awaitBand.findOne({name:'Motley Crue'}).populate('numMembers');
doc.numMembers;// 2
```


## Populate Virtuals: The Match Option

[Populate Virtuals: The Match Option](#match)


Another option for Populate virtuals ismatch.
This option adds an extra filter condition to the query Mongoose uses topopulate():

`match`
`populate()`

```javascript
// Same example as 'Populate Virtuals' sectionAuthorSchema.virtual('posts', {ref:'BlogPost',localField:'_id',foreignField:'author',match: {archived:false}// match option with basic query selector});constAuthor= mongoose.model('Author',AuthorSchema,'Author');constBlogPost= mongoose.model('BlogPost',BlogPostSchema,'BlogPost');// After populationconstauthor =awaitAuthor.findOne().populate('posts');

author.posts;// Array of not `archived` posts
```


You can also set thematchoption to a function.
That allows configuring thematchbased on the document being populated.
For example, suppose you only want to populate blog posts whosetagscontain one of the author'sfavoriteTags.

`match`
`match`
`tags`
`favoriteTags`

```javascript
AuthorSchema.virtual('posts', {ref:'BlogPost',localField:'_id',foreignField:'author',// Add an additional filter `{ tags: author.favoriteTags }` to the populate query// Mongoose calls the `match` function with the document being populated as the// first argument.match:author=>({tags: author.favoriteTags})
});
```


You can overwrite thematchoption when callingpopulate()as follows.

`match`
`populate()`

```javascript
// Overwrite the `match` option specified in `AuthorSchema.virtual()` for this// single `populate()` call.awaitAuthor.findOne().populate({path: posts,match: {} });
```


You can also set thematchoption to a function in yourpopulate()call.
If you want to merge yourpopulate()match option, rather than overwriting, use the following.

`match`
`populate()`
`populate()`

```javascript
awaitAuthor.findOne().populate({path: posts,// Add `isDeleted: false` to the virtual's default `match`, so the `match`// option would be `{ tags: author.favoriteTags, isDeleted: false }`match:(author, virtual) =>({
    ...virtual.options.match(author),isDeleted:false})
});
```


## Populating Maps

[Populating Maps](#populating-maps)


Mapsare a type that represents an object with arbitrary
string keys. For example, in the below schema,membersis a map from strings to ObjectIds.

[Maps](schematypes.html#maps)

`members`

```javascript
constBandSchema=newSchema({name:String,members: {type:Map,of: {type:'ObjectId',ref:'Person'}
  }
});constBand= mongoose.model('Band', bandSchema);
```


This map has aref, which means you can usepopulate()to populate all the ObjectIds
in the map. Suppose you have the belowbanddocument:

`ref`
`populate()`
`band`

```javascript
constperson1 =newPerson({name:'Vince Neil'});constperson2 =newPerson({name:'Mick Mars'});constband =newBand({name:'Motley Crue',members: {singer: person1._id,guitarist: person2._id}
});
```


You canpopulate()every element in the map by populating the special pathmembers.$*.$*is a special syntax that tells Mongoose to look at every key in the map.

`populate()`
`members.$*`
`$*`

```javascript
constband =awaitBand.findOne({name:'Motley Crue'}).populate('members.$*');

band.members.get('singer');// { _id: ..., name: 'Vince Neil' }
```


You can also populate paths in maps of subdocuments using$*. For example, suppose you
have the belowlibrarySchema:

`$*`
`librarySchema`

```javascript
constlibrarySchema =newSchema({name:String,books: {type:Map,of:newSchema({title:String,author: {type:'ObjectId',ref:'Person'}
    })
  }
});constLibrary= mongoose.model('Library', librarySchema);
```


You canpopulate()every book's author by populatingbooks.$*.author:

`populate()`
`books.$*.author`

```javascript
constlibraries =awaitLibrary.find().populate('books.$*.author');
```


## Populate in Middleware

[Populate in Middleware](#populate-middleware)


You can populate in either pre or posthooks. If you want to
always populate a certain field, check out themongoose-autopopulate plugin.

[hooks](http://mongoosejs.com/docs/middleware.html)

[mongoose-autopopulate plugin](http://npmjs.com/package/mongoose-autopopulate)


```javascript
// Always attach `populate()` to `find()` callsMySchema.pre('find',function() {this.populate('user');
});
```


```javascript
// Always `populate()` after `find()` calls. Useful if you want to selectively populate// based on the docs found.MySchema.post('find',asyncfunction(docs) {for(constdocofdocs) {if(doc.isPublic) {awaitdoc.populate('user');
    }
  }
});
```


```javascript
// `populate()` after saving. Useful for sending populated data back to the client in an// update API endpointMySchema.post('save',function(doc, next) {
  doc.populate('user').then(function() {next();
  });
});
```


## Populating Multiple Paths in Middleware

[Populating Multiple Paths in Middleware](#populating-multiple-paths-middleware)


Populating multiple paths in middleware can be helpful when you always want to populate some fields. But, the implementation is just a tiny bit trickier than what you may think. Here's how you may expect it to work:


```javascript
constuserSchema =newSchema({email:String,password:String,followers: [{type: mongoose.Schema.Types.ObjectId,ref:'User'}],following: [{type: mongoose.Schema.Types.ObjectId,ref:'User'}]
});

userSchema.pre('find',function(next) {this.populate('followers following');next();
});constUser= mongoose.model('User', userSchema);
```


However, this will not work. By default, passing multiple paths topopulate()in the middleware will trigger an infinite recursion, which means that it will basically trigger the same middleware for all of the paths provided to thepopulate()method - For example,this.populate('followers following')will trigger the same middleware for bothfollowersandfollowingfields and the request will just be left hanging in an infinite loop.

`populate()`
`populate()`
`this.populate('followers following')`
`followers`
`following`

To avoid this, we have to add the_recursedoption, so that our middleware will avoid populating recursively. The example below will make it work as expected.

`_recursed`

```javascript
userSchema.pre('find',function(next) {if(this.options._recursed) {returnnext();
  }this.populate({path:'followers following',options: {_recursed:true} });next();
});
```


Alternatively, you can check out themongoose-autopopulate plugin.

[mongoose-autopopulate plugin](http://npmjs.com/package/mongoose-autopopulate)


## Transform populated documents

[Transform populated documents](#transform-populated-documents)


You can manipulate populated documents using thetransformoption.
If you specify atransformfunction, Mongoose will call this function on every populated document in the result with two arguments: the populated document, and the original id used to populate the document.
This gives you more control over the result of thepopulate()execution.
It is especially useful when you're populating multiple documents.

`transform`
`transform`
`populate()`

Theoriginal motivationfor thetransformoption was to give the ability to leave the unpopulated_idif no document was found, instead of setting the value tonull:

[original motivation](https://github.com/Automattic/mongoose/issues/3775)

`transform`
`_id`
`null`

```javascript
// With `transform`doc =awaitParent.findById(doc).populate([
  {path:'child',// If `doc` is null, use the original id insteadtransform:(doc, id) =>doc ==null? id : doc
  }
]);

doc.child;// 634d1a5744efe65ae09142f9doc.children;// [ 634d1a67ac15090a0ca6c0ea, { _id: 634d1a4ddb804d17d95d1c7f, name: 'Luke', __v: 0 } ]
```


You can return any value fromtransform().
For example, you can usetransform()to "flatten" populated documents as follows.

`transform()`
`transform()`

```javascript
letdoc =awaitParent.create({children: [{name:'Luke'}, {name:'Leia'}] });

doc =awaitParent.findById(doc).populate([{path:'children',transform:doc=>doc ==null?null: doc.name}]);

doc.children;// ['Luke', 'Leia']
```


Another use case fortransform()is setting$localsvalues on populated documents to pass parameters to getters and virtuals.
For example, suppose you want to set a language code on your document for internationalization purposes as follows.

`transform()`
`$locals`

```javascript
constinternationalizedStringSchema =newSchema({en:String,es:String});constingredientSchema =newSchema({// Instead of setting `name` to just a string, set `name` to a map// of language codes to strings.name: {type: internationalizedStringSchema,// When you access `name`, pull the document's localeget:function(value) {returnvalue[this.$locals.language||'en'];
    }
  }
});constrecipeSchema =newSchema({ingredients: [{type: mongoose.ObjectId,ref:'Ingredient'}]
});constIngredient= mongoose.model('Ingredient', ingredientSchema);constRecipe= mongoose.model('Recipe', recipeSchema);
```


You can set the language code on all populated exercises as follows:


```javascript
// Create some sample dataconst{ _id } =awaitIngredient.create({name: {en:'Eggs',es:'Huevos'}
});awaitRecipe.create({ingredients: [_id] });// Populate with setting `$locals.language` for internationalizationconstlanguage ='es';constrecipes =awaitRecipe.find().populate({path:'ingredients',transform:function(doc) {
    doc.$locals.language= language;returndoc;
  }
});// Gets the ingredient's name in Spanish `name.es`recipes[0].ingredients[0].name;// 'Huevos'
```


[Source](https://mongoosejs.com/docs/populate.html#match)