abarnes.app Portfolio Website
This repository contains the source code for my personal portfolio website, abarnes.app. The site is designed to be a modern and responsive platform to showcase mobile applications I've developed. It features a general home page, dedicated pages for each app, and relevant information like privacy policies and contact details.

The entire site is built using static HTML and is styled with the utility-first framework Tailwind CSS for rapid and highly customizable development.

🛠️ Technology Stack
HTML: The core structure of all web pages.

Tailwind CSS: A utility-first CSS framework for fast, custom styling.

Node.js & npm: Used to manage dependencies and run the Tailwind CSS build process.

GitHub Pages: The hosting service used to deploy the static website.

🚀 Getting Started
Follow these steps to get a local copy of the project running.

Prerequisites
Node.js and npm installed on your machine.

Installation & Build
Clone the repository to your local machine:

Bash

git clone https://github.com/tempest918/abarnes.app.git
cd abarnes.app
Install the project dependencies (Tailwind CSS and PostCSS):

Bash

npm install
Run the Tailwind CSS build process with the --watch flag to compile the CSS automatically as you make changes:

Bash

npm exec -- tailwindcss -i ./input.css -o ./output.css --watch
You can now open any of the HTML files in your browser to view the website. Any changes you save to the HTML will be automatically reflected.

📂 Project Structure
abarnes.app/
├── index.html
├── contact.html
├── truck-loads-app.html
├── truck-loads-privacy.html
├── images/
│   └── appicon.png
├── node_modules/
├── output.css
├── input.css
├── package.json
├── tailwind.config.js
└── README.md
🌐 Hosting
This website is hosted for free using GitHub Pages. The main branch is configured to automatically deploy any changes made to the repository.
