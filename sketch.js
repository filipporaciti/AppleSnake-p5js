const canvasWidth = side*20
const canvasHeight = side*20

const timeInterval = 200

let canvasY = 150

let score = 0


function setup() {
    let canvas = createCanvas(canvasWidth, canvasHeight);
    canvas.position(windowWidth/2-width/2, canvasY)
    snake = new Snake(canvasWidth/2,canvasHeight)
    gameInterval = setInterval(() => snake.moveInterval(), timeInterval)
}

function draw() {
    background(0)

    snake.show()

}

function windowResized() {
    let canvas = createCanvas(canvasWidth, canvasHeight);
    canvas.position(windowWidth/2-width/2, canvasY)
}
