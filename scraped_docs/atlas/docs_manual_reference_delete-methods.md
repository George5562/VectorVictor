# Delete Methods - MongoDB Manual v8.0


Docs Home / MongoDB Manual / CRUD Operations / Remove Delete Methods MongoDB provides the following methods to delete documents of a
collection: db.collection.deleteOne() Delete at most a single document that match a specified filter
even though multiple documents may match the specified filter. db.collection.deleteMany() Delete all documents that match a specified filter. db.collection.remove() Delete a single document or all documents that match a specified filter. Starting in MongoDB 6.1: To improve efficiency, MongoDB may batch multiple document deletions
together. The explain command results contain a new BATCHED_DELETE stage for batched document deletions. Additional Methods The following methods can also delete documents from a collection: db.collection.findOneAndDelete() . findOneAndDelete() provides a sort option. The option allows for the deletion of the
first document sorted by the specified order. db.collection.findAndModify() . db.collection.findAndModify() provides a sort option.
The option allows for the deletion of the first document sorted by
the specified order. db.collection.bulkWrite() . See the individual reference pages for the methods for more information
and examples. Back Remove Next Bulk Write
