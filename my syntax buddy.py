# Python Syntax Reference Application with Tkinter GUI, Search, Highlighting, Run, Dark/Light Mode, Descriptions, Python, HTML, CSS Categories with Webbrowser Previews

import tkinter as tk
from tkinter import scrolledtext, messagebox
import re
import webbrowser
import tempfile
import os

# Syntax data dictionary with "Python," "HTML," and "CSS" categories
syntax_data = {
    "Python": {
        "Variable Assignment": {
            "syntax": "variable_name = value",
            "example": "x = 10  # Assigns 10 to x\nname = 'Alice'",
            "description": "Used to store data in a named container for later use or manipulation in the program."
        },
        "Integer": {
            "syntax": "variable = int_value",
            "example": "age = 25  # Integer value",
            "description": "Represents whole numbers, useful for counting or performing arithmetic operations."
        },
        "String": {
            "syntax": "variable = 'text' or \"text\"",
            "example": "greeting = 'Hello'\ngreeting = \"Hi\"",
            "description": "Stores text data, such as names or messages, for display or processing."
        },
        "List": {
            "syntax": "variable = [item1, item2, ...]",
            "example": "fruits = ['apple', 'banana', 'orange']",
            "description": "Holds an ordered, mutable collection of items, ideal for managing multiple values."
        },
        "If Statement": {
            "syntax": "if condition:\n    statement",
            "example": "x = 10\nif x > 5:\n    print('x is greater than 5')",
            "description": "Executes code conditionally based on whether a condition is true, enabling decision-making."
        },
        "For Loop": {
            "syntax": "for item in iterable:\n    statement",
            "example": "for i in range(3):\n    print(i)",
            "description": "Iterates over a sequence (like a list or range), useful for repetitive tasks."
        },
        "While Loop": {
            "syntax": "while condition:\n    statement",
            "example": "count = 0\nwhile count < 3:\n    print(count)\n    count += 1",
            "description": "Repeats code as long as a condition remains true, good for dynamic looping."
        },
        "Function Definition": {
            "syntax": "def function_name(parameters):\n    statement\n    return value",
            "example": "def add(a, b):\n    return a + b\nresult = add(3, 4)",
            "description": "Defines reusable code blocks to perform specific tasks, improving modularity."
        },
        "Lambda Function": {
            "syntax": "lambda arguments: expression",
            "example": "double = lambda x: x * 2\nprint(double(5))",
            "description": "Creates small, anonymous functions for quick, one-off operations."
        },
        "Class Definition": {
            "syntax": "class ClassName:\n    def __init__(self, parameters):\n        self.attribute = value",
            "example": "class Dog:\n    def __init__(self, name):\n        self.name = name\nmy_dog = Dog('Rex')\nprint(my_dog.name)",
            "description": "Defines a blueprint for objects, enabling object-oriented programming."
        },
        "Method": {
            "syntax": "def method_name(self, parameters):\n    statement",
            "example": "class Dog:\n    def bark(self):\n        print('Woof!')\nmy_dog = Dog()\nmy_dog.bark()",
            "description": "Adds behavior to classes, allowing objects to perform actions."
        },
        "Try-Except": {
            "syntax": "try:\n    statement\nexcept ExceptionType:\n    statement",
            "example": "try:\n    x = 1 / 0\nexcept ZeroDivisionError:\n    print('Cannot divide by zero')",
            "description": "Handles errors gracefully, preventing program crashes."
        },
        "Open File": {
            "syntax": "with open('file.txt', 'r') as f:\n    statement",
            "example": "with open('data.txt', 'r') as f:\n    print(f.read())",
            "description": "Reads or writes file contents safely, ensuring the file is properly closed."
        },
        "Import": {
            "syntax": "import module_name",
            "example": "import math\nprint(math.pi)",
            "description": "Accesses external libraries or modules to extend functionality."
        }
    },
    "HTML": {
        "Basic Tag": {
            "syntax": "<tag>content</tag>",
            "example": "<p>This is a paragraph</p>",
            "description": "Defines the structure and content of a webpage, marking up text or elements."
        },
        "Attribute": {
            "syntax": "<tag attribute=\"value\">content</tag>",
            "example": "<a href=\"https://example.com\">Link</a>",
            "description": "Adds properties or behaviors to HTML tags, such as links or styling."
        },
        "Heading": {
            "syntax": "<h1> to <h6>content</h1> to </h6>",
            "example": "<h1>Main Title</h1>\n<h2>Subtitle</h2>",
            "description": "Creates hierarchical headings to organize content and improve readability."
        },
        "Image": {
            "syntax": "<img src=\"image.jpg\" alt=\"description\">",
            "example": "<img src=\"https://via.placeholder.com/150\" alt=\"A placeholder image\">",
            "description": "Embeds images in a webpage, with alt text for accessibility."
        },
        "List (Unordered)": {
            "syntax": "<ul>\n    <li>item</li>\n</ul>",
            "example": "<ul>\n    <li>Apple</li>\n    <li>Banana</li>\n</ul>",
            "description": "Creates a bulleted list for unordered items, useful for grouping related content."
        },
        "Division": {
            "syntax": "<div>content</div>",
            "example": "<div>\n    <h1>Title</h1>\n    <p>Text</p>\n</div>",
            "description": "Groups related content or elements together for styling or layout purposes."
        },
        "Form": {
            "syntax": "<form action=\"url\" method=\"method\">\n    content\n</form>",
            "example": "<form action=\"/submit\" method=\"post\">\n    <input type=\"text\" name=\"username\">\n    <button>Submit</button>\n</form>",
            "description": "Collects user input, typically for sending data to a server."
        },
        "Input": {
            "syntax": "<input type=\"type\" name=\"name\">",
            "example": "<input type=\"text\" name=\"email\" placeholder=\"Enter email\">",
            "description": "Creates interactive fields for user input, like text boxes or buttons."
        },
        "Link": {
            "syntax": "<a href=\"url\">content</a>",
            "example": "<a href=\"https://example.com\" target=\"_blank\">Visit Example</a>",
            "description": "Creates hyperlinks to navigate between pages or resources."
        },
        "Table": {
            "syntax": "<table>\n    <tr>\n        <th>header</th>\n        <td>data</td>\n    </tr>\n</table>",
            "example": "<table>\n    <tr>\n        <th>Name</th>\n        <th>Age</th>\n    </tr>\n    <tr>\n        <td>Alice</td>\n        <td>25</td>\n    </tr>\n</table>",
            "description": "Displays data in a tabular format with rows and columns."
        },
        "List (Ordered)": {
            "syntax": "<ol>\n    <li>item</li>\n</ol>",
            "example": "<ol>\n    <li>First</li>\n    <li>Second</li>\n</ol>",
            "description": "Creates a numbered list for ordered items, useful for steps or rankings."
        },
        "Meta Tags": {
            "syntax": "<meta name=\"name\" content=\"value\">",
            "example": "<meta name=\"description\" content=\"A sample webpage\">\n<meta charset=\"UTF-8\">",
            "description": "Provides metadata about the webpage, like character encoding or SEO details."
        },
        "Script Tag": {
            "syntax": "<script>script content</script> or <script src=\"script.js\"></script>",
            "example": "<script>\n    alert('Hello from HTML!');\n</script>",
            "description": "Embeds or links to JavaScript code to add interactivity to the webpage."
        },
        "Style Tag": {
            "syntax": "<style>css rules</style>",
            "example": "<style>\n    body { background-color: lightblue; }\n    p { color: red; }\n</style>",
            "description": "Defines inline CSS to style HTML elements directly within the page."
        }
    },
    "CSS": {
        "Selector (Element)": {
            "syntax": "element { property: value; }",
            "example": "p { color: blue; }",
            "description": "Targets all instances of an HTML element to apply styles universally."
        },
        "Selector (Class)": {
            "syntax": ".class { property: value; }",
            "example": ".highlight { background-color: yellow; }",
            "description": "Targets elements with a specific class for reusable styling."
        },
        "Selector (ID)": {
            "syntax": "#id { property: value; }",
            "example": "#header { font-size: 24px; }",
            "description": "Targets a unique element by its ID for specific styling."
        },
        "Color": {
            "syntax": "element { color: value; }",
            "example": "h1 { color: #ff0000; }",
            "description": "Sets the text color of an element, enhancing visual appeal."
        },
        "Background": {
            "syntax": "element { background: value; }",
            "example": "body { background: lightgray url('https://via.placeholder.com/150') no-repeat center; }",
            "description": "Defines the background (color, image, etc.) of an element for design customization."
        },
        "Font Size": {
            "syntax": "element { font-size: value; }",
            "example": "p { font-size: 16px; }",
            "description": "Adjusts the size of text to improve readability or emphasis."
        },
        "Margin": {
            "syntax": "element { margin: value; }",
            "example": "div { margin: 10px 20px; }",
            "description": "Sets the outer spacing around an element to control layout."
        },
        "Padding": {
            "syntax": "element { padding: value; }",
            "example": ".box { padding: 15px; }",
            "description": "Sets the inner spacing within an element to adjust content placement."
        },
        "Border": {
            "syntax": "element { border: width style color; }",
            "example": "table { border: 1px solid black; }",
            "description": "Adds a border around an element for visual separation or decoration."
        },
        "Display": {
            "syntax": "element { display: value; }",
            "example": ".inline { display: inline-block; }",
            "description": "Controls the layout behavior of an element (e.g., block, inline, none)."
        },
        "Flexbox": {
            "syntax": "element { display: flex; property: value; }",
            "example": ".container { display: flex; justify-content: space-between; }",
            "description": "Creates a flexible layout for arranging items in a container efficiently."
        },
        "Position": {
            "syntax": "element { position: value; top/right/bottom/left: value; }",
            "example": ".fixed { position: fixed; top: 10px; right: 10px; }",
            "description": "Controls the positioning of an element (e.g., absolute, relative, fixed)."
        },
        "Grid": {
            "syntax": "element { display: grid; grid-template-columns: value; }",
            "example": ".grid { display: grid; grid-template-columns: 1fr 1fr 1fr; }",
            "description": "Creates a grid layout for precise control over rows and columns."
        },
        "Transition": {
            "syntax": "element { transition: property duration timing-function; }",
            "example": "button { transition: background-color 0.3s ease; }\nbutton:hover { background-color: blue; }",
            "description": "Adds smooth transitions to property changes for interactive effects."
        },
        "Media Query": {
            "syntax": "@media (condition) { element { property: value; } }",
            "example": "@media (max-width: 600px) { body { font-size: 14px; } }",
            "description": "Applies styles based on device characteristics, enabling responsive design."
        }
    }
}

