function add(a:number, b:number):number{
  return a+b;
}

function square(a:number, b:number = a):number{//default argument
  return a*b;
}

function integer(a:number, b?:boolean):number{//optional argument
  if(b){
    return Math.floor(a);
  }
  return a;
}

function addNumbers(...num:number[]){//rest argument
  var i:number = 0;
  var sum:number = 0;

  for(i;i<num.length;i++){
    sum+=num[i];
  }
  return sum;
}

var f = (x:number)=>{
  10+x
}
