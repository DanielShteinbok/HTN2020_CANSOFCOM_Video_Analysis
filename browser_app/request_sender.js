var authToken;
var databaseUrl;
var projetcName;

function setAuth(tokenVal) {
	authToken = tokenVal;

function setDatabase(url) {
	databaseUrl = url;

function setProject(name) {
	projectName = name;

submitRequest(requestVal) {
	var xhttp = new XMLHttpRequest();
	xhttp.onreadystage = function() {
		if (this.readyState == 4 && this.status == 200) {

