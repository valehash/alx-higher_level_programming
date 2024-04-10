#!/usr/bin/node

if (process.argv[2] === undefined){
  conosle.log("Not a number")
}
const num = parseInt(process.argv[2]);
if (isNaN(num)){
  console.log("Not a number");
}else
  console.log("My number:",num);
