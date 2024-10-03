function r() {
    var randomNumber = Math.floor(Math.random() * (360-1)) + 1;
    return randomNumber;
}

window.onload = function () {

    event_cards = document.getElementsByClassName("event-card");

    for (var i = 0; i < event_cards.length; i++) {
        event_cards[i].style.background = `linear-gradient(${r()}deg, rgb(133, 106, 145) 0%, rgb(30, 80, 66) 100%)`;
    }

};