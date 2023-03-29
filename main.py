import tkinter as tk
import openai

# Set your OpenAI API key
openai.api_key = "sk-wniXXXXXXXXXXXXXXXXXXXXXXXXXXXX"

# Set the ID of your fine-tuned model
print("Loading the fine-tuned model.....")
model_id = "ada:ft-personal-2023-XX-XX-XX-XX"
print("Completed loading the fine-tuned model")

# Create the GUI window
root = tk.Tk()
root.title("ChatGPT Fine-Tuned Model")

# Create the prompt entry field
prompt_label = tk.Label(root, text="Enter your prompt:")
prompt_label.pack()
prompt_entry = tk.Entry(root, width=50)
prompt_entry.pack()

# Define the submit function
def submit():
    # Get the prompt from the entry field
    prompt = prompt_entry.get()

    # Generate a response from the fine-tuned model
    response = openai.Completion.create(
        engine=model_id,
        prompt=prompt,
        max_tokens=250,
        n=1,
        stop=None,
        temperature=0.7
    )
    print(response)
    # Display the response in the text area
    response_text.delete("1.0", tk.END)
    response_text.insert(tk.END, response.choices[0].text)
    print(response_text)

# Create the submit button
submit_button = tk.Button(root, text="Submit", command=submit)
submit_button.pack()

# Create the text area for displaying the response
response_text = tk.Text(root, width=80, height=20)
response_text.pack()

# Run the GUI
root.mainloop()