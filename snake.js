

class Snake{

    constructor(x, y){
        this.color = {r:255,g:255,b:255}
        this.headColor = {r:50,g:255,b:50}
        this.x = x
        this.y = y
        this.scelta = 'u'
        this.bodyRect = [new Rect(this.x, this.y, color=this.color), new Rect(this.x, this.y, color=this.color), new Rect(this.x, this.y, color=this.color)]
        this.apple = new Rect(0, 0, {r:255,g:0,b:0})
        this.randomApple()
    }

    show(){
        this.apple.show()
        controls()
        for(let r of this.bodyRect){
            r.show()
        }

    }


    randomApple(){
        this.apple.x = parseInt(random(canvasWidth/side))*side
        this.apple.y = parseInt(random(canvasHeight/side))*side
    }


    addElement(){
        this.bodyRect.push(new Rect(this.x, this.y, color=this.color))
    }

    moveInterval(){
        this.moveRect()
        this.gameOver()
        this.gameWin()
    }

    moveRect(){
    
        if(this.scelta == 'u'){
            this.y -= side
        }
        if(this.scelta == 'b'){
            this.y += side
        }
        if(this.scelta == 'l'){
            this.x -= side
        }
        if(this.scelta == 'r'){
            this.x += side
        }

        this.bodyRect[this.bodyRect.length-1].color =  this.color
        this.bodyRect.push(new Rect(this.x, this.y, this.headColor))
        this.bodyRect.shift()
    }

    move(scelta){
        this.scelta = scelta
    }

    gameWin(){
        if(this.x == this.apple.x && this.y == this.apple.y){
            this.addElement()
            this.randomApple()
            score += 10*(this.bodyRect.length-3)
            document.getElementById('score').innerHTML = score
        }
    }

    gameOver(){

        let collision = false

        for(let r of this.bodyRect.slice(0, -1)){
            if(this.bodyRect[this.bodyRect.length-1].x == r.x && this.bodyRect[this.bodyRect.length-1].y == r.y){
                collision = true
            }
        }

        if(this.x < 0 || this.x > canvasWidth-side || this.y < 0 || this.y > canvasHeight-side || collision){
            alert('Game Over')
            addClassifica()
            
        }
    }

    
      
   
      


}