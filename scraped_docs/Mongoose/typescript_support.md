# TypeScript Support


# TypeScript Support

[TypeScript Support](#typescript-support)


Mongoose introducedofficially supported TypeScript bindings in v5.11.0.
Mongoose'sindex.d.tsfile supports a wide variety of syntaxes and strives to be compatible with@types/mongoosewhere possible.
This guide describes Mongoose's recommended approach to working with Mongoose in TypeScript.

[officially supported TypeScript bindings in v5.11.0](https://thecodebarbarian.com/working-with-mongoose-in-typescript.html)

`index.d.ts`
`@types/mongoose`

## Creating Your First Document

[Creating Your First Document](#creating-your-first-document)


To get started with Mongoose in TypeScript, you need to:


Create an interface representing a document in MongoDB.Create aSchemacorresponding to the document interface.Create a Model.Connect to MongoDB.

- Create an interface representing a document in MongoDB.

- Create aSchemacorresponding to the document interface.

- Create a Model.

- Connect to MongoDB.


```javascript
import{Schema, model, connect }from'mongoose';// 1. Create an interface representing a document in MongoDB.interfaceIUser{name:string;email:string;
  avatar?:string;
}// 2. Create a Schema corresponding to the document interface.constuserSchema =newSchema<IUser>({name: {type:String,required:true},email: {type:String,required:true},avatar:String});// 3. Create a Model.constUser= model<IUser>('User', userSchema);run().catch(err=>console.log(err));asyncfunctionrun() {// 4. Connect to MongoDBawaitconnect('mongodb://127.0.0.1:27017/test');constuser =newUser({name:'Bill',email:'bill@initech.com',avatar:'https://i.imgur.com/dM7Thhn.png'});awaituser.save();console.log(user.email);// 'bill@initech.com'}
```


You as the developer are responsible for ensuring that your document interface lines up with your Mongoose schema.
For example, Mongoose won't report an error ifemailisrequiredin your Mongoose schema but optional in your document interface.

`email`
`required`

TheUser()constructor returns an instance ofHydratedDocument<IUser>.IUseris adocument interface, it represents the raw object structure thatIUserobjects look like in MongoDB.HydratedDocument<IUser>represents a hydrated Mongoose document, with methods, virtuals, and other Mongoose-specific features.

`User()`
`HydratedDocument<IUser>`
`IUser`
`IUser`
`HydratedDocument<IUser>`

```javascript
import{HydratedDocument}from'mongoose';constuser:HydratedDocument<IUser> =newUser({name:'Bill',email:'bill@initech.com',avatar:'https://i.imgur.com/dM7Thhn.png'});
```


## ObjectIds and Other Mongoose Types

[ObjectIds and Other Mongoose Types](#objectids-and-other-mongoose-types)


To define a property of typeObjectId, you should useTypes.ObjectIdin the TypeScript document interface. You should use'ObjectId'orSchema.Types.ObjectIdin your schema definition.

`ObjectId`
`Types.ObjectId`
`'ObjectId'`
`Schema.Types.ObjectId`

```javascript
import{Schema,Types}from'mongoose';// 1. Create an interface representing a document in MongoDB.interfaceIUser{name:string;email:string;// Use `Types.ObjectId` in document interface...organization:Types.ObjectId;
}// 2. Create a Schema corresponding to the document interface.constuserSchema =newSchema<IUser>({name: {type:String,required:true},email: {type:String,required:true},// And `Schema.Types.ObjectId` in the schema definition.organization: {type:Schema.Types.ObjectId,ref:'Organization'}
});
```


That's becauseSchema.Types.ObjectIdis aclass that inherits from SchemaType,notthe class you use to create a new MongoDB ObjectId.

`Schema.Types.ObjectId`
[class that inherits from SchemaType](schematypes.html)


## Using Custom Bindings

[Using Custom Bindings](#using-custom-bindings)


If Mongoose's built-inindex.d.tsfile does not work for you, you can remove it in a postinstall script in yourpackage.jsonas shown below.
However, before you do, pleaseopen an issue on Mongoose's GitHub pageand describe the issue you're experiencing.

`index.d.ts`
`package.json`
[open an issue on Mongoose's GitHub page](https://github.com/Automattic/mongoose/issues/new)


```javascript
{"postinstall":"rm ./node_modules/mongoose/index.d.ts"}
```


## Next Up

[Next Up](#next-up)


Now that you've seen the basics of how to use Mongoose in TypeScript, let's take a look atstatics in TypeScript.

[statics in TypeScript](typescript/statics-and-methods.html)


[Source](https://mongoosejs.com/docs/typescript.html)