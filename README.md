# TEXT SUMMARIZATION TOOL

*COMPANY*: CODTECH IT SOLUTIONS

*NAME*: ABHISHEK SINGH RAJPUT

*INTERN ID*: CT04DG3397

*DOMAIN*: ARTIFICIAL INTELLIGENCE

*DURATION*: 4 WEEKS

*MENTOR*: NEELA SANTOSH

#  Text Summarization Tool

## Overview

The **Text Summarization Tool** is a simple yet effective Python-based application that uses state-of-the-art Natural Language Processing (NLP) techniques to generate concise summaries of long passages of text. This tool is built using Hugging Face's Transformers library and utilizes the pre-trained `t5-small` model to perform extractive and abstractive summarization of user-provided input.

This project demonstrates the core concept of how machines can reduce lengthy articles or passages into brief, meaningful summaries — a technique that has broad use cases in news aggregation, education, legal review, academic research, and document automation. It allows users to interact with the model directly through the command line and summarize any English text they input manually.


##  Features

*  Summarizes long texts in a clear, coherent format
*  Uses Hugging Face’s pre-trained `t5-small` model for quick results
*  Adjusts summary length automatically based on input size
*  Built with modern NLP (Natural Language Processing) principles
*  Accepts user input from the terminal interactively (no GUI)
*  No need for internet connection after initial model download
*  Light-weight, CPU-compatible (no GPU required)


##  Technologies Used

* **Python 3.10+**
* **Transformers** (by Hugging Face)
* **PyTorch** (CPU-compatible)
* **Textwrap** (for readable output formatting)


##  How It Works

Once the script is executed, the user is prompted to enter text into the terminal. You can either type or paste content into the terminal. After hitting **Enter twice**, the tool processes your input using the `t5-small` model and generates a summarized version of it.

Unlike extractive summarization (which pulls key sentences), this tool performs **abstractive summarization**—rewriting the key information in new language, closer to how humans summarize.

 **Note**: Input should not exceed the model's capacity. Currently, the maximum input size is approximately **256 words** due to the model's token limit. This limit is imposed by the design of the `t5-small` model and is not a script limitation.


##  Folder Structure

```
TEXT SUMMARIZATION TOOL/
│
├── text_summarizer.py        # Main Python script
├── sample.txt (optional)     # Sample input file (not required for execution)
├── README.md                 # Project documentation
```

##  Installation & Setup

1. **Clone this repository**:

   ```bash
   git clone https://github.com/yourusername/text-summarization-tool.git
   cd text-summarization-tool
   ```

2. **Install dependencies**:

   ```bash
   pip install transformers torch
   ```

3. **Run the script**:

   ```bash
   python text_summarizer.py
   ```

## Example

### Sample Input (entered manually):

```
Immunity is concerned with resistance to infection. Immunity means the ability of an organism to recognize and defend itself against infectious agents or foreign material. To protect ourselves, the human body has a defense mechanism that resists pathogens and their toxic products. This resistance forms the basis of the subject known as immunology.
```

### Output:

```
immunity is concerned with resistance to infection. the human body resists the invasion of pathogens and their toxic products.
```

##  Known Limitations

*  **Input Limit**: Due to `t5-small` model limits, text longer than \~256 words may be truncated or lead to incomplete summaries.
*  **Copy-Paste Issue**: On some systems (especially Windows PowerShell), pasting large blocks of text may lead to execution errors. It's recommended to **type or paste smaller chunks manually**.
*  **Sample File Usage**: Although a sample file may be provided, the summarizer does **not require or load any external file**. It's kept for reference and testing only.

##  Final Notes

This tool offers a minimal yet effective approach to summarization using modern NLP. It is built to be used by students, educators, and researchers who want a lightweight, offline, and easy-to-use summarization option from the command line.

If you're looking to extend the tool in the future, you could explore:

* Web-based UI with Streamlit or Flask
* Support for summarizing from `.txt` or `.pdf` files
* Using larger models like `t5-base` or `bart-large` for better summaries (with GPU support)

#OUTPUT


<img width="1853" height="827" alt="Image" src="https://github.com/user-attachments/assets/54106855-ff1a-4461-b5d0-c46e06618a6d" />
