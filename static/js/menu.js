function filterProducts(searchQuery) {
  const productCards = document.querySelectorAll('.col.mb-5');

  productCards.forEach((productCard) => {
    const productName = productCard.querySelector('.fw-bolder').textContent.toLowerCase();

    if (productName.includes(searchQuery.toLowerCase())) {
      productCard.style.display = 'block';
    } else {
      productCard.style.display = 'none';
    }
  });
}

function handleSearch(event) {
  event.preventDefault();

  const searchInput = document.querySelector('.search-input');
  const searchQuery = searchInput.value.trim();

  filterProducts(searchQuery);

  console.log(`Search query: ${searchQuery}`);
}

document.addEventListener('DOMContentLoaded', () => {
  const searchForm = document.querySelector('#search-form');

  if (searchForm) {
    searchForm.addEventListener('submit', handleSearch);
  } else {
    console.error('Search form not found');
  }
});

function selectPizza(event) {
  const pizzaName = event.currentTarget.getAttribute('data-pizza-name');
  const pizzaDescription = event.currentTarget.getAttribute('data-pizza-description');
  const pizzaId = event.currentTarget.getAttribute('data-pizza-id');
  localStorage.setItem('selectedPizzaName', pizzaName);
  localStorage.setItem('selectedPizzaId', pizzaId);
  window.location.href = '/menus/create_pizza/' + pizzaId;
}

const selectButtons = document.getElementsByClassName('pizza-select-button');
for (let i = 0; i < selectButtons.length; i++) {
  selectButtons[i].addEventListener('click', selectPizza);
}

function getSelectedPizza(event) {
  const selectedPizzaName = localStorage.getItem('selectedPizzaName');
  const selectedPizzaId = localStorage.getItem('selectedPizzaId');
  const selectedPizzaElement = document.getElementById('selected-pizza');
  selectedPizzaElement.textContent = selectedPizzaId;
  selectedPizzaElement.textContent = selectedPizzaName;
  const form = document.getElementsByClassName("form");
  console.log(form);
  console.log(selectedPizzaId);
  const x = form[0].action = selectedPizzaId;
}


function filterByCategory(category) {
    const productCards = document.querySelectorAll('.col.mb-5');

    productCards.forEach((productCard) => {
        const productCategories = productCard.getAttribute('data-category').split(' ');

        if (category === '' || productCategories.includes(String(category))) {
            productCard.style.display = 'block';
        } else {
            productCard.style.display = 'none';
        }
    });
}

document.addEventListener('DOMContentLoaded', () => {
    const categorySelect = document.querySelector('#category-select');

    if (categorySelect) {
        categorySelect.addEventListener('change', (event) => {
            filterByCategory(event.target.value);
        });
    } else {
        console.error('Category select not found');
    }
});


function sortProducts(order) {
    const productContainer = document.querySelector('.row-cols-2');
    const productCards = Array.from(document.querySelectorAll('.col.mb-5'));

    // Sort based on the selected order
    if (order === 'price') {
        productCards.sort((a, b) => parseFloat(a.getAttribute('data-price')) - parseFloat(b.getAttribute('data-price')));
    } else if (order === 'alpha') {
        productCards.sort((a, b) => a.getAttribute('data-name').localeCompare(b.getAttribute('data-name')));
    }

    // Clear the container
    productContainer.innerHTML = '';

    // Append the sorted cards
    productCards.forEach((productCard) => {
        productContainer.appendChild(productCard);
    });
}
document.querySelector('#sort-order').addEventListener('change', function() {
    sortProducts(this.value);
});
