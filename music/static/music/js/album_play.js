$("a[id*='album-play']").each(function (i, el) {
    $(this).click(function() {
        var audio = document.getElementById("player");
        $('#play-icon').find('i').toggleClass('fa-play fa-pause')
        $(this).find('i').toggleClass('fa-play fa-pause')
        if($(this).find('i').hasClass('fa-pause')){
            audio.play();
        } else {
            audio.pause();
        }
    });
});

$("a[id*='playlist-play']").each(function (i, el) {
    $(this).click(function() {
        var audio = document.getElementById("player");
        $('#play-icon').find('i').toggleClass('fa-play fa-pause')
        $(this).find('i').toggleClass('fa-play fa-pause')
        if($(this).find('i').hasClass('fa-pause')){
            audio.play();
        } else {
            audio.pause();
        }
    });
});

previouslyClicked = $(".btn").eq(0);
$(".track").click(function () {
     previouslyClicked.removeClass("selected");
     $(this).addClass("selected");
     previouslyClicked = $(this);
     var audio = document.getElementById("player");
     if($('#play-icon').find('i').hasClass('fa-play')){
            $('#play-icon').find('i').toggleClass('fa-play fa-pause');
            audio.play();
     }
});