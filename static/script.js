// script.js

$(document).ready(function () {
    $('#productForm').submit(function () {
        // Show loading spinner
        $('#loading-spinner').css('display', 'block');
        // Disable the submit button to prevent multiple submissions
        $('#submit-button').prop('disabled', true);
    });
});

function showCardDetail(scriptIdea) {
    // Code for showing card details, if needed
}

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

function closeModal() {
    // Code for closing the modal, if needed
}