# Color schemes
themes = {
    "light": {
        "bg": "#f0f0f0", "fg": "black", "button_bg": "#e0e0e0", "button_fg": "black",
        "text_bg": "white", "text_fg": "black", "keyword": "blue", "comment": "green", "string": "orange",
        "description": "green"
    },
    "dark": {
        "bg": "#2b2b2b", "fg": "white", "button_bg": "#4a4a4a", "button_fg": "white",
        "text_bg": "#1e1e1e", "text_fg": "white", "keyword": "#569cd6", "comment": "#6a9955", "string": "#ce9178",
        "description": "#2ecc71"
    }
}

current_theme = "light"
sub_frame = None  # To track the sub-button frame

# Function to apply syntax highlighting
def highlight_syntax(text_widget, content):
    text_widget.delete(1.0, tk.END)
    text_widget.insert(tk.END, content)
    
    text_widget.tag_configure("keyword", foreground=themes[current_theme]["keyword"])
    text_widget.tag_configure("comment", foreground=themes[current_theme]["comment"])
    text_widget.tag_configure("string", foreground=themes[current_theme]["string"])
    text_widget.tag_configure("description", foreground=themes[current_theme]["description"])

    keywords = ["if", "for", "while", "def", "class", "try", "except", "with", "import", "return", "lambda", "as", "self"]
    for keyword in keywords:
        start = "1.0"
        while True:
            pos = text_widget.search(keyword, start, stopindex=tk.END)
            if not pos:
                break
            end = f"{pos}+{len(keyword)}c"
            text_widget.tag_add("keyword", pos, end)
            start = end

    start = "1.0"
    while True:
        pos = text_widget.search("#", start, stopindex=tk.END)
        if not pos:
            break
        end = text_widget.search("\n", pos, stopindex=tk.END) or tk.END
        text_widget.tag_add("comment", pos, end)
        start = end

    for quote in ["'", '"']:
        start = "1.0"
        while True:
            pos = text_widget.search(quote, start, stopindex=tk.END)
            if not pos:
                break
            end = text_widget.search(quote, f"{pos}+1c", stopindex=tk.END)
            if not end:
                end = tk.END
            else:
                end = f"{end}+1c"
            text_widget.tag_add("string", pos, end)
            start = end

    start = "1.0"
    while True:
        pos = text_widget.search("Why Use:", start, stopindex=tk.END)
        if not pos:
            break
        desc_start = f"{pos}+9c"
        desc_end = text_widget.search("\n\n", desc_start, stopindex=tk.END) or tk.END
        if desc_end != tk.END:
            desc_end = f"{desc_end}+1c"
        text_widget.tag_add("description", desc_start, desc_end)
        start = desc_end

