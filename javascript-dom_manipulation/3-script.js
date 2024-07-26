// Script that toggles the class of the header element 
// when the user clicks on the tag id toggle_header
document.addEventListener('DOMContentLoaded', function() {
    const toggleHeaderDiv = document.getElementById('toggle_header');
    const header = document.querySelector('header');

    // Adds a click event listener
    toggleHeaderDiv.addEventListener('click', function() {
      // Checks if the header currently has the class 'red'
      if (header.classList.contains('red')) {
        header.classList.remove('red');
        header.classList.add('green');
      } else {
        header.classList.remove('green');
        header.classList.add('red');
      }
    });
  });
