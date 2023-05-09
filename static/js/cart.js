// Get references to the radio buttons and the popup window
const payOnArrivalRadio = document.getElementById('inlineRadio1');
const payWithCardRadio = document.getElementById('inlineRadio2');
const popupCardWindow = document.getElementById('popupCardWindow');
const popupCheckout = document.getElementById('popupCheckout');


// Add event listeners to the radio buttons
payOnArrivalRadio.addEventListener('click', hidePopupWindow);
payWithCardRadio.addEventListener('click', showPopupWindow);

popupCheckout.style.display='none';

// Define the event handlers
function hidePopupWindow() {
  popupCardWindow.style.display = 'none';
  popupCheckout.style.display = 'block';

}

function showPopupWindow() {
  popupCardWindow.style.display = 'block';
  popupCheckout.style.display='none';
}

