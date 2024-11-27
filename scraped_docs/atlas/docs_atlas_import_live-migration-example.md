# Example: Live Migration of Replica Sets to Sharded Clusters - MongoDB Atlas


Docs Home / MongoDB Atlas / Migrate or Import Data / Live Migrate a 6.0.17+ or a 7.0.13+ Cluster Example: Live Migration of Replica Sets to Sharded Clusters You may choose to live migrate a source replica set running MongoDB
6.0.17+ or 7.0.13+ to a sharded destination MongoDB 6.0.17+
or 7.0.13+ cluster.
In this case, you might specify the sharding configuration, similar to the
following example, in the live migration Atlas UI. MongoDB shards only those collections that you include into the shardingEntries array. The array specifies which collections to shard. To learn more,
see Sharding . If you choose to omit the sharding configuration during the migration,
you can shard collections on the destination cluster after you migrate
your cluster to Atlas . { "shardingEntries" : [ { "database" : "database-name" , "collection" : "collection-name" , "shardCollection" : { "key" : [ { "location" : 1 } , { "region" : 1 } ] } } ] } In addition to this configuration, the Atlas destination cluster
also needs a compatible index for the specified sharding keys. When starting
the migration via the Atlas UI, you can configure MongoDB to create
these supporting indexes automatically. To learn more, see: Live migrate (pull) a MongoDB 6.0.17+ or 7.0.13+ cluster into Atlas Live migrate (push) a MongoDB 6.0.17+ or 7.0.13+ cluster into Atlas Back Push from Cloud Manager Next Legacy Migration
