# new-content.sh Usage Guide

This script helps you create new Hugo blog or newsletter posts with filenames automatically prefixed by the current date.

## Prerequisites
- You must have [Hugo](https://gohugo.io/getting-started/installing/) installed and available in your PATH.
- You must be using a Unix-like shell (Linux, macOS, or Git Bash/WSL on Windows).

## Setup
1. Place `new-content.sh` inside your site's `scripts` directory (already done).
2. Make the script executable (run this command once):
   ```bash
   chmod +x scripts/new-content.sh
   ```

## Usage
Run the script from your site's root directory:

```
./scripts/new-content.sh <blog|newsletter> <title-with-hyphens>
```

- `<blog|newsletter>`: Specify whether you want to create a blog post or a newsletter.
- `<title-with-hyphens>`: The title for your new post, using hyphens or underscores (no spaces).

### Examples

**Create a new blog post:**
```bash
./scripts/new-content.sh blog my-awesome-post
```

**Create a new newsletter:**
```bash
./scripts/new-content.sh newsletter weekly-update
```

This will create files like:
- `content/blog/2025-06-28_my-awesome-post.md`
- `content/newsletter/2025-06-28_weekly-update.md`

## Notes
- The script must be run from the root of your Hugo site (where the `content` folder is located).
- The script will print a success or error message after attempting to create the file.
- If you get a permission error, ensure the script is executable (`chmod +x scripts/new-content.sh`).

---

Enjoy fast, consistent content creation for your Hugo site!
