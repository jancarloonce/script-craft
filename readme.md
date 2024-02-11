<div align="center">
<h1 align="center">
<br>ScriptCraft: Crafting Testimonial Video Ads Made Simple with OpenAI</h1>
<h3>◦ Developed with the software and tools below.</h3>
 


<p align="center">
<img src="https://img.shields.io/badge/GNU%20Bash-4EAA25.svg?style=flat-square&logo=GNU-Bash&logoColor=white" alt="GNU%20Bash" />
<img src="https://img.shields.io/badge/tqdm-FFC107.svg?style=flat-square&logo=tqdm&logoColor=black" alt="tqdm" />
<img src="https://img.shields.io/badge/JavaScript-F7DF1E.svg?style=flat-square&logo=JavaScript&logoColor=black" alt="JavaScript" />
<img src="https://img.shields.io/badge/HTML5-E34F26.svg?style=flat-square&logo=HTML5&logoColor=white" alt="HTML5" />
<img src="https://img.shields.io/badge/Jinja-B41717.svg?style=flat-square&logo=Jinja&logoColor=white" alt="Jinja" />
<img src="https://img.shields.io/badge/Jinja-B41717.svg?style=flat-square&logo=Jinja&logoColor=white" alt="Jinja" />
<img src="https://img.shields.io/badge/C-A8B9CC.svg?style=flat-square&logo=C&logoColor=black" alt="C" />

<img src="https://img.shields.io/badge/Poetry-60A5FA.svg?style=flat-square&logo=Poetry&logoColor=white" alt="Poetry" />
<img src="https://img.shields.io/badge/OpenAI-412991.svg?style=flat-square&logo=OpenAI&logoColor=white" alt="OpenAI" />
<img src="https://img.shields.io/badge/Python-3776AB.svg?style=flat-square&logo=Python&logoColor=white" alt="Python" />
<img src="https://img.shields.io/badge/AIOHTTP-2C5BB4.svg?style=flat-square&logo=AIOHTTP&logoColor=white" alt="AIOHTTP" />
<img src="https://img.shields.io/badge/JSON-000000.svg?style=flat-square&logo=JSON&logoColor=white" alt="JSON" />
<img src="https://img.shields.io/badge/Flask-000000.svg?style=flat-square&logo=Flask&logoColor=white" alt="Flask" />
</p>
<img src="https://img.shields.io/github/license/jancarloonce/script-craft?style=flat-square&color=5D6D7E" alt="GitHub license" />
<img src="https://img.shields.io/github/last-commit/jancarloonce/script-craft?style=flat-square&color=5D6D7E" alt="git-last-commit" />
<img src="https://img.shields.io/github/commit-activity/m/jancarloonce/script-craft?style=flat-square&color=5D6D7E" alt="GitHub commit activity" />
<img src="https://img.shields.io/github/languages/top/jancarloonce/script-craft?style=flat-square&color=5D6D7E" alt="GitHub top language" />
</div>

---

## 📖 Table of Contents
- [📖 Table of Contents](#-table-of-contents)
- [📍 Overview](#-overview)
- [📦 Features](#-features)
- [📂 repository Structure](#-repository-structure)
- [🚀 Getting Started](#-getting-started)
    - [🔧 Installation](#-installation)
    - [🤖 Running script-craft](#-running-script-craft)


---


## 📍 Overview

ScriptCraft is a web application that simplifies the creation of testimonial video ads using the power of OpenAI's GPT-3 API. Built with Flask and designed for ease of use, ScriptCraft provides users with a user-friendly interface to input product information. Leveraging the capabilities of OpenAI's GPT-3, the application dynamically generates three script ideas for a testimonial video ad based on the provided product details.

---

## 📦 Features

1. User-Friendly Interface: The app features a clean and intuitive interface that allows users to easily input product information through a form.

2. Dynamic Script Generation: Upon form submission, the app sends the product details to the OpenAI GPT-3 API, which dynamically generates three script ideas for a testimonial video ad.

3. Responsive Design: The app is designed to be responsive, ensuring a seamless experience across various devices, including desktops, tablets, and mobile phones.

4. Separation of Concerns: The code follows best practices, with separation of concerns between the Flask application, HTML templates, and static CSS files for easy maintenance and scalability.

---


## 📂 Repository Structure

```sh
└── script-craft/
    ├── .replit
    ├── main.py
    ├── poetry.lock
    ├── pyproject.toml
    ├── replit_zip_error_log.txt
    ├── requirements.txt
    └── static/
        ├── index.css
        └── result.css
        └── script.js
    └── templates/
        ├── index.html
        └── result.html

```


## 🚀 Getting Started

***Dependencies***

Please ensure you have the following dependencies installed on your system:

`Openai`

`Flask`

### 🔧 Installation

1. Change to the project directory:
```sh
cd script-craft
```

2. Install the dependencies:
```sh
pip install -r requirements.txt
```

### 🤖 Running script-craft

```sh
python main.py
```

