document.addEventListener('DOMContentLoaded', function() {
  // Get a reference to the checkout form
  var checkoutForm = document.getElementById('checkout-form');

  // Add an event listener to the form submission
  checkoutForm.addEventListener('submit', function(event) {
    event.preventDefault(); // Prevent form submission

    // Retrieve form data
    var name = document.getElementById('name').value;
    var email = document.getElementById('email').value;
    var cardNumber = document.getElementById('card-number').value;
    var expiration = document.getElementById('expiration').value;
    var cvc = document.getElementById('cvc').value;

    // Validate form inputs
    if (!name || !email || !cardNumber || !expiration || !cvc) {
      // Display an error message or handle validation errors
      alert('Please fill in all required fields.');
      return;
    }

    // Create an object with the form data
    var formData = {
      name: name,
      email: email,
      cardNumber: cardNumber,
      expiration: expiration,
      cvc: cvc
    };

    // Send the form data to the server for processing
    // You can use AJAX, Fetch API, or any other method to send the data

    // Example using Fetch API
    fetch('/checkout', {
      method: 'POST',
      body: JSON.stringify(formData),
      headers: {
        'Content-Type': 'application/json'
      }
    })
      .then(function(response) {
        if (response.ok) {
          // Successful response, redirect to confirmation page or display success message
          window.location.href = '/confirmation';
        } else {
          // Error response, handle the error or display an error message
          alert('Error processing payment. Please try again.');
        }
      })
      .catch(function(error) {
        // Error occurred during the request, handle the error or display an error message
        console.error('Error processing payment:', error);
        alert('An error occurred. Please try again later.');
      });
  });
});
