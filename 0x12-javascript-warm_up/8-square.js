#!/usr/bin/node

const num = parseInt(process.argv[2]);
if (isNaN(num)){
  console.log("Missing size");
}else
  for (let i = 0; i < process.argv[2]; i++){
    let row = ""
    for (let j = 0; j < process.argv[2]; j++){
      row += "x";
    }
    console.log(row);
  }
