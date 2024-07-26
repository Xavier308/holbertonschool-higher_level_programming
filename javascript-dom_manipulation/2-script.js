// Script that adds the class red to the header element when the user clicks on
// the tag with id red_header
document.addEventListener('DOMContentLoaded', function() {
    const redHeaderDiv = document.getElementById('red_header');
    const header = document.querySelector('header');
    
    // Adds a click event listener
    redHeaderDiv.addEventListener('click', function() {
      header.classList.add('red');
    });
  });
