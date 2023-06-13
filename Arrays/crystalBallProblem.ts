// Given two crystal balls that will break if dropped from high enough distance, determine the exact spot in which it will break-
// in the most optimized way.
let breaks = [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1]

const jmpAmount = Math.floor(Math.sqrt(breaks.length));
let i=jmpAmount
for (; i < breaks.length; i += jmpAmount) {
    if (breaks[i]){
        break;
    }
}
i -= jmpAmount;

for (let j = 0; j < jmpAmount && i < breaks.length){

}