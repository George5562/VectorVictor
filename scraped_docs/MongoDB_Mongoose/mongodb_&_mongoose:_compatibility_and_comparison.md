# MongoDB & Mongoose: Compatibility and Comparison

###### JavaScript

# MongoDB & Mongoose: Compatibility and Comparison

## What is Mongoose?

## What is MongoDB Schema Validation?

## Getting Started

## Object Data Modeling in MongoDB

### Mongoose Schema and Model

```lg-highlight-hljs-dark
1const blog = new Schema({2   title: String,3   slug: String,4   published: Boolean,5   content: String,6   tags: [String],7   comments: [{8       user: String,9       content: String,10       votes: Number11   }]12});13 14const Blog = mongoose.model('Blog', blog);
```

### Executing Operations on MongoDB with Mongoose

```lg-highlight-hljs-dark
1// Create a new blog post2const article = new Blog({3   title: 'Awesome Post!',4   slug: 'awesome-post',5   published: true,6   content: 'This is the best post ever',7   tags: ['featured', 'announcement'],8});9 10// Insert the article in our MongoDB database11article.save();12 13// Find a single blog post14Blog.findOne({}, (err, post) => {15   console.log(post);16});
```

### Mongoose vs MongoDB Node.js Driver: A Comparison

```lg-highlight-hljs-dark
1db.collection('posts').insertOne({2   title: 'Better Post!',3   slug: 'a-better-post',4   published: true,5   author: 'Ado Kukic',6   content: 'This is an even better post',7   tags: ['featured'],8});
```

```lg-highlight-hljs-dark
1function Blog(post) {2   this.title = post.title;3   this.slug = post.slug;4   ...5}
```

```lg-highlight-hljs-dark
1db.collection('posts').findOne({}).then((err, post) => {2   let article = new Blog(post);3});
```

## Adding Schema Validation

### Schema Validation with Mongoose

```lg-highlight-hljs-dark
1const blog = new Schema({2   title: {3       type: String,4       required: true,5   },6   slug: {7       type: String,8       required: true,9   },10   published: Boolean,11   content: {12       type: String,13       required: true,14       minlength: 25015   },16   ...17});18 19const Blog = mongoose.model('Blog', blog);
```

```lg-highlight-hljs-dark
1[{"title":"Better Post!","slug":"a-better-post","published":true,"author":"Ado Kukic","content":"This is an even better post","tags":["featured"]}, {"_id":{"$oid":"5e714da7f3a665d9804e6506"},"title":"Awesome Post","slug":"awesome-post","published":true,"content":"This is an awesome post","tags":["featured","announcement"]}]
```

```lg-highlight-hljs-dark
1{2  $jsonSchema: {3    bsonType: "object",4    required: [ "author" ]5  }6}
```

```lg-highlight-hljs-dark
1{2  $jsonSchema: {3    bsonType: "object",4    required: [ "tags" ],5    properties: {6      title: {7        type: "string",8        minLength: 20,9        maxLength: 8010      }11    }12  }13}
```

### Expanding on Schema Validation

```lg-highlight-hljs-dark
1db.collection('posts').insertOne({ title: 'Awesome' });
```

```lg-highlight-hljs-dark
1db.collection('posts').insertOne(2   { title: 'Awesome' },3   { bypassDocumentValidation: true }4);
```

## Populate and Lookup

```lg-highlight-hljs-dark
1const user = new Schema({2   name: String,3   email: String4});5 6const blog = new Schema({7   title: String,8   slug: String,9   published: Boolean,10   content: String,11   tags: [String],12   comments: [{13       user: { Schema.Types.ObjectId, ref: 'User' },14       content: String,15       votes: Number16   }]17});18 19const User = mongoose.model('User', user);20const Blog = mongoose.model('Blog', blog);
```

```lg-highlight-hljs-dark
1Blog.updateOne({2   comments: [{ user: "12345", content: "Great Post!!!" }]3});
```

```lg-highlight-hljs-dark
1Blog.2   findOne({}).3   populate('comments.user').4   exec(function (err, post) {5       console.log(post.comments[0].user.name) // Name of user for 1st comment6   });
```

```lg-highlight-hljs-dark
1db.collection('posts').aggregate([2  {3    '$lookup': {4      'from': 'users', 5      'localField': 'comments.user', 6      'foreignField': '_id', 7      'as': 'users'8    }9  }, {}10], (err, post) => {11    console.log(post.users); //This would contain an array of users12});
```

## Final Thoughts: Do I Really Need Mongoose?

##### Related

### Write A Serverless Function with AWS Lambda and MongoDB 

### Serverless MEAN Stack Applications with Cloud Run and MongoDB Atlas 

### Currency Analysis with Time Series Collections #2 — Simple Moving Average and Exponential Moving Average Calculation 

### An Introduction to IoT (Internet of Toilets) 

###### Table of Contents

* What is Mongoose?

* What is MongoDB Schema Validation?

* Getting Started

* Object Data Modeling in MongoDB

* Adding Schema Validation

* Populate and Lookup

* Final Thoughts: Do I Really Need Mongoose?

What is Mongoose?


What is MongoDB Schema Validation?


Getting Started


Object Data Modeling in MongoDB


Adding Schema Validation


Populate and Lookup


Final Thoughts: Do I Really Need Mongoose?



[Source](https://www.mongodb.com/developer/languages/javascript/mongoose-versus-nodejs-driver/)