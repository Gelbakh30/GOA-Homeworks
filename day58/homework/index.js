// for (let i = 20; i >= 5; i++) {
//     console.log(i);
// }



function sumOfEvens(max) {
    let sum = 0;
    for (let i = 0; i <= max; i += 2) { 
        sum += i;
    }
    return sum;
}


console.log(sumOfEvens(10)); 
console.log(sumOfEvens(20)); 
