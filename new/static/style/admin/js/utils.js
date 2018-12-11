function Post(url, data) {
	var form = document.createElement("form");
	form.setAttribute("action", url);
	form.setAttribute("method", "post");
	form.style.display = "none";
	for (var k in data) {
		var tx = document.createElement("textarea");
		tx.name = k;
		if (typeof data[k] === 'string') {
			data[k] = data[k].trim();
		}
		tx.value = data[k];
		form.appendChild(tx);
	}
	document.body.appendChild(form);
	form.submit();
}

function Get(url, data) {
	var uri = "";
	for (var k in data) {
		if (typeof data[k] === 'string') {
			data[k] = data[k].trim();
		}
		uri += (k+"="+data[k]+"&");
	}
	uri = uri.substring(0, uri.length - 1);
	if (uri != "") url += "?" + uri;
	location.href = url;
}