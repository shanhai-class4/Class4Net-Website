function accept()
{
	var xhr = new XMLHttpRequest();
	xhr.open('POST', './handle/accept/', true);
	xhr.setRequestHeader('Content-Type', 'text/plain');
	xhr.send("action=accept");
	xhr.onload = function() {
 		if (xhr.status == 200) {
            var response = JSON.parse(xhr.responseText);
    			window.location.href = xhr.responseText;
  		}
	};
}
function reject()
{
	var xhr = new XMLHttpRequest();
	xhr.open('POST', './handle/reject/', true);
	xhr.setRequestHeader('Content-Type', 'text/plain');
	xhr.send("action=reject");
	xhr.onload = function() {
 		if (xhr.status == 200) {
            var response = JSON.parse(xhr.responseText);
    			window.location.href = xhr.responseText;
  		}
	};
}
function delete_()
{
	var xhr = new XMLHttpRequest();
	xhr.open('POST', './handle/delete/', true);
	xhr.setRequestHeader('Content-Type', 'text/plain');
	xhr.send("action=delete");
	xhr.onload = function() {
 		if (xhr.status == 200) {
            var response = JSON.parse(xhr.responseText);
    			window.location.href = xhr.responseText;
  		}
	};
}