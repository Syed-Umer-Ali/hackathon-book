import os
import re
from pathlib import Path

# Assuming the docs directory is at the root level relative to the backend
BASE_DIR = Path(__file__).resolve().parent.parent.parent.parent
DOCS_DIR = BASE_DIR / "physical-ai-book" / "docs"

def find_file_fuzzy(base_path: Path, parts: list[str]) -> Path | None:
    """
    Recursively finds a path by matching parts, ignoring leading numbers (e.g., '01-').
    """
    if not parts:
        # If we have exhausted parts, we check if base_path is a file or has index.md
        if base_path.is_file():
            return base_path
        if base_path.is_dir():
            index_md = base_path / "index.md"
            if index_md.exists():
                return index_md
            # Docusaurus sometimes uses README.md or similar, but index.md is standard
        return None

    current_part = parts[0]
    remaining_parts = parts[1:]
    
    if not base_path.exists() or not base_path.is_dir():
        return None

    # Iterate over all items in the current directory
    for item in base_path.iterdir():
        # Normalize item name by removing leading numbers and hyphens for comparison
        # Regex: remove starting digits followed by optional hyphen/dot/underscore
        normalized_name = re.sub(r'^\d+[-_.]', '', item.name)
        
        # Check if it matches
        # If it's the last part, we look for .md extension match
        if not remaining_parts:
            if item.is_file() and item.stem == current_part: # item.stem is filename without extension
                 return item
            if item.is_file() and re.sub(r'^\d+[-_.]', '', item.stem) == current_part:
                 return item
        
        # If it's a directory, check if it matches the current part
        if item.is_dir():
            if normalized_name == current_part:
                result = find_file_fuzzy(item, remaining_parts)
                if result:
                    return result

    return None

def get_markdown_content(slug: str) -> str:
    """
    Reads the markdown content for a given slug.
    Handles Docusaurus number prefixes (e.g., slug 'intro' finds '01-intro.md').
    """
    # Security check
    if ".." in slug or slug.startswith("/"):
        raise ValueError("Invalid slug")

    # 1. Try direct match first (fastest)
    direct_path = DOCS_DIR / f"{slug}.md"
    if direct_path.exists():
        with open(direct_path, "r", encoding="utf-8") as f:
            return f.read()

    # 2. Try fuzzy match (walking the tree)
    slug_parts = slug.split('/')
    found_path = find_file_fuzzy(DOCS_DIR, slug_parts)
    
    if found_path and found_path.exists():
        with open(found_path, "r", encoding="utf-8") as f:
            return f.read()

    # Debug info for Vercel logs
    print(f"DEBUG: DOCS_DIR={DOCS_DIR}, Exists={DOCS_DIR.exists()}")
    if DOCS_DIR.exists():
        print(f"DEBUG: Listing {DOCS_DIR}: {[p.name for p in DOCS_DIR.iterdir()]}")

    raise FileNotFoundError(f"Lesson content not found for slug: {slug}")
