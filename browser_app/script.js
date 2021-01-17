
function search() {
  var table = document.getElementById("sidePane");
}

function populateSideWindows() {
  var table = document.getElementById("sidePane");
  var row; 
  data = ["MAybe this will work"]
  for(var i = 0; i < data.length; i++) { //all events
      fps = 29.97;
      objectName = i[0];
      entOrExit = i[1];
      frameNumber = i[2];
      time = frameNumber/fps;

      row = table.insertRow();
      row.outerHTML = '<tr onclick="jump()"><tr onclick="jump(5)" class="nonStickey"><td>' + objectName + '<</tr></tr>'
      
  }
}

var isPlaying = false; //true --> is playing

function togglePlay() {
  isPlaying = !isPlaying;
  var player = document.getElementById('video_player');

  if(isPlaying) {
    player.play();
    document.getElementById("play_button").outerHTML = '<img src="GUI/pause.jpg" width="25" height="25" onclick="togglePlay()"  id="play_button"></img> '
  }
  else {
    player.pause();
    document.getElementById("play_button").outerHTML = '<img src="GUI/play.jpg" width="25" height="25" onclick="togglePlay()"  id="play_button"></img> '
  }
}

function jump(time) {
  var player = document.getElementById("video_player");
  player.currentTime=time
}

if (document.readyState === "complete") {
  console.log("test")
}

