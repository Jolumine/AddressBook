import hashlib 


def generate_hash(text: str) -> str: 
    return hashlib.sha1(text.encode("utf-8")).hexdigest()

