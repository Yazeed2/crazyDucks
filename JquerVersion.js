var score = 100
var enm = 20

function start(){
var here = 0
var scoring = setInterval(()=>{
    here += 3
    $('#score').replaceWith(' <h1 id="score">'+here+'</h1>')

}, 130)

var interval = 1000
   var timing = setInterval(() => {
       if(score > 0){

      
        spawn()
        interval += 1000
    console.log('hey');
    
        if(interval == 4000){
            spawn()
        }else if(interval >= 6000){
                spawn()
                spawn()
            }
        }else{
            // clearInterval(scoring);

            clearInterval(timing);
            alert('game Over')
            clearInterval(timing);
            clearInterval(scoring);
            location.reload()
            
        }
    }, interval);


function spawn(){
    count(-enm)
    let i = Math.floor(Math.random() * 729)+ 1;
    if (score < 0 ){
        clearInterval(timing);

       
    }
    let duck = $('<div onload="sub()" class = "duck animation'+i+'"></div> ')
    duck.on('click',(thisduck)=>{
        count(+enm)
        duck.hide()
    console.log(score);

    })
    
     duck.prependTo($('#game')); 
}
}
function count(i){
    score = score + i
    $('#health').replaceWith(' <p id="health">'+score+'%</p>')
    if(score <= 0){

        clearInterval(timing);
        alert('game Over')
        clearInterval(timing);
        clearInterval(scoring);
        location.reload()
    }
    
}