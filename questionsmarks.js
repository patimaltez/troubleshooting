function QuestionsMarks(str) {
    let numbers = [];
    let count = 0;
    let isTen = false;

    for (let i = 0; i < str.length; i++) {
        if (!isNaN(parseInt(str[i]))) {
            if (numbers.length === 0) {
                numbers.push(parseInt(str[i]));
            } else {
                let sum = numbers[numbers.length - 1] + parseInt(str[i]);
                if (sum === 10) {
                    isTen = true;
                    if (count !== 3) {
                        return "false";
                    } else {
                        count = 0;
                    }
                }
                numbers.push(parseInt(str[i]));
            }
        } else if (str[i] === "?") {
            count++;
        }
    }

    return isTen ? "true" : "false";
}

   
// keep this function call here 
console.log(QuestionsMarks(readline()));