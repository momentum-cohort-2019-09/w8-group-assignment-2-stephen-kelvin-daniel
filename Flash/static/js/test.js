//========================================================================| card flip in <test-deck.html> |============\\
console.log('<test_deck> js loaded')

function flip() {
    card.classList.toggle('flipped');
};
document.getElementById('container').addEventListener('click', flip)

//========================================================================| guesses in <test-deck.html> |============\\
console.log('starting feedback...')

let correct_btn = document.getElementById('button_right')
correct_btn.addEventListener('click', correct)

function correct(event) {
    console.log('correct button clicked!')
    let ev = event.target
    let cardpk = ev.dataset.cardPk
    console.log(cardpk)
    fetch(cardpk + '/correct_guess', {
        method: 'POST'
    }).then(res => {
        if (res.ok) {} else {

        }
    })

};

let incorrect_btn = document.getElementById('button_wrong')
incorrect_btn.addEventListener('click', incorrect)

function incorrect(event) {
    console.log('incorrect button clicked!')
    let ev = event.target
    let cardpk = ev.dataset.cardPk
    console.log(cardpk)
    fetch(cardpk + '/total_guesses', {
        method: 'POST'
    }).then(res => {
        if (res.ok) {}
    })

};