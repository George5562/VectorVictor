# Statics and Methods in TypeScript


# Statics and Methods in TypeScript

[Statics and Methods in TypeScript](#statics-and-methods-in-typescript)


You can define instance methods and static functions on Mongoose models.
With a little extra configuration, you can also register methods and statics in TypeScript.


## Methods

[Methods](#methods)


To define aninstance methodin TypeScript, create a new interface representing your instance methods.
You need to pass that interface as the 3rd generic parameter to theSchemaconstructorandas the 3rd generic parameter toModelas shown below.

[instance method](../guide.html#methods)

`Schema`
`Model`

```javascript
import{Model,Schema, model }from'mongoose';interfaceIUser{firstName:string;lastName:string;
}// Put all user instance methods in this interface:interfaceIUserMethods{fullName():string;
}// Create a new Model type that knows about IUserMethods...typeUserModel=Model<IUser, {},IUserMethods>;// And a schema that knows about IUserMethodsconstschema =newSchema<IUser,UserModel,IUserMethods>({firstName: {type:String,required:true},lastName: {type:String,required:true}
});
schema.method('fullName',functionfullName() {returnthis.firstName+' '+this.lastName;
});constUser= model<IUser,UserModel>('User', schema);constuser =newUser({firstName:'Jean-Luc',lastName:'Picard'});constfullName:string= user.fullName();// 'Jean-Luc Picard'
```


## Statics

[Statics](#statics)


Mongoosemodelsdonothave an explicit generic parameter forstatics.
If your model has statics, we recommend creating an interface thatextendsMongoose'sModelinterface as shown below.

[models](../models.html)

[statics](../guide.html#statics)

[extends](https://www.typescriptlang.org/docs/handbook/interfaces.html)

`Model`

```javascript
import{Model,Schema, model }from'mongoose';interfaceIUser{name:string;
}interfaceUserModelextendsModel<IUser> {myStaticMethod():number;
}constschema =newSchema<IUser,UserModel>({name:String});
schema.static('myStaticMethod',functionmyStaticMethod() {return42;
});constUser= model<IUser,UserModel>('User', schema);constanswer:number=User.myStaticMethod();// 42
```


Mongoose does support auto typed static functions now that it is supplied in schema options.
Statics functions can be defined as following:


```javascript
import{Schema, model }from'mongoose';constschema =newSchema(
  {name:String},
  {statics: {myStaticMethod() {return42;
      }
    }
  }
);constUser=model('User', schema);constanswer =User.myStaticMethod();// 42
```


## Both Methods and Statics

[Both Methods and Statics](#both-methods-and-statics)


Below is how you can define a model that has both methods and statics.


```javascript
import{Model,Schema,HydratedDocument, model }from'mongoose';interfaceIUser{firstName:string;lastName:string;
}interfaceIUserMethods{fullName():string;
}interfaceUserModelextendsModel<IUser, {},IUserMethods> {createWithFullName(name:string):Promise<HydratedDocument<IUser,IUserMethods>>;
}constschema =newSchema<IUser,UserModel,IUserMethods>({firstName: {type:String,required:true},lastName: {type:String,required:true}
});
schema.static('createWithFullName',functioncreateWithFullName(name:string) {const[firstName, lastName] = name.split(' ');returnthis.create({ firstName, lastName });
});
schema.method('fullName',functionfullName():string{returnthis.firstName+' '+this.lastName;
});constUser= model<IUser,UserModel>('User', schema);User.createWithFullName('Jean-Luc Picard').then(doc=>{console.log(doc.firstName);// 'Jean-Luc'doc.fullName();// 'Jean-Luc Picard'});
```


[Source](https://mongoosejs.com/docs/typescript/statics-and-methods.html)