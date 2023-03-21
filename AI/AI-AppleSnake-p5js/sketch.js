let canvasWidth = side*20
let canvasHeight = side*20

const timeInterval = 500

let canvasY = 135

let score = 0

let press = false
let touchMov = ''

let gameInterval

let end = false



let x = 0 
let y = 0 
let xm = 0 
let ym = 0
let l = 0

let nx = 0 
let ny = 0 
let nxm = 0 
let nym = 0
let nl = 0

let reward = 100


function setup() {
    while(window.innerHeight < canvasHeight+canvasY || window.innerWidth < canvasWidth){
        side -= 1
        canvasHeight = side*20
        canvasWidth = side*20
    }
    let canvas = createCanvas(canvasWidth, canvasHeight);
    canvas.position(windowWidth/2-width/2, canvasY)
    snake = new Snake(canvasWidth/2,canvasHeight-side)


    gameInterval = setInterval(() => snake.moveInterval(), timeInterval)
}

function draw() {
    background(0)

    snake.show()

}

function controls(action){
   //console.log(action)
    switch (action){
      case 0:
        snake.move('u')
        break
      case 1:
        snake.move('l')
        break
      case 2:
        snake.move('b')
        break
      case 3:
        snake.move('r')
        break
    }
    
}

function getAction(){
  x = snake.bodyRect[snake.bodyRect.length-1].x/side 
  y = snake.bodyRect[snake.bodyRect.length-1].y/side 
  xm = snake.apple.x/side 
  ym = snake.apple.y/side 
  l = snake.winTime

  //clearInterval(gameInterval)

  fetch('http://192.168.1.253:5050/getAction?' + new URLSearchParams({
    l: l,
    x: x,
    y: y,
    xm: xm,
    ym: ym
  }))
  .then((response) => response.json())
  .then((data) => {
      if(data['action'] == 'Errore getAction'){
        // print(x, y, xm, ym, l)
      }else{
        controls(data['action'])
      }
      
  //gameInterval = setInterval(() => snake.moveInterval(), timeInterval)

      
  })
}


function sendReward(l, x, y, xm, ym, nl, nx, ny, nxm, nym){
  print('reward: ', reward)
  data = {'l': l, 'x': x, 'y': y, 'xm': xm, 'ym': ym, 'nl': nl, 'nx': nx, 'ny': ny, 'nxm': nxm, 'nym': nym, 'reward': reward}
  fetch('http://192.168.1.56:8081/setAction', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(data)
    })
        .then((response) => response.json())
        .finally(() => {
          if (end) {
            location.reload();
          }
        })
  print(reward, x, y)
}


  
function windowResized() {
    let canvas = createCanvas(canvasWidth, canvasHeight);
    canvas.position(windowWidth/2-width/2, canvasY)
    setCanvasSize()
}



