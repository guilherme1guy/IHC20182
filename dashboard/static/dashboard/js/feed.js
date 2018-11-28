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
