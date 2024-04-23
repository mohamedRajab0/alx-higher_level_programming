#!/usr/bin/node
if (process.argv.length < 4) {
  console.log(0);
  return;
}
let max = process.argv[2];
let sec_bigest = process.argv[2];
for (let i = 3; i < process.argv.length; i++) {
  if (process.argv[i] > max) {
      sec_bigest = max;
    max = process.argv[i];
  }
}
console.log(sec_bigest);
