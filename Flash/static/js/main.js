//======================| Javascript for Deleting each Deck from Dashboard |===============================================\\
let buttons = document.getElementsByClassName('button_delete_deck')

function create_delete_buttons() {
    for (button of buttons) {
        // button.addEventListener('click', delete_deck(event,pk))
        button.addEventListener('click', function(event, pk) {
            let el = event.target
            let deckpk = el.dataset.deckPk
            fetch('/delete_deck/' + deckpk, {
                method: 'POST'
            }).then(res => {
                if (res.ok) {
                    event.target.closest('.container_deck').remove()
                }
            })
        });
    }
}

create_delete_buttons()