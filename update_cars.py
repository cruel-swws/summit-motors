import re
import os
import urllib.parse

from pathlib import Path

# Mapping of car ID to their directory
dirs = {
    0: "2018 Tesla Model 3",
    1: "2022 Infiniti q50 3.7 Sedan 4D",
    2: "2018 Hyundai elantra value edition",
    3: "2016 Kia Sedona Lx Minivan 4D"
}

html_file = r"c:\Users\renat\Downloads\Summit\index.html"

with open(html_file, "r", encoding="utf-8") as f:
    content = f.read()

# Build the images array and video literal for each car
replacements = {}
for cid, folder in dirs.items():
    folder_path = os.path.join(r"c:\Users\renat\Downloads\Summit", folder)
    if os.path.exists(folder_path):
        all_files = os.listdir(folder_path)
        
        # JPEG files
        jpg_files = [f for f in all_files if f.lower().endswith(".jpg")]
        capa_files = [f for f in jpg_files if "capa" in f.lower()]
        other_files = [f for f in jpg_files if "capa" not in f.lower()]
        other_files.sort()
        final_jpgs = capa_files + other_files
        
        # MP4 files
        mp4_files = [f for f in all_files if f.lower().endswith(".mp4")]
        video_file = mp4_files[0] if mp4_files else ""
        
        video_str = f'video: "{urllib.parse.quote(folder)}/{urllib.parse.quote(video_file)}",\n                ' if video_file else 'video: "",\n                '
        
        arr_str = video_str + "images: [\n                    " + ",\n                    ".join(
            [f'"{urllib.parse.quote(folder)}/{urllib.parse.quote(img)}"' for img in final_jpgs]
        ) + "\n                ]"
        
        replacements[cid] = arr_str

for cid, replacement_str in replacements.items():
    # Since we already ran the script before, it might have 'images: [ ... ]' 
    # Let's match from 'tags: ["...", "..."],' to 'desc: "'
    # Wait, the best way in this Python script is to use regex matching the exact current structure
    # Since I don't know exactly how many spaces, a regex like r'images:\s*\[[^\]]+\]\s*,' will work better, assuming there's a comma after the array.
    
    # Wait, let's look at the structure from previous index.html:
    # tags: ["...", "..."],
    # images: [
    #    ...
    # ],
    # desc: "..."
    # So we can match `images:\s*\[[\s\S]*?\],?` and replace with `replacement_str + ","`
    # Let's add a trailing comma to arr_str
    
    arr_str_with_comma = replacement_str + ","
    
    if cid == 0:
        content = re.sub(r'images:\s*\[[\s\S]*?Tesla[\s\S]*?\],', arr_str_with_comma, content)
    elif cid == 1:
        content = re.sub(r'images:\s*\[[\s\S]*?Infiniti[\s\S]*?\],', arr_str_with_comma, content)
    elif cid == 2:
        content = re.sub(r'images:\s*\[[\s\S]*?Hyundai[\s\S]*?\],', arr_str_with_comma, content)
    elif cid == 3:
        content = re.sub(r'images:\s*\[[\s\S]*?Kia[\s\S]*?\],', arr_str_with_comma, content)

with open(html_file, "w", encoding="utf-8") as f:
    f.write(content)

print("Cars array updated successfully with videos.")
