console.log('<dashboard> js loaded')

for (button of buttons) {
    let buttons = document.getElementsByClassName('button_delete_deck');
    button.addEventListener('click', function(event) {
        event.target.closest('.container_deck').remove();
    });
};