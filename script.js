var video = document.querySelector('#videoElement');
var canvas = document.querySelector('#canvas');
var display = document.querySelector("#display");
var logElem = document.querySelector("#log");

var context = canvas.getContext('2d');
var rawImData; var link; var fileName;

let stopButton = document.getElementById("stopButton");

navigator.mediaDevices.getUserMedia({video: true})
  .then(function(stream) {
    video.srcObject = stream;
  }).then(getScreenshot());


var intSetter = setInterval(function() {
  context.clearRect(0,0, canvas.width, canvas.height);
  context.beginPath();
  context.drawImage(video, 0, 0, canvas.width, canvas.height);
  download();
}, 1000);
  
function getScreenshot(){
  intSetter;
  textSetter;
}

function stop(stream) {
  stream.getTracks().forEach(track => track.stop());
  clearInterval(intSetter);
}

function download() {
  rawImData = canvas.toDataURL("image/jpeg", 1.0);
  fileName = "ss_file.jpeg";
  link = document.createElement('a');
  link.href = rawImData;
  link.download = fileName;
  document.body.appendChild(link);
  link.click();
  document.body.removeChild(link);
}

stopButton.addEventListener("click", function() {
  stop(video.srcObject);
}, false);

var http_request = new XMLHttpRequest();

function makeRequest() {
  http_request.onreadystatechange = handleCheckboxRequest;
  http_request.open('GET','file.txt',true);
  http_request.send(null);
}  

function handleCheckboxRequest() {     
  if (http_request.readyState == 4 && http_request.status == 200) {
	logElem.innerHTML = http_request.responseText;
  }
}

var textSetter = setInterval(function() {
	http_request.onreadystatechange = handleCheckboxRequest;
	http_request.open('GET','file.txt',true);
	http_request.send(null);
}, 100);