function submitRequest(query) {
	var xhttp = new XMLHttpRequest();
	xhttp.onreadystage = function() {
		if (this.readyState == 4 && this.status == 200)  {
			this.on("data", (value) => {
				populateSideWindow(JSON.parse(value));
			}
		}
	};
	xhttp.open("GET", "localhost:3000/", true);
	//xhttp.setRequestHeader("Authorization", authToken);
	xhttp.send();
}
