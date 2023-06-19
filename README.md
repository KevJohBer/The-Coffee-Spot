# The Coffee Spot

The Coffee Spot is an online web application that lets you order coffee from a The Coffee Spot coffee shop. It is in this application that you can sign up for a subscription so that you can order at much coffee as you like

## Contents

* [User Experience](#user-experience)
    * [User stories](#user-stories)
* [Design](#design)
    * [Color Scheme](#color-scheme)
    * [typography](#typography)
    * [imagery](#imagery)
* [Features](#features)
    * [Navbar](#navbar)
    * [Home page](#home-page)
    * [Subscription detail](#subscription-page)
    * [Order page](#order-page)
    * [Profile page](#profile-page)
    * [Create Product](#create-product-page)
* [Technologies Used](#technologies-used)
    * [Languages](#languages-used)
    * [Frameworks, libraies & programs used](#frameworks-libraries--programs-used)
* [Deployment & Local Development](#deployment--local-development)
    * [Initial Deployment](#initial-deployment)
    * [Deployment](#deployment)
    * [Environment Variables](#environment-variables)
* [Testing](#testing)
* [Credits](#credits)
    * [Code used](#code-used)
    * [Media](#media)

## User Experience

### User Stories

* As a user I can create an account and log in aswell as log out
* As a user I can view subscriptions to see which one fits me the most. I can then subscribe with a monthly fee. I can also change or cancel a subscription if it, despite choice, does not fit me.
* As a user I can search for what coffee I would like to order or view the list of products or in the menu part of the home page.
* As a user, once I have chosen what product I am ordering, I can create an order by filling out the details. I can also cancel the order while it is active. 
* As a user I can view previous orders that I have made when viewing my profile page.
* As a user I can view the current subscriptions that I have active by viewing my progile page.
* As a user I can view my invoices to see how much I am paying.

## Design

The Coffee spot has many features. alot of these features are located in the same place to make them easily accessible by the user. For example, alot of the information regarding special offers, subscriptions, menu items and general information about the page can be found right at the home page. This is all to avoid the hassle of having to go back and forth between pages in order for the user to complete a specific task. The site is minimal in its design so that it does not overstimulate the user with images and unecessary design features. The application is a tool that is meant to be used often or as frequently as the user will want the product.

### Color Scheme

The coffee spot favors brown color to remind users of coffee. The website does not focus a whole lot on images but uses different shades of brown to separate sections on the pages. The admin does have the ability to set images to the products on creation.

### Typography

### Imagery

### Order page

Order page has a unique design choice inspired by streaming websites (oddly enough) that allows users to scroll horizontally to view products. They also have the option to search. The idea is to not display the checkout part of the page until the user has chosen their products. It is supposed to function as an all in one solution so that you don't have your store and cart separate. 

## Features

### Navbar

The Coffee Spot website has a navbar that can be accessed on every template. It allows the users to

* Access the home page by clicking the logo
* Access the subscriptions part of the home page by clicking "subscriptions"
* Access the menu part of the home page by clicking "Menu"
* Access the about part of the home page by clicking "about"
* Access the login and logout templates by clicking login or logout

The navbar also contains another link named "create product" that allows admin to access the "create product" template.

### Home Page

The first page that you are greeted with when opening the Coffee Spot is the home page. The home page consists of four sections.
* special offer
* subscriptions
* menu
* about
These sections are supposed to help the user find what they are looking for. The navbar helps navigate through these sections aswell.

At the top of the page you will find a special offer. It has some information about the one year discount on a subscription and also features a button which takes you to that specific subscription. Right below it is the subscriptions section. Here, if the special offer was not good enough, you can look at the other subscriptions and see if they are more in alignment with the product you are looking for. After the subscriptions section, you can find the menu, which is a list of all the products that are included in the menu. From here you can decide what you would like to order. And at the bottom of the page is the about section. Here you can find a text about the website and its history.

### Subscription page

By selecting one of the subscriptions on the home page by clicking "see more" you can view more details about the subscription, price information and what drinks are included in it. At the bottom of the subscription page is a form. The idea is to fill this form out to get yourself subscribed. The invoices start on the same day that you sign up. 

### Order page 

The order page features a search bar that let's you search for specific drinks to make it easier for users to find what they are looking for. If they prefer to browse, they have the horizontal scroll bar that let's you browse through the drinks. Once you add a drink to your order, a form will appear and you can enter your credit card information and finish your order. Once you have filled out the form and created your forum, you will be redirected to a confirmation page where you can view the details of your order. 

For the admin, there is an edit and delete button on each product. The edit button will let you edit the information of all products. The delete button will let you delete the product from the database entirely. 

### Profile page

The Profile page can be viewed by clicking "profile" on the navbar. The profile page has your own profile image displayed along with your name and your own personalized description. Clicking your profile image will let you edit your profile. Here you can edit your default order information. Below your profile image, you have a set of links which can help you find various information. You have a link for order history, which displays your previous orders, aswell as your active orders. If the order is active, you can cancel the order with a press of a button. You can also view your subscriptions so that you always know what subscription you have active. You can even cancel the subscription in in the same view. You can view your subscription invoices with the invoices link. 

### Create Product Page

If you are logged in as an admin, you can view the create product page by clicking "Create Product" on the navbar. The create product page is just a form that lets you enter a name, price, category and image of whatever product you would like to add.


### Future implementations

* Editable subscriptions, admin should have the ability to change subscriptions to add discounts and let it include other drinks
* Advanced search logic. Users should be able to search for products and get results despite spelling mistakes
* Advanced form handling. Users should not be able to have accounts with fake or inappropriate information
* Customized confirmation. Confirmations are the standard browser confirmations, these ruin the experience for users.
* Customizable profiles. Users should be able to personalize their profiles
* Automatically fill order fields with default information
* 

## Technologies Used

### Languages Used

* HTML
* CSS
* Python
* Javascript

### Frameworks, libraries & Programs Used

* Django Web Framework
* Bootstrap 5
* Stripe

## Deployment & Local Development

### Initial Deployment

Heroku was used to deploy the live website

1. Login to Heroku
2. In the dashboard click your already created application
3. Click the deploy tab
4. Click the github icon and select the corresponding github repository
5. Enter your github credentials

### deployment

1. Scroll down to "Manual deploy
2. Select "main" as the branch you want to deploy to
3. click "Deploy Branch"

### Environment Variables

* AWS_ACCESS_KEY_ID
    * Obtained from amazon webservice s3 bucket
* AWS_SECRET_ACCESS_KEY
    * Obtained from amazon webservice s3 bucket
* EMAIL_HOST_PASS
    * This can be obtained from your gmail account
* EMAIL_HOST_USER
    * This can be obtained from your gmail account
* SECRET_KEY
    * This secret key was obtained with this [secret key generator](https://djecrety.ir/)
* STRIPE_PLAN_PREMIUM
* STRIPE_PLAN_REGULAR
* STRIPE_PLAN_SPECIAL
* STRIPE_PUBLIC_KEY
* STRIPE_SECRET_KEY
    * Stripe variables can be obtained from your store on Stripe
* DATABASE_URL
    * This variable can be found by creating a database with ElephantSQL

## Testing

All testing can be found [here](TESTING.md)

## Credits

### Code Used

The Product and Order models were inspired by the CI Boutique Ado tutorial

### Media




