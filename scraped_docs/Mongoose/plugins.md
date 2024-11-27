# Plugins


# Plugins

[Plugins](#plugins)


Schemas are pluggable, that is, they allow for applying pre-packaged capabilities to extend their functionality. This is a very powerful feature.


ExampleGlobal PluginsApply Plugins Before Compiling ModelsOfficially Supported Plugins

- Example

- Global Plugins

- Apply Plugins Before Compiling Models

- Officially Supported Plugins


## Example

[Example](#example)


Plugins are a tool for reusing logic in multiple schemas. Suppose you have
several models in your database and want to add aloadedAtproperty
to each one. Just create a plugin once and apply it to eachSchema:

`loadedAt`
`Schema`

```javascript
// loadedAt.jsmodule.exports=functionloadedAtPlugin(schema, options) {
  schema.virtual('loadedAt').get(function() {returnthis._loadedAt; }).set(function(v) {this._loadedAt= v; });

  schema.post(['find','findOne'],function(docs) {if(!Array.isArray(docs)) {
      docs = [docs];
    }constnow =newDate();for(constdocofdocs) {
      doc.loadedAt= now;
    }
  });
};// game-schema.jsconstloadedAtPlugin =require('./loadedAt');constgameSchema =newSchema({/* ... */});
gameSchema.plugin(loadedAtPlugin);// player-schema.jsconstloadedAtPlugin =require('./loadedAt');constplayerSchema =newSchema({/* ... */});
playerSchema.plugin(loadedAtPlugin);
```


We just added loaded-time behavior to both ourGameandPlayerschemas and declared an index on theloadedAtpath of our Games to boot. Not bad for a few lines of code.

`Game`
`Player`
`loadedAt`

## Global Plugins

[Global Plugins](#global)


Want to register a plugin for all schemas? The mongoose singleton has a.plugin()function that registers a plugin for every schema. For
example:

`.plugin()`

```javascript
constmongoose =require('mongoose');
mongoose.plugin(require('./loadedAt'));constgameSchema =newSchema({/* ... */});constplayerSchema =newSchema({/* ... */});// `loadedAtPlugin` gets attached to both schemasconstGame= mongoose.model('Game', gameSchema);constPlayer= mongoose.model('Player', playerSchema);
```


## Apply Plugins Before Compiling Models

[Apply Plugins Before Compiling Models](#apply-plugins-before-compiling-models)


Because many plugins rely onmiddleware, you should make sure to apply pluginsbeforeyou callmongoose.model()orconn.model(). Otherwise,any middleware the plugin registers won't get applied.

[middleware](middleware.html)

`mongoose.model()`
`conn.model()`
[any middleware the plugin registers won't get applied](middleware.html#defining)


```javascript
// loadedAt.jsmodule.exports=functionloadedAtPlugin(schema, options) {
  schema.virtual('loadedAt').get(function() {returnthis._loadedAt; }).set(function(v) {this._loadedAt= v; });

  schema.post(['find','findOne'],function(docs) {if(!Array.isArray(docs)) {
      docs = [docs];
    }constnow =newDate();for(constdocofdocs) {
      doc.loadedAt= now;
    }
  });
};// game-schema.jsconstloadedAtPlugin =require('./loadedAt');constgameSchema =newSchema({/* ... */});constGame= mongoose.model('Game', gameSchema);// `find()` and `findOne()` hooks from `loadedAtPlugin()` won't get applied// because `mongoose.model()` was already called!gameSchema.plugin(loadedAtPlugin);
```


## Officially Supported Plugins

[Officially Supported Plugins](#official)


The Mongoose team maintains several plugins that add cool new features to
Mongoose. Here's a couple:


mongoose-autopopulate: Alwayspopulate()certain fields in your Mongoose schemas.mongoose-lean-virtuals: Attach virtuals to the results of Mongoose queries when using.lean().mongoose-cast-aggregation

- mongoose-autopopulate: Alwayspopulate()certain fields in your Mongoose schemas.

`populate()`
- mongoose-lean-virtuals: Attach virtuals to the results of Mongoose queries when using.lean().

`.lean()`
- mongoose-cast-aggregation


You can find a full list of officially supported plugins onMongoose's plugins search site.

[Mongoose's plugins search site](https://plugins.mongoosejs.io/)


## Community

[Community](#community)


Not only can you re-use schema functionality in your own projects, but you
also reap the benefits of the Mongoose community as well. Any plugin
published tonpmand with
'mongoose' as annpm keywordwill show up on oursearch resultspage.

[npm](https://npmjs.org/)

[npm keyword](https://docs.npmjs.com/files/package.json#keywords)

[search results](http://plugins.mongoosejs.io)


[Source](https://mongoosejs.com/docs/plugins.html)