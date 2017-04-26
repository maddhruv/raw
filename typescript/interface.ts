interface operatorInterface {
  shape: string,
  side: number
}

function area(x:operatorInterface){
  return x.side*x.side;
}

var cal = area({shape:"square", side:2});
