const https = require("https")

var authToken = "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJkYXRhYmFzZUlkIjoiYUN4MjJXNGhmNFY4eU5hRFJXVDJTSCIsImFjY2Vzc1Blcm0iOiJmdWxsIiwidG9rZW5JZCI6IlpGVHh6UEVuT3kyZEZJa0QzbmtiT3hLVXNCNW0wM3laM2JjZWhjZDltQ0RmMjhPUGhVZGgxOFB3NUZ4Z3NMaXYiLCJpYXQiOjE2MTA4NjcxODIsImV4cCI6MTYxMDkxMDM4MiwiaXNzIjoiZHJvcGJhc2UuaW8iLCJzdWIiOiJEQ2J3ZHd2UGQyYjNDN3pTS3o5WFhYIn0.0hBdKiLe25rIAXLqaU0SlBNU7iaqL2fZDGBusgNPXXM";

var databaseUrl = "https://query.dropbase.io/aCx22W4hf4V8yNaDRWT2SH/";
var projectName = "trackingtable";

/*
function setAuth(tokenVal) {
	authToken = tokenVal;
}

function setDatabase(url) {
	databaseUrl = url;
}

function setProject(name) {
	projectName = name;
}
*/

/*
exports.sendGetReq = (requestVal) => {
	var xhttp = new XMLHttpRequest();
	xhttp.onreadystage = function() {
		if (this.readyState == 4 && this.status == 200) {
			populateSideWindow(JSON.parse(this.responseText));
		}
	};
	xhttp.open("GET", databaseUrl+projectName, true);
	xhttp.setRequestHeader("Authorization", authToken);
	xhttp.send();
}
*/

exports.submitRequest = (query, callback) => {
	let options = {
		//hostname: databaseUrl,
		//path: projectName + (query.length > 0) ? "?" + query : "",
		headers: {
			Authorization: authToken
		}
	}
	path = databaseUrl + projectName;
	console.log(path);

	https.get(path, options, callback);
};

