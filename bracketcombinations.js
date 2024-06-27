function BracketCombinations(num) { 

    if (num ===0) {
      return 1;
    }
    let count = 0;
    for (let i = 0; i < num; i++) {
      count += BracketCombinations(i) * BracketCombinations(num - i - 1);
    }
        
    return count; 
  
  }
     
  // keep this function call here 
  console.log(BracketCombinations(readline()));