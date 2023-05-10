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

  localStorage.setItem('selectedPizzaName', pizzaName);

  window.location.href = '/menus/create_pizza';
}

const selectButtons = document.getElementsByClassName('pizza-select-button');
for (let i = 0; i < selectButtons.length; i++) {
  selectButtons[i].addEventListener('click', selectPizza);
}

function getSelectedPizza(event) {
  const selectedPizzaName = localStorage.getItem('selectedPizzaName');
  const selectedPizzaElement = document.getElementById('selected-pizza');
  selectedPizzaElement.textContent = selectedPizzaName;
}



