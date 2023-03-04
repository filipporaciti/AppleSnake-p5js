let side = 34



class Rect{
    constructor(x=0, y=0, color={r:0, g:0, b:0}){
        this.x = x
        this.y = y
        this.color = color
        this.side = side
    }

    show() {
        fill(this.color["r"], this.color["g"], this.color["b"])
        strokeWeight(1.5)
        rect(this.x, this.y, this.side, this.side, 1)
    }

}