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

// Add an event listener to the search form
document.addEventListener('DOMContentLoaded', () => {
  const searchForm = document.querySelector('#search-form');

  if (searchForm) {
    searchForm.addEventListener('submit', handleSearch);
  } else {
    console.error('Search form not found');
  }
});
