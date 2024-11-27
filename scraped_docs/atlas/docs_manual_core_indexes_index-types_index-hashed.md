# Hashed Indexes - MongoDB Manual v8.0


Docs Home / MongoDB Manual / Indexes / Types Hashed Indexes On this page Use Cases Behavior Floating-Point Numbers Limitations Get Started Details Hashing Function Embedded Documents Learn More Hashed indexes collect and store hashes of the values of the indexed
field. Hashed indexes support sharding using hashed shard keys. Hashed based sharding uses a hashed index of a field as the shard
key to partition data across your sharded cluster. Use Cases Hashed indexing is ideal for shard keys with fields that change monotonically like ObjectId values
or timestamps. When you use ranged sharding with a monotonically increasing shard key value, the chunk with an upper
bound of MaxKey receives the majority incoming writes. This
behavior restricts insert operations to a single shard, which removes
the advantage of distributed writes in a sharded cluster. For more information on choosing the best sharding approach for your
application, see Hashed vs Ranged Sharding Behavior Floating-Point Numbers Hashed indexes truncate floating-point numbers to 64-bit integers before
hashing. For example, a hashed index uses the same hash to store the
values 2.3 , 2.2 , and 2.9 . This is a collision , where
multiple values are assigned to a single hash key. Collisions may
negatively impact query performance. To prevent collisions, do not use a hashed index for floating-point
numbers that cannot be reliably converted to 64-bit integers and then
back to floating point. Hashed indexes do not support floating-point numbers larger than 2 53 . Limitations Hashed indexes have limitations for array fields and the unique
property. Array Fields The hashing function does not support multi-key indexes . You cannot create a hashed index on a field that
contains an array or insert an array into a hashed indexed field. Unique Constraint You cannot specify a unique constraint on a
hashed index. Instead, you can create an additional non-hashed index
with the unique constraint. MongoDB can use that non-hashed index to
enforce uniqueness on the chosen field. Get Started To create a hashed index, see Create a Hashed Index . Details This section describes technical details for hashed indexes. Hashing Function Important When MongoDB uses a hashed index to resolve a query, it uses a
hashing function to automatically compute the hash values.
Applications do not need to compute hashes. To see what the hashed value would be for a key, use the convertShardKeyToHashed() method. This method uses the same
hashing function as the hashed index. Embedded Documents The hashing function collapses embedded documents and computes the hash
for the entire value. Learn More Sharding Hashed Sharding Hashed vs Ranged Sharding Back Restrictions Next Create
