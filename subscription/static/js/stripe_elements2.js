var stripePublicKey = $('#id_stripe_public_key').text().slice(1, -1);
var clientSecret = $('#id_client_secret').text().slice(1, -1);
var stripe = Stripe(stripePublicKey);
var elements = stripe.elements();
var style = {
    base: {
        color: 'white',
        fontSize: '16px',
        '::placeholder': {
            color: 'white',
            iconColor: 'white',
        }
    },
    invalid: {
        color: '#dc3545',
        iconColor: '#dc3545'
    }
};
var card = elements.create('card', {'style': style});
card.mount('#card-element');


// Form submit handler

var form = document.getElementById('payment-form');

form.addEventListener('submit', function(ev) {
    ev.preventDefault();

    customer_email = document.getElementById('email').value;

    stripe.createToken(card).then(function(result) {
        var token = result.token.id;
        var hiddenInputTwo = document.createElement('input');
            hiddenInputTwo.setAttribute('type', 'hidden');
            hiddenInputTwo.setAttribute('name', 'token');
            hiddenInputTwo.setAttribute('value', token);
        stripe.createPaymentMethod({
            type: 'card',
            card: card,
            billing_details: {
                email: customer_email
            },
        }).then(function(payment_method_result){
            var hiddenInput = document.createElement('input');
            hiddenInput.setAttribute('type', 'hidden');
            hiddenInput.setAttribute('name', 'payment_method_id');
            hiddenInput.setAttribute('value', payment_method_result.paymentMethod.id);

            form.appendChild(hiddenInput);
            form.appendChild(hiddenInputTwo);
            form.submit();
        });
    });
});
