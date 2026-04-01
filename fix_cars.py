import urllib.parse
import os
import re

dirs = [
    {
        "name": "2018 Tesla Model 3",
        "price": "$17,000",
        "miles": "92k mi",
        "subtitle": "Auto • Electric",
        "tags": ["Clean Title", "100% EV"],
        "folder": "2018 Tesla Model 3",
        "desc": "Experience the future of driving with a whisper-quiet, incredibly smooth ride. Exceptionally well maintained and drives like new.",
        "specs": ["98% Battery Health", "Zero mechanical issues"]
    },
    {
        "name": "2022 Infiniti Q50",
        "price": "$26,500",
        "miles": "54k mi",
        "subtitle": "Sensory • 3.0L V6",
        "tags": ["Clean Title", "Fully Loaded"],
        "folder": "2022 Infiniti q50 3.7 Sedan 4D",
        "desc": "Unmatched luxury and very fast performance. Twin Turbo V6 packed with premium tech including 360-camera and leather trim.",
        "specs": ["Premium Sound & Sunroof", "Blind spot & Lane assist"]
    },
    {
        "name": "2018 Hyundai Elantra",
        "price": "$9,900",
        "miles": "96k mi",
        "subtitle": "Value Ed. • Auto",
        "tags": ["Clean Title", "Eco-Friendly"],
        "folder": "2018 Hyundai elantra value edition",
        "desc": "Ultra-reliable and smooth commuter with excellent gas mileage. Impeccably clean inside and out. Recently serviced and good to go.",
        "specs": ["Backup Cam & Bluetooth", "Alloy Wheels"]
    },
    {
        "name": "2016 Kia Sedona LX",
        "price": "$9,900",
        "miles": "90k mi",
        "subtitle": "Auto • 24 MPG",
        "tags": ["Clean Title", "1 Owner"],
        "folder": "2016 Kia Sedona Lx Minivan 4D",
        "desc": "Spacious, family-ready minivan in excellent condition. Running perfectly with 13 detailed service records and zero issues.",
        "specs": ["No Accidents", "Engine & trans perfect"]
    }
]

html_file = r"c:\Users\renat\Downloads\Summit\index.html"
with open(html_file, "r", encoding="utf-8") as f:
    content = f.read()

cars_js = "const cars = [\n"
for idx, car in enumerate(dirs):
    folder_path = os.path.join(r"c:\Users\renat\Downloads\Summit", car["folder"])
    all_files = os.listdir(folder_path) if os.path.exists(folder_path) else []
    
    jpg_files = [f for f in all_files if f.lower().endswith(".jpg")]
    capa_files = [f for f in jpg_files if "capa" in f.lower()]
    other_files = [f for f in jpg_files if "capa" not in f.lower()]
    other_files.sort()
    final_jpgs = capa_files + other_files
    
    mp4_files = [f for f in all_files if f.lower().endswith(".mp4")]
    video_file = mp4_files[0] if mp4_files else ""
    
    images_str = ",\n                ".join([f'"{urllib.parse.quote(car["folder"])}/{urllib.parse.quote(img)}"' for img in final_jpgs])
    video_str = f'"{urllib.parse.quote(car["folder"])}/{urllib.parse.quote(video_file)}"' if video_file else '""'
    
    cars_js += f"""        {{
            id: {idx},
            name: "{car['name']}",
            price: "{car['price']}",
            miles: "{car['miles']}",
            subtitle: "{car['subtitle']}",
            tags: {car['tags']},
            video: {video_str},
            images: [
                {images_str}
            ],
            desc: "{car['desc']}",
            specs: {car['specs']}
        }}{"," if idx < len(dirs) - 1 else ""}
"""
cars_js += "    ];"

# Replace block
content = re.sub(r'const\s+cars\s*=\s*\[[\s\S]*?\];', cars_js, content)

with open(html_file, "w", encoding="utf-8") as f:
    f.write(content)
print("Cars fixed.")
