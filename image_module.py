from PIL import Image
import imagehash
import json
from utils.hashing import get_phash

def check_image(file):
    img = Image.open(file)
    uploaded_hash = get_phash(img)

    with open("database/owner_registry.json", "r") as f:
        db = json.load(f)

    for media_name, info in db.get("images", {}).items():
        if abs(imagehash.hex_to_hash(info["hash"]) - uploaded_hash) < 5:
            return {"status": "Match Found", "owner": info["owner"], "media": media_name}

    return {"status": "No Match", "owner": None}
