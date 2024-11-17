import os
import shutil

# Function to find and move all files within a directory and its subdirectories
def organize_by_file_type(directory):
    if not os.path.isdir(directory):
        print("Invalid directory. Please provide a valid path.")
        return

    print(f"Organizing files in: {directory}")

    # Traverse the directory tree recursively
    for root, _, files in os.walk(directory):
        for filename in files:
            file_path = os.path.join(root, filename)

            # Get the file extension (e.g., '.jpg', '.pdf')
            file_extension = os.path.splitext(filename)[1].lower()

            # Skip files without extensions
            if not file_extension:
                continue

            # Create a folder for the file type if it doesn't exist
            folder_path = os.path.join(directory, file_extension[1:] + "_files")  # Remove the dot from the extension
            if not os.path.exists(folder_path):
                os.makedirs(folder_path)

            try:
                # Move the file into the appropriate folder
                shutil.move(file_path, os.path.join(folder_path, filename))
                print(f"Moved {filename} to {folder_path}")
            except FileNotFoundError:
                print(f"File not found during move: {filename}")
            except Exception as e:
                print(f"Could not move {filename}: {e}")

    print("Files have been organized by their type.")

# Run the function and ask the user for a folder path
if __name__ == "__main__":
    folder_path = input("Enter the path to the folder you want to organize: ").strip()
    if folder_path:
        organize_by_file_type(folder_path)
    else:
        print("No path provided. Exiting.")
        
