function getLottoNums() {
    let nums = [];
    
    while (nums.length < 6){
        let randomNum = Math.ceil(Math.random() * 47);
        if (randomNum === 17 || randomNum === 39) {
            continue;
        } else if (!nums.includes(randomNum)) {
            nums.push(randomNum);
        }
    }

    return nums;
}

let lottoNums = getLottoNums();
console.log(lottoNums);
