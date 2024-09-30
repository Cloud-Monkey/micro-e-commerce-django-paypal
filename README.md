![Button mashers logo](readme-images/logo-readme.png)


![Button mashers responsive screenshot](readme-images/Button-mashers-responsive-img.png)

## Introduction

View live site: [Button mashers](https://button-mashers-11120a298309.herokuapp.com/)

Our micro-ecommerce site caters to fighting game enthusiasts who build custom controllers. We sell high-quality arcade controller parts like buttons and joysticks. Our products are designed for reliability and performance, ensuring every punch, kick, and combo is spot-on. We offer a wide variety of colors and styles, allowing for creative and personalized designs.

For full Admin access to Django Admin panel with relevant sign-in credentials: [Button mashers Admin](https://button-mashers-11120a298309.herokuapp.com/admin/login/?next=/admin/)

## Table of Contents

- [Button mashers](#Button mashers)
  - [Introduction](#introduction)
  - [Table of Contents](#table-of-contents)
  - [Overview](#overview)
  - [Customer Goals](#customer-goals)
  - [Business Goals](#business-goals)
- [UX/UI - User Experience/User Interface](#uxui---user-experienceuser-interface)
  - [Design Inspiration](#design-inspiration)
    - [Color Scheme](#color-scheme)
    - [Typography \& Iconography](#typography--iconography)
- [Project Planning](#project-planning)
  - [Strategy Plane](#strategy-plane)
    - [Site Goals](#site-goals)
  - [Agile Methodologies](#agile-methodologies)
    - [MoSCoW Prioritization](#moscow-prioritization)
    - [Sprints](#sprints)
  - [Marketing](#marketing)
  - [User Stories](#user-stories)
    - [Visitor User Stories](#visitor-user-stories)
    - [Epic - Home View \& User Account](#epic---home-view--user-account)
    - [Epic - Products](#epic---products)
    - [Epic - Basket Management \& Purchasing](#epic---basket-management--purchasing)
    - [Epic - Wishlist](#epic---wishlist)
    - [Epic - Newsletter](#epic---newsletter)
  - [Scope Plane](#scope-plane)
  - [Structural Plane](#structural-plane)
  - [Skeleton \& Surface Planes](#skeleton--surface-planes)
    - [Wireframes](#wireframes)
    - [Database Schema](#database-schema)
    - [Defensive Design](#defensive-design)
- [Features](#features)
  - [User View - Guests/Account Holders](#user-view---guestsaccount-holders)
  - [CRUD Functionality](#crud-functionality)
  - [Features Showcase](#features-showcase)
  - [Future Features](#future-features)
- [Technologies \& Languages Used](#technologies--languages-used)
  - [Libraries \& Frameworks](#libraries--frameworks)
  - [Tools \& Programs](#tools--programs)
- [Testing](#testing)
- [Deployment](#deployment)
  - [Connecting to GitHub](#connecting-to-github)
  - [Django Project SetUp](#django-project-setup)
    - [Elephant SQL](#elephant-sql)
  - [Heroku Deployment](#heroku-deployment)
    - [Media Folder Setup](#media-folder-setup)
  - [Clone Project](#clone-project)
  - [Fork Project](#fork-project)
- [Credits](#credits)
  - [Code](#code)
  - [Media](#media)
    - [Additional reading/tutorials/books/blogs](#additional-readingtutorialsbooksblogs)
  - [Acknowledgements](#acknowledgements)

## Overview

Buttonmashers is a arcade controller modding/customisation products store focusing on procuring the best components for high level players. Users are invited to:

- View the store as Guests
- Register for an Account
- Review and rate products
- Browse products
- View, add and edit products in their cart
- Checkout and purchase items

## Customer Goals

Buttonmashers offers gamers a seamless and user-friendly shopping experience, focusing on high-quality, durable arcade components and peripherals. We encourage our customers to create accounts, unlocking access to exclusive features of shopping and the ability review/rate products.

Our product range emphasizes longevity and performance, promoting sustainable gaming practices by reducing the need for frequent replacements. We consistently guide our customers towards premium, tournament-grade products that offer the best value in terms of quality and durability.

## Business Goals

Buttonmashers offers the business owners an intuitive Admin Dashboard that simplifies inventory and order management. Users can easily access detailed information about users and orders through the Admin Dashboard, which provides a direct link to the data stored in the Django Admin Panel.

Button Mashers aims to cultivate a loyal community of gaming enthusiasts who appreciate high-quality, durable arcade components and peripherals. The site's focus on premium arcade parts and accessories attracts players looking for authentic, tournament-grade gaming experiences.

# UX/UI - User Experience/User Interface

## Design Inspiration

A simple logo, created using *logo reference here <----------*

![button mashers logo] 
*button mashers logo*


![Hero Image]()
*Image created by ....?*



![Header Feedback](docs/readme_images/header_feedback.png)  
*Header feedback is kept clean and intuitive*

### Color Scheme

![Button mashers Color Scheme]()
*Button mashers Color Scheme*

Variables were used within the CSS file to call colours as they were needed:
- --colours here

The above colours were chosen to reflect colours found ... where?

![Button mashers main button]()  
*Button Mashers Main Button*

![Button mashers Color Scheme accessibility Check]()  
*Button mashers Color Accessibility Check*

![Button mashers Color Scheme Contrast Check]()  
* Button mashers Color Contrast Check - Main*

![Button mashers Color Scheme Contrast Check]()  
*Button mashers Color Contrast Check - Button*

### Typography & Iconography

![Button mashers Font Pairing](docs/readme_images/fontpair.png)
*Button mashers Font Pairing*

Karla and Inconsolata were both imported from [Google Fonts](https://fonts.google.com/). They were chosen for their compatibility and aesthetics that aligned with the store brand. Karla is a sans-serif typeface with a clean and modern design which delivers a fresh and simple look to the store. Inconsolata is a monospace font which allows clear display of descriptions and information about the products. Together they apply enough textual contrast to allow for a good flow of information to the user, improving user experience. Using Google Fonts allows for faster, reliable loading times for the website, ensuring the user stays when they visit.

In development, 'Karla' was identified by variable ```--title```, whilst 'Inconsolata' was set as ```--main-font``` within the CSS file. Similar to my setup for the project's colours, using variables helped to speed up the frontend process.

# Project Planning

## Strategy Plane

The primary objective was to create an e-commerce store that satisfied the assessment criteria of the Code Institute's Project 5: E-Commerce Module. The store must provide the expected functions of a responsive e-commerce store using Stripe as a payment system, user/guest views for authentication and store features, some extra features of my choosing, wishlist and articles, and demonstration of some marketing/SEO skills. Orders on Button mashers were to display the carbon footprint totals and carbon saved, (where data is available, see below), reflecting the pressing need for eco-consciousness in these modern times. The User, whether paying customer or just browsing, must receive the best in UX and feel that Button mashers is relatable and trust-worthy. 

The site's design and graphic assets were collected through various copyright-free image websites. Images were edited for the website to be cohesive. The hero-image on the home page and above, was created by myself in Figma. Bootstrap and Crispy Forms were used for the project's frontend to speed up the process and to keep the templates consistent. Further customisation to the buttons, forms, modals, toasts and user feedback processes were added to the project's CSS files. 

If a customer chooses to make a purchase then they are given consistent feedback through the use of 'toasts' messages and confirmation emails. The purchasing process is presented using Stripe payment handlers, obtained and setup using [Stripe's](https://stripe.com/docs) documentation and website.


### Site Goals

- Site provides enjoyable experience for shoppers.
- Customers are educated about carbon footprints/credits/sustainable products through the checkout process and through reading the site articles and FAQ's.
- Customers feel informed that they are making a good choice shopping with Button mashers.
- UX remains similar across screen sizes.
- CRUD functionalities work as intended with easy to use frontend forms.
- Scalable site to allow for extra features in the future.

## Agile Methodologies

Button mashers followed Agile planning methodologies to its completion. [GitHub Projects](https://github.com/users/amylour/projects/6) provided an ideal platform to create issues, boards and milestones for each of the project's Epics. Using labels I could easily identify my next task and organise them into the appropriate Milestones and Sprints. Keeping focused on individual sections as I built Button mashers reduced the number of bugs and human errors.

### MoSCoW Prioritization

I chose to follow the MoSCoW Prioritization method for Button mashers, identifying and labeling my:

- **Must Haves**: the 'required', critical components of the project. Completing my 'Must Haves' helped me to reach the MVP (Minimum Viable Product) for this project.
- **Should Haves**: the components that are valuable to the project but not absolutely 'vital' at the MVP stage. The 'Must Haves' must receive priority over the 'Should Haves'.
- **Could Haves**: these are the features that are a 'bonus' to the project, it would be nice to have them in this phase, but only if the most important issues have been completed first and time allows.
- **Won't Haves**: the features or components that either no longer fit the project's brief or are of very low priority for this release.

### Sprints

My Sprints were broken down into appropriately sized chunks from the beginning and I followed them to the best of my abilities. It is difficult to quantify the time taken exactly for each sprint as running a busy household outside of the course meant the hours the project was completed in hours outside of the normal working week. I have done my best to record them below. They are representative of a general timeframe of focus on the project areas.

| Sprint No. | Sprint Content | Start/Finish Dates |
|------------|----------------|--------------------|
|    # 1     | Project Setup  |   01/08/23 - 20/08/23   |
|    # 2     | AllAuth & Basic Navigation |  20/08/23 - 22/09/23  |
|    # 3     | Product Views & CRUD       |  22/09/23 - 02/09/23  |
|    # 4     | Shopping Bag Functionality & Styling | 02/09/23 - 15/09/23   |
|    # 5     | Wishlist Feature   |   15/09/23 - 17/09/23       |
|    # 6     | Carbon Footprint & Articles  |  17/09/23 - 22/09/23   |
|    # 7     | Admin Dashboard        |  22/09/23 - 26/09/23    |
|    # 8     | User/Customer Correspondence  |  26/09/23 - 02/10/23   |
|    # 9     | Documentation & Testing   |    02/10/23 - 15/10/23   |

## Marketing

An [Button mashers Facebook Page](https://www.facebook.com/profile.php?id=61552368530738) was created to demonstrate promotion of the Button mashers store on social media. Posts informing customers of deals and new products would be made on the page with the hopes of drawing in more revenue. Facebook provides an easy, minimal-step process to allow business owners to promote their business, with additional paid 'boost' features to further promote and spread the reach of the posts. Button mashers also offers a newsletter subscription service through MailChimp. The benefit of both of these services is that the customer is not forced to sign up to either and potentially worry that they will be spammed with an unnecessary amount of information. Button mashers avoids this in order to keep its brand clean and uphold its eco-friendly efforts.

Within the head's meta tags of the base template are researched keywords and a description of Button mashers's goal as a business. These keywords have been researched using[Wordtracker](https://www.wordtracker.com/) to ensure that both short-tail and long-tail keywords are included. Keywords such as 'carbon-neutral', 'zero waste' and 'practical products' aim to reach most of the market, with additional descriptive key phrases such as 'buy longlife products' and 'buy once products' to draw in users who know exactly what type of product they are looking for. Important keywords like 'Vegan', 'Organic' and 'Bamboo' are present in the product names and descriptions in the hope to catch a chance to appear at the top of the customers' Google searches.

In addition to this, sitemap.xml and robots.txt files are included to increase the site's visibility. These files are essential for SEO (Search Engine Optimisation). The sitemap.xml was generated using [XML Sitemap](https://www.xml-sitemaps.com/) and included in the root folder of the project. A robots.txt file was created in the root folder to instruct search engine crawlers on how to access and crawl the site's pages.

![Button mashers Facebook Business Page]()
*Button mashers Facebook Business Page*

## User Stories

User stories and features were recorded and managed on [GitHub Projects](https://github.com/users/amylour/projects/6)

### Visitor User Stories

| User Story | Priority |
|------------|------------------|
| As a **customer**, I can **view the site's home page** so that I can **understand the site's intentions and purpose**. | **MUST HAVE** |
| As a **customer**, I can **see and use the navigation bar** so that I can **make my way around the site and get to where I would like**. | **MUST HAVE** |
| As a **customer**, I can **enter text into the search bar** so that I can **search for a specific item**. | **MUST HAVE** |

### Epic - Home View & User Account

| User Story | Priority |
|------------------|---------------------|
| As a **customer** I can **create and manage an account with Button mashers** so that I can **keep my personal details, order history and speed up my checkout process**. | **MUST HAVE** |
| As a **customer**, I can **edit my personal details on my account** so that I can **keep them up to date**. | **MUST HAVE** |
| As a **site user**, I can **enter my login details** so that I can **login in to my account**. | **MUST HAVE** |
| As a **site user**, I can **click on the visible links in the footer** so that I can **view the relevant information and destinations**. | **MUST HAVE** |
| As a **site user**, I can **register my email and receive a validation link via email** so that I can **create an account with Button mashers to track my spending and purchases**. | **SHOULD HAVE** |
| As a **customer**, I can **use the Contact Us form** so I can **send a message to the business/site admin**. | **SHOULD HAVE** |

### Epic - Products

| User Story | Priority |
|------------------|---------------------|
| As a **site user** I can **interact with sorting and view features on the 'All Products' page** so that I can **improve my shopping experience on the site**. | **MUST HAVE** |
| As a **site user**, I can **click on a navbar item for a specific category** so that I can **choose to view a smaller amount of related products**. | **MUST HAVE** |
| As a **customer**, I can **choose an individual product** so that I can **view its description, price, colours, sizes available etc**. | **MUST HAVE** |
| As a **site admin** I can **add a product to my inventory using a frontend from** so that I can **increase my range/amount of products available on site**. | **MUST HAVE** |
| As a**site admin**, I can **edit existing inventory from a frontend form** so I can **change the quantity of stock, sizes, colours or edit products description, price or image**. | **MUST HAVE** |
| As a **site admin**, I can **delete product from the inventory using a frontend form** so that I can **remove it from sale**. | **MUST HAVE** |

### Epic - Basket Management & Purchasing

| User Story | Priority |
|------------------|---------------------|
| As a **customer** I can **create and manage an account with Button mashers** so that I can **keep my personal details, order history and speed up my checkout process**. | **MUST HAVE** |
| As a **customer**, I can **click on 'Add to Bag' in my product view**so that I can **add the product to my bag**. | **MUST HAVE** |
| As a **customer**, I can **increase/decrease/remove quantities of a product in my bag** so that I can **have control over what I wish to purchase**. | **MUST HAVE** |
| As a **customer**, I can **view my bag total from any page** so that I can **keep track of my potential spending**. | **MUST HAVE** |
| As a **customer**, I can **view my running total of carbon saved when I add products** so that I can **see how much carbon my purchases would had saved in their production vs non eco-friendly products of the same type**. | **MUST HAVE** |
| As a **customer**, I can **view my total carbon footprint saving on checkout and it's associated climate impact/lifestyle changes** so that I can **understand the equivalent value of carbon saved versus purchasing the same non eco-friendly products**. | **MUST HAVE** |
| As a **customer**, I can **checkout my products securely** so that I can **complete my purchase**. | **MUST HAVE** |
| As a **customer**, I can **receive an email after purchasing** so that I can **confirm my purchase and keep a record of my order**. | **MUST HAVE** |
| As a **site user** I can **view error pages with 'Home' links** so that I can **return to the main page if a page is missing or forbidden**. | **MUST HAVE** |

### Epic - Wishlist

| User Story | Priority |
|------------------|---------------------|
| As a **logged-in user** I can **click the 'Add to Wishlist' button** so that I can **keep a record of my favourite items**. | **COULD HAVE** |
| As a **logged-in user** I can **click the 'Remove' icon beside my Wishlist item** so that I can **remove that product from my Wishlist**. | **COULD HAVE** |

### Epic - Newsletter

| User Story | Priority |
|------------------|---------------------|
| As a **customer**, I can **enter my details into the newsletter form** so I can **receive emails about products or environmental issues/climate saving tips**. | **SHOULD HAVE** |

## Scope Plane

To focus on the learning of the Stripe API and webhook handlers that would ultimately drive the inner workings of the project, I kept my Button mashers scope lower than my previous project, FreeFido. A working e-commerce store was essential so I initially planned to keep to the MVP to ensure that I would complete the project successfully. Especially with the project being my final one for this Diploma, a rigorous year of learning left me ecstatic with my progress but cautious not to fall at the final hurdle from fatigue. However, through the planning stages I realised that I wanted to push further with the theme of an eco store and introduce carbon footprint as a currency that we may see in the future in the form of carbon credits.

Adding an Articles feature posted solely by the Admin of the website felt important to give more information to the customers on climate-change and manufacturing processes and their environmental impacts. An additional Wishlist feature would complement the site as some of the items have a higher price point due to their robust and eco-friendly manufacturing processes and longevity and the customer may like to purchase them at a later date.

Django's MVT framework allowed these features to be built quickly and addition of an Admin frontend panel for managing products and articles created a robust e-commerce site that could start taking orders tomorrow.

Essential features were:
- User Accounts with AllAuth
- Payment system with Stripe
- Articles creation and management - Full CRUD
- Product inventory management - Full CRUD
- Shopping UX with Bag and Checkout processes - Full CRUD
- Site responsivity
- Business details to inform the user
    
## Structural Plane

Button mashers is built using Bootstrap, with Code Institute's Boutique Ado e-commerce project as its foundation. However, I picked apart the structure and styling to fit my own vision and changed quite a bit of the code. In particular I simplified the navbar and made the delivery banner a dropdown source of information, as is common with many modern e-commerce applications. Icons were sourced from Fontawesome and Flaticon through the wireframing process in Figma. The typography was chosen to give a clean, strong reading experience for the user. The Button mashers icon was used as the Favicon. This is also repeated through the newsletter email.

A dashed forest green 2px border is used for form fields throughout the project to replace browsers default blue highlight. Form validation has been left with it's original styling as no change was needed. Bootstrap allowed for easy transition between screen sizes as many ecommerce purchases are made using our mobiles, so this was a priority focus. Bootstrap components such as forms, an accordion section and a product carousel raised the spec of the project, to give it a professional finish.

## Skeleton & Surface Planes

### Wireframes

[Figma](https://www.figma.com) was used to create basic wireframes for Button mashers. I had a vision of what the site would look like from the beginning so the planning process went smoothly. Figma allows easy creation of wireframes to the appropriate frame sizes for different screens. Addition of icons and extra design features is easy with their Plugins component which can connect to Flaticon for example.

<details open>
    <summary>Desktop/Tablet Home Page Wireframe</summary>  
    <img src="docs/readme_images/wf_home_dt.png">  
</details>

<details>
    <summary>Mobile Home Page Wireframe</summary>  
    <img src="docs/readme_images/wf_home_mob01.png">  
</details>

<details>
    <summary>Mobile Home Page Wireframe</summary>  
    <img src="docs/readme_images/wf_home_mob02.png">  
</details>

<details open>
    <summary>Desktop/Tablet/Mobile All Products Page Wireframe</summary>  
    <img src="docs/readme_images/wf_proddet.png">  
</details>

<details open>
    <summary>Desktop/Tablet Product Page Wireframe</summary>  
    <img src="docs/readme_images/wf_prod.png">  
</details>

<details>
    <summary>Shopping Bag Wireframe</summary>  
    <img src="docs/readme_images/wf_bag.png">  
</details>

<details>
    <summary>Bag Contents Toast Wireframe</summary>  
    <img src="docs/readme_images/wf_toast_bag.png">  
</details>

<details open>
    <summary>Mobile Menu & Auth Pages Wireframe</summary>  
    <img src="docs/readme_images/mob_menu_auth_wf.png">  
</details>

<details>
    <summary>Desktop Register Page Wireframe</summary>  
    <img src="docs/readme_images/wf_reg.png">  
</details>

<details>
    <summary>Desktop SignIn Page Wireframe</summary>  
    <img src="docs/readme_images/wf_signin.png">  
</details>

<details>
    <summary>Desktop SignOut Wireframe</summary>  
    <img src="docs/readme_images/wf_signout.png">  
</details>

### Database Schema

![Button mashers Eco Eco-Ecommerce ERC]()  
*Database Schema (ERD) for Button mashers displaying relationships between feature components saved within the database*

[Lucidchart](https://www.lucidchart.com/pages/) was used to create the ERD(Entity Relationship Diagram) for Button mashers. To satisfy the assessment criteria, multiple models were created to personalise the Button mashers project. These include:
- **Articles**: Articles may be added by Admin with image and text fields within the Add/Edit Article forms.
- **Order**: Carbon Footprint total and Carbon Saved Total have been added to the Boutique Ado Order model to handle the carbon total logic. This logic duplicates the product adding/updating/quantity logic within the bag contexts to allow for the carbon footprint to be calculated for products that had some form of data available to me to calculate approximate values.
- **Product**: Carbon Footprint and Carbon Saved have been added to the Boutique Ado Product model to handle the carbon total logic. The Admin can enter these values into the Product Management forms to be made available for the bag/checkout logic to process them.
- **Wishlist**: The Wishlist model takes simple values of the connected user and the product id to display the items in a list for the individual user.

Future Feature models are visible in the ERD for Reactions, Reviews and Discount Codes. These will be incorporated into the next version of Button mashers. At the moment they are beyond the MVP.

### Defensive Design

Button mashers was developed to ensure a reliable user experience. It's intention was to cause no frustrations for the users and to ensure they return to make further purchases.

- Django AllAuth for user registration/log in/log out
- Input validation and error messages provide feedback to the user to guide them towards the desired outcome. 
- Unregistered users are diverted to the Sign Up page from restricted access pages. 
- Authentication processes control edit/delete icons to reveal them to the Admin only, this is further secured through accessing of CRUD functionalities in the Admin Dashboard. 
- Deletion of data is confirmed through an additional modal, double-checking with the user.
- Error pages are displayed with 'Home' buttons to help users get back on track. 
- Testing and validation of features completes the process.

**CSRF Tokens**

CSRF (Cross-Site Request Forgery) tokens are included in every form to help authenticate the request with the server when the form is submitted. Absence of these tokens can leave a site vulnerable to attackers who may steal a user's data.

# Features

## User View - Guests/Account Holders

| Feature   | Guest | Registered, Account Holder |
|-----------|-------------------|-----------------|
| Home Page | Visible           | Visible         |
| Account  | Not Visible - 'Account' option only appears for registered, logged-in users | Visible and full feature interaction available |
| All Products  | Visable - items can be viewed and added to Bag, Wishlist function not available | Visible and full feature interaction available |
| Categories   | Visible - items can be viewed and added to Bag, Wishlist function not available | Visible and full feature interaction available |
| Read   | Visible | Visible |
| Search  | Visible | Visible |
| Contact Us/Newsletter | Visible | Visible |
| Admin Dashboard | Not Visible | Only visible to Admin |

## CRUD Functionality

Customers have full CRUD functionality with their prospective purchases. They may edit their cart, add more items or remove all items. They may also edit their delivery details if they are registered, logged-in users. Button mashers Admin have access to the Admin Dashboard which allow them full CRUD over Product Management and Review posting.

| Feature | Create | Read | Update | Delete |
|---------|--------|------|--------|--------|
| Account | On registration | Yes, delivery details and order history | Yes, update address | No, users are unable to delete their accounts, this is restricted to Admin |
| Bag | Yes, customers may add to their bag | Yes | Yes, items can be added/removed | Yes |
| Products | Yes, Admin only | Yes, all users | Yes, Admin only | Yes, Admin only |
| Articles | Yes, Admin only | Yes, all users | Yes, Admin only | Yes, Admin only |

## Features Showcase

**Header & Navigation - All Users**

**Home Page - All Users**

**Delivery Banner - All Users**

**All Auth - All Users who wish to create an account**

Django AllAuth provides a comprehensive, customisable authentication system that keeps user data safe. If a customer wishes to register an account they may enter their username and email and password x 2 to ensure precision. Upon submitting the form the user will receive an email to validate their email and then sign in to Button mashers. Similar to all form fields throughout the site, I have applied my own styling to keep in line with Button mashers's design. The log in page is similar to the register page with the log out page presenting the user with two buttons to continue the log out process or to return home.

Feedback is continually released to the user through toast messages to confirm successful registration, log in and log out.

AllAuth handles password reset by sending an email to the user with a link to change their password to something new.

**Account - Registered, logged in User**

**All Products - All Users**

**Articles - All Users/Admin CRUD**

**Cart - All Users**

**Checkout - All Users**

**Admin Dashboard - Logged in Admin/Superuser only**

When developing this project it was important to me to have a separate Admin area accessible via the frontend, in addition to the Django Backend Panel. I fulfilled this by separating out the CRUD features for the Admin/Superuser into an Admin Dashboard. This provides a direct link to editable forms for adding/editing products and articles. A separated 'Admin' view (viewable only to the Admin when they are logged in) has been created for Articles and Products with lists that display 'Edit' and 'Delete' Buttons. The 'Add' buttons bring the Admin directly to adding products or articles. Crispy Forms and Summernote render forms that allow for a high degree of editing, manipulation and connection to the database models. Defensive design for deletion of items appears in the form of a 'Delete Confirmation' modal.

**Footer - All Users**

**Contact Us - All Users**

## Future Features

- **Stock Levels**

- **Article Comment, Article React**

- **Reviews feature with Ratings**
  
- **Eco-Labels**
  
- **Newsletter Discount Code**

- **Sale Section**

- **Product Slugs**

# Technologies & Languages Used

- HTML
- CSS
- JavaScript
- Python
- [Git](https://git-scm.com/) used for version control.
- [Github](https://www.github.com) used for online storage of codebase and Projects tool.
- [CodeAnywhere](https://app.codeanywhere.com) as an online, cloud-based IDE for development.
- [Figma](https://www.figma.com) for project design planning and wireframe creation.
- [Adobe Color](https://color.adobe.com) for colour theme creation and accessibility checkers.
- [Django](https://www.djangoproject.com/) was used as the Python framework for the site.
- [Heroku](https://www.heroku.com) was used to host the 'Button mashers' application.
- [WAVE](https://wave.webaim.org/) to evaluate the accessibility of the site.
- [Procreate](https://procreate.com/) for image creation and editing.

## Libraries & Frameworks

Libraries and frameworks used were dictated by the 'Boutique Ado' walkthrough from our course material with the Code Institute. This project will be upgraded on completion of the course to more recent packages to meet current standards and security packages.

- [Django v3.2](https://docs.djangoproject.com/en/4.2/releases/3.2/) 
- [AllAuth v0.41](https://django-allauth.readthedocs.io/) for user authentication and account management.
- [Bootstrap v4.6](https://getbootstrap.com/docs/4.6/getting-started/introduction/) for template rendering.
- [Crispy Forms](https://pypi.org/project/crispy-bootstrap4/) for form rendering.
- [boto3](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html) for AWS CRUD with Python scripts.
- [dj-database-url](https://pypi.org/project/dj-database-url/) for DATABASE_URL.
- [django-countries](https://pypi.org/project/django-countries/) for country field rendering in checkout form.
- [django-storages](https://django-storages.readthedocs.io/en/latest/) for handling static and media files.
- [django-summernote](https://pypi.org/project/django-summernote/) a WYSIWYG editor for Django forms and models.
- [gunicorn](https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/gunicorn/) apure-Python WSGI server for UNIX.
- [oauthlib](https://pypi.org/project/oauthlib/) OAuth request-signing logic.
- [psycopg2](https://pypi.org/project/psycopg2/) s PostgreSQL database adapter for Python.
- [Stripe](https://stripe.com/en-ie) for processing Button mashers's payment system.

## Tools & Programs
- [ImageCompressor](https://imagecompressor.com/) for compressing PNG/WEbp files
- [Image ReSizer](https://www.simpleimageresizer.com/) for reducing image size
- [EZGif](<https://ezgif.com/>) for gif conversion.
- [Convertio](https://convertio.co/) for file conversion to PNG, WEBP.
- [Tiny Png](https://tinypng.com/) for file size reduction.
- [Lucidchart](https://www.lucidchart.com/pages) for ERD (entity relationship diagram) creation.
- [Favicon](https://favicon.io/) for converting an icon into a favicon.
- [amiresponsive](https://ui.dev/amiresponsive) for screenshot of Button mashers on different screen sizes.
- [Perplexity AI](https://www.perplexity.ai/) for breaking down Python concepts and Django documentation into more understandable chunks.
- [Mailchimp](https://mailchimp.com/) is used for marketing with their newsletter subscription service.

# Testing

- For all testing, please refer to the [TESTING.md](TESTING.md) file.

# Deployment

## Connecting to GitHub  

To begin this project from scratch, you must first create a new GitHub repository using the [Code Institute's Template](https://github.com/Code-Institute-Org/ci-full-template). This template provides the relevant tools to get you started. To use this template:

1. Log in to [GitHub](https://github.com/) or create a new account.
2. Navigate to the above CI Full Template.
3. Click '**Use this template**' -> '**Create a new repository**'.
4. Choose a new repository name and click '**Create repository from template**'.
5. In your new repository space, click the purple CodeAnywhere (if this is your IDE of choice) button to generate a new workspace.

## Django Project SetUp

1. Install Django and supporting libraries:

- ```pip3 install 'django<4' gunicorn```
- ```pip3 install dj_database_url psycopg2``` 
  
1. Once you have installed any relevant dependencies or libraries, such as the ones listed above, it is important to create a **requirements.txt** file and add all installed libraries to it with the ```pip3 freeze --local > requirements.txt``` command in the terminal.  
2. Create a new Django project in the terminal ```django-admin startproject Button mashers .```
3. Create a new app eg. ```python3 mangage.py startapp home```
5. Add this to list of **INSTALLED_APPS** in **settings.py** - 'home',
6. Create a superuser for the project to allow Admin access and enter credentials: ```python3 manage.py createsuperuser```
7. Migrate the changes with commands: ```python3 manage.py migrate```
8. An **env.py** file must be created to store all protected data such as the **DATABASE_URL** and **SECRET_KEY**. These may be called upon in your project's **settings.py** file along with your Database configurations. The **env.py** file must be added to your **gitignore** file so that your important, protected information is not pushed to public viewing on GitHub. For adding to **env.py**:

- ```import os```
- ```os.environ["DATABASE_URL"]="<copiedURLfromElephantSQL>"```
- ```os.environ["SECRET_KEY"]="my_super^secret@key"```
  
For adding to **settings.py**:

- ```import os```
- ```import dj_database_url```
- ```if os.path.exists("env.py"):```
- ```import env```
- ```SECRET_KEY = os.environ.get('SECRET_KEY')``` (actual key hidden within env.py)  

9. Replace **DATABASES** with:

```
DATABASES = {
    'default': dj_database_url.parse(os.environ.get("DATABASE_URL"))
  }
```

10. Set up the templates directory in **settings.py**:

- Under ``BASE_DIR`` enter ``TEMPLATES_DIR = os.path.join(BASE_DIR, ‘templates’)``
- Update ``TEMPLATES = 'DIRS': [TEMPLATES_DIR]`` with:

```
os.path.join(BASE_DIR, 'templates'),
os.path.join(BASE_DIR, 'templates', 'allauth')
```

- Create the media, static and templates directories in the top level of the project file in the IDE workspace.

11. A **Procfile** must be created within the project repo for Heroku deployment with the following placed within it: ```web: gunicorn ecommerce.wsgi```
12. Make the necessary migrations again.

### Elephant SQL

A new database instance can be created on [Elephant SQL](https://www.elephantsql.com/) for your project. 

- Choose a name and select the **Tiny Turtle** plan, which is free.
- Select your Region and the nearest Data Center to you. 
- From your user dashboard, retrieve the important 'postgres://....' value. Place the value within your **DATABASE_URL**  in your **env.py** file and follow the below instructions to place it in your Heroku Config Vars.

## Heroku Deployment

To start the deployment process , please follow the below steps:

1. Log in to [Heroku](https://id.heroku.com/login) or create an account if you are a new user.
2. Once logged in, in the Heroku Dashboard, navigate to the '**New**' button in the top, right corner, and select '**Create New App**'.
3. Enter an app name and choose your region. Click '**Create App**'.
4. In the Deploy tab, click on the '**Settings**', reach the '**Config Vars**' section and click on '**Reveal Config Vars**'. Here you will enter KEY:VALUE pairs for the app to run successfully. The KEY:VALUE pairs that you will need are your:

   - **DATABASE_URL**:**postgres://...**
   - **DISABLE_COLLECTSTATIC** of value '1' (N.B Remove this Config Var before deployment),
   - **SECRET_KEY** and value  
   <!-- - **AWS_ACCESS_KEY** and value
   - **AWS_SECRET_ACCESS_KEY** and value
   - **EMAIL_HOST_PASS** and value
   - **EMAIL_HOST_USER** and value
   - **STRIPE_PUBLIC_KEY** and value
   - **STRIPE_SECRET_KEY** and value
   - **STRIPE_WH_SECRET** and value
   - **USE_AWS** and value -->

5. Add the Heroku host name into **ALLOWED_HOSTS** in your projects **settings.py file** -> ```['herokuappname', ‘localhost’, ‘8000 port url’].```
2. Once you are sure that you have set up the required files including your requirements.txt and Procfile, you have ensured that **DEBUG=False**, save your project, add the files, commit for initial deployment and push the data to GitHub.
3. Go to the '**Deploy**' tab and choose GitHub as the Deployment method.
4. Search for the repository name, select the branch that you would like to build from, and connect it via the '**Connect**' button.
5. Choose from '**Automatic**' or '**Manual**' deployment options, I chose the 'Manual' deployment method. Click '**Deploy Branch**'.
6.  Once the waiting period for the app to build has finished, click the '**View**' link to bring you to your newly deployed site. If you receive any errors, Heroku will display a reason in the app build log for you to investigate. **DISABLE_COLLECTSTATIC**  may be removed from the Config Vars once you have saved and pushed an image within your project.

<!-- ## Google Mail Setup

1. Setup a Gmail Account that will be used to hold and store the emails for your project.
2. Logged in, navigate to **Settings** -> **Other Google Account Settings** -> **Accounts** -> **Import** -> **Other Account Settings**
3. Activate 2-Step Verification
4. Once verified access **App Passwords** -> **Other** -> enter a name for the password, eg Button mashers.
5. Click **Create** -> copy the 16 digit password that is generated.
6. In your `settings.py` add the following Email Settings:
   ![django email settings](docs/readme_images/email_settings.png)  
   *Django Email Settings for Button mashers Email setup*  
7. Add EMAIL_HOST_PASS, EMAIL_HOST_USER variable, password and email address to your Heroku Config Vars -->
    
## AWS Config

[AWS](https://aws.amazon.com) is used to store the media and static files online for Button mashers. Please follow the below steps to set it up for yourself:

1. Setup AWS Account and Login
2. Create a new S3 Bucket -> name it to match your Heroku App name -> Choose the region closest to you.
3. Allow **Clock All Public Access**, tick 'Bucket will be public' in order for the bucket to connect to Heroku. 
4. In **Object Ownership** -> **ACLS Enabled** -> **Bucket Owner Preferred**.
5. **Properties** tab -> turn on static web hosting and add 'index.html' and 'error.html' into the correct fields -> click **Save**
6. In the **Permissions** tab, paste in the following CORS config:

   ```
	[
		{
			"AllowedHeaders": [
				"Authorization"
			],
			"AllowedMethods": [
				"GET"
			],
			"AllowedOrigins": [
				"*"
			],
			"ExposeHeaders": []
		}
	]
	```
7. Copy your **ARN** string.
8. From the **Bucket Policy** tab, select the **Policy Generator** link, and use the following steps:
	- Policy Type: **S3 Bucket Policy**
	- Effect: **Allow**
	- Principal: `*`
	- Actions: **GetObject**
	- Amazon Resource Name (ARN): **paste-your-ARN-here**
	- Click **Add Statement**
	- Click **Generate Policy**
	- Copy the entire Policy, and paste it into the **Bucket Policy Editor**

		```shell
		{
			"Id": "Policy1234567890",
			"Version": "2012-10-17",
			"Statement": [
				{
					"Sid": "Stmt1234567890",
					"Action": [
						"s3:GetObject"
					],
					"Effect": "Allow",
					"Resource": "arn:aws:s3:::bucket-name/*"
					"Principal": "*",
				}
			]
		}
		```
    - Before you click "Save", add `/*` to the end of the Resource key in the Bucket Policy Editor (like above).
	- Click **Save**.
9. In the **ACL - Access Control List** -> **Edit** -> enable **List** for **Everyone(Public Access)** -> Accept the warning.

### AWS - IAM setup

1. AWS Services Menu -> **Create New Group** -> add name eg. 'group-project-name'.
2. Navigate from there to **REview Policy** page -> **User Groups** -> Select newly named group.
3. Navigate to **Permissions** tab -> **Add Permissions** -> Click **Attach Policies**
4. Select policy -> **Add Permissions** at the bottom, click when finished.
5. From **JSON** tab -> select **Import Managed Policy** link -> search for **S3** -> select **Amazon3FullAccess** policy -> **Import**.
6. Copy **ARN** from S3 Bucket again ->

   ```
		{
			"Version": "2012-10-17",
			"Statement": [
				{
					"Effect": "Allow",
					"Action": "s3:*",
					"Resource": [
						"arn:aws:s3:::bucket-name",
						"arn:aws:s3:::bucket-name/*"
					]
				}
			]
		}
	```
7. Click **Review Policy** -> name eg. 'policy-Button mashers' -> enter a description -> **Create Policy**
8. Search for your new policy and click it to **Attach Policy**
9. **User Groups** -> **Add User** -> name eg. 'user-Button mashers'
10. For **Select AWS Access Type** -> select **Programmatic Access** -> Add group to 'user-Button mashers' -> **Review User** -> **Create User**.
11. Find **Download.csv** button to download immediately and save a copy.
    - This contains the user's **Access key ID** and **Secret access key**.
	- `AWS_ACCESS_KEY_ID` = **Access key ID**
	- `AWS_SECRET_ACCESS_KEY` = **Secret access key** 

### Media Folder Setup
1. In Heroku Config Vars, remove `DISABLE_COLLECTSTATIC`.
<!-- 2. In AWS S3 create a new folder -> **media** -> Add project images -> **Manage Public Permissions** -> **Grant public read access to the objects** -> **Upload** -->

## Clone Project

A local clone of this repository can be made on GitHub. Please follow the below steps:

1. Navigate to GitHub and log in.
2. The [Button mashers repository]() can be found at this location.
3. Above the repository file section, locate the '**Code**' button.
4. Click on this button and choose your clone method from HTTPS, SSH or GitHub CLI, copy the URL to your clipboard by clicking the '**Copy**' button.
5. Open your Git Bash Terminal.
6. Change the current working directory to the location you want the cloned directory to be made.
7. Type `git clone` and paste in the copied URL from step 4.
8. Press '**Enter**' for the local clone to be created.
9. Using the ``pip3 install -r requirements.txt`` command, the dependencies and libraries needed for FreeFido will be installed.
10. Set up your **env.py** file and from the above steps for ElephantSQL, gather the Elephant SQL url for addition to your code and add your SECRET_KEY and STRIPE/AWS keys if using these services.
11. Ensure that your **env.py** file is placed in your **.gitignore** file and follow the remaining steps in the above Django Project Setup section before pushing your code to GitHub.

## Fork Project

A copy of the original repository can be made through GitHub. Please follow the below steps to fork this repository:  

1. Navigate to GitHub and log in.  
2. Once logged in, navigate to this repository using this link [Button mashers Repository](https://github.com/amylour/Button mashers).
3. Above the repository file section and to the top, right of the page is the '**Fork**' button, click on this to make a fork of this repository.
4. You should now have access to a forked copy of this repository in your Github account.
5. Follow the above Django Project Steps if you wish to work on the project.

# Credits

## Code

The following blogs/tutorials complimented my learning for this project

## Media

Image credits are as follows:



### Additional reading/tutorials/books/blogs



## Acknowledgements

- A huge thanks to my wife Katie for her continued support during this project and bootcamp, through all tears for the many cups of coffee, the continued love and support. You are a blessing in my life 

- Much gratitude is extended to my subject matter expert Mark Briscoe, coding coach John Rearden and my personal facilitator Amy Richardson for their expert guidance and advice during this bootcamp, which gave me the confidence to make the most out of every project.

- Thank you to my fellow students and Code Institute alumni for their guidance and support.