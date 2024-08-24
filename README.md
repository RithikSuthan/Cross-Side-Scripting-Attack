# Flask XSS Vulnerability Demonstration

This project demonstrates a Cross-Site Scripting (XSS) vulnerability in a simple Flask web application. The application features a blog post where users can submit comments. Due to the lack of proper input sanitization, the application is vulnerable to XSS attacks, showcasing the importance of securing web applications against such vulnerabilities.

## About the Project

This project is designed to demonstrate how a lack of input sanitization can lead to Cross-Site Scripting (XSS) vulnerabilities. The application allows users to post comments on a blog post. However, because the comments are rendered without escaping HTML, any JavaScript code included in the comments will be executed in the browser, leading to potential security breaches.

## Technologies Used

- **Python**: Programming language
- **Flask**: A lightweight WSGI web application framework
- **HTML/CSS**: For structuring and styling the web page

## Setup and Installation

Follow these steps to set up and run the project locally:

1. **Clone the repository**:

   ```bash
   git clone https://github.com/RithikSuthan/Cross-Side-Scripting-Attack.git
   cd Cross-Side-Scripting-Attack

2 .**Follow the given steps**:
python -m venv myenv
myenv\Scripts\activate
pip install -r requirements.txt
python main.py

![image](https://github.com/user-attachments/assets/c76c8dda-65d5-463b-b565-9b7aed9a078c)

