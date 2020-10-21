use zoo;

db.animals.dropIndexes();

// db.animals.createIndex({type: "text", description: "text"})

// db.animals.find({$text: {$search: "Polar"}}).pretty();

const id = ObjectId("5f8d89805b81063b7a10feb7");
db.animals.findOne({name: "Norman"});

db.animals.deleteOne({_id: ObjectId("5f8d89805b81063b7a10feb7")})

// db.animals.updateOne(
//     {_id: ObjectId("5f8d89805b81063b7a10feb7")},
//     {$set: {name: "Pip"}}
// );

