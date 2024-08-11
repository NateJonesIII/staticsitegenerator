

# Create an extract_title(markdown) function.
def extract_title(markdown):
    # Splitting markdown in lines
    lines = markdown.splitlines()
    
    for line in lines:
        # If begins with white space
        stripped_line = line.lstrip()
        # pull line that starts with #
        if stripped_line.startswith('#'):
            return stripped_line.lstrip('#').strip()
    # If no h1 header was found, raise an exception
    raise Exception('No h1 header was found')