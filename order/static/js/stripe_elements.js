var stripePublicKey = $('#id_stripe_public_key').text().slice(1, -1);
var clientSecret = $('#id_client_secret').text().slice(1, -1);
var stripe = Stripe(stripePublicKey);
var elements = stripe.elements();
var style = {
    base: {
        color: 'white',
        fontFamily: '"Helvetica Neue", Helvetica, sans-serif',
        fontSmoothing: 'antialiased',
        fontSize: '16px',
        '::placeholder': {
            color: '#aab7c4'
        }
    },
    invalid: {
        color: '#dc3545',
        iconColor: '#dc3545'
    }
};
var card = elements.create('card' , {'style': style});
card.mount('#card-element');


// Form submit handler
var form = document.getElementById('payment-form');
var total = document.getElementById('total').value;

if (total > 0) {
    form.addEventListener('submit', function(ev) {
        ev.preventDefault();
        card.update({'disabled': true});
        $('#submit-button').attr('disabled', true);
        stripe.confirmCardPayment(clientSecret, {
            payment_method: {
                card: card,
            }
        }).then(function(result) {
            if (result.error) {
                var errorDiv = document.getElementById('card-errors');
                var html = `
                    <span class="icon" role="alert">
                        <i class="fas fa-times"></i>
                    </span>
                    <span>${result.error.message}</span>`;
                $(errorDiv).html(html);
                card.update({'disabled': false});
            } else {
                if (result.paymentIntent.status === 'succeeded') {
                    form.submit();
                }
            }
        });
    });
}