# Function to go back to main view
def go_back():
    global sub_frame
    if sub_frame:
        sub_frame.destroy()
        sub_frame = None
    text_area.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=10, pady=10)
    run_button.pack(side=tk.BOTTOM, pady=5)
    highlight_syntax(text_area, "Welcome to the Syntax Reference Tool!\n\nClick 'Python', 'HTML', or 'CSS' to explore syntax or use the search bar.\n")
    run_button.config(state="disabled")

# Function to show sub-buttons for a category
def show_sub_buttons(category):
    global sub_frame
    if sub_frame:
        sub_frame.destroy()
    
    text_area.pack_forget()
    run_button.pack_forget()
    
    sub_frame = tk.Frame(root, bg=themes[current_theme]["bg"])
    sub_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=10, pady=10)
    
    tk.Label(sub_frame, text=f"{category} Syntax:", font=("Arial", 14, "bold"), 
             bg=themes[current_theme]["bg"], fg=themes[current_theme]["fg"]).pack(pady=5)
    
    for item in syntax_data[category].keys():
        btn = tk.Button(sub_frame, text=item, font=("Arial", 12), 
                        command=lambda i=item: show_sub_syntax(category, i), anchor="w", width=30,
                        bg=themes[current_theme]["button_bg"], fg=themes[current_theme]["button_fg"])
        btn.pack(pady=2)
    
    back_btn = tk.Button(sub_frame, text="Back", font=("Arial", 12), command=go_back,
                         bg=themes[current_theme]["button_bg"], fg=themes[current_theme]["button_fg"])
    back_btn.pack(pady=10)

