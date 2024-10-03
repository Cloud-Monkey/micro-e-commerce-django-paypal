![Button mashers logo](readme-images/logo-readme.png)


![Button mashers responsive screenshot](readme-images/Button-mashers-responsive-img.png)

## Introduction

View live site: [Button mashers](https://button-mashers-11120a298309.herokuapp.com/)

Our micro-ecommerce site caters to fighting game enthusiasts who build custom controllers. We sell high-quality arcade controller parts like buttons and joysticks. Our products are designed for reliability and performance, ensuring every punch, kick, and combo is spot-on. We offer a wide variety of colors and styles, allowing for creative and personalized designs.

For full Admin access to Django Admin panel with relevant sign-in credentials: [Button mashers Admin](https://button-mashers-11120a298309.herokuapp.com/admin/login/?next=/admin/)

## Table of Contents

- ![Button mashers logo](readme-images/logo-readme.png)
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
  - [User Stories](#user-stories)
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

From the outset of the Button Mashers project, I envisioned a vibrant color palette that reflects the energy of arcade gaming, with bold hues and striking contrasts to create an engaging visual experience. The website maintains a clean and organized layout, utilizing ample white space to draw attention to our products and enhance the overall user experience. This design approach not only highlights our extensive range of arcade components but also captures the dynamic spirit of the gaming community.

created using https://www.textstudio.com/logo 

A pixel art text header was chosen for the Button Mashers website to evoke a sense of nostalgia and excitement that resonates with the gaming community. 

This distinctive style not only captures the essence of classic arcade games but also enhances visual engagement, enhancing key sections of the site.

![Button mashers logo](/readme-images/logo-readme.png)

Product images showcase arcade components against a neutral background on box elements, allowing customers to clearly see details of buttons, joysticks, and other peripherals. The included buttons stand out allowing the user to clearly see options to add the product to their cart or view the product in detail.

![Product box item display](/readme-images/product-box-item.png)

The site's header dynamically updates to display the user's login status and the current number of items in their cart, providing visual feedback. Interactive notifications, appear after user actions to confirm operations or offer additional information.

![Nav bar screenshot](/readme-images/nav-bar-dynamic.png) ![Sign out message](/readme-images/sign-out-message.png)

### Color Scheme

Initial colour schemes were generated using http://colormind.io/image/

![Button mashers Color Scheme](/readme-images/colour-palette-img2.png)

Variables were used within the CSS file to call colours as they were needed:

- Fire-Brick: #9D3A3B;
- Space: #1F212A;
- Teal: #4D848A;
- Off-White: #F4F4F4;
- Gold: #C9A539;

The above colours were chosen to be vibrant and bold but also cohesive enough to work in unison and to aid in a clean simple and accessable design layout.

Compromises were made with Bootstrap components where colours, although similar enough to match the theme, did not exactly match, however design desicions were made based on the functionality of the component to ensure use case was clear.

### Typography & Iconography

In developing my full-stack Django site, I chose to utilize Bootstrap's default fonts to keep the project scope manageable. By leveraging these pre-designed fonts, I was able to maintain a consistent and professional aesthetic without the added complexity of custom typography. This decision not only streamlined the design process but also allowed me to focus on core functionalities and features, ensuring that I could deliver a high-quality user experience efficiently. Using Bootstrap's default fonts provided a solid foundation for my site's visual identity while simplifying development and enhancing overall productivity.

# Project Planning



## Strategy Plane

In developing my project, I adopted an Agile methodology for the strategy plane to ensure flexibility and responsiveness throughout the development process.

The primary goal of the site was to display products to customers, give them the ability to add items to heir cart when logged in/registered and complete a purchase. The functionality to review and rate products was also important to satisfy CRUD criteria on the project.

By breaking down the project into smaller, manageable tasks and prioritizing them based on effort and value, I was able to maintain a focused and iterative development cycle

The site's design and graphic assets were collected through various copyright-free image websites. Images were edited for the website to be cohesive. Bootstrap and Crispy Forms were used for the project's frontend to speed up the process and to keep the templates consistent. Additional customization for buttons, forms, modals, alerts, and user feedback processes has been incorporated into the project's CSS files.. 

### Site Goals

- Site provides enjoyable experience for shoppers.
- Site is clear and accessable.
- Customers feel informed that they are making a good choice of products with Button mashers.
- UX remains similar across screen sizes.
- CRUD functionalities work as intended with easy to use frontend forms.
- Scalable site to allow for extra features in the future (Paypal, build forums etc)

## Agile Methodologies

Button mashers followed Agile planning methodologies to its completion. [GitHub Projects](https://github.com/users/Cloud-Monkey/projects/5/views/1) provided an ideal platform to create issues, boards and milestones for each of the project's Epics. By utilizing labels, I was able to efficiently pinpoint my upcoming tasks and categorize them into the relevant Milestones and Sprints. Concentrating on specific components while developing Button Mashers helped minimize bugs and reduce the likelihood of human errors.

### MoSCoW Prioritization

I chose to follow the MoSCoW Prioritization method for Button mashers, identifying and labeling my:

**Must Haves** These are the essential, non-negotiable elements of the project. Implementing these 'Must Haves' was crucial in achieving the Minimum Viable Product (MVP) status for this initiative.

**Should Haves** While important and beneficial, these features are not critical for the initial MVP phase. 'Must Haves' take precedence over 'Should Haves' in terms of development priority.

**Could Haves** These represent additional enhancements that would augment the project. They're desirable but should only be pursued after addressing more critical components and if resources permit.

**Won't Haves** This category encompasses features that have been deprioritized or deemed unsuitable for the current project scope. These items are either no longer aligned with the project's objectives or are considered low-priority for the present release cycle.

## User Stories

User stories and features were recorded and managed on [GitHub Projects](https://github.com/users/Cloud-Monkey/projects/5/views/1)

## Scope Plane

To focus on the CRUD functionality of the project and learning the new framework of Django, I kept my Button mashers scope lower than some of my previous projects, A fully working e-commerce store was not essential, so I initially planned to keep to the MVP to ensure that I would complete the project successfully.

Features such as a gallery of projects built by customers, an about us page, footer with links, paypal integration were all planned for a future itteration.

Django's MVT framework allowed these features to be built quickly and addition of an Admin frontend panel for managing products and articles created a robust e-commerce site that could start taking orders once paypal is integrated.

Essential features were:
- User Accounts with AllAuth
- Reviews creation and management - Full CRUD
- Product inventory management for Admin - Full CRUD
- Shopping UX with Cart and Checkout processes - Full CRUD
- Site responsivity
    
## Structural Plane

Button mashers is built using Bootstrap and Django incorporating both Python and Javascript with Code Institute's Blog walkthrough as a foundation. I changed structures and styling to fit my own vision and had to add a lot of my own functionality to get cart and checkout features fully working.

A solid green 2px border is used for view buttons on products to replace bootstraps default styling and address contrast issues. Form validation has been left with it's original styling as no change was needed. Bootstrap allowed for easy transition between screen sizes as many ecommerce purchases are made using our mobiles, so this was a priority focus. Bootstrap components such as forms also gave an acceptable finish with minimal or no styling.

## Skeleton & Surface Planes

In the skeleton and surface planes of my project, I focused on creating an intuitive and visually appealing user interface that enhances the overall user experience. The skeleton plane involved carefully structuring the layout and navigation of the website, ensuring that users can easily find and interact with key features such as product listings, shopping cart, and user reviews. 

### Wireframes

[Scene.io](https://www.scene.io/) was used to create initial wireframes for Button mashers. I had a good understanding of what the site would look like and planning followed this initial outline. Although the scope was rolled back to a simple three page design during the iterative process.

![Wireframes](/readme-images/wireframe-img.png)

### Database Schema

<!-- ![Button mashers Eco Eco-Ecommerce ERD]()  
*Database Schema (ERD) for Button mashers displaying relationships between feature components saved within the database*

[Lucidchart](https://www.lucidchart.com/pages/) was used to create the ERD(Entity Relationship Diagram) for Button mashers. To satisfy the assessment criteria, multiple models were created to personalise the Button mashers project. These include:
- **Articles**: Articles may be added by Admin with image and text fields within the Add/Edit Article forms.
- **Order**: Carbon Footprint total and Carbon Saved Total have been added to the Boutique Ado Order model to handle the carbon total logic. This logic duplicates the product adding/updating/quantity logic within the bag contexts to allow for the carbon footprint to be calculated for products that had some form of data available to me to calculate approximate values.
- **Product**: Carbon Footprint and Carbon Saved have been added to the Boutique Ado Product model to handle the carbon total logic. The Admin can enter these values into the Product Management forms to be made available for the bag/checkout logic to process them.
- **Wishlist**: The Wishlist model takes simple values of the connected user and the product id to display the items in a list for the individual user.

Future Feature models are visible in the ERD for Reactions, Reviews and Discount Codes. These will be incorporated into the next version of Button mashers. At the moment they are beyond the MVP. -->

### Defensive Design

Button Mashers was designed to provide a dependable user experience, aiming to eliminate any frustrations for users and encouraging them to return for future purchases.

- Django AllAuth for user registration/log in/log out
- Input validation and error messages provide feedback to the user to guide them towards the desired outcome. 
- Unregistered users are diverted to the Sign Up page from restricted actions. 
- Authentication processes control edit/delete buttons to reveal them to the Admin only, this is further secured through accessing of CRUD functionalities in the Admin Dashboard. 
- Deletion of data is confirmed through a message, double-checking with the user.
- Testing and validation of features completes the process.

# Features

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
- [Figma](https://www.figma.com) for project design planning and wireframe creation.
- [Django](https://www.djangoproject.com/) was used as the Python framework for the site.
- [Heroku](https://www.heroku.com) was used to host the 'Button mashers' application.
- [WAVE](https://wave.webaim.org/) to evaluate the accessibility of the site.

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
- [Convertio](https://convertio.co/) for file conversion to PNG, WEBP.
- [Tiny Png](https://tinypng.com/) for file size reduction.
- [Lucidchart](https://www.lucidchart.com/pages) for ERD (entity relationship diagram) creation.
- [Favicon](https://favicon.io/) for converting an icon into a favicon.
- [amiresponsive](https://ui.dev/amiresponsive) for screenshot of Button mashers on different screen sizes.
- [Perplexity AI](https://www.perplexity.ai/) for breaking down Python concepts and Django documentation into more understandable chunks.

# Testing



# Deployment

## Connecting to GitHub  

To begin this project from scratch, you must first create a new GitHub repository using the [Code Institute's Template](https://github.com/Code-Institute-Org/ci-full-template). This template provides the relevant tools to get you started. To use this template:

1. Log in to [GitHub](https://github.com/) or create a new account.
2. Navigate to the above CI Full Template.
3. Click '**Use this template**' -> '**Create a new repository**'.
4. Choose a new repository name and click '**Create repository from template**'.
5. In your new repository space, click the gitpod open button to generate a new workspace.

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