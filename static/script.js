// static/script.js

function toggleCardText(button) {
    var cardContent = button.parentElement.querySelector('.card-text');
    var showMoreText = button.textContent === 'Show More';

    if (showMoreText) {
        cardContent.style.maxHeight = 'none'; /* Show all text */
        button.textContent = 'Show Less';
    } else {
        cardContent.style.maxHeight = '150px'; /* Show limited text */
        button.textContent = 'Show More';
    }
}
