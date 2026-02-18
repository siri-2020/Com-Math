import pathlib

def clean_emote_names(directory_path):
    folder = pathlib.Path(directory_path)
    
    if not folder.exists():
        print(f"Error: Path not found -> {directory_path}")
        return

    print(f"Cleaning files in: {folder}\n" + "-"*30)

    for file_path in folder.iterdir():
        if file_path.is_file():
            original_stem = file_path.stem  # Filename without extension
            extension = file_path.suffix     # e.g., ".png"
            
            # Split the name by underscores
            parts = original_stem.split('_')
            
            # Logic: We need at least 3 parts (Name, Type, Timestamp)
            # Example: ["midorima", "Type Annoyed", "2026-02-15-21-40-51"]
            if len(parts) >= 3:
                # [1:-1] slices the list to skip the first and the last items
                middle_parts = parts[1:-1]
                
                # Rejoin the middle parts (in case the 'Type' itself had underscores)
                clean_name = "_".join(middle_parts)
                
                # Create the new filename
                new_filename = f"{clean_name}{extension}"
                new_file_path = folder / new_filename
                
                # Collision handling: If "Type Annoyed.png" exists, make it "Type Annoyed_1.png"
                counter = 1
                while new_file_path.exists():
                    new_filename = f"{clean_name}_{counter}{extension}"
                    new_file_path = folder / new_filename
                    counter += 1

                try:
                    file_path.rename(new_file_path)
                    print(f"Renamed: {original_stem} -> {new_filename}")
                except Exception as e:
                    print(f"Failed to rename {original_stem}: {e}")
            else:
                print(f"Skipped (Pattern not matched): {original_stem}")

# Your specific path
emote_path = r"C:\Users\Tanya\OneDrive\Documents\EmoteLab\Export\Byte"

clean_emote_names(emote_path)
print("-" * 30 + "\nDone!")