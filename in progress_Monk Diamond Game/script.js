function startGame(){
    gameLoop();
}

var loop = 0;
var characterVisible = false;
function gameLoop(){
    characterVisible=!characterVisible;

    loop++;
    if(loop<12){
        // alert("Game has Started!");
        setTimeout(gameLoop,1000);
        flashCharacter();
    } else{
        alert("Game Over!");
    }
}

function flashCharacter(){
    var Guests = document.querySelectorAll(".guest");
    var classToSet = "";
    if (characterVisible){
        classToSet="guest visible";
    }else{
        classToSet="guest hidden";
    }

    for (var index = 0; index < 12; index++){
        Guests[index].classList=classToSet;
    }
}