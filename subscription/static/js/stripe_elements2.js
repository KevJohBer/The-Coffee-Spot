var stripePublicKey = $('#id_stripe_public_key').text().slice(1, -1);
var clientSecret = $('#id_client_secret').text().slice(1, -1);
var stripe = Stripe(stripePublicKey);
var elements = stripe.elements();
var card = elements.create('card');
card.mount('#card-element');


// Form submit handler

var form = document.getElementById('payment-form');

form.addEventListener('submit', function(ev) {
    ev.preventDefault();

    customer_email = document.getElementById('email').value

    stripe.createToken(card).then(function(result) {
        stripe.createPaymentMethod({
            type: 'card',
            card: card,
            billing_details: {
                email: customer_email
            },
        }).then(function(payment_method_result){
            var hiddenInput = document.createElement('input');
            hiddenInput.setAttribute('type', 'hidden')
            hiddenInput.setAttribute('name', 'payment_method_id')
            hiddenInput.setAttribute('value', payment_method_result.paymentMethod.id)
            form.appendChild(hiddenInput)
            form.submit()
        })
    })
    

    // card.update({'disabled': true});
    // $('#submit-button').attr('disabled', true)
    // stripe.confirmCardPayment(clientSecret, {
    //     payment_method: {
    //         card: card,
    //     }
    // }).then(function(result) {
    //     if (result.error) {
    //         var errorDiv = document.getElementById('card-errors');
    //         var html = `
    //             <span class="icon" role="alert">
    //                 <i class="fas fa-times"></i>
    //             </span>
    //             <span>${result.error.message}</span>`;
    //         $(errorDiv).html(html);
    //         card.update({'disabled': false});
    //     } else {
    //         if (result.paymentIntent.status === 'succeeded') {
    //             form.submit()
    //         }
    //     }
    // });
});