var video = document.querySelector('#videoElement');
var canvas = document.querySelector('#canvas');

var context = canvas.getContext('2d');
var rawImData; var link; var fileName;

navigator.mediaDevices.getUserMedia({video: true})
  .then(function(stream) {
    video.srcObject = stream;
  }).then(getScreenshot());

function getScreenshot(){
  setInterval(function() {
    context.clearRect(0,0, canvas.width, canvas.height);
    context.beginPath();
    context.drawImage(video, 0, 0, canvas.width, canvas.height);
    //download();
  }, 1000);
}

function download() {
  rawImData = canvas.toDataURL("image/jpeg", 1.0);
  fileName = "download.jpeg";
  //rawImData = rawImData.replace("image/jpeg", "image/octet");
  //document.location.href = rawImData;
  //document.body.removeChild(canvas);
  
  link = document.createElement('a');
  link.href = rawImData;
  link.download = fileName;
  document.body.appendChild(link);
  link.click();
  document.body.removeChild(link);
}
