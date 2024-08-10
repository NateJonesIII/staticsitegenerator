import os.path, os, shutil

def clean_directory(destination_dir):
    if os.path.exists(destination_dir):
        for item in os.listdir(destination_dir):
            # store destination item location path
            item_loc = os.path.join(destination_dir, item)
            if os.path.isfile(item_loc):
                # remove item at that location
                os.remove(item_loc)
            elif os.path.isdir(item_loc):
                # If it's a directory, delete it and its contents recursively
                shutil.rmtree(item_loc)
                
def copy_directory(source_dir, destination_dir):
    
    if not os.path.exists(destination_dir): 
        # Create directory if not created               
        os.mkdir(destination_dir)
    
    # enumerate the directory
    for item in os.listdir(source_dir):   
        # store source item location path
        item_source_loc = os.path.join(source_dir, item) 
        
        # store destination item location path
        item_dest_loc = os.path.join(destination_dir, item)
            
        if os.path.isfile(item_source_loc):
            # Log to console, the file being copied
            print(f"Copying file: {item_source_loc} to {item_dest_loc}")
            # Copy the file to the destination
            shutil.copy2(item_source_loc, item_dest_loc)

        elif os.path.isdir(item_source_loc):
            # Log to console, the directory being copied
            print(f"Copying directory: {item_source_loc} to {item_dest_loc}")
            # Recursively call copy_directory for the subdirectory
            copy_directory(item_source_loc, item_dest_loc)    
            
def main():
    source_dir = "./static"
    destination_dir = "./public"

    # Step 1: Clean the destination directory
    clean_directory(destination_dir)

    # Step 2: Copy contents from source to destination
    copy_directory(source_dir, destination_dir)


main()