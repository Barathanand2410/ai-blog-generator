# AI Blog Generator (Advanced)

## Overview
AI Blog Generator is an LLM-powered application that generates structured, SEO-friendly blog content based on user inputs such as topic, tone, and keywords.

This project demonstrates practical implementation of prompt engineering, user-controlled generation, and AI application development.

---

## Problem Statement
Creating high-quality, structured blogs manually is time-consuming and requires effort in formatting, tone adjustment, and SEO optimization.

---

## Solution
Developed an AI-powered tool that:
- Generates complete blogs instantly
- Adapts content based on tone and length
- Incorporates SEO keywords
- Provides downloadable output

---

## Features
- Blog topic input  
- Tone selection (Professional, Casual, Marketing)  
- Word limit control (200 / 500 / 800 words)  
- SEO keyword integration  
- Structured blog output:
  - Title  
  - Introduction  
  - Main sections  
  - Conclusion  
- Clean markdown formatting  
- Download generated blog as text file  
- Interactive UI using Streamlit  

---

## Tech Stack
- Python  
- Streamlit  
- Groq API (LLM)  

---

## How It Works
1. User enters blog topic  
2. Selects tone and word limit  
3. Adds optional SEO keywords  
4. Application sends structured prompt to LLM  
5. LLM generates formatted blog content  
6. Output is displayed and available for download  

---

## Installation & Setup

### 1. Clone Repository
git clone https://github.com/Barathanand2410/ai-blog-generator.git

### 2. Navigate to Project
cd ai-blog-generator

### 3. Install Dependencies
pip install -r requirements.txt

### 4. Run Application
python -m streamlit run app.py

---

## Sample Input
- Topic: AI in Healthcare  
- Tone: Professional  
- Word Limit: 500  
- Keywords: AI, healthcare, automation  

---

## Sample Output
- Well-structured blog with headings  
- SEO-friendly content  
- Clear and readable format  

---

## Key Learnings
- Prompt engineering for structured output  
- Building end-to-end LLM applications  
- Handling user input for dynamic generation  
- UI integration using Streamlit  
- Managing API-based applications  

---

## Future Enhancements
- Export as PDF  
- Multi-language support  
- Blog editing interface  
- History of generated blogs  

---

## Author
Barath – NLP / LLM Application Developer (Aspiring)
