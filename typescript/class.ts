class avengers{
  name:string;
  age:number;
}

class hero{
  name:string;
  age:number;

  constructor(a:string,b:number){
    this.name = a;
    this.age = b;
  }

  ageR():string{//method
    return this.age +' Years';
  }
}

class rect{
  l1:number;
  l2:number;
  perm:number;

  constructor(l1:number, l2:number){
    this.l1 = l1;
    this.l2 = l2;
  }

  get area():number{//getter
    return this.l1*this.l2;
  }

  set perimeter(len:number){//setter
    this.perm = len;
  }
}

var ironman = new avengers();

ironman.name = "Tony Stark";
ironman.age = 42;

var captain = new hero("Steve", 32);
console.log(captain.ageR());


var myRect = new rect(10,20);
myRect.perimeter = 200;
console.log(myRect.area);
