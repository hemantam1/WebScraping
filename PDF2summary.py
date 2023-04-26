# Task : PDF document into its summary
# Cyber security strategy of Australia is used as input PDF
#chatgpt api is used 
# Faced Issues: The whole document not able to process at single excution
# Solution: Need to split the document into many text files and determine summary of each text and
# finally combine all the summary results.
# Here only first 5 pages used from the PDF document which are having title page and content pages 


# Import required libraries
import PyPDF2

# Open the PDF file
with open('Australia_cybersecuritystrategy.pdf', mode='rb') as file:
    
    # Read the PDF file
    reader = PyPDF2.PdfReader(file)
    
    # Get the number of pages in the PDF file
    num_pages = len(reader.pages)
    
    # Extract text from each page of the PDF file
    text = ""
    for i in range(5):
        page = reader.pages[i]
        text += page.extract_text()

#print(text)
# Install the transformers library
# Import required libraries
from transformers import AutoTokenizer, AutoModelWithLMHead

# Load the GPT-3 model with 125M parameters
model_name = "EleutherAI/gpt-neo-125M"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelWithLMHead.from_pretrained(model_name)

# Example 1: Text generation
#prompt = "The quick brown fox"
#input_ids = tokenizer.encode(prompt, return_tensors="pt")
#output = model.generate(input_ids, max_length=50, do_sample=True)
#generated_text = tokenizer.decode(output[0], skip_special_tokens=True)
#print(generated_text)

# Example 2: Text summarization
#text = "The quick brown fox jumps over the lazy dog. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Proin ac augue nec felis volutpat luctus. Fusce sed ligula vel quam fermentum ultrices."
input_ids = tokenizer.encode(text, return_tensors="pt")
summary_ids = model.generate(input_ids, max_length=324, min_length=10, num_beams=2)
summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
print(summary)