# Function to show syntax for a sub-item
def show_sub_syntax(category, item):
    global sub_frame
    if sub_frame:
        sub_frame.destroy()
        sub_frame = None
    
    text_area.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=10, pady=10)
    run_button.pack(side=tk.BOTTOM, pady=5)
    
    details = syntax_data[category][item]
    output = f"--- {item} ---\n\n"
    output += f"  Syntax: {details['syntax']}\n"
    output += f"  Example: {details['example']}\n"
    output += f"  Why Use: {details['description']}\n"
    highlight_syntax(text_area, output)
    run_button.config(state="normal")  # Enable for all categories

# Function to display syntax for categories
def show_syntax(category):
    show_sub_buttons(category)

# Function to search syntax
def search_syntax():
    if sub_frame:
        sub_frame.destroy()
        sub_frame = None
    text_area.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=10, pady=10)
    run_button.pack(side=tk.BOTTOM, pady=5)
    
    keyword = search_entry.get().strip().lower()
    if not keyword:
        messagebox.showwarning("Warning", "Please enter a keyword to search.")
        return
    
    results = ""
    found = False
    for category, items in syntax_data.items():
        for item, details in items.items():
            if (keyword in item.lower() or 
                keyword in details["syntax"].lower() or 
                keyword in details["example"].lower() or 
                keyword in details["description"].lower()):
                results += f"--- {category}: {item} ---\n"
                results += f"  Syntax: {details['syntax']}\n"
                results += f"  Example: {details['example']}\n"
                results += f"  Why Use: {details['description']}\n\n"
                found = True
    
    if found:
        highlight_syntax(text_area, results)
        run_button.config(state="disabled")
    else:
        text_area.delete(1.0, tk.END)
        text_area.insert(tk.END, f"No results found for '{keyword}'.\n")
        run_button.config(state="disabled")

