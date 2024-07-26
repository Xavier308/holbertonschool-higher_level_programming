// Script that updates the text of the header element to New Header,
// when the user clicks on the element with id update_header
document.addEventListener('DOMContentLoaded', function() {
    const updateHeaderDiv = document.getElementById('update_header');
    const header = document.querySelector('header');

    // Adds a click event listener
    updateHeaderDiv.addEventListener('click', function() {
      header.textContent = 'New Header!!!'; // Updates the text of the header
    });
  });
