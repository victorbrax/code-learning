const express = require('express')
let app = express();

app.use(express.static("."));

app.get("/", (req,res)=>{
    res.sendFile(__dirname + '/index.html')
})

app.listen(proccess.env.PORT, ()=>{
    console.log("Server is listening on port 3000")
})