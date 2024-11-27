# Schemas in TypeScript


# Schemas in TypeScript

[Schemas in TypeScript](#schemas-in-typescript)


Mongooseschemasare how you tell Mongoose what your documents look like.
Mongoose schemas are separate from TypeScript interfaces, so you need to either define both araw document interfaceand aschema; or rely on Mongoose to automatically infer the type from the schema definition.

[schemas](../guide.html)


## Automatic type inference

[Automatic type inference](#automatic-type-inference)


Mongoose can automatically infer the document type from your schema definition as follows.
We recommend relying on automatic type inference when defining schemas and models.


```javascript
import{Schema, model }from'mongoose';// Schemaconstschema =newSchema({name: {type:String,required:true},email: {type:String,required:true},avatar:String});// `UserModel` will have `name: string`, etc.constUserModel= mongoose.model('User', schema);constdoc =newUserModel({name:'test',email:'test'});
doc.name;// stringdoc.email;// stringdoc.avatar;// string | undefined | null
```


There are a few caveats for using automatic type inference:


You need to setstrictNullChecks: trueorstrict: truein yourtsconfig.json. Or, if you're setting flags at the command line,--strictNullChecksor--strict. There areknown issueswith automatic type inference with strict mode disabled.You need to define your schema in thenew Schema()call. Don't assign your schema definition to a temporary variable. Doing something likeconst schemaDefinition = { name: String }; const schema = new Schema(schemaDefinition);will not work.Mongoose addscreatedAtandupdatedAtto your schema if you specify thetimestampsoption in your schema,exceptif you also specifymethods,virtuals, orstatics. There is aknown issuewith type inference with timestamps and methods/virtuals/statics options. If you use methods, virtuals, and statics, you're responsible for addingcreatedAtandupdatedAtto your schema definition.

- You need to setstrictNullChecks: trueorstrict: truein yourtsconfig.json. Or, if you're setting flags at the command line,--strictNullChecksor--strict. There areknown issueswith automatic type inference with strict mode disabled.

`strictNullChecks: true`
`strict: true`
`tsconfig.json`
`--strictNullChecks`
`--strict`
- You need to define your schema in thenew Schema()call. Don't assign your schema definition to a temporary variable. Doing something likeconst schemaDefinition = { name: String }; const schema = new Schema(schemaDefinition);will not work.

`new Schema()`
`const schemaDefinition = { name: String }; const schema = new Schema(schemaDefinition);`
- Mongoose addscreatedAtandupdatedAtto your schema if you specify thetimestampsoption in your schema,exceptif you also specifymethods,virtuals, orstatics. There is aknown issuewith type inference with timestamps and methods/virtuals/statics options. If you use methods, virtuals, and statics, you're responsible for addingcreatedAtandupdatedAtto your schema definition.

`createdAt`
`updatedAt`
`timestamps`
`methods`
`virtuals`
`statics`
`createdAt`
`updatedAt`

If you must define your schema separately, useas const(const schemaDefinition = { ... } as const;) to preventtype widening. TypeScript will automatically widen types likerequired: falsetorequired: boolean, which will cause Mongoose to assume the field is required. Usingas constforces TypeScript to retain these types.

[as const](https://www.typescriptlang.org/docs/handbook/release-notes/typescript-3-4.html#const-assertions)

`const schemaDefinition = { ... } as const;`
`required: false`
`required: boolean`
`as const`

If you need to explicitly get the raw document type (the value returned fromdoc.toObject(),await Model.findOne().lean(), etc.) from your schema definition, you can use Mongoose'sinferRawDocTypehelper as follows:

`doc.toObject()`
`await Model.findOne().lean()`
`inferRawDocType`

```javascript
import{Schema,InferRawDocType, model }from'mongoose';constschemaDefinition = {name: {type:String,required:true},email: {type:String,required:true},avatar:String}asconst;constschema =newSchema(schemaDefinition);constUserModel=model('User', schema);constdoc =newUserModel({name:'test',email:'test'});typeRawUserDocument=InferRawDocType<typeofschemaDefinition>;useRawDoc(doc.toObject());functionuseRawDoc(doc:RawUserDocument) {// ...}
```


If automatic type inference doesn't work for you, you can always fall back to document interface definitions.


## Separate document interface definition

[Separate document interface definition](#separate-document-interface-definition)


If automatic type inference doesn't work for you, you can define a separate raw document interface as follows.


```javascript
import{Schema}from'mongoose';// Raw document interface. Contains the data type as it will be stored// in MongoDB. So you can ObjectId, Buffer, and other custom primitive data types.// But no Mongoose document arrays or subdocuments.interfaceUser{name:string;email:string;
  avatar?:string;
}// Schemaconstschema =newSchema<User>({name: {type:String,required:true},email: {type:String,required:true},avatar:String});
```


By default, Mongoose doesnotcheck if your raw document interface lines up with your schema.
For example, the above code won't throw an error ifemailis optional in the document interface, butrequiredinschema.

`email`
`required`
`schema`

## Generic parameters

[Generic parameters](#generic-parameters)


The MongooseSchemaclass in TypeScript has 9generic parameters:

`Schema`
[generic parameters](https://www.typescriptlang.org/docs/handbook/2/generics.html)


RawDocType- An interface describing how the data is saved in MongoDBTModelType- The Mongoose model type. Can be omitted if there are no query helpers or instance methods to be defined.default:Model<DocType, any, any>TInstanceMethods- An interface containing the methods for the schema.default:{}TQueryHelpers- An interface containing query helpers defined on the schema. Defaults to{}.TVirtuals- An interface containing virtuals defined on the schema. Defaults to{}TStaticMethods- An interface containing methods on a model. Defaults to{}TSchemaOptions- The type passed as the 2nd option toSchema()constructor. Defaults toDefaultSchemaOptions.DocType- The inferred document type from the schema.THydratedDocumentType- The hydrated document type. This is the default return type forawait Model.findOne(),Model.hydrate(), etc.

- RawDocType- An interface describing how the data is saved in MongoDB

`RawDocType`
- TModelType- The Mongoose model type. Can be omitted if there are no query helpers or instance methods to be defined.default:Model<DocType, any, any>

`TModelType`

default:Model<DocType, any, any>

- default:Model<DocType, any, any>

`Model<DocType, any, any>`
- TInstanceMethods- An interface containing the methods for the schema.default:{}

`TInstanceMethods`

default:{}

- default:{}

`{}`
- TQueryHelpers- An interface containing query helpers defined on the schema. Defaults to{}.

`TQueryHelpers`
`{}`
- TVirtuals- An interface containing virtuals defined on the schema. Defaults to{}

`TVirtuals`
`{}`
- TStaticMethods- An interface containing methods on a model. Defaults to{}

`TStaticMethods`
`{}`
- TSchemaOptions- The type passed as the 2nd option toSchema()constructor. Defaults toDefaultSchemaOptions.

`TSchemaOptions`
`Schema()`
`DefaultSchemaOptions`
- DocType- The inferred document type from the schema.

`DocType`
- THydratedDocumentType- The hydrated document type. This is the default return type forawait Model.findOne(),Model.hydrate(), etc.

`THydratedDocumentType`
`await Model.findOne()`
`Model.hydrate()`

```javascript
exportclassSchema<RawDocType=any,TModelType=Model<RawDocType,any,any,any>,TInstanceMethods= {},TQueryHelpers= {},TVirtuals= {},TStaticMethods= {},TSchemaOptions=DefaultSchemaOptions,DocType= ...,THydratedDocumentType=HydratedDocument<FlatRecord<DocType>,TVirtuals&TInstanceMethods>
>extendsevents.EventEmitter{// ...}
```


The first generic param,DocType, represents the type of documents that Mongoose will store in MongoDB.
Mongoose wrapsDocTypein a Mongoose document for cases like thethisparameter to document middleware.
For example:

`DocType`
`DocType`
`this`

```javascript
schema.pre('save',function():void{console.log(this.name);// TypeScript knows that `this` is a `mongoose.Document & User` by default});
```


The second generic param,M, is the model used with the schema. Mongoose uses theMtype in model middleware defined in the schema.

`M`
`M`

The third generic param,TInstanceMethodsis used to add types for instance methods defined in the schema.

`TInstanceMethods`

The 4th param,TQueryHelpers, is used to add types forchainable query helpers.

`TQueryHelpers`
[chainable query helpers](query-helpers.html)


## Schema vs Interface fields

[Schema vs Interface fields](#schema-vs-interface-fields)


Mongoose checks to make sure that every path in your schema is defined in your document interface.


For example, the below code will fail to compile becauseemailis a path in the schema, but not in theDocTypeinterface.

`email`
`DocType`

```javascript
import{Schema,Model}from'mongoose';interfaceUser{name:string;email:string;
  avatar?:string;
}// Object literal may only specify known properties, but 'emaill' does not exist in type ...// Did you mean to write 'email'?constschema =newSchema<User>({name: {type:String,required:true},emaill: {type:String,required:true},avatar:String});
```


However, Mongoose doesnotcheck for paths that exist in the document interface, but not in the schema.
For example, the below code compiles.


```javascript
import{Schema,Model}from'mongoose';interfaceUser{name:string;email:string;
  avatar?:string;createdAt:number;
}constschema =newSchema<User,Model<User>>({name: {type:String,required:true},email: {type:String,required:true},avatar:String});
```


This is because Mongoose has numerous features that add paths to your schema that should be included in theDocTypeinterface without you explicitly putting these paths in theSchema()constructor. For example,timestampsandplugins.

`DocType`
`Schema()`
[timestamps](https://masteringjs.io/tutorials/mongoose/timestamps)

[plugins](../plugins.html)


## Arrays

[Arrays](#arrays)


When you define an array in a document interface, we recommend using vanilla JavaScript arrays,notMongoose'sTypes.Arraytype orTypes.DocumentArraytype.
Instead, use theTHydratedDocumentTypegeneric for models and schemas to define that the hydrated document type has paths of typeTypes.ArrayandTypes.DocumentArray.

`Types.Array`
`Types.DocumentArray`
`THydratedDocumentType`
`Types.Array`
`Types.DocumentArray`

```javascript
importmongoosefrom'mongoose'const{Schema} = mongoose;interfaceIOrder{tags:Array<{name:string}>
}// Define a HydratedDocumentType that describes what type Mongoose should use// for fully hydrated docs returned from `findOne()`, etc.typeOrderHydratedDocument= mongoose.HydratedDocument<IOrder,
  {tags: mongoose.HydratedArraySubdocument<{name:string}> }
>;typeOrderModelType= mongoose.Model<IOrder,
  {},
  {},
  {},OrderHydratedDocument// THydratedDocumentType>;constorderSchema =newmongoose.Schema<IOrder,OrderModelType,
  {},// methods{},// query helpers{},// virtuals{},// staticsmongoose.DefaultSchemaOptions,// schema optionsIOrder,// doctypeOrderHydratedDocument// THydratedDocumentType>({tags: [{name: {type:String,required:true} }]
});constOrderModel= mongoose.model<IOrder,OrderModelType>('Order', orderSchema);// Demonstrating return types from OrderModelconstdoc =newOrderModel({tags: [{name:'test'}] });

doc.tags;// mongoose.Types.DocumentArray<{ name: string }>doc.toObject().tags;// Array<{ name: string }>asyncfunctionrun() {constdocFromDb =awaitOrderModel.findOne().orFail();
  docFromDb.tags;// mongoose.Types.DocumentArray<{ name: string }>constleanDoc =awaitOrderModel.findOne().orFail().lean();
  leanDoc.tags;// Array<{ name: string }>};
```


UseHydratedArraySubdocument<RawDocType>for the type of array subdocuments, andHydratedSingleSubdocument<RawDocType>for single subdocuments.

`HydratedArraySubdocument<RawDocType>`
`HydratedSingleSubdocument<RawDocType>`

If you are not usingschema methods, middleware, orvirtuals, you can omit the last 7 generic parameters toSchema()and just define your schema usingnew mongoose.Schema<IOrder, OrderModelType>(...).
The THydratedDocumentType parameter for schemas is primarily for setting the value ofthison methods and virtuals.

[schema methods](../guide.html#methods)

[virtuals](../tutorials/virtuals.html)

`Schema()`
`new mongoose.Schema<IOrder, OrderModelType>(...)`
`this`

[Source](https://mongoosejs.com/docs/typescript/schemas.html)