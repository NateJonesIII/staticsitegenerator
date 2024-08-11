import os
import pathlib
from block_markdown import markdown_to_html_node
from extract_title import extract_title


def generate_page(from_path, template_path, dest_path):
    # Print a message
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    # Read the markdown file at from_path and store the contents in a variable.
    with open(from_path, 'r') as file:
        markdown_content = file.read()
    
    # Read the template file at template_path and store the contents in a variable.
    with open(template_path, 'r') as file:
        template_content = file.read()

    # Use your markdown_to_html_node function and .to_html() method to convert the markdown file to an HTML string.
    html_node = markdown_to_html_node(markdown_content)
    html_content = html_node.to_html()
    # Use the extract_title function to grab the title of the page.
    title = extract_title(markdown_content)

    # Replace the {{ Title }} and {{ Content }} placeholders in the template with the HTML and title you generated.
    page_content = template_content.replace('{{ Title }}', title)
    page_content = page_content.replace('{{ Content }}', html_content)
    
    
    # Ensure the destination directory exists
    destination_dir = os.path.dirname(dest_path)
    if not os.path.exists(destination_dir):
        os.makedirs(destination_dir)
    
    # Write the HTML content to the destination file
    with open(dest_path, 'w') as file:
        file.write(page_content)


# Create a generate_pages_recursive(dir_path_content, template_path, dest_dir_path) function
def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    # Walk through the content directory
    for root, dirs, files in os.walk(dir_path_content):
        for file in files:
            if file.endswith(".md"):
                # Compute the full path to the markdown file
                md_file_path = os.path.join(root, file)
                
                # Compute the relative path from the content directory
                rel_path = os.path.relpath(md_file_path, dir_path_content)
                
                # Change the .md extension to .html
                html_file_name = os.path.splitext(rel_path)[0] + ".html"
                
                # Compute the full path to the output file in the public directory
                output_file_path = os.path.join(dest_dir_path, html_file_name)
                
                # Ensure the destination directory exists
                output_dir = os.path.dirname(output_file_path)
                if not os.path.exists(output_dir):
                    os.makedirs(output_dir)
                
                # Generate the HTML file from the markdown file using the template
                generate_page(md_file_path, template_path, output_file_path)