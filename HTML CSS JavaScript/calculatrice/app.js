const buttons_write = document.querySelectorAll('.write');
const ac = document.querySelector('.ac');
const backspace = document.querySelector('.backspace');
const equal = document.querySelector('.equal');
const userEntry = document.querySelector('.user-entry');
const result = document.querySelector('.result');
const arraySymbolsNames = ['division', 'multiplication', 'addition', 'subtraction', 'point']
const arraySymbols = ['/', '*', '+', '-', '(', ')'];


// let us make those buttons able to write on the screen
buttons_write.forEach(item =>{
    item.addEventListener('click', ()=>{
        userEntry.innerText += item.innerText;
        let entry = userEntry.innerText;
        let charBeforeEntry = entry.charAt(entry.length - 2);
        if(arraySymbolsNames.includes(item.classList[0])){          
            if(['+', '-', '.', '÷', '×'].includes(charBeforeEntry)){
                result.innerText = 'SyntaxError';
            }
        }
        if(item.classList[0]==='zero'){            
            if(charBeforeEntry==='÷'){
                result.innerText = 'MathError';
            }
        }
        if(item.classList[0]==='parenthesis-open'){
            if(charBeforeEntry==='.'){
                result.innerText = 'SyntaxError';
            }
        }
        if(item.classList[0]==='parenthesis-close'){
            if(['+', '-', '.', '÷', '×', '('].includes(charBeforeEntry)){
                result.innerText = 'SyntaxError';
            }
        }
        
    }, false)
});

// let us make the buttons, except equal, to work
ac.addEventListener('click', ()=>{
    userEntry.innerText = '';
    result.innerText = '';
}, false);

backspace.addEventListener('click', ()=>{
    userEntry.innerText = userEntry.innerText.slice(0, -1);
    let resultText = result.innerText ;
    if(resultText !== '' || resultText.includes('Error')){
        result.innerText = '';
    }
}, false);

// now, let us make the button equal able to work
equal.addEventListener('click',()=>{
    let entry = userEntry.innerText;
    let lastChar = entry.charAt(entry.length - 1);
    let charBeforeLast = entry.charAt(entry.length - 2);
    if(entry.includes('Error')){
        return true;
    }else{
        result.innerText = operate(entry);
    }

} , false)

function operate(data){
    let arrayData = data.split('');
    // let us change symbols '÷' and '×' by '/' and '*'
    for(let i = 0; i < arrayData.length; i++){
        if(arrayData[i]==='÷'){
            arrayData[i]='/';
        }
        if(arrayData[i]==='×'){
            arrayData[i]='*';
        }
    }
    arrayData = splitAsWill(arrayData);
    let array_length = arrayData.length;
    console.log(array_length);
    // let's continue
    
    if(array_length===0){
        return '';
    }else if(array_length===1){
        if(isNaN(parseFloat(data))){
            return 'SyntaxError';
        }else{
            return data;
        }
    }else if(array_length===2){
        if(['.', '/', '*', ')', '('].includes(arrayData[0])){
            return 'SyntaxError';
        }else if(isNaN(parseFloat(arrayData[1]))){
            return 'SyntaxError';
        }else{
            return eval(arrayData.join(''));
        }
    }else if(array_length==3){        
        return eval(arrayData.join('')); // eval() returns a number not a string in this case.
    }else{
        if((''+eval(arrayData.join(''))) === 'Infinity'){
            return 'MathError';
        }else if((arrayData.includes('(') || arrayData.includes(')'))){
            if(nbOccurence('(', arrayData) !== nbOccurence(')', arrayData)){
                alert('( :' + nbOccurence('(', arrayData) + ') :' + nbOccurence(')', arrayData) );
                return 'SyntaxError';
            }else{
                return eval(arrayData.join(''));
            }
        }else{
            return eval(arrayData.join(''));
        }
    }
    
}
function splitAsWill(tab){
    // let operators_array = str.split('').filter(item=>{isNaN(parseFloat(item))});
    let array = [];
    let temp ='';
    for(let i = 0, c = tab.length; i < c; i++){
        if(arraySymbols.includes(tab[i])){
            if(temp !== ''){
                array.push(temp);
            }
            if(tab[i]!==temp){
                array.push(tab[i]);
            }
            temp = '';
        }else{
            temp += tab[i];
        }
    }
    if(temp){
        array.push(temp);
    }
    return array;
}
function nbOccurence(elt, tab){
    let count = tab.reduce((accumulator, currentValue)=>{
        return currentValue === elt ? accumulator + 1 : accumulator ;
    }, 0);

    return count;
}