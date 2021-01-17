const express = require("express");
const https = require("https")

var authToken = "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJkYXRhYmFzZUlkIjoiYUN4MjJXNGhmNFY4eU5hRFJXVDJTSCIsImFjY2Vzc1Blcm0iOiJmdWxsIiwidG9rZW5JZCI6IlpGVHh6UEVuT3kyZEZJa0QzbmtiT3hLVXNCNW0wM3laM2JjZWhjZDltQ0RmMjhPUGhVZGgxOFB3NUZ4Z3NMaXYiLCJpYXQiOjE2MTA4NjcxODIsImV4cCI6MTYxMDkxMDM4MiwiaXNzIjoiZHJvcGJhc2UuaW8iLCJzdWIiOiJEQ2J3ZHd2UGQyYjNDN3pTS3o5WFhYIn0.0hBdKiLe25rIAXLqaU0SlBNU7iaqL2fZDGBusgNPXXM";

var databaseUrl = "https://query.dropbase.io/aCx22W4hf4V8yNaDRWT2SH/";
var projectName = "trackingtable";


//const request_sender = require("./request_sender.js");
const app = express()
const port = 3000

app.get('/', async (req, res) => {
	console.log("received request");
	let options = {
		//hostname: databaseUrl,
		//path: projectName + (query.length > 0) ? "?" + query : "",
		headers: {
			Authorization: authToken
		}
	}
	path = databaseUrl + projectName;
	console.log(path);

	https.get(path, options, async (response) => {
		//response.on("data", (d) => {
		await response;
			//res.send(JSON.parse(response));
			console.log(response.toString());
			res.send(response.toString());
		//});
	});

	//res.send("Hello World!");
	return;
});

app.listen(port, () => {
	console.log(`Example app listening at http://localhost${port}`)
});


