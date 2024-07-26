// Script that updates the text color of the header element to red (#FF0000) 
// when the user clicks on the tag with id red_header
document.addEventListener('DOMContentLoaded', function() {
    const redHeaderDiv = document.getElementById('red_header');
    const header = document.querySelector('header');

    // Adds a click event listener
    redHeaderDiv.addEventListener('click', function() {
      header.style.color = '#FF0000';
    });
  });
