 let buttons = document.getElementsByClassName('button_delete_deck')

 for (button of buttons) {
     button.addEventListener('click', function(event) {
         event.target.closest('.container_deck').remove()
     });
 }