## Revisiting the User Stories

This document revisits the original user stories, reviewing the status of implementation, how achievement of each has been demonstrated, and how these will be developed further in future.

- [A. Visiting the Site](#A-Visiting-the-Site)
- [B. Store Browsing and Navigation](#B-Store-Browsing-and-Navigation)
- [C. Searching and Sorting](#C-Searching-and-Sorting)
- [D. User Registration and Accounts](#D-User-Registration-and-Accounts)
- [E. Purchasing and Checkout](#E-Purchasing-and-Checkout)
- [F. Store Management](#F-Store-Management)
- [F. Store Management](#F-Store-Management)
- [G. Product Reviews](#G-Product-Reviews)

- - -

### A. Visiting the Site

| User Story ID | As a …  | I want to be able to ... | So that I can ... | Implementation | How is this Demonstrated | Future Development|
| ----- | ----- | ----- | ----- | ----- | ----- | ----- |
| A.1| Visitor | Understand the purpose of the site immediately upon visiting | Decide whether to stay on the site and become a shopper.| Complete| Explanation of store and navigation options to products on the home/landing page| The text could be improved with further editing.|
| A.2| Visitor | Visit a site with a recognisable interface| Quickly and easily recognise the site in my bookmarks and when revisiting it in future| Complete| Favicon of cup containing an 's' has been added to the site, to ensure site is identifiable in browser tabs and bookmarks||
| A.3| Visitor | Use a responsive website| View and use the site on a variety of devices| Complete| Site designed with a mobile-first approach, implementing a responsive layout (including site navigation bar) that responds to each viewport size.| Expand the wireframes to cover a wider variety of viewport sizes, using the Bootstrap breakpoints as the foundational structure, to ensure the site is appropriate across all viewports. In particular, the site could be improved by improving responsive font sizing.
| A.4| Visitor | Learn about the company| Make an informed decision whether or not to make a purchase| Complete | About page provides information about the company, its ethos and its products.<br/>A link to Trustpilot is also in the footer, but is not yet functional due to the business being fictional. | Trustpilot link to enable to visitors to see company reviews would be established upon company launch.<br/>Additional information pages to be added, including learning about tea. |
| A.5 | Visitor | Find the company on social media | Learn more and keep up to date on products, offers, etc. | Partial | Links to relevant social media sites available on the footer across all pages. Currently links to social home pages as SereniTea Emporium-specific social pages to not exist | Social Media accounts for publishing updates and promotions would be established upon company launch. |
| A.6 | Visitor | Contact the company | Get answers to any queries that I may have | Partial | Email addresses are included across the site and in conformation notices | An online contact form will be added to allow for contact without using email <br/>Contact form will include a set of subject options, including 'General enquiry', 'About an order', 'About a product', 'About my account' (etc) to enable messages to reach the appropriate team. |
| A.7 | Visitor | Receive feedback when using the site | Know if my actions have been successful, without cluttering the site with additional text | Complete | As actions are undertaken, such as adding items to basket, messages are displayed in the message bar at to of the page.<br/>Message bar timed to fade away after 10 seconds, so not clutter the screen and distract from the user browsing experience. | Incorporate Bootstrap toasts to provide more informative and engaging site notifications |

- - -

### B. Store Browsing and Navigation

| User Story ID | As a …  | I want to be able to ... | So that I can ... | Implementation | How is this Demonstrated | Future Development|
| ----- | ----- | ----- | ----- | ----- | ----- | ----- |
| B.1 | Customer | Easily and intuitively navigate the site | Find what I'm looking for without using the browser buttons | Complete | Navigation menu available directly from homepage (and across all site pages) enables quick navigation to all areas of the site. | Navigation menu for products could be dynamically constructed to allow the site administrator to create, update and delete product categories. |
| B.2 | Customer | View all products available | Select products for purchase. | Complete | Navigation menu includes a link to 'All Products'. This generates a page showing all products available to purchase. | |
| B.3 | Customer | View specific category of products | Browse all items of interest without having to look through all store products. | Complete | Navigation menu includes a link to each category of product. This generates a page showing all products available to purchase in that specific category. | |
| B.4 | Customer | View all products in a group of related categories | Browse selection of items of potential interest, without having to look through all store products or each individual category. | Complete | Navigation menu includes a link to each category group. This generates a page showing all products available to purchase in the related sub-categories. | |
| B.5 | Customer | View details of individual products | See price, description and image of product and learn more about the individual products. | Complete | Details of each individual product can be accessed by clicking on the relevant product listing, or clicking on an item in the shopping basket. | |
| B.6 | Customer | See item reviews | Make an informed decision about what items to purchase. | Partial | Where an item has a review star rating this is listed on both the products overview page and the product details page. Where no rating is yet available, the product is marked with 'No Rating'. | Additional feature for registered users to submit a review for each product they purchase, with the reviews then displayed at the bottom of the relevant product page. Users will be able to submit then edit their reviews until published. Administrators will moderate each review before it's published. Users will be able to see all reviews they have written via their user profile.<br/><br/>Customers will also be able to add a start rating to their purchases (with or without writing a full review). Rating star values for each product will then be dynamic, calculated based upon these star ratings. |
| B.7 | Customer | Easily see all store offers | Take advantage of any special offers and discounts on products I'm considering purchasing. | Complete | Navigation menu includes a link to the group of 'Specials', including 'offers' and 'clearance' items, which will be listed as and when available. | Back-end to be expanded to enable administrators to more easily add offers and other special items to this section of the product catalogue. |
| B.8 | Customer | Easily see limited edition items | Consider purchasing limited edition/special products whilst they're available. | Complete | Navigation menu includes a link to the group of 'Specials', within which there is a 'Limited Editions' option. Any limited edition products will be available to view there, as and when available. |

- - -

### C. Searching and Sorting

| User Story ID | As a …  | I want to be able to ... | So that I can ... | Implementation | How is this Demonstrated | Future Development|
| ----- | ----- | ----- | ----- | ----- | ----- | ----- |
| C.1 | Customer | Sort all products into order                               | Easily identify the best priced and highest  rated products, and sort according to product name. | Complete | A 'Sort products by …' option at the top of the product listing page allows for a selection of ordering options. | |
| C.2 | Customer | Sort products per category into order                      | Easily identify the best priced and highest  rated products per category, and sort items in each category by name. | No | Ordering currently only available on the full product catalogue. | Enable sorting on currently selected category. |
| C.3 | Customer | Search for items by name or description | Quickly find specific items that I'm interested in | Complete | Search box included at the top of each page, enabling visitor to search for any items according to entered terms, across product names and descriptions (including descriptions of product images). | Include 'you searched for ...' at the top of the search results, reminding the user of their search term.  <br/>Expand search capacity to search through product details in the catalogue, to enable searching for organic products, teas of specific brew strength, etc. |
| C.4 | Customer | Easily see the results of my search and my search criteria | Quickly see if the item I'd like are available for purchase | Complete | When searching for products, all products found relating to the inputted search term are listed in the Products listing page, along with a reminder of the entered search term(s). |

- - -

### D. User Registration and Accounts

| User Story ID | As a …  | I want to be able to ... | So that I can ... | Implementation | How is this Demonstrated | Future Development|
| ----- | ----- | ----- | ----- | ----- | ----- | ----- |
| D.1 | Customer | Register for a user account | Have a personal profile page for this online store | Complete | Visitors can register for an account by<br/>- Choosing the 'Register' option from the 'My Account' menu at the top of every page<br/>- Click  the 'Create an account' option during the Secure Checkout process | |
| D.2 | Customer | Log in and out of my account                                       | Securely access my account information | Complete | Registered users can 'sign in' to access their account, then 'logout', using the two named links in the 'My Account' dropdown menu at the top of the page. | |
| D.3 | Customer | Recover my password | Regain access to my account if I lose my password | Complete | Selecting the 'Forgot your password?' option in the Login page, the user can enter their email address and will then receive an email to reset their password. | |
| D.4 | Customer | Receive an email confirmation when I've registered for an account  | Verify that my account registration has been successful | Complete | When a user registers for an account, an email will be sent to the email address to verify their registration. | |
| D.5 | Customer | Have a personalised user profile | Save personal information for faster checkout | Complete | Personal delivery address can be added to 'My Profile' page, or saved by checking the 'save' option during checkout. | |
| D.6 | Customer | Update my user profile | Keep my personal details up to date | Complete | Profile details can be updated and saved at any time via the 'My Account > My Profile' page | |
| D.7 | Customer | See my order history | Remind myself of previous products I've purchased | Complete | Full history of orders placed when logged in displayed in the 'My Account > My Profile' page, ordered according to date. | Add ability to re-order past orders based on personal preference (e.g., order by date, order number, total cost, etc). <br/>Add search facility to be able to search through order history for specific orders or products. |

- - -

### E. Purchasing and Checkout

| User Story ID | As a …  | I want to be able to ... | So that I can ... | Implementation | How is this Demonstrated | Future Development|
| ----- | ----- | ----- | ----- | ----- | ----- | ----- |
| E.1 | Customer | Easily add items I want to purchase to my shopping basket | Ensure I purchase the correct items | Complete | Every product detail page includes am 'add to basket' button plus an option to change the quantity to add more than one. | Expand the product listing pages to include a 'Quick Add' option, to enable adding products to the basket without having to view the individual product details pages. |
| E.2 | Customer | View current items in my shopping basket | Keep track of the items I'd like to purchase | Complete | Clicking the shopping basket icon at the top of the page will display the full basket contents. | Improve responsiveness on very small viewports (<330), transposing the shopping basket layout from landscape to portrait. |
| E.3 | Customer | Easily update the contents of my shopping basket | Update quantity of items in my bag before checkout | Complete | When viewing the shopping basket contents the quantity of each item can be updated. | Styling of the quantity box could be improved to reduce it's size and add plus/ minus buttons, to make quantity update facility easier to see and use. |
| E.4 | Customer | Delete items from my shopping basket | Remove items I don't want to purchase before checkout | Complete | When viewing the shopping basket, an item can be removed by clicking the delete (bin) option. | |
| E.5 | Customer | Easily view the total cost of my current purchases | Keep track of my spending and not spend too much | Complete       | The current cost of basket items, including standard shipping, is show next to the basket icon at the top of every page. | Update basket total visible at top of the page to show (not including postage), enabling variable postage options to be selected from at checkout. |
| E.6 | Customer | See shipping cost of basket contents                             | Keep track of my spending | Complete | Standard shipping cost included in basket cost displayed at top of every page, and explicitly shown in the shopping basket page | |
| E.7 | Customer | See how much I need to spend to get free shipping | Take advantage of free shipping offer | Complete | Amount left to spend to get free standard shipping is shown in the shopping basket, under the current cost. | |
| E.8 | Customer | Complete checkout securely | Pay for items whilst knowing that no-one has access to my personal payment details | Complete | When ready to checkout the 'secure checkout' button can be clicked from the shopping basket page. The Stripe system is then used for ensuring payments can be processed securely and reliably. | Checkout page layout to be improved to eliminate side-scrolling on smaller devices. |
| E.9 | Customer | Enter my payment information | Purchase the items in my shopping bag | Complete | After clicking 'secure checkout' from the shopping basket, payment information can be entered to then be processed by Stripe to take payment | |
| E.10 | Customer | View order confirmation after checkout | Ensure the purchase has been successful | Complete | Order confirmation page displayed upon successful order being placed.<br/>Message displayed at top of page confirming order placed. | |
| E.11 | Customer | Receive and email confirmation after completing checkout process | Retain confirmation for my records. | Complete       | Email confirmation of order, including order details, sent to email address included with order submission. | Single free email address currently used for the company. In future the confirmation email would be sent from a more professional 'confirmation-noreply@serenitea.com'<br/>Email formats will be improved - text emails will be structured more professionally, and an option will be added to receive HTML formatted emails. |
| E.12 | Customer | Use my saved profile details during checkout | Quickly purchase items without having to re-enter my details | Complete       | If user is logged in and has previously requested that their delivery details be saved, the checkout form is automatically pre-populated with their previously saved delivery details. | Inclusion of multiple customer-provided delivery addresses from which they can select. Enables easy ordering to other addresses such as workplace, family and friends. |
| E.13 | Customer | Purchase products without having to create an account            | Avoid having to sign up to the store. | Complete       | If not registered the checkout page provides an option to create a profile, but this is optional. | After successful checkout, customer will be given an option to use their entered details to create an account, enabling them faster checkout in future and providing access to record of all previous orders. |

- - -

### F. Store Management

| User Story ID | As a …  | I want to be able to ... | So that I can ... | Implementation | How is this Demonstrated | Future Development|
| ----- | ----- | ----- | ----- | ----- | ----- | ----- |
| F.1 | Site Admin | Add a product | Add a new product to the items for sale through my store | Complete       | New products can be added via the 'Add new product' link in the 'My Account' dropdown menu | Adding a new persistent image to the site is not currently possible (see the Bugs section). In future hosting/deployment process would be improved to allow for adding new product photos to the product catalogue, as well as adding user profile pictures, and pictures in support of customer reviews. |
| F.2 | Site Admin | Edit/Update a product | Change product prices, details, images and other relevant information | Complete       | Site products can be edited:<br/>- through the products list page by clicking the green 'edit' icon<br/>- through the individual product details page by clicking the green 'Edit' option               | Confirmation needs to be added to allow for the updates to be checked before being committed. |
| F.3 | Site Admin | Delete a product | Removed items from the store that are no longer for sale | Complete       | Site products can be deleted:<br/>- through the products list page by clicking the red 'bin' icon<br/>- through the individual product details page by clicking the red 'Delete' option | Confirmation needs to be added to allow for the deletion to be checked and considered before the item is permanently removed. |
| F.4 | Site Admin | See number of items of products in stock           | Monitor stock levels to re-order as needed | Complete       | Stock level for products are visible from the site administration page.<br/>Stock level visible on the product details page for every product.<br/>Excludes loose leaf teas, which are bagged to order. | Upon purchase the stock count of a product would be reduced by the quantity purchased, ensuring the online product catalogue is up-to-date. The status would be reviewed to ensure orders have completed. If an issue has arisen, such as a failed stripe payment, then the product(s) would be added back into stock (based on stripe webhook notification). |
| F.5 | Site Admin | Ensure no orders are placed for out of stock items | Be confident that the store can complete all submitted orders         | Complete       | When a product is out of stock this is marked on the product listing page. <br/>Product detail page states out of stock, and add to basket option is disabled. | The inclusion of dynamic product stock level updates (outlined above) would help support this user story. |


- - -

### G. Product Reviews

| User Story ID | As a …  | I want to be able to ... | So that I can ... | Implementation | How is this Demonstrated | Future Development|
| ----- | ----- | ----- | ----- | ----- | ----- | ----- |
| G.1 | Customer | Write a review for a product I have used (purchased or gifted) | Provide feedback to the seller and share my experience with others | Complete | When logged in, a customer can choose 'Review a Product' from the menu. This provides customers with an online from in which they can select their product, write a review, add a rating and publication name, then submit to the Site Administrator for review. | Limiting the products that can be reviewed to only those purchased by each customer will help reduce the site administration workload in validating submitted reviews.<br/>Customer view will be improved by providing quick access to list of products they have purchased, which they haven't yet reviewed, and a direct link to add a review for each product. |
| G.2 | Customer | See all product reviews that I have written | Keep track of which products I've reviewed | Complete | When logged in, a customer can select the 'My Product Reviews' option from the top menu. This will display a page of all reviews written by that customer and submitted to the store, and the status of each review (whether that have been accepted or not) | Addition of view options to select which reviews to see (e.g. those not yet reviewed, and those published, all reviews, category reviews) and to choose review ordering (e.g. order by date, product name, product category, etc) |
| G.3 | Customer | Edit a submitted review | Correct any mistakes or change my rating | Complete | When logged in, a customer can access all reviews via the 'My Product Reviews' page, where a green Edit button is available for those reviews that have not yet been reviewed and approved for publication. Clicking this button provides the user with a form where they can modify their review and resubmit. | |
| G.4 | Customer | Delete a submitted review | Change my mind and remove my comments. | Complete | When logged in, a customer can access all reviews via the 'My Product Reviews' page, where a read Delete button is available for all submitted reviews. Clicking this button deletes the review. | Addition of an additional confirmation step where the customer is asked "Are you sure you want to delete this review?" Only after confirming will the review be deleted. |
| G.5 | Site Admin | Validate customer written product reviews before making them visible to all customers | Ensure reviews are appropriate and not fake or abusive, so that no inappropriate reviews are published to the site. | Complete | Site administrators can access all submitted reviews through the site admin panel. Submitted reviews are initially marked with a cross (not approved). Once checked the site administrator can change this to 'approved'. Approved reviews will appear in the admin panel alongside a green tick. | Creation of a site administration section of the web application to support the quick and easy approval of reviews. This approach will be more intuitive and quicker than using the Django admin site. |


- - -
