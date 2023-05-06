const image = document.getElementById('myImage');
const checkbox = document.getElementById('myCheckbox');

image.classList.remove('checked')
image.addEventListener('DOMContentLoaded', function() {
  checkbox.checked = !checkbox.checked;
  if (checkbox.checked) {
    image.classList.add('checked');
  } else {
    image.classList.remove('checked');
  }
});

checkbox.addEventListener('click', function() {
  if (checkbox.checked) {
    image.classList.add('checked');
  } else {
    image.classList.remove('checked');
  }
});

checkbox.checked = false;
