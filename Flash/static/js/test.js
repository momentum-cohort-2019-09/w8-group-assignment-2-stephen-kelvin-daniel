//========================================================================| card flip in <test-deck.html> |============\\
console.log('<test_deck> js loaded')

function flip() {
    card.classList.toggle('flipped');
};
document.getElementById('container').addEventListener('click', flip)

//========================================================================| guesses in <test-deck.html> |============\\
console.log('starting feedback...')

function correct(event) {
    console.log('correct button clicked!')

};
document.getElementById('button_right').addEventListener('click', correct)

function incorrect() {
    console.log('incorrect button clicked!')

};
document.getElementById('button_wrong').addEventListener('click', incorrect)