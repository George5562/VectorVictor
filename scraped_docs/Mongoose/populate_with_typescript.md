# Populate with TypeScript


# Populate with TypeScript

[Populate with TypeScript](#populate-with-typescript)


Mongoose's TypeScript bindingsadd a generic parameterPathsto thepopulate():

[Mongoose's TypeScript bindings](https://thecodebarbarian.com/working-with-mongoose-in-typescript.html)

`Paths`
`populate()`

```javascript
import{Schema, model,Document,Types}from'mongoose';// `Parent` represents the object as it is stored in MongoDBinterfaceParent{
  child?:Types.ObjectId,
  name?:string}constParentModel= model<Parent>('Parent',newSchema({child: {type:Schema.Types.ObjectId,ref:'Child'},name:String}));interfaceChild{name:string;
}constchildSchema:Schema=newSchema({name:String});constChildModel= model<Child>('Child', childSchema);// Populate with `Paths` generic `{ child: Child }` to override `child` pathParentModel.findOne({}).populate<{child:Child}>('child').orFail().then(doc=>{// Worksconstt:string= doc.child.name;
});
```


An alternative approach is to define aPopulatedParentinterface and usePick<>to pull the properties you're populating.

`PopulatedParent`
`Pick<>`

```javascript
import{Schema, model,Document,Types}from'mongoose';// `Parent` represents the object as it is stored in MongoDBinterfaceParent{
  child?:Types.ObjectId,
  name?:string}interfaceChild{name:string;
}interfacePopulatedParent{child:Child|null;
}constParentModel= model<Parent>('Parent',newSchema({child: {type:Schema.Types.ObjectId,ref:'Child'},name:String}));constchildSchema:Schema=newSchema({name:String});constChildModel= model<Child>('Child', childSchema);// Populate with `Paths` generic `{ child: Child }` to override `child` pathParentModel.findOne({}).populate<Pick<PopulatedParent,'child'>>('child').orFail().then(doc=>{// Worksconstt:string= doc.child.name;
});
```


## UsingPopulatedDoc

[UsingPopulatedDoc](#using-code>populateddoc</code>)

`PopulatedDoc`

Mongoose also exports aPopulatedDoctype that helps you define populated documents in your document interface:

`PopulatedDoc`

```javascript
import{Schema, model,Document,PopulatedDoc}from'mongoose';// `child` is either an ObjectId or a populated documentinterfaceParent{
  child?:PopulatedDoc<Document<ObjectId> &Child>,
  name?:string}constParentModel= model<Parent>('Parent',newSchema({child: {type:'ObjectId',ref:'Child'},name:String}));interfaceChild{
  name?:string;
}constchildSchema:Schema=newSchema({name:String});constChildModel= model<Child>('Child', childSchema);ParentModel.findOne({}).populate('child').orFail().then((doc:Parent) =>{constchild = doc.child;if(child ==null|| childinstanceofObjectId) {thrownewError('should be populated');
  }else{// Worksdoc.child.name.trim();
  }
});
```


However, we recommend using the.populate<{ child: Child }>syntax from the first section instead ofPopulatedDoc.
Here's two reasons why:

`.populate<{ child: Child }>`
`PopulatedDoc`

You still need to add an extra check to check ifchild instanceof ObjectId. Otherwise, the TypeScript compiler will fail withProperty name does not exist on type ObjectId. So usingPopulatedDoc<>means you need an extra check everywhere you usedoc.child.In theParentinterface,childis a hydrated document, which makes it slow difficult for Mongoose to infer the type ofchildwhen you uselean()ortoObject().

- You still need to add an extra check to check ifchild instanceof ObjectId. Otherwise, the TypeScript compiler will fail withProperty name does not exist on type ObjectId. So usingPopulatedDoc<>means you need an extra check everywhere you usedoc.child.

`child instanceof ObjectId`
`Property name does not exist on type ObjectId`
`PopulatedDoc<>`
`doc.child`
- In theParentinterface,childis a hydrated document, which makes it slow difficult for Mongoose to infer the type ofchildwhen you uselean()ortoObject().

`Parent`
`child`
`child`
`lean()`
`toObject()`

[Source](https://mongoosejs.com/docs/typescript/populate.html)