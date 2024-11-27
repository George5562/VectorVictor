# Query Helpers in TypeScript


# Query Helpers in TypeScript

[Query Helpers in TypeScript](#query-helpers-in-typescript)


Query helperslet you define custom helper methods on Mongoose queries.
Query helpers make queries more semantic using chaining syntax.

[Query helpers](http://thecodebarbarian.com/mongoose-custom-query-methods.html)


The following is an example of how query helpers work in JavaScript.


```javascript
ProjectSchema.query.byName=function(name) {returnthis.find({name: name });
};constProject= mongoose.model('Project',ProjectSchema);// Works. Any Project query, whether it be `find()`, `findOne()`,// `findOneAndUpdate()`, `delete()`, etc. now has a `byName()` helperProject.find().where('stars').gt(1000).byName('mongoose');
```


## Manually Typed Query Helpers

[Manually Typed Query Helpers](#manually-typed-query-helpers)


In TypeScript, you can define query helpers using a separate query helpers interface.
Mongoose'sModeltakes 3 generic parameters:

`Model`

TheDocTypeaTQueryHelperstypeaTMethodstype

- TheDocType

`DocType`
- aTQueryHelperstype

`TQueryHelpers`
- aTMethodstype

`TMethods`

The 2nd generic parameter,TQueryHelpers, should be an interface that contains a function signature for each of your query helpers.
Below is an example of creating aProjectModelwith abyNamequery helper.

`TQueryHelpers`
`ProjectModel`
`byName`

```javascript
import{HydratedDocument,Model,QueryWithHelpers,Schema, model, connect }from'mongoose';interfaceProject{
  name?:string;
  stars?:number;
}interfaceProjectQueryHelpers{byName(name:string):QueryWithHelpers<HydratedDocument<Project>[],HydratedDocument<Project>,ProjectQueryHelpers>
}typeProjectModelType=Model<Project,ProjectQueryHelpers>;constProjectSchema=newSchema<Project,Model<Project,ProjectQueryHelpers>,
  {},ProjectQueryHelpers>({name:String,stars:Number});ProjectSchema.query.byName=functionbyName(this:QueryWithHelpers<any,HydratedDocument<Project>,ProjectQueryHelpers>,name:string) {returnthis.find({name: name });
};// 2nd param to `model()` is the Model class to return.constProjectModel= model<Project,ProjectModelType>('Project',ProjectSchema);run().catch(err=>console.log(err));asyncfunctionrun():Promise<void> {awaitconnect('mongodb://127.0.0.1:27017/test');// Equivalent to `ProjectModel.find({ stars: { $gt: 1000 }, name: 'mongoose' })`awaitProjectModel.find().where('stars').gt(1000).byName('mongoose');
}
```


## Auto Typed Query Helpers

[Auto Typed Query Helpers](#auto-typed-query-helpers)


Mongoose does support auto typed Query Helpers that it are supplied in schema options.
Query Helpers functions can be defined as following:


```javascript
import{Schema, model }from'mongoose';constProjectSchema=newSchema({name:String,stars:Number}, {query: {byName(name:string) {returnthis.find({ name });
    }
  }
});constProjectModel=model('Project',ProjectSchema);// Equivalent to `ProjectModel.find({ stars: { $gt: 1000 }, name: 'mongoose' })`awaitProjectModel.find().where('stars').gt(1000).byName('mongoose');
```


[Source](https://mongoosejs.com/docs/typescript/query-helpers.html)