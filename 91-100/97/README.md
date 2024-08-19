# Overview

This is the day 97 assignment.

## _From the course:_
200 minutes to complete
1,335 student solutions
An eCommerce website with payment processing.

Using what you have learnt by building the blog website using Flask, you're now going to build your own eCommerce website. Your website needs to have a working cart and checkout.

It should be able to display items for sale and take real payment from users.

It should have login/registration authentication features.

Here is an example website:
https://store.waitbutwhy.com/


You should consider using the Stripe API:
https://stripe.com/docs/payments/checkout


## My comments:
I finished early.  The main outstanding item is the connection to Stripe for my cart.

I can send users to static (easy) links with defined items, but I know the better option is to build the shopping cart and then we'll calculate total cost and taxes.

See this page for more details:
https://docs.stripe.com/payments/checkout/how-checkout-works

I have a stripe account, and I can see the benefit of using their service to collect payments on my behalf.

This could be very interesting!


# Running

```bash
flask --app main run
```

# External Links


# requirements.txt


# TODOs

- Finalize the connection from my one-premise (laptop) server to the web application to complete a [Checkout session.](https://docs.stripe.com/payments/checkout/how-checkout-works?ui=embedded-form#session)
- Allow people to delete items from their cart.
- Allow people to do a + or - to the quantity of their cart.