# Getting Started With MongoDB & Mongoose

###### JavaScript

# Getting Started With MongoDB & Mongoose

## What is Mongoose?

## Why Mongoose?

## What is a schema?

```lg-highlight-hljs-dark
1const blog = new Schema({2  title: String,3  slug: String,4  published: Boolean,5  author: String,6  content: String,7  tags: [String],8  createdAt: Date,9  updatedAt: Date,10  comments: [{11    user: String,12    content: String,13    votes: Number14  }]15});
```

* String

* Number

* Date

* Buffer

* Boolean

* Mixed

* ObjectId

* Array

* Decimal128

* Map

String


Number


Date


Buffer


Boolean


Mixed


ObjectId


Array


Decimal128


Map


## What is a model?

```lg-highlight-hljs-dark
1const Blog = mongoose.model('Blog', blog);
```

## Environment setup

```lg-highlight-hljs-dark
1mkdir mongodb-mongoose2cd mongodb-mongoose3npm init -y4npm i mongoose5npm i -D nodemon6code .
```

```lg-highlight-hljs-dark
1...2  "scripts": {3    "dev": "nodemon index.js"4  },5  "type": "module",6...
```

## Connecting to MongoDB

```lg-highlight-hljs-dark
1import mongoose from 'mongoose'23mongoose.connect("mongodb+srv://<username>:<password>@cluster0.eyhty.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
```

## Creating a schema and model

```lg-highlight-hljs-dark
1import mongoose from 'mongoose';2const { Schema, model } = mongoose;34const blogSchema = new Schema({5  title: String,6  slug: String,7  published: Boolean,8  author: String,9  content: String,10  tags: [String],11  createdAt: Date,12  updatedAt: Date,13  comments: [{14    user: String,15    content: String,16    votes: Number17  }]18});1920const Blog = model('Blog', blogSchema);21export default Blog;
```

## Inserting data // method 1

```lg-highlight-hljs-dark
1import mongoose from 'mongoose';2import Blog from './model/Blog';34mongoose.connect("mongodb+srv://mongo:mongo@cluster0.eyhty.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")56// Create a new blog post object7const article = new Blog({8  title: 'Awesome Post!',9  slug: 'awesome-post',10  published: true,11  content: 'This is the best post ever',12  tags: ['featured', 'announcement'],13});1415// Insert the article in our MongoDB database16await article.save();
```

```lg-highlight-hljs-dark
1// Find a single blog post2const firstArticle = await Blog.findOne({});3console.log(firstArticle);
```

```lg-highlight-hljs-dark
1npm run dev
```

## Inserting data // method 2

```lg-highlight-hljs-dark
1// Create a new blog post and insert into database2const article = await Blog.create({3  title: 'Awesome Post!',4  slug: 'awesome-post',5  published: true,6  content: 'This is the best post ever',7  tags: ['featured', 'announcement'],8});910console.log(article);
```

## Update data

```lg-highlight-hljs-dark
1article.title = "The Most Awesomest Post!!";2await article.save();3console.log(article);
```

## Finding data

```lg-highlight-hljs-dark
1const article = await Blog.findById("62472b6ce09e8b77266d6b1b").exec();2console.log(article);
```

## Projecting document fields

```lg-highlight-hljs-dark
1const article = await Blog.findById("62472b6ce09e8b77266d6b1b", "title slug content").exec();2console.log(article);
```

## Deleting data

```lg-highlight-hljs-dark
1const blog = await Blog.deleteOne({ author: "Jesse Hall" })2console.log(blog)34const blog = await Blog.deleteMany({ author: "Jesse Hall" })5console.log(blog)
```

## Validation

```lg-highlight-hljs-dark
1const blogSchema = new Schema({2  title:  {3    type: String,4    required: true,5  },6  slug:  {7    type: String,8    required: true,9    lowercase: true,10  },11  published: {12    type: Boolean,13    default: false,14  },15  author: {16    type: String,17    required: true,18  },19  content: String,20  tags: [String],21  createdAt: {22    type: Date,23    default: () => Date.now(),24    immutable: true,25  },26  updatedAt: Date,27  comments: [{28    user: String,29    content: String,30    votes: Number31  }]32});
```

## Other useful methods

```lg-highlight-hljs-dark
1const blog = await Blog.exists({ author: "Jesse Hall" })2console.log(blog)
```

```lg-highlight-hljs-dark
1// Instead of using a standard find method2const blogFind = await Blog.findOne({ author: "Jesse Hall" });34// Use the equivalent where() method5const blogWhere = await Blog.where("author").equals("Jesse Hall");6console.log(blogWhere)
```

```lg-highlight-hljs-dark
1const blog = await Blog.where("author").equals("Jesse Hall").select("title author")2console.log(blog)
```

## Multiple schemas

```lg-highlight-hljs-dark
1import mongoose from 'mongoose';2const {Schema, model} = mongoose;34const userSchema = new Schema({5  name: {6    type: String,7    required: true,8  },9  email: {10    type: String,11    minLength: 10,12    required: true,13    lowercase: true14  },15});1617const User = model('User', userSchema);18export default User;
```

```lg-highlight-hljs-dark
1import mongoose from 'mongoose';2const { Schema, SchemaTypes, model } = mongoose;34const blogSchema = new Schema({5  ...,6  author: {7    type: SchemaTypes.ObjectId,8    ref: 'User',9    required: true,10  },11  ...,12  comments: [{13    user: {14      type: SchemaTypes.ObjectId,15      ref: 'User',16      required: true,17    },18    content: String,19    votes: Number20  }];21});22...
```

```lg-highlight-hljs-dark
1...2import User from './model/User.js';34...56const user = await User.create({7  name: 'Jesse Hall',8  email: 'jesse@email.com',9});1011const article = await Blog.create({12  title: 'Awesome Post!',13  slug: 'Awesome-Post',14  author: user._id,15  content: 'This is the best post ever',16  tags: ['featured', 'announcement'],17});1819console.log(article);
```

```lg-highlight-hljs-dark
1const article = await Blog.findOne({ title: "Awesome Post!" }).populate("author");2console.log(article);
```

## Middleware

```lg-highlight-hljs-dark
1blogSchema.pre('save', function(next) {2  this.updated = Date.now(); // update the date every time a blog post is saved3  next();4});
```

```lg-highlight-hljs-dark
1const article = await Blog.findById("6247589060c9b6abfa1ef530").exec();2article.title = "Updated Title";3await article.save();4console.log(article);
```

## Next steps

## Conclusion

##### Related

### Build a Modern Blog with Gatsby and MongoDB 

### NextAuth.js Authentication With MongoDB 

### Zap, Tweet, and Repeat! How to Use Zapier with MongoDB 

### MongoDB Atlas Serverless Instances: Quick Start 

###### Table of Contents

* What is Mongoose?

* Why Mongoose?

* What is a schema?

* What is a model?

* Environment setup

* Connecting to MongoDB

* Creating a schema and model

* Inserting data // method 1

* Inserting data // method 2

* Update data

* Finding data

* Projecting document fields

* Deleting data

* Validation

* Other useful methods

* Multiple schemas

* Middleware

* Next steps

* Conclusion

What is Mongoose?


Why Mongoose?


What is a schema?


What is a model?


Environment setup


Connecting to MongoDB


Creating a schema and model


Inserting data // method 1


Inserting data // method 2


Update data


Finding data


Projecting document fields


Deleting data


Validation


Other useful methods


Multiple schemas


Middleware


Next steps


Conclusion



[Source](https://www.mongodb.com/developer/languages/javascript/getting-started-with-mongodb-and-mongoose/)