# Function to run example code or preview HTML/CSS in browser
def run_example():
    current_text = text_area.get(1.0, tk.END).strip()
    if not current_text.startswith("---"):
        messagebox.showwarning("Warning", "Please select a syntax item to run or preview its example.")
        return
    
    header = current_text.split("---")[1].split("---")[0].strip()
    if ": " in header:
        category, item = header.split(": ", 1)
    else:
        category = "Python"  # Default to Python if no category prefix
        item = header
    
    example = syntax_data[category][item]["example"]
    
    if category == "Python":
        output = ""
        safe_globals = {"__builtins__": {}}  # Restrict built-ins
        safe_locals = {}
        try:
            code = re.sub(r"# Output:.*$", "", example, flags=re.MULTILINE).strip()
            exec(code, safe_globals, safe_locals)
            if "print" in code:
                output += f"Output from {example.splitlines()[0]}:\n"
                for line in code.splitlines():
                    if "print(" in line:
                        var = line.split("print(")[1].rstrip(")")
                        if var in safe_locals:
                            output += f"{safe_locals[var]}\n"
                        else:
                            output += "Output captured\n"
            if output:
                messagebox.showinfo("Run Output", output)
            else:
                messagebox.showinfo("Run Output", "Example executed successfully (no output).")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to run example: {str(e)}")
    elif category in ["HTML", "CSS"]:
        # Create a temporary HTML file for preview
        if category == "HTML":
            full_content = f"""
            <!DOCTYPE html>
            <html>
            <head>
                <title>HTML Preview: {item}</title>
            </head>
            <body>
                {example}
            </body>
            </html>
            """
        else:  # CSS
            full_content = f"""
            <!DOCTYPE html>
            <html>
            <head>
                <title>CSS Preview: {item}</title>
                <style>{example}</style>
            </head>
            <body>
                <div class="container">
                    <h1>Sample Heading</h1>
                    <p>This is a sample paragraph to demonstrate CSS styling.</p>
                    <button>Hover Me</button>
                </div>
            </body>
            </html>
            """
        
        # Write to a temporary file
        with tempfile.NamedTemporaryFile(mode='w', suffix='.html', delete=False) as temp_file:
            temp_file.write(full_content)
            temp_file_path = temp_file.name
        
        # Open in default browser
        try:
            webbrowser.open(f"file://{temp_file_path}")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to open preview: {str(e)}")
            # Clean up if opening fails
            os.remove(temp_file_path)
        # Note: File will persist until manually deleted or system cleanup; could add cleanup logic if needed

# Function to toggle theme
def toggle_theme():
    global current_theme
    current_theme = "dark" if current_theme == "light" else "light"
    theme = themes[current_theme]
    
    root.configure(bg=theme["bg"])
    search_frame.configure(bg=theme["bg"])
    category_frame.configure(bg=theme["bg"])
    if sub_frame:
        sub_frame.configure(bg=theme["bg"])
    
    search_label.configure(bg=theme["bg"], fg=theme["fg"])
    search_entry.configure(bg=theme["text_bg"], fg=theme["text_fg"], insertbackground=theme["fg"])
    welcome_label.configure(bg=theme["bg"], fg=theme["fg"])
    
    python_btn.configure(bg=theme["button_bg"], fg=theme["button_fg"])
    html_btn.configure(bg=theme["button_bg"], fg=theme["button_fg"])
    css_btn.configure(bg=theme["button_bg"], fg=theme["button_fg"])
    theme_btn.configure(bg=theme["button_bg"], fg=theme["button_fg"])
    if sub_frame:
        for widget in sub_frame.winfo_children():
            if isinstance(widget, tk.Button) or isinstance(widget, tk.Label):
                widget.configure(bg=theme["button_bg"] if isinstance(widget, tk.Button) else theme["bg"], 
                                 fg=theme["button_fg"] if isinstance(widget, tk.Button) else theme["fg"])
    
    search_button.configure(bg=theme["button_bg"], fg=theme["button_fg"])
    run_button.configure(bg=theme["button_bg"], fg=theme["button_fg"])
    exit_btn.configure(bg="#ff6666", fg="white")
    
    text_area.configure(bg=theme["text_bg"], fg=theme["text_fg"], insertbackground=theme["fg"])
    highlight_syntax(text_area, text_area.get(1.0, tk.END))

