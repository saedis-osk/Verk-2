function handleSearch(event) {
  event.preventDefault(); // prevent the form from submitting and reloading the page

  const searchInput = document.querySelector('.search-input');
  const searchQuery = searchInput.value.trim();

  // Do something with the search query (e.g. fetch search results from a server)
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
}


  console.log(`Search query: ${searchQuery}`);
}

// No need to add an event listener to the search button, as the form's onsubmit attribute takes care of it.
