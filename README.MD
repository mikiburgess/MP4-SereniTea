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
  - [Site Content](#Site-Content)
- [Testing](#Testing)
- [Guide to Deployment and Development](#Guide-to-Deployment-and-Development)
- [Project Review and Reflection](#Project-Review-and-Reflection)
- [Credits](#Credits)

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
The primary goal of this project is to design, develop and deploy an e-commerce site for SereniTea Emporium.

### Strategy
<!-- What are we aiming to achieve, and for whom? -->

### Scope
<!-- What features do we want to include in the design? What's on the table, and whats off (for now)? -->

### Structure
<!-- How is the information structured, and is it logically grouped? -->


### Skeleton
<!-- How the information should be implemented, and how the user will navigate through the info/features -->

### Surface


<kbd>[Return to ToC](#Table-of-Contents)</kbd>
- - -

## Site Development


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

<kbd>[Return to ToC](#Table-of-Contents)</kbd>
- - -



## Credits

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
  - [Django 4.2](https://docs.djangoproject.com/en/4.2/) online documentation, for guidance on setting up and using the Django framework
  - [Django allauth](https://docs.allauth.org/en/latest/) online documentation, for tailoring and using the authentication modules
  -[Django crispy forms](https://django-crispy-forms.readthedocs.io/en/latest/) documentation, to learn how to use the latest version (5.0) in Django forms
  - [Stripe](https://docs.stripe.com/) online documentation, in particular the [Getting Started](https://docs.stripe.com/get-started), [Payment APIs](https://docs.stripe.com/payments/payment-intents) and [Webhooks](https://docs.stripe.com/payments/handling-payment-events) sections, in developing the checkout app,
  - [Jinja](https://jinja.palletsprojects.com/en/3.1.x/) templating engine documentation, for building dynamic web page content
  - [Bootstrap 5.3](https://getbootstrap.com/docs/5.3/) online documentation, for styling the project website

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
- The idea of an online tea store was inspired by [Jing Tea](https://jingtea.com/)
- 

### Acknowledgements
I would like to acknowledge the following people who helped me complete this milestone project:
- [Amy Richardson](https://code-institute-room.slack.com/team/U06CZC2JZTN) - our Code Institute cohort facilitator.
- [Jubril Akolade](https://github.com/Jubrillionaire) - my Code Institute mentor.
- The Code Institute Slack community, in particular my fellow students in the feb-2023-pla cohort. 



<kbd>[Return to ToC](#Table-of-Contents)</kbd>

- - -