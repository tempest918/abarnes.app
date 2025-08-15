# abarnes.app Portfolio Website

This repository contains the source code for my personal portfolio website, `abarnes.app`. The site is designed to be a modern and responsive platform to showcase mobile applications I've developed. It features a general home page, dedicated pages for each app, and relevant information like privacy policies and contact details.

The entire site is built using static HTML and is styled with the utility-first framework **Tailwind CSS** for rapid and highly customizable development.

---

## Repository Description

A clean, modern, and responsive portfolio website built with HTML and Tailwind CSS to showcase mobile applications.

---

## 🛠️ Technology Stack

* **HTML:** The core structure of all web pages.
* **Tailwind CSS:** A utility-first CSS framework for fast, custom styling.
* **Node.js & npm:** Used to manage dependencies and run the Tailwind CSS build process.
* **GitHub Pages:** The hosting service used to deploy the static website.

---

## 🚀 Getting Started

Follow these steps to get a local copy of the project running.

### Prerequisites

* **Node.js** and **npm** installed on your machine.

### Installation & Build

1.  Clone the repository to your local machine:
    ```bash
    git clone [https://github.com/tempest918/abarnes.app.git](https://github.com/tempest918/abarnes.app.git)
    cd abarnes.app
    ```
2.  Install the project dependencies (Tailwind CSS, PostCSS, and Autoprefixer):
    ```bash
    npm install -D tailwindcss@3 postcss autoprefixer
    ```
3.  Initialize Tailwind CSS configuration files (`tailwind.config.js` and `postcss.config.js`):
    ```bash
    npx tailwindcss init -p
    ```
    **Note:** If `npx` encounters issues, try `npm exec -- tailwindcss init -p`.
4.  Open `tailwind.config.js` and configure the `content` array to scan your HTML files:
    ```javascript
    /** @type {import('tailwindcss').Config} */
    module.exports = {
      content: [
        "./*.html", // Scans all HTML files in the root directory
      ],
      theme: {
        extend: {
          fontFamily: {
            sans: ['Inter', 'sans-serif'],
            heading: ['Poppins', 'sans-serif'],
          },
        },
      },
      plugins: [],
    }
    ```
5.  Create an input CSS file named `input.css` in your project's root and add the following Tailwind directives:
    ```css
    @tailwind base;
    @tailwind components;
    @tailwind utilities;
    ```
6.  Start the Tailwind CSS build process. This command will watch for changes in your HTML and generate the `output.css` file:
    ```bash
    npx tailwindcss -i ./input.css -o ./output.css --watch
    ```
    Keep this command running in your terminal while developing.
7.  Update your HTML files (`index.html`, `truck-loads-app.html`, `contact.html`, `truck-loads-privacy.html`) to link to the generated `output.css` file. Replace the old CDN link with:
    ```html
    <link href="./output.css" rel="stylesheet">
    ```

You can now open any of the HTML files directly in your browser to view the website. Any changes you save to the HTML will be automatically reflected by the running build process.

---

## 📂 Project Structure
