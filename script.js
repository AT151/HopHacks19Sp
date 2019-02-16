var video = document.querySelector('#videoElement');
var canvas = document.querySelector('#canvas');
var display = document.querySelector("#display");


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
}


function stop(stream) {
  stream.getTracks().forEach(track => track.stop());
  clearInterval(intSetter);
}

function download() {
  rawImData = canvas.toDataURL("image/jpeg", 1.0);
  fileName = "download.jpeg";
  link = document.createElement('a');
  link.href = rawImData;
  link.download = fileName;
  document.body.appendChild(link);
  link.click();
  document.body.removeChild(link);
}

stopButton.addEventListener("click", function() {
  stop(video.srcObject);
}, false)
