# Migrating from 7.x to 8.x


# Migrating from 7.x to 8.x

[Migrating from 7.x to 8.x](#migrating-from-7x-to-8.x)


There are several backwards-breaking changes you should be aware of when migrating from Mongoose 7.x to Mongoose 8.x.


If you're still on Mongoose 6.x or earlier, please read theMongoose 6.x to 7.x migration guideand upgrade to Mongoose 7.x first before upgrading to Mongoose 8.

[Mongoose 6.x to 7.x migration guide](migrating_to_7.html)


We also recommend reviewing theMongoDB Node.js driver's release notes for v6.0.0before upgrading to Mongoose 8.

[MongoDB Node.js driver's release notes for v6.0.0](https://github.com/mongodb/node-mongodb-native/releases/tag/v6.0.0)


RemovedrawResultoption forfindOneAndUpdate()Document.prototype.deleteOne()now returns a queryMongoDB Node Driver 6.0RemovedfindOneAndRemove()Removedcount()Removed id Setternullis valid for non-required string enumsApply minimize whensave()updates an existing documentApply base schema paths before discriminator pathsRemovedoverwriteoption forfindOneAndUpdate()Changed behavior forfindOneAndUpdate()withorFail()and upsertcreate()waits until all saves are done before throwing any errorModel.validate()returns copy of objectAllownullFor Optional Fields in TypeScriptModel constructor properties are all optional in TypeScriptInferdistinct()return types from schema

- RemovedrawResultoption forfindOneAndUpdate()

`rawResult`
`findOneAndUpdate()`
- Document.prototype.deleteOne()now returns a query

`Document.prototype.deleteOne()`
- MongoDB Node Driver 6.0

- RemovedfindOneAndRemove()

`findOneAndRemove()`
- Removedcount()

`count()`
- Removed id Setter

- nullis valid for non-required string enums

`null`
- Apply minimize whensave()updates an existing document

`save()`
- Apply base schema paths before discriminator paths

- Removedoverwriteoption forfindOneAndUpdate()

`overwrite`
`findOneAndUpdate()`
- Changed behavior forfindOneAndUpdate()withorFail()and upsert

`findOneAndUpdate()`
`orFail()`
- create()waits until all saves are done before throwing any error

`create()`
- Model.validate()returns copy of object

`Model.validate()`
- AllownullFor Optional Fields in TypeScript

`null`
- Model constructor properties are all optional in TypeScript

- Inferdistinct()return types from schema

`distinct()`

## RemovedrawResultoption forfindOneAndUpdate()

[RemovedrawResultoption forfindOneAndUpdate()](#removed-rawresult-option-for-findoneandupdate)

`rawResult`
`findOneAndUpdate()`

TherawResultoption forfindOneAndUpdate(),findOneAndReplace(), andfindOneAndDelete()has been replaced by theincludeResultMetadataoption.

`rawResult`
`findOneAndUpdate()`
`findOneAndReplace()`
`findOneAndDelete()`
`includeResultMetadata`

```javascript
constfilter = {name:'Will Riker'};constupdate = {age:29};constres =awaitCharacter.findOneAndUpdate(filter, update, {new:true,upsert:true,// Replace `rawResult: true` with `includeResultMetadata: true`includeResultMetadata:true});
```


includeResultMetadatain Mongoose 8 behaves identically torawResult.

`includeResultMetadata`
`rawResult`

## Document.prototype.deleteOnenow returns a query

[Document.prototype.deleteOnenow returns a query](#document-prototype-deleteone-now-returns-a-query)

`Document.prototype.deleteOne`

In Mongoose 7,doc.deleteOne()returned a promise that resolved todoc.
In Mongoose 8,doc.deleteOne()returns a query for easier chaining, as well as consistency withdoc.updateOne().

`doc.deleteOne()`
`doc`
`doc.deleteOne()`
`doc.updateOne()`

```javascript
constnumberOne =awaitCharacter.findOne({name:'Will Riker'});// In Mongoose 7, q is a Promise that resolves to `numberOne`// In Mongoose 8, q is a Query.constq = numberOne.deleteOne();// In Mongoose 7, `res === numberOne`// In Mongoose 8, `res` is a `DeleteResult`.constres =awaitq;
```


## MongoDB Node Driver 6

[MongoDB Node Driver 6](#mongodb-node-driver-6)


Mongoose 8 usesv6.x of the MongoDB Node driver.
There's a few noteable changes in MongoDB Node driver v6 that affect Mongoose:

[v6.x of the MongoDB Node driver](https://github.com/mongodb/node-mongodb-native/releases/tag/v6.0.0)


TheObjectIdconstructor no longer accepts strings of length 12. In Mongoose 7,new mongoose.Types.ObjectId('12charstring')was perfectly valid. In Mongoose 8,new mongoose.Types.ObjectId('12charstring')throws an error.Deprecated SSL options have been removedsslCA->tlsCAFilesslCRL->tlsCRLFilesslCert->tlsCertificateKeyFilesslKey->tlsCertificateKeyFilesslPass->tlsCertificateKeyFilePasswordsslValidate->tlsAllowInvalidCertificatestlsCertificateFile->tlsCertificateKeyFile

- TheObjectIdconstructor no longer accepts strings of length 12. In Mongoose 7,new mongoose.Types.ObjectId('12charstring')was perfectly valid. In Mongoose 8,new mongoose.Types.ObjectId('12charstring')throws an error.


TheObjectIdconstructor no longer accepts strings of length 12. In Mongoose 7,new mongoose.Types.ObjectId('12charstring')was perfectly valid. In Mongoose 8,new mongoose.Types.ObjectId('12charstring')throws an error.

`ObjectId`
`new mongoose.Types.ObjectId('12charstring')`
`new mongoose.Types.ObjectId('12charstring')`
- Deprecated SSL options have been removedsslCA->tlsCAFilesslCRL->tlsCRLFilesslCert->tlsCertificateKeyFilesslKey->tlsCertificateKeyFilesslPass->tlsCertificateKeyFilePasswordsslValidate->tlsAllowInvalidCertificatestlsCertificateFile->tlsCertificateKeyFile


Deprecated SSL options have been removed


sslCA->tlsCAFilesslCRL->tlsCRLFilesslCert->tlsCertificateKeyFilesslKey->tlsCertificateKeyFilesslPass->tlsCertificateKeyFilePasswordsslValidate->tlsAllowInvalidCertificatestlsCertificateFile->tlsCertificateKeyFile

- sslCA->tlsCAFile

`sslCA`
`tlsCAFile`
- sslCRL->tlsCRLFile

`sslCRL`
`tlsCRLFile`
- sslCert->tlsCertificateKeyFile

`sslCert`
`tlsCertificateKeyFile`
- sslKey->tlsCertificateKeyFile

`sslKey`
`tlsCertificateKeyFile`
- sslPass->tlsCertificateKeyFilePassword

`sslPass`
`tlsCertificateKeyFilePassword`
- sslValidate->tlsAllowInvalidCertificates

`sslValidate`
`tlsAllowInvalidCertificates`
- tlsCertificateFile->tlsCertificateKeyFile

`tlsCertificateFile`
`tlsCertificateKeyFile`

## RemovedfindOneAndRemove()

[RemovedfindOneAndRemove()](#removed-findoneandremove)

`findOneAndRemove()`

In Mongoose 7,findOneAndRemove()was an alias forfindOneAndDelete()that Mongoose supported for backwards compatibility.
Mongoose 8 no longer supportsfindOneAndRemove().
UsefindOneAndDelete()instead.

`findOneAndRemove()`
`findOneAndDelete()`
`findOneAndRemove()`
`findOneAndDelete()`

Similarly, Mongoose 8 no longer supportsfindByIdAndRemove(), which was an alias forfindByIdAndDelete().
Please usefindByIdAndDelete()instead.

`findByIdAndRemove()`
`findByIdAndDelete()`
`findByIdAndDelete()`

## Removedcount()

[Removedcount()](#removed-count)

`count()`

Model.count()andQuery.prototype.count()were removed in Mongoose 8. UseModel.countDocuments()andQuery.prototype.countDocuments()instead.

`Model.count()`
`Query.prototype.count()`
`Model.countDocuments()`
`Query.prototype.countDocuments()`

## Removed id Setter

[Removed id Setter](#removed-id-setter)


In Mongoose 7.4, Mongoose introduced anidsetter that madedoc.id = '0'.repeat(24)equivalent todoc._id = '0'.repeat(24).
In Mongoose 8, that setter is now removed.

`id`
`doc.id = '0'.repeat(24)`
`doc._id = '0'.repeat(24)`

## nullis valid for non-required string enums

[nullis valid for non-required string enums](#null-is-valid-for-non-required-string-enums)

`null`

Before Mongoose 8, setting a string path with anenumtonullwould lead to a validation error, even if that path wasn'trequired.
In Mongoose 8, it is valid to set a string path tonullifrequiredis not set, even withenum.

`enum`
`null`
`required`
`null`
`required`
`enum`

```javascript
constschema =newSchema({status: {type:String,enum: ['on','off']
  }
});constTest= mongoose.model('Test', schema);// Works fine in Mongoose 8// Throws a `ValidationError` in Mongoose 7awaitTest.create({status:null});
```


## Apply minimize whensave()updates an existing document

[Apply minimize whensave()updates an existing document](#apply-minimize-when-save-updates-an-existing-document)

`save()`

In Mongoose 7, Mongoose would only apply minimize when saving a new document, not when updating an existing document.


```javascript
constschema =newSchema({nested: {field1:Number}
});constTest= mongoose.model('Test', schema);// Both Mongoose 7 and Mongoose 8 strip out empty objects when saving// a new document in MongoDB by defaultconst{ _id } =awaitTest.create({nested: {} });letrawDoc =awaitTest.findById(_id).lean();
rawDoc.nested;// undefined// Mongoose 8 will also strip out empty objects when saving an// existing document in MongoDBconstdoc =awaitTest.findById(_id);
doc.nested= {};
doc.markModified('nested');awaitdoc.save();letrawDoc =awaitTest.findById(_id).lean();
rawDoc.nested;// undefined in Mongoose 8, {} in Mongoose 7
```


## Apply base schema paths before discriminator paths

[Apply base schema paths before discriminator paths](#apply-base-schema-paths-before-discriminator-paths)


This means that, in Mongoose 8, getters and setters on discriminator paths runaftergetters and setters on base paths.
In Mongoose 7, getters and setters on discriminator paths ranbeforegetters and setters on base paths.


```javascript
constschema =newSchema({name: {type:String,get(v) {console.log('Base schema getter');returnv;
    }
  }
});constTest= mongoose.model('Test', schema);constD =Test.discriminator('D',newSchema({otherProp: {type:String,get(v) {console.log('Discriminator schema getter');returnv;
    }
  }
}));constdoc =newD({name:'test',otherProp:'test'});// In Mongoose 8, prints "Base schema getter" followed by "Discriminator schema getter"// In Mongoose 7, prints "Discriminator schema getter" followed by "Base schema getter"console.log(doc.toObject({getters:true}));
```


## Removedoverwriteoption forfindOneAndUpdate()

[Removedoverwriteoption forfindOneAndUpdate()](#removed-overwrite-option-for-findoneandupdate)

`overwrite`
`findOneAndUpdate()`

Mongoose 7 and earlier supported anoverwriteoption forfindOneAndUpdate(),updateOne(), andupdate().
Before Mongoose 7,overwritewould skip wrapping theupdateparameter in$set, which meant thatfindOneAndUpdate()andupdate()would overwrite the matched document.
In Mongoose 7, settingoverwritewould convertfindOneAndUpdate()tofindOneAndReplace()andupdateOne()toreplaceOne()to retain backwards compatibility.

`overwrite`
`findOneAndUpdate()`
`updateOne()`
`update()`
`overwrite`
`update`
`$set`
`findOneAndUpdate()`
`update()`
`overwrite`
`findOneAndUpdate()`
`findOneAndReplace()`
`updateOne()`
`replaceOne()`

In Mongoose 8, theoverwriteoption is no longer supported.
If you want to overwrite the entire document, usefindOneAndReplace()orreplaceOne().

`overwrite`
`findOneAndReplace()`
`replaceOne()`

## Changed behavior forfindOneAndUpdate()withorFail()and upsert

[Changed behavior forfindOneAndUpdate()withorFail()and upsert](#changed-behavior-for-findoneandupdate-with-orfail-and-upsert)

`findOneAndUpdate()`
`orFail()`

In Mongoose 7,findOneAndUpdate(filter, update, { upsert: true }).orFail()would throw aDocumentNotFoundErrorif a new document was upserted.
In other words,findOneAndUpdate().orFail()always threw an error if no document was found, even if a new document was upserted.

`findOneAndUpdate(filter, update, { upsert: true }).orFail()`
`DocumentNotFoundError`
`findOneAndUpdate().orFail()`

In Mongoose 8,findOneAndUpdate(filter, update, { upsert: true }).orFail()always succeeds.findOneAndUpdate().orFail()now throws aDocumentNotFoundErrorif there's no document returned, rather than if no document was found.

`findOneAndUpdate(filter, update, { upsert: true }).orFail()`
`findOneAndUpdate().orFail()`
`DocumentNotFoundError`

## Create waits until all saves are done before throwing any error

[Create waits until all saves are done before throwing any error](#create-waits-until-all-saves-are-done-before-throwing-any-error)


In Mongoose 7,create()would immediately throw if anysave()threw an error by default.
Mongoose 8 instead waits for allsave()calls to finish before throwing the first error that occurred.
Socreate()will throw the same error in both Mongoose 7 and Mongoose 8, Mongoose 8 just may take longer to throw the error.

`create()`
`save()`
`save()`
`create()`

```javascript
constschema =newSchema({name: {type:String,enum: ['Badger','Mushroom']
  }
});
schema.pre('save',asyncfunction() {awaitnewPromise(resolve=>setTimeout(resolve,1000));
});constTest= mongoose.model('Test', schema);consterr =awaitTest.create([
  {name:'Badger'},
  {name:'Mushroom'},
  {name:'Cow'}
]).then(() =>null,err=>err);
err;// ValidationError// In Mongoose 7, there would be 0 documents, because `Test.create()`// would throw before 'Badger' and 'Mushroom' are inserted// In Mongoose 8, there will be 2 documents. `Test.create()` waits until// 'Badger' and 'Mushroom' are inserted before throwing.awaitTest.countDocuments();
```


## Model.validate()returns copy of object

[Model.validate()returns copy of object](#model-validate-returns-copy-of-object)

`Model.validate()`

In Mongoose 7,Model.validate()would potentially modify the passed in object.
Mongoose 8 instead copies the passed in object first.

`Model.validate()`

```javascript
constschema =newSchema({answer:Number});constTest= mongoose.model('Test', schema);constobj = {answer:'42'};constres =Test.validate(obj);typeofobj.answer;// 'string' in Mongoose 8, 'number' in Mongoose 7typeofres.answer;// 'number' in both Mongoose 7 and Mongoose 8
```


## AllownullFor Optional Fields in TypeScript

[AllownullFor Optional Fields in TypeScript](#allow-null-for-optional-fields-in-typescript)

`null`

In Mongoose 8, automatically inferred schema types in TypeScript allownullfor optional fields.
In Mongoose 7, optional fields only allowedundefined, notnull.

`null`
`undefined`
`null`

```javascript
constschema =newSchema({name:String});constTestModel=model('Test', schema);constdoc =newTestModel();// In Mongoose 8, this type is `string | null | undefined`.// In Mongoose 7, this type is `string | undefined`doc.name;
```


## Model constructor properties are all optional in TypeScript

[Model constructor properties are all optional in TypeScript](#model-constructor-properties-are-all-optional-in-typescript)


In Mongoose 8, no properties are required on model constructors by default.


```javascript
import{Schema, model,Model}from'mongoose';interfaceIDocument{name:string;createdAt:Date;updatedAt:Date;
}constdocumentSchema =newSchema<IDocument>(
  {name: {type:String,required:true} },
  {timestamps:true}
);constTestModel= model<IDocument>('Document', documentSchema);// Would throw a compile error in Mongoose 7, compiles in Mongoose 8constnewDoc =newTestModel({name:'Foo'});// Explicitly pass generic param to constructor to specify the expected// type of the model constructor param. The following will cause TS// to complain about missing `createdAt` and `updatedAt` in Mongoose 8.constnewDoc2 =newTestModel<IDocument>({name:'Foo'});
```


## Inferdistinct()return types from schema

[Inferdistinct()return types from schema](#infer-distinct-return-types-from-schema)

`distinct()`

```javascript
interfaceUser{name:string;email:string;
  avatar?:string;
}constschema =newSchema<User>({name: {type:String,required:true},email: {type:String,required:true},avatar:String});// Works in Mongoose 8. Compile error in Mongoose 7.constnames:string[] =awaitMyModel.distinct('name');
```


[Source](https://mongoosejs.com/docs/migrating_to_8.html)