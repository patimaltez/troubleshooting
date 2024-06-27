function BracketMatcher(str) { 

    let stack = [];
    for (let char of str) {
      if (char === '(') {
        stack.push('(');
      } 
      else if (char === ')') {
        if(stack.length === 0) {
          return 0;
        }
        stack.pop();
      }
    }
    return stack.length === 0 ? 1 : 0; 
  
  }
     
  // keep this function call here 
  console.log(BracketMatcher(readline()));