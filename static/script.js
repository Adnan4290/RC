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
 //function to handle sse
function handleSSE(event) {
if (event.data.startsWith('data:image/jpeg;base64,')) {
  $('#video-stream').attr('src', event.data);
}
}
//code to open a new SSE connection
var eventSource = new EventSource('/video_feed');
eventSource.addEventListener('message', handleSSE);




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
    sendControals({ 'right': 0 });
  });
