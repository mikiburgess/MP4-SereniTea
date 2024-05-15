// Stripe checkout code for SereniTea
// Adapted from Boutique Ado
// ----------------------------------

// element styles 
var style = {
    base: {
        color: '#000',
        fontFamily: '"Montserrat", sans-serif',
        fontSmoothing: 'antialiased',
        fontSize: '16px',
        '::placeholder': {
            color: 'rgb(208,204,192)'
        }
    },
    invalid: {
        color: 'rgb(220, 53, 69)',
        iconColor: 'rgb(220, 53, 69)'
    }
}

// Get keys from template using JQuery, stripping the first and last characters to remove quotation marks
var stripePublicKey = $('#id_stripe_public_key').text().slice(1, -1);
var clientSecret = $('#id_client_secret').text().slice(1, -1);

// Create instance of Stripe
var stripe = Stripe(stripePublicKey);
// Use to create an instance of stripe elements
var elements = stripe.elements();
// use that to create a card element
var card = elements.create('card', {style: style});
// then mount the card element to the div in the checkout page
card.mount('#card-element');


// Handle realtime validation errors on card element, displaying information to user
card.addEventListener('change', function(event) {
    var errorDiv = document.getElementById('card-errors');
    if (event.error) {
        var html = `
            <span class="icon" role="alert">
                <i class="bi bi-x-lg"></i>
            </span>
            <span>${event.error.message}</span>
        `;
        $(errorDiv).html(html);
    } else {
        errorDiv.textContent = '';
    }
});

// Handle form submit
var form = document.getElementById('payment-form');

form.addEventListener('submit', function(ev) {
    // stop default action on 'submit'
    ev.preventDefault();
    // disable card element and submit button to stop multiple submissions
    card.update({ 'disabled': true });
    $('submit-button').attr('disabled', true);
    // fade out form
    $('#payment-form').fadeToggle(100);
    // fade in loading spinner
    $('#loading-overlay').fadeToggle(100);
    // call the confirm card payment method, 

    var saveInfo = Boolean($('#id-save-info').attr('checked'));
    var csrfToken = $('input[name="csrfmiddlewaretoken"]').val();
    var postData = {
        'csrfmiddlewaretoken': csrfToken,
        'client_secret': clientSecret,
        'save_info': saveInfo,
    };
    
    var url = '/checkout/cache_checkout_data/';

    $.post(url, postData).done(function() {
        stripe.confirmCardPayment(clientSecret, {
            payment_method: {
                card: card,
                billing_details: {
                    title: $.trim(form.title.value),
                    first_name: $.trim(form.first_name.value),
                    surname: $.trim(form.surname.value),
                    email: $.trim(form.email.value),
                    phone: $.trim(form.phone_number.value),
                    address:{
                        line1: $.trim(form.street_address1.value),
                        line2: $.trim(form.street_address2.value),
                        city: $.trim(form.town_or_city.value),
                        country: $.trim(form.country.value),
                        state: $.trim(form.county.value),
                    }
                }
            },
            shipping: {
                title: $.trim(form.title.value),
                first_name: $.trim(form.first_name.value),
                surname: $.trim(form.surname.value),
                phone: $.trim(form.phone_number.value),
                address: {
                    line1: $.trim(form.street_address1.value),
                    line2: $.trim(form.street_address2.value),
                    city: $.trim(form.town_or_city.value),
                    country: $.trim(form.country.value),
                    state: $.trim(form.county.value),
                }
            },
        }).then(function(result) {
            if (result.error) {
                // Handle errors when submitting payment
                var errorDiv = document.getElementById('card-errors');
                var html = `
                    <span class="icon" role="alert">
                    <i class="bi bi-x-lg"></i>
                    </span>
                    <span>${result.error.message}</span>`;
                $(errorDiv).html(html);
                $('#payment-form').fadeToggle(100);
                $('#loading-overlay').fadeToggle(100);
                card.update({ 'disabled': false});
                $('#submit-button').attr('disabled', false);
            } else {
                // Confirm payment when succesfull
                if (result.paymentIntent.status === 'succeeded') {
                    form.submit();
                }
            }
        });
    }).fail(function () {
        // just reload the page, the error will be in django messages
        location.reload();
    })
});