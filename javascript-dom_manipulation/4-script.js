// Script that adds a li element to a list when the user clicks on the element with id add_item
document.addEventListener('DOMContentLoaded', function() {
    const addItemDiv = document.getElementById('add_item');
    const myList = document.querySelector('.my_list');

    // Adds a click event listener
    addItemDiv.addEventListener('click', function() {
      const newListItem = document.createElement('li');
      newListItem.textContent = 'Item';
      myList.appendChild(newListItem); // Appends the new 'li' to the 'ul' element
    });
  });
