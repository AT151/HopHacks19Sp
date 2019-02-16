var video = document.querySelector('#videoElement');
var canvas = document.querySelector('#canvas');
var context = canvas.getContext('2d');
var rawImData;

navigator.mediaDevices.getUserMedia({video: true})
  .then(function(stream) {
    video.srcObject = stream;
  }).then(getScreenshot());

function getScreenshot(){
  setInterval(function() {
    context.clearRect(0,0, canvas.width, canvas.height);
    context.beginPath();
    context.drawImage(video, 0, 0, canvas.width, canvas.height);
    download();
  }, 1000);
}

function download() {
  rawImData = canvas.toDataURL("image/jpg;base64");
  rawImData = rawImData.replace("image/jpg", "image/octet");
  document.location.href = rawImData;
  document.body.removeChild(canvas);
}
