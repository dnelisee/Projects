const form = document.querySelector('.form-quizz')
const arrayResults = ['b', 'a', 'a']; // this is the array that contents the true answers of the quizz
const emojis = ['✔','✨', '👀', '😭', '👎'];
let arrayAnswers = []; // This is the array that will content the user's answers
const titleResultat = document.querySelector('.resultats h2');
const scoreResultat = document.querySelector('.score');
const helpResultat = document.querySelector('.help');
const arrayQuestions = document.querySelectorAll('.question-block');
const total = arrayResults.length;
let verifArray = [];


form.addEventListener('submit', (e)=>{
    e.preventDefault();
    
    for(var i = 0; i < total; i++){
        let question = arrayQuestions[i];
        arrayAnswers.push(
            question.querySelector('div input:checked').value
        );
    }

    verifFunc(arrayAnswers);
    arrayAnswers = [];
}, false)

function verifFunc(arrAnswers){
    for(let i = 0; i < total; i++){
        if(arrAnswers[i]===arrayResults[i]){
            verifArray.push(true);
        }else{
            verifArray.push(false);
        }
    }
    printResult(verifArray);
    colorFunc(verifArray);
    verifArray = [];
}

function printResult(verifArray){
    const nbDeFautes = verifArray.filter(elt => elt !== true).length;
    if(nbDeFautes===0){
        titleResultat.innerText = "👍👌 Bravo, c'est un sans faute ! 👌👍";
        helpResultat.innerText = '';
        scoreResultat.innerText = total + '/' + total;
    }else if(nbDeFautes===total){
        titleResultat.innerText = "👎 Peux mieux faire 👎";
        helpResultat.innerText = 'Retentez une autre réponse dans les cases rouges et re-validez !';
        scoreResultat.innerText = '0/'+ total;
    }else if(nbDeFautes === 1){
        titleResultat.innerText = "✨ Vous y êtes presque ✨";
        helpResultat.innerText = 'Retentez une autre réponse dans la case rouge et re-validez !';
        scoreResultat.innerText = (total-1) + '/' + total;
    }else{
        titleResultat.innerText = "😭Encore un effort... 👀";
        helpResultat.innerText = 'Retentez une autre réponse dans les cases rouges et re-validez !';
        scoreResultat.innerText = (total-nbDeFautes) + '/' + total;
    }
}

function colorFunc(verifArray){
    for(let i = 0; i < total; i++){
        if(verifArray[i]===true){
            arrayQuestions[i].classList.add('success');   
        }else{
            arrayQuestions[i].classList.add('echec');
        }
    }
    
}
arrayQuestions.forEach(item => {
    item.addEventListener('click', ()=>{
        if(item.classList.contains('echec')){
            item.classList.remove('echec');
        }
        if(item.classList.contains('success')){
            item.classList.remove('success');
        }
    }, false);
})

