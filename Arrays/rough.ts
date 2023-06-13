let haystack =  [1, 2, 5, 8, 10, 22, 67, 88, 93, 144, 655];
let needle = 22
let hi = haystack.length;
let lo = 0

do{
    const m = Math.floor(lo + (hi-lo) / 2) 
    const val = haystack[m]

    if(val === needle) {
        console.log("True");
    }
    else if(val > needle) {
        hi = m;
    }
    else{
        lo = m + 1
    }
} while(lo > hi);
