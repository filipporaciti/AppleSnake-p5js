let canvasWidth = side*20
let canvasHeight = side*20

const timeInterval = 200

let canvasY = 135

let score = 0

let press = false
let touchMov = ''

let gameInterval




function setup() {
    while(window.innerHeight < canvasHeight+canvasY || window.innerWidth < canvasWidth){
        side -= 1
        canvasHeight = side*20
        canvasWidth = side*20
    }
    let canvas = createCanvas(canvasWidth, canvasHeight);
    canvas.position(windowWidth/2-width/2, canvasY)
    snake = new Snake(canvasWidth/2,canvasHeight)
    gameInterval = setInterval(() => snake.moveInterval(), timeInterval)
}

function draw() {
    background(0)

    snake.show()

}

function controls(){
    if(keyIsPressed == true || touchMov != ''){

        if ((key == "ArrowLeft" || key == "a" || touchMov == 'l') && !press && snake.scelta != 'r') {
            snake.move('l')
        }
        if ((key == "ArrowRight" || key == "d" || touchMov == 'r') && !press && snake.scelta != 'l') {
            snake.move('r')
        }
        if ((key == "ArrowDown" || key == "s" || touchMov == 'b') && !press && snake.scelta != 'u') {
            snake.move('b')
        }
        if ((key == "ArrowUp" || key == "w" || touchMov == 'u') && !press && snake.scelta != 'b') {
            snake.move('u')
        }
        press = true
        touchMov = ''
      }else{
        press = false
      }
    
}

function touchStarted() {
    touchMov = ''
    startX = mouseX
    startY = mouseY
    
  }
function touchEnded() {
    if(startX < mouseX && ((mouseX-startX) > Math.pow(Math.pow(mouseY-startY, 2), 0.5))){
      touchMov = 'r'
    }else if(startX >= mouseX && ((startX-mouseX) > Math.pow(Math.pow(mouseY-startY, 2), 0.5))){
      touchMov = 'l'
    }else if(startY < mouseY && ((mouseY-startY) > Math.pow(Math.pow(mouseX-startX, 2), 0.5))){
      touchMov = 'b'
    }else if(startY >= mouseY && ((startY-mouseY) > Math.pow(Math.pow(mouseX-startX, 2), 0.5))){
      touchMov = 'u'
    }
    controls()
  }
  
function windowResized() {
    let canvas = createCanvas(canvasWidth, canvasHeight);
    canvas.position(windowWidth/2-width/2, canvasY)
    setCanvasSize()
}



