// Define a function to send the control data to the server
function sendControls(data) {
    // Send the AJAX request to the server
    $.ajax({
        type: 'POST',
        url: '/control',
        data: data,
        success: function (response) {
            // Update the message on the webpage
            $('#message').html(response);
        }
    });
}
// Bind event listeners to the control buttons
$('#up').on('mousedown', function () {
    sendControls({ 'up': 1 });
}).on('mouseup', function () {
    sendControls({ 'up': 0 });
});

$('#down').on('mousedown', function () {
    sendControls({ 'down': 1 });
}).on('mouseup', function () {
    sendControls({ 'down': 0 });
});

$('#left').on('mousedown', function () {
    sendControls({ 'left': 1 });
}).on('mouseup', function () {
    sendControls({ 'left': 0 });
});

$('#right').on('mousedown', function () {
    sendControls({ 'right': 1 });
}).on('mouseup', function () {
    sendControls({ 'right': 0 });
});
// ------------------------------------------------------input control code --------------------------
//------------------------------------------------------video controlling code starts ------------------
  var video = document.querySelector('#video');
  var stream = new MediaSource();
  var sourceBuffer = null;

  stream.addEventListener('sourceopen', function() {
    sourceBuffer = stream.addSourceBuffer('video/mp4; codecs="avc1.42E01E"');
  });

  video.src = window.URL.createObjectURL(stream);

  fetch('/video_feed')
    .then(function(response) {
      return response.body;
    })
    .then(function(body) {
      var reader = body.getReader();
      function read() {
        reader.read().then(function(result) {
          if (result.done) {
            return;
          }
          sourceBuffer.appendBuffer(result.value.buffer);
          read();
        });
      }
      read();
    });
    //-------------------------------------------------------------
    var socket = io.connect('http://' + document.domain + ':' + location.port);
    socket.on('connect', function() {
      console.log('Connected to server');
    });
    socket.on('disconnect', function() {
      console.log('Disconnected from server');
    });
    socket.on('frame', function(data) {
      var canvas = document.getElementById('video-canvas');
      var context = canvas.getContext('2d');
      var img = new Image();
      img.onload = function() {
        context.drawImage(img, 0, 0);
      };
      img.src = 'data:image/jpeg;base64,' + data;
    });
    // ----------------------------maps code --------------
    function initMap() {
      const map = new google.maps.Map(document.getElementById("map"), {
        center: { lat: 37.7749, lng: -122.4194 }, // set the initial center of the map
        zoom: 8, // set the initial zoom level
      });
    }
    // ---------------------------------------------------------
    // const switchCameraBtn = document.getElementById('switch-camera-btn');

    // switchCameraBtn.addEventListener('click', () => {
    //   // Define the request parameters
    //   const requestOptions = {
    //     method: 'POST',
    //     headers: { 'Content-Type': 'application/json' },
    //     body: JSON.stringify({}),
    //   };
    
    //   // Send the POST request
    //   fetch('/switch_camera', requestOptions)
    //     .then(response => {
    //       // Handle the response
    //       console.log('Switch camera request sent successfully');
    //     })
    //     .catch(error => {
    //       // Handle the error
    //       console.error('Error sending switch camera request:', error);
    //     });
    // });
    // ==============================


    


