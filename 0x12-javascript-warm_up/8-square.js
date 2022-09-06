#!/usr/bin/node

const size = parseInt(process.argv[2]);

if (isNaN(size)) console.log('Missing size');

for (let i = 1; i <= size; i++) {
  const temp = [];
  for (let j = 1; j <= size; j++) temp.push('X');
  console.log(temp.join(''));
}
