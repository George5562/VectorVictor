# Handling Subdocuments in TypeScript


# Handling Subdocuments in TypeScript

[Handling Subdocuments in TypeScript](#handling-subdocuments-in-typescript)


Subdocuments are tricky in TypeScript.
By default, Mongoose treats object properties in document interfaces asnested propertiesrather than subdocuments.


```javascript
// Setupimport{Schema,Types, model,Model}from'mongoose';// Subdocument definitioninterfaceNames{_id:Types.ObjectId;firstName:string;
}// Document definitioninterfaceUser{names:Names;
}// Models and schemastypeUserModelType=Model<User>;constuserSchema =newSchema<User,UserModelType>({names:newSchema<Names>({firstName:String})
});constUserModel= model<User,UserModelType>('User', userSchema);// Create a new document:constdoc =newUserModel({names: {_id:'0'.repeat(24),firstName:'foo'} });// "Property 'ownerDocument' does not exist on type 'Names'."// Means that `doc.names` is not a subdocument!doc.names.ownerDocument();
```


Mongoose provides a mechanism to override types in the hydrated document.
Define a separateTHydratedDocumentTypeand pass it as the 5th generic param tomongoose.Model<>.THydratedDocumentTypecontrols what type Mongoose uses for "hydrated documents", that is, whatawait UserModel.findOne(),UserModel.hydrate(), andnew UserModel()return.

`THydratedDocumentType`
`mongoose.Model<>`
`THydratedDocumentType`
`await UserModel.findOne()`
`UserModel.hydrate()`
`new UserModel()`

```javascript
// Define property overrides for hydrated documentstypeTHydratedUserDocument= {
  names?: mongoose.Types.Subdocument<Names>
}typeUserModelType= mongoose.Model<User, {}, {}, {},THydratedUserDocument>;constuserSchema =newmongoose.Schema<User,UserModelType>({names:newmongoose.Schema<Names>({firstName:String})
});constUserModel= mongoose.model<User,UserModelType>('User', userSchema);constdoc =newUserModel({names: {_id:'0'.repeat(24),firstName:'foo'} });
doc.names!.ownerDocument();// Works, `names` is a subdocument!
```


## Subdocument Arrays

[Subdocument Arrays](#subdocument-arrays)


You can also override arrays to properly type subdocument arrays usingTMethodsAndOverrides:

`TMethodsAndOverrides`

```javascript
// Subdocument definitioninterfaceNames{_id:Types.ObjectId;firstName:string;
}// Document definitioninterfaceUser{names:Names[];
}// TMethodsAndOverridestypeTHydratedUserDocument= {
  names?:Types.DocumentArray<Names>
}typeUserModelType=Model<User, {}, {}, {},THydratedUserDocument>;// Create modelconstUserModel= model<User,UserModelType>('User',newSchema<User,UserModelType>({names: [newSchema<Names>({firstName:String})]
}));constdoc =newUserModel({});
doc.names[0].ownerDocument();// Works!
```


[Source](https://mongoosejs.com/docs/typescript/subdocuments.html)