function myFunction(e, number) {
  var element;

  if(e.id == "like"){
    e.id = "unlike";
    e.querySelector('#heart').className = "fas fa-heart red-icon col-auto px-1";
    number++;
    e.querySelector('#number_likes').innerHTML = number;
  }
  else if(e.id == "unlike"){
    e.id = "like";
    e.querySelector('#heart').className = "far fa-heart red-icon col-auto px-1";
    e.querySelector('#number_likes').innerHTML = number--;
  }

}

function playAudio(e) {
  var x = document.getElementById("myAudio");
  
  if(e.querySelector('#play').className == "fas fa-play fa-3x play-button"){
    e.querySelector('#play').className = "fas fa-pause fa-3x play-button"
    x.play(); 
  }
  else if(e.querySelector('#play').className == "fas fa-pause fa-3x play-button"){
    e.querySelector('#play').className = "fas fa-play fa-3x play-button"
    x.pause();
  }

} 

function playAudio2(e) {
  var x = document.getElementById("myAudio");
  
  if(e.querySelector('#play').className == "fas fa-play fa-2x small-play-button play-icon"){
    e.querySelector('#play').className = "fas fa-pause fa-2x small-play-button play-icon"
    x.play(); 
  }
  else if(e.querySelector('#play').className == "fas fa-pause fa-2x small-play-button play-icon"){
    e.querySelector('#play').className = "fas fa-play fa-2x small-play-button play-icon"
    x.pause();
  }

}  

