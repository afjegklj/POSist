var MongoClient = require('mongodb').MongoClient;
var url = 'mongodb://localhost:27017/test';
var entries = [ ... ] // a huge array containing the entry objects

var createNewEntries = function(db, entries, callback) {

    // Get the collection and bulk api artefacts
    var collection = db.collection('entries'),          
        bulkUpdateOps = [];    

    entries.forEach(function(doc) {
        bulkUpdateOps.push({ "insertOne": { "document": doc } });

        if (bulkUpdateOps.length === 1000) {
            collection.bulkWrite(bulkUpdateOps).then(function(r) {
                // do something with result
            });
            bulkUpdateOps = [];
        }
    })

    if (bulkUpdateOps.length > 0) {
        collection.bulkWrite(bulkUpdateOps).then(function(r) {
            // do something with result
        });
    }
};