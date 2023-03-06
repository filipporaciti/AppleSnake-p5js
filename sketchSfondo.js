var canvasSfondo = function( sketch ) {

    sketch.setup = function() {
     let canvas = sketch.createCanvas(sketch.windowWidth, sketch.windowHeight);
       canvas.style("z-index: -100");
     canvas.position(0,0);
   }
   sketch.draw = function() {
  
    
    let circle = sketch.createDiv();
    circle.style("width: 6px;");
    circle.style("height: 6px;");
    circle.style("background-color: coral");
    circle.style("z-index: -100");
    circle.style("border-radius: 100px");
    circle.position(sketch.random(sketch.windowWidth), sketch.random(sketch.windowHeight));

   
   }
  };
  
  
  new p5(canvasSfondo);