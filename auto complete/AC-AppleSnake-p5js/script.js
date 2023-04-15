

windowChangeStyle()




onresize = (event) => {
    windowChangeStyle()
};


function windowChangeStyle(){
    let width = window.innerWidth
    
}



function setCanvasSize(){
    side = 35
    canvasHeight = side*20
    canvasWidth = side*20
    while(window.innerHeight < canvasHeight+canvasY || window.innerWidth < canvasWidth){
        side -= 1
        canvasHeight = side*20
        canvasWidth = side*20
    }

   

    
}

