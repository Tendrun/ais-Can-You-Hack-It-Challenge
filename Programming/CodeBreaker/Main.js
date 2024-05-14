function getElement(index) {
    chars = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'.split('');
    return chars[index]
}

let currentScore = 0;
let password = '';

function inputElement(index = 0, position = 0){
    let element = getElement(index);
    return new Promise(resolve => {
    CodeBreaker_submit(password + element)
        .then(score => {
        console.log("Number " + password + element + " score = " + score);
        if(score > currentScore){
            password += element;
            if(position >= 7){
                console.log("TO JEST HASLO = " + password)
                return Promise.resolve(password);
            }
            currentScore = score;
            index = 0;
            inputElement(index, position + 1).then(resolve);
            return;
        }
        inputElement(index + 1, position).then(resolve);
    });
});
}

function solve(){
    inputElement()
        .then(result => {
            console.log("result" + result);
        })

}
solve();