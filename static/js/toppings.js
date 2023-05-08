const checkboxes = document.querySelectorAll('.myCheckbox');
const images = document.querySelectorAll('.checked');

images.forEach(function(image) {
  image.classList.remove('checked');
});

checkboxes.forEach(function(checkbox) {
  checkbox.addEventListener('click', function() {
    const image = this.previousElementSibling;

    if (this.checked) {
      image.classList.add('checked');
    } else {
      image.classList.remove('checked');
    }
  });
});

