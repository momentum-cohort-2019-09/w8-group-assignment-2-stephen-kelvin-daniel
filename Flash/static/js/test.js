console.log('<test_deck> js loaded')

function flip() {
    card.classList.toggle('flipped');
};
document.getElementById('container').addEventListener('click', flip)