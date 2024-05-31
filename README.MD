<p align="center">
  <img src="docs/images/serenitea_emporium_small.jpg" alt="SereniTea Emporium Company Logo">
</p>

<h1 align="center">SereniTea Emporium</h1>

 
<p align="center"> This repository and the accompanying Full Stack Web Application is presented for Code Institute Milestone Project 4.</p>

- - -

- - -

## Table of Contents

- [Introduction](#Introduction)
- [User Experience (UX)](#User-Experience-(UX))
  - [Project Goals](#Project-Goals)
  - [Strategy](#Strategy)
  - [Scope](#Scope)
  - [Structure](#Structure)
  - [Skeleton](#Skeleton)
  - [Surface](#Surface)
- [Site Functionality](#Site-Functionality)
- [Site Development](#Site-Development)
  - [Underlying Site Data](#Underlying-Site-Data)
  - [Site Content](#Site-Content)
  - [User Management](#User-Management)
  - [Site Navigation](#Site-Navigation)
  - [Tools & Technologies](#Tools-&-Technologies)
- [Walkthrough](#Walkthrough)
- [Testing](#Testing)
- [Guide to Deployment and Development](#Guide-to-Deployment-and-Development)
- [Project Review and Reflection](#Project-Review-and-Reflection)
- [Project Credits and Acknowledgements](#Project-Credits-and-Acknowledgements)

- - -

## Introduction
This repository and the associated deployed website comprise my submission for the Diploma in Web Development, Milestone Project 4. 
The purpose of this project is to demonstrate ability to design and develop a Full Stack Web Application in the form of an e-commerce site, implemented using the Django framework with appropriate associated technologies and APIs (including Python, HTML, CSS and JavaScript).


<kbd>[Return to ToC](#Table-of-Contents)</kbd>
- - -

<p align="center">
  <img src="docs/images/serenitea_emporium_small.jpg" alt="SereniTea Emporium Company Logo">
</p>

## User Experience (UX)
The focus of this project and the developed full stack web application is the SereniTea Emporium, a fictional store specializing in the sale of loose leaf teas and related paraphernalia. 
The underlying mission of the company is to promote positive mental health through peace, relaxation and serenity. This is reflected in the company name and the products selected for sale through the store.

The intended users of this web application are as follows:
- Site administrator, maintaining the application on behalf of the store owner.
- Store customers, visiting the site to browse for, order and pay for desired products.
- Casual site visitors, exploring the site to learn more and potentially become a store customer.


### Project Goals
The primary goal of this project is to design, develop and deploy an e-commerce site for SereniTea Emporium. This project will adopt a full stack approach to develoment, from the front end interactive web site to the back end data storage ('data at rest'), transfer ('data in motion') and manipulation ('data in use').


### Strategy
<!-- What are we aiming to achieve, and for whom? -->
This e-commerce application is developed as the online presence of a (fictional) store that specializes in selling loose leaf teas and tea-related/themed products directly to non-commercial customers. The UX needs to consider the ethos of the company, promoting wellbeing and relaxation, and maintaining an ethical business model (supporting local producers and artists and using biodegradable packaging). The intended users of the site will be the store owner and administrators (managing the store), store customers (purchasing products) and casual website visitors (learning more about the company before becoming a customer).

### Scope
<!-- What features do we want to include in the design? What's on the table, and whats off (for now)? -->
The scope of this project is the design, build and deployment of a full stack online e-commerce application. It will include the ability for customers to browse a product catalogue, add products to a basket and securely pay for a basket of items once shopping is complete. Site visitors will be able to create a user profile to save their details to enable faster checkout (for customers) and controlled feature access (for customers and site administrators). It will also, however, enable anonymous checkout for customers who do not want to create an account.
At the back-end it will include full CRUD functionality for one or more aspects of the site, specifically allowing site administrators to add, edit and delete store products.






### Structure
<!-- How is the information structured, and is it logically grouped? -->


### Skeleton
<!-- How the information should be implemented, and how the user will navigate through the info/features -->

### Surface


<kbd>[Return to ToC](#Table-of-Contents)</kbd>
- - -

## Site Development

### Data Management
...RDBMS and DB & Models
...

### Site Content
<!-- Generation of data for the site -->

The data for SereniTea Emporium was primarily produced using AI tools:
- Product Descriptions - [ChatGPT (v3.5)](https://chatgpt.com/)
- Product Images - [ImageFX](https://aitestkitchen.withgoogle.com/tools/image-fx)
- SereniTea Store Descriptions/Text - [ChatGPT (v3.5)](https://chatgpt.com/)

These tools were used to enable a good selection of products to be included in the store, without adversely affecting the time available for the milestone project.


#### Populating the Product Catalogue

The following describes the process for generating product catalogue data:
1. Create set of product category definitions and export to csv file [categories.csv](docs/product-catalogue/categories.csv)
2. Write initial product title and brief description
3. Use description as input into [ChatGPT](https://chatgpt.com/) to generate full product description
4. Review and edit text as required
5. Use initial description [ImageFX](https://aitestkitchen.withgoogle.com/tools/image-fx) to generate potential images
6. Repeat image generation process until appropriate image created (complementary to other image styles in the current image set)
7. Add all product details and image urls to a spreadsheet
8. Spreadsheet autogenerates sku, (non-friendly) name and image filenames
9. Export data to csv file [products.csv](docs/product-catalogue/products.csv)

10. Convert csv files to Django fixtures json format using python scripts 
- [makeJsonCategories.py](docs/product-catalogue/makeJsonCategories.py) --> [categories.json](docs/product-catalogue/categories.json)
- [makeJsonProducts.py](docs/product-catalogue/makeJsonProducts.py) --> [products.json](docs/product-catalogue/products.json)

11. Add fixture files to the product app fixture folder
12. Finally, add the json fixture files into the project using the following CLI commands:
```
python3 manage.py loaddata categories
python3 manage.py loaddata products

```

#### Producing Site Text

Some site text was also generated using AI.

1. Write initial brief description of text requirement (for example 'description of an online store selling loose leaf teas and accessories, focussed on relaxation and wellbeing)
2. Use description as input into [ChatGPT](https://chatgpt.com/) to generate candidate site text
3. Review and edit text, using it as a basis for creating the final site text.


### User Management
Incorporating Django Allauth
...

### Site Navigation
...

### Tools & Technologies
Below is a summary of the tools and languages used during this project, from design through to development and testing.


#### Coding
- [Django v4.2](https://www.djangoproject.com/ "Django"): The Web Framework underpinning this Full Stack Web Application.
- [Python](https://www.python.org/ "Python.org"): Used to provide the majority of the backend functionality.   
- [JavaScript](https://www.w3schools.com/js/js_intro.asp "JavaScript Introduction, W3Schools") & [jQuery](https://jquery.com/ "jQuery"): These were used to add additional functionality to the site, including adding interactivity to some of the site pages. 
- [Django-allauth v0.60](https://docs.allauth.org/en/latest/index.html "allauth"): For the provision of user access functionality, including site registration, signin and logout.
- [Stripe](https://stripe.com/gb "Stripe"): The Stripe payment mechanism was employed in the backend to process payments, used in 'Test Mode' to ensure no payments can actually be taken from any visitors.

#### Markup Languages
- [HTML](https://www.w3schools.com/html/html_intro.asp "HTML Introduction, W3Schools"): The standard web page markup language for constructing static web pages.
- [Jinja2](https://jinja.palletsprojects.com/en/3.1.x/ "Jinja Templating Engine"): This templating language was used to enable dynamic data modifications across the site pages.
- [Markdown](https://en.wikipedia.org/wiki/Markdown "Markdown overview, Wikipedia"): Use to produce project documentation, including this README.

#### Styling
- [Bootstrap 5.3.3](https://getbootstrap.com/ "Bootstrap"): The Bootstrap toolkit was used for site layout and styling.
- [Bootstrap Icons](https://icons.getbootstrap.com/ "Bootstrap Icons"): The course for all icons used across the site.
- [CSS](https://www.w3schools.com/css/css_intro.asp "CSS Introduction, W3Schools"): Additional styling was added to the site using CSS.
- [Google Fonts](https://fonts.google.com/ "Google Fonts"): The source for the fonts used across the site - [Yeseva One](https://fonts.google.com/specimen/Yeseva+One "Yeseva One @ Google Fonts") and [Montserrat](https://fonts.google.com/specimen/Montserrat "Montserrat @ Google Fonts")
- The pairing of Yeseva One and Montserrat fonts was inspired by a suggestion from [####](####).
- Site color palette was developed using [####](####).

#### Tools
This section lists the tools used during this project in support of the development and deployment stages.
- [Balsamiq Wireframes](####): Used to create the initial site wireframes during the design stage, to guide the development stage.
- [Draw.io](####): This free online drawing tool was used to create the entity relationship diagram (ERD), describing the underlying data storage (postgres database) model.
- [Elephant ###](####): The relational database management system (RDBMS) used to store site data, as defined by the ERD.
- [Visual Studio Code](https://code.visualstudio.com/ "VSCode"): All code was developed using a local installation of VS Code. (Code Institute development tools were not used during this project)
- Git & [GitHub](####): Git used for version control, with GitHub being employed as the online repository for all project work.
- [Google Chrome Developer Tools](https://developer.chrome.com/docs/devtools "DevTools"): Used throughout development to support page design, testing and accessibility. 
- [ImageFX](https://aitestkitchen.withgoogle.com/tools/image-fx "ImageFX"): Generative AI tool, used to create al product and site images.
- [ChatGPT v3.5](https://chatgpt.com/ "ChatGPT-3.5"): Generative AI tool, used to create initial draft of all product descriptions and site text.
- [Tinyfy](https://tinypng.com/ "Tnyfy - compress your images"): Used to optimize site images to reduce download time.
- [10MinEmail](https://temp-mail.org/en/10minutemail "TempMail"): Used to obtain free, time-limited temporary email addresses for testing user actions.
- [Heroku](https://www.heroku.com/ "Heroku"): The Heroku platform has been used in this project to host the final, [deployed web site](https://mp4-serenitea-emporium-5454dc22e46f.herokuapp.com/ "Serenitea Emporium").


<kbd>[Return to ToC](#Table-of-Contents)</kbd>

- - -


## Walkthrough
...


<kbd>[Return to ToC](#Table-of-Contents)</kbd>
- - -

## Testing

<kbd>[Return to ToC](#Table-of-Contents)</kbd>
- - -

## Project Review and Reflection
There are a number of areas where this project could be improved, and where the site can (and will) be developed further.

### Improvements to Design and Development

#### Project Structure
Organize project MEDIA folders to separate product images from general site images (such as backgrounds), rather than the current approach of storing all images in the same folder.

#### Defensive Programming
Currently the side administrator (superuser) is able to edit product details and delete products with a single click. Site functionality could be improved by adopting a more defensive approach to coding by including checks, asking users to actively confirm deletions and edits.
The same approach would be adopted for registered site visitors editing their profile details.

### Future Features
As can be seen in the Testing section, there are a number of areas where the current implementation of the site could be developed further and therefore improved. The features listed below are in addition to those previously listed future developments, and have been identified as those that would add greatest benefit to the site if implemented within the next development stage.

#### Product and Company Reviews
To improve communication with visitors and customers, as well as customer engagement, the first significant development would be the inclusion of customer-written, dynamic product (and company) reviews. This would include the following:
- Enable registered users to write and submit product reviews, editable until published to the site and visible to site visitors via the associated product details page. Optional customer images of store products could be added.
- Additional facility for site administrators to review and approve customer-written product reviews (with the option to publish immediately without any review), and remove any inappropriate reviews from the site.
- Calculate product rating scores dynamically based on customer-entered star ratings, rather than using static star ratings stored in the backend database.

#### User Profile Improvements
The current approach to customer access and profile management could also be developed further:
- Extending the account login system to allow for login using social media identity authentication (oauth).
- Enable registered users to add a profile image to their user profiles.

#### Additional Site Pages

- Add an autogenerated site map to provide an overview for site visitors.
- A contact page containing a validated form, enabling visitors to send a message directly to the company from the web site.

#### Improved Navigation, using Breadcrumbs
Navigating the site could be made easier for visitors with the inclusion of [Breadcrumbs](https://getbootstrap.com/docs/5.3/components/breadcrumb/ "Bootstrap Breadcrumbs"). These would provide site visitors with a clearer pointer to their location in the site and, in particular, the product catalogue.

#### Improved Site Messages
Site messages are currently displayed in a message bar at the top of the page, under the offers carousel. This has been included to ensure visitors receive messages regardless of whether they have blocked site popups. In a future development this would be updated to be included only where popups are blocked, with toasts or other popups being used when the browser permits them. This decision has been made to support user browsing security.

Site messages will also be color-coded according to the type of notification being raised (success, error, etc).

#### Position of page footer and top navigation bar
Ideally, 
1. the footer should be at the bottom of every page, then stick the the bottom of the viewport window when the page doesn't fill the complete window, and
2. the top navigation bar should stick to the top of the viewport window, remaining there as the site visitor scrolls down the page.

At present, these two elements are positioned at the top and bottom of the page, being positioned according to the page size and page scrolling. Fixed and Sticky positioning will be employed in future to improve site usability (minimizing scrolling).


### Bugs
The following bugs are still present in this application:

#### Adding a product
When adding a product with a product image, the image is initially available and displayed in the product page. However, this is not persistent. After a while the image is lost. 

I suspect this may be due to Heroku saving it in cache, then clearing it after some time.
I also suspect this could be rectified by including an improved file storage option, such as AWS, or deploying the site to another platform with supports dynamic file storage.

<kbd>[Return to ToC](#Table-of-Contents)</kbd>
- - -

## Project Credits and Acknowledgements

### Site Media
The following sites were used to obtain/generate visual site content:
- Google [fonts](https://fonts.google.com/) have been used across the site.
- All site icons are from Bootstrap [icons](https://icons.getbootstrap.com/).
- Product images were AI generated using [ImageFX](https://aitestkitchen.withgoogle.com/tools/image-fx)
- Product descriptions and site text creation was drafted using[ChatGPT (v3.5)](https://chatgpt.com/)
- Additional images obtained from [Pixabay](https://pixabay.com/) are free to use under their [Content License](https://pixabay.com/service/license-summary/).

### Additional Code and Resources
- Inspiration for site button styling was taken from [Slider revolution](https://www.sliderrevolution.com/resources/css-button-hover-effects/). 
- Information badges at top of README created using [Shields.io](https://shields.io/).

### Learning Resources
The following resources were used to develop coding skills, in addition to the Code Institute learning materials:
  - [Django 4.2](https://docs.djangoproject.com/en/4.2/) online documentation, for guidance on setting up and using the Django framework, along with the [Django Github Repo](https://github.com/django/)
  - [Django allauth](https://docs.allauth.org/en/latest/) online documentation, for tailoring and using the authentication modules
  - [Django crispy forms](https://django-crispy-forms.readthedocs.io/en/latest/) documentation, to learn how to use the latest version (5.0) in Django forms
  - [Django Clearable File Input Widget](https://github.com/django/django/blob/main/django/forms/templates/django/forms/widgets/clearable_file_input.html) documentation, for implementing the file input element in the Add/Edit Product page.
  - [Stripe](https://docs.stripe.com/) online documentation, in particular the [Getting Started](https://docs.stripe.com/get-started), [Payment APIs](https://docs.stripe.com/payments/payment-intents) and [Webhooks](https://docs.stripe.com/payments/handling-payment-events) sections, in developing the checkout app,
  - [Jinja](https://jinja.palletsprojects.com/en/3.1.x/) templating engine documentation, for building dynamic web page content
  - [Bootstrap 5.3](https://getbootstrap.com/docs/5.3/) online documentation, for styling the project website
  - [Heroku](https://github.com/heroku) github repo, for guidance and examples regarding deploying django and python.

General accessibility guidance was obtained from :
  - [W3C ARIA guidelines](https://www.w3.org/WAI/ARIA/apg/) for general guidance
  - [MDN](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA) for ARIA roles and descriptions

Development of the project markdown files were supported through reference to the following resources:
  - GitHub's [Writing on GitHub](https://docs.github.com/en/get-started/writing-on-github) documentation
  - Kera Cudmore's [Readme Examples](https://github.com/kera-cudmore/readme-examples/blob/main/milestone1-readme.md) for Code Institute Diploma Students
  - Adam Pritchard's [Markdown Cheatsheet](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet)

Approach taken to testing was supported by the following:
- Guidance on using the three Lighthouse modes (user flows) was obtained from Google Chrome's [Lighthouse documentation](https://github.com/GoogleChrome/lighthouse/blob/HEAD/docs/user-flows.md)


### Inspiration
- The primary inspiration behind this project was Code Institute's Boutique Ado project. This greatly supported my learning and heavily influenced the design and development of the SereniTea Emporium project.
- The idea of an online tea store was inspired by [Jing Tea](https://jingtea.com/) and [Whittard UK](https://www.whittard.co.uk/)


### Acknowledgements
I would like to acknowledge the following people who helped me complete this milestone project:
- The Code Institute Slack community, in particular my fellow students in the feb-2023-pla cohort. 
- [Amy Richardson](https://code-institute-room.slack.com/team/U06CZC2JZTN) - our Code Institute cohort facilitator, for her support and encouragement throughout this project.
- [Jubril Akolade](https://github.com/Jubrillionaire) - my Code Institute mentor,m for their support, guidance and advice.
- Dr N. Caine - for his support and advice, particularly with regard to converting site data into JSON format and testing approaches to project deployment.


<kbd>[Return to ToC](#Table-of-Contents)</kbd>

- - -