# Create the main window
root = tk.Tk()
root.title("Syntax Reference Tool")
root.geometry("900x700")
root.configure(bg=themes["light"]["bg"])

# Frame for search bar (top)
search_frame = tk.Frame(root, bg=themes["light"]["bg"])
search_frame.pack(side=tk.TOP, fill=tk.X, padx=10, pady=5)

search_label = tk.Label(search_frame, text="Search Syntax:", font=("Arial", 12), bg=themes["light"]["bg"], fg=themes["light"]["fg"])
search_label.pack(side=tk.LEFT, padx=5)

search_entry = tk.Entry(search_frame, width=30, font=("Arial", 12), bg=themes["light"]["text_bg"], fg=themes["light"]["fg"])
search_entry.pack(side=tk.LEFT, padx=5)

search_button = tk.Button(search_frame, text="Search", font=("Arial", 12), command=search_syntax, bg=themes["light"]["button_bg"], fg=themes["light"]["button_fg"])
search_button.pack(side=tk.LEFT, padx=5)

# Frame for category buttons (left side)
category_frame = tk.Frame(root, width=200, bg=themes["light"]["bg"])
category_frame.pack(side=tk.LEFT, fill=tk.Y, padx=10, pady=10)

welcome_label = tk.Label(category_frame, text="Syntax Categories:", font=("Arial", 14, "bold"), bg=themes["light"]["bg"], fg=themes["light"]["fg"])
welcome_label.pack(pady=10)

# "Python" button
python_btn = tk.Button(category_frame, text="Python", font=("Arial", 12), 
                       command=lambda: show_syntax("Python"), anchor="w", width=20,
                       bg=themes["light"]["button_bg"], fg=themes["light"]["button_fg"])
python_btn.pack(pady=5)

# "HTML" button
html_btn = tk.Button(category_frame, text="HTML", font=("Arial", 12), 
                     command=lambda: show_syntax("HTML"), anchor="w", width=20,
                     bg=themes["light"]["button_bg"], fg=themes["light"]["button_fg"])
html_btn.pack(pady=5)

# "CSS" button
css_btn = tk.Button(category_frame, text="CSS", font=("Arial", 12), 
                    command=lambda: show_syntax("CSS"), anchor="w", width=20,
                    bg=themes["light"]["button_bg"], fg=themes["light"]["button_fg"])
css_btn.pack(pady=5)

theme_btn = tk.Button(category_frame, text="Toggle Dark/Light Mode", font=("Arial", 12), command=toggle_theme,
                      bg=themes["light"]["button_bg"], fg=themes["light"]["button_fg"])
theme_btn.pack(pady=5)

exit_btn = tk.Button(category_frame, text="Exit", font=("Arial", 12), command=root.quit, bg="#ff6666", fg="white")
exit_btn.pack(pady=20)

# Text area for syntax and examples (right side)
text_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=80, height=40, font=("Courier", 12),
                                      bg=themes["light"]["text_bg"], fg=themes["light"]["text_fg"])
text_area.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=10, pady=10)

# Run button (below text area)
run_button = tk.Button(root, text="Run Example", font=("Arial", 12), command=run_example, state="disabled",
                       bg=themes["light"]["button_bg"], fg=themes["light"]["button_fg"])
run_button.pack(side=tk.BOTTOM, pady=5)

# Initial message
highlight_syntax(text_area, "Welcome to the Syntax Reference Tool!\n\nClick 'Python', 'HTML', or 'CSS' to explore syntax or use the search bar.\n")

# Start the application
root.mainloop()