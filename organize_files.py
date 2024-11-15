import os
import shutil

# Function to create folders and move files
def organize_by_file_type(directory):
    if not os.path.isdir(directory):
        print("Invalid directory. Please provide a valid path.")
        return

    # Iterate over files in the directory
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)

        # Skip if it's a folder
        if os.path.isdir(file_path):
            continue

        # Get the file extension (e.g., '.jpg', '.pdf')
        file_extension = os.path.splitext(filename)[1].lower()

        # Skip files without extensions
        if not file_extension:
            continue

        # Create a folder for the file type if it doesn't exist
        folder_path = os.path.join(directory, file_extension[1:] + "_files")  # Remove the dot from the extension
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

        # Move the file into the appropriate folder
        shutil.move(file_path, os.path.join(folder_path, filename))

    print("Files have been organized by their type.")

# Run the function and ask the user for a folder path
if __name__ == "__main__":
    folder_path = input("Enter the path to the folder you want to organize: ")
    organize_by_file_type(folder_path)
