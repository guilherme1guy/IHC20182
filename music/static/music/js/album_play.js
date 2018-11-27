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