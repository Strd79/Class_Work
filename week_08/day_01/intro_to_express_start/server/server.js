const express = require('express');
const app = express();
const cors = require("cors");
app.use(cors());

app.get("/", function(req, res) {
    res.json({message: "Hello World!"});
})

app.listen(3000, function() {
    console.log('App running on port 3000');
})