# AI Smart Email Writer using Streamlit and Gemini API

## Overview

AI Smart Email Writer is a web application built using Python, Streamlit, and Google's Gemini AI model.
The application helps users generate professional emails, reply to emails, and create quick responses with adjustable tones.

Users can enter a prompt or email context, and the AI generates smart email content instantly.

---

## Features

* Generate professional emails
* Reply to emails automatically
* Tone adjustment support
* Quick email replies
* User-friendly Streamlit interface
* Powered by Gemini AI

---

## Technologies Used

* Python
* Streamlit
* Google Generative AI (Gemini API)

---

## Project Structure

```bash
AI-Email-Writer/
│
├── app.py
├── requirements.txt
└── README.md
```

---

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/AI-Email-Writer.git
```

### 2. Navigate to the Project Folder

```bash
cd AI-Email-Writer
```

### 3. Install Required Packages

```bash
pip install -r requirements.txt
```

---

## Required Packages

Create a `requirements.txt` file and add:

```txt
streamlit
google-generativeai
```

---

## API Key Setup

Get your Gemini API key from Google AI Studio:

https://aistudio.google.com/

Replace:

```python
gen.configure(api_key = "YOUR API KEY")
```

with your actual API key.

Example:

```python
gen.configure(api_key="AIzaSyXXXXXX")
```

---

## Application Code

```python
import streamlit as st
import google.generativeai as gen

gen.configure(api_key="YOUR API KEY")

model = gen.GenerativeModel("gemini-2.5-flash")

prompt = st.text_input("Answer any questions asked by the user")

if st.button("Submit"):
    res = model.generate_content(
        prompt + " you are a smart email writer.write or replay to email with tone adjustment and quick replies"
    )
    
    st.write(res.text)
```

---

## Run the Application

Use the following command:

```bash
streamlit run app.py
```

---

## Example Use Cases

* Professional email writing
* Business communication
* Leave request emails
* Interview reply emails
* Customer support responses
* Quick formal replies

---

## Future Enhancements

* Multiple email tone selection
* Copy-to-clipboard feature
* Email templates
* Download email as PDF
* Email history storage
* Dark mode UI

---

## Sample Output

The application can generate:

* Formal emails
* Friendly emails
* Professional replies
* Quick responses
* Tone-based email drafts

---

## Author

Arun

---

## License

This project is for educational purposes only.
