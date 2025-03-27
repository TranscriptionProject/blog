import sys
import subprocess
import os
import re
import glob

def update_config_toml():
    config_path = os.path.join("site", "config.toml")
    
    if not os.path.exists(config_path):
        print(f"Warning: {config_path} not found. Cannot update theme configuration.")
        return
    
    print("\nUpdating config.toml with theme...")
    
    # Read config file
    with open(config_path, 'r') as file:
        content = file.read()
    
    # Check if theme is already defined
    if 'theme = ' in content or 'themes = ' in content:
        # Replace existing theme setting
        lines = content.split('\n')
        for i, line in enumerate(lines):
            if line.strip().startswith('theme =') or line.strip().startswith('themes ='):
                lines[i] = 'theme = "hugo-theme-cleanwhite"'
                break
        content = '\n'.join(lines)
    else:
        # Add theme setting after title
        if 'title = ' in content:
            lines = content.split('\n')
            for i, line in enumerate(lines):
                if line.strip().startswith('title ='):
                    lines.insert(i+1, 'theme = "hugo-theme-cleanwhite"')
                    break
            content = '\n'.join(lines)
        else:
            # If title not found, add theme at the top
            content = 'theme = "hugo-theme-cleanwhite"\n' + content
    
    # Write updated config back to file
    with open(config_path, 'w') as file:
        file.write(content)
    
    print("Config.toml updated successfully.")

def fix_href_quotes():
    """Fix unescaped quotes in href attributes within markdown files"""
    post_dir = os.path.join("site", "content", "post")
    if not os.path.exists(post_dir):
        print(f"Warning: {post_dir} not found. Cannot fix href quotes in posts.")
        return
    
    print("\nFixing unescaped quotes in markdown files...")
    
    # Find all markdown files
    md_files = glob.glob(os.path.join(post_dir, "*.md"))
    
    if not md_files:
        print(f"No markdown files found in {post_dir}")
        return
    
    fixed_count = 0
    
    for file_path in md_files:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        if 'href="' in content and '{{< figure' in content:
            # Pattern to match figure shortcodes with href attributes
            pattern = r'({{<\s*figure.*?caption=".*?)href="(.*?)"(.*?>}})'
            
            # Function to process each match
            def replace_quotes(match):
                before = match.group(1)
                url = match.group(2)
                after = match.group(3)
                return f'{before}href=\\"{url}\\"{after}'
            
            # Replace all occurrences with a max iteration limit
            updated_content = content
            max_iterations = 10  # Limit iterations to avoid infinite loops
            for i in range(max_iterations):
                previous_content = updated_content
                updated_content = re.sub(pattern, replace_quotes, updated_content, flags=re.DOTALL)
                
                # Stop if no more changes are being made
                if previous_content == updated_content:
                    break
            
            if updated_content != content:
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(updated_content)
                print(f"  Fixed quotes in {os.path.basename(file_path)}")
                fixed_count += 1
    
    if fixed_count > 0:
        print(f"Fixed quotes in {fixed_count} files.")
    else:
        print("No files needed quote fixing.")

def clone_theme():
    theme_path = os.path.join("site", "themes", "hugo-theme-cleanwhite")
    
    # Check if the theme directory already exists
    if os.path.exists(theme_path):
        print(f"Theme directory '{theme_path}' already exists. Skipping clone.")
        return
    
    # Make sure the themes directory exists
    os.makedirs(os.path.join("site", "themes"), exist_ok=True)
    
    # Clone the theme repository
    try:
        print("\nCloning theme repository...")
        clone_cmd = ["git", "clone", "https://github.com/zhaohuabing/hugo-theme-cleanwhite", theme_path]
        subprocess.run(clone_cmd, check=True)
        print("Theme cloned successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error cloning theme: {e}")
        print("You may need to manually clone the theme.")
    except FileNotFoundError:
        print("Error: Git not found. Make sure git is installed and available in your PATH.")
        print("You may need to manually clone the theme.")

def customize_navbar():
    """Customize the navbar to match zainrizvi.io"""
    print("\nCustomizing navbar...")
    
    # Create layouts directory if it doesn't exist
    layouts_dir = os.path.join("site", "layouts", "partials")
    os.makedirs(layouts_dir, exist_ok=True)
    
    # Create custom navbar partial
    navbar_path = os.path.join(layouts_dir, "nav.html")
    
    # Only create if it doesn't exist already
    if os.path.exists(navbar_path):
        print("Custom navbar already exists. Skipping customization.")
        return
    
    # Create the custom navbar HTML file based on zainrizvi.io style
    navbar_html = """<!-- Custom navbar for zainrizvi.io style -->
<nav class="navbar navbar-default navbar-custom navbar-fixed-top">
    <div class="container-fluid">
        <div class="site-header-inside">
            <!-- Brand and toggle -->
            <div class="navbar-header page-scroll">
                <button type="button" class="navbar-toggle">
                    <span class="sr-only">Toggle navigation</span>
                    <span class="icon-bar"></span>
                    <span class="icon-bar"></span>
                    <span class="icon-bar"></span>
                </button>
                <div class="site-branding">
                    <h1 class="site-title"><a class="navbar-brand" href="{{ "/" | relLangURL }}">{{ .Site.Title }}</a></h1>
                </div>
            </div>

            <!-- Nav links -->
            <div id="huxblog_navbar">
                <div class="navbar-collapse">
                    <ul class="nav navbar-nav navbar-right">
                        <li class="menu-item current-menu-item"><a href="{{ "/" | relLangURL }}">Start Here</a></li>
                        <li class="menu-item"><a href="{{ "/" | relLangURL }}blog/">Essays</a></li>
                        <li class="menu-item"><a href="{{ "/" | relLangURL }}categories/career-advice/">Career Advice</a></li>
                        <li class="menu-item"><a href="{{ "/" | relLangURL }}categories/software-engineering/">Software Engineering</a></li>
                    </ul>
                </div>
            </div>
        </div>
    </div>
</nav>
"""
    
    # Write the custom navbar file
    with open(navbar_path, 'w') as file:
        file.write(navbar_html)
    
    # Create custom CSS file for navbar styling
    css_dir = os.path.join("site", "static", "css")
    os.makedirs(css_dir, exist_ok=True)
    
    custom_css_path = os.path.join(css_dir, "custom.css")
    custom_css = """/* Custom styles to match zainrizvi.io navbar */
.navbar-custom {
    background-color: #fff;
    border-bottom: 1px solid #eaeaea;
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Oxygen, Ubuntu, Cantarell, "Open Sans", "Helvetica Neue", sans-serif;
}

.navbar-custom .site-header-inside {
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 0 15px;
    width: 100%;
}

.navbar-custom .site-branding {
    padding: 0;
}

.navbar-custom .site-title {
    font-size: 22px;
    margin: 0;
    line-height: 1.2;
}

.navbar-custom .navbar-brand {
    color: #33383f;
    font-weight: 700;
    height: auto;
    padding: 20px 0;
}

.navbar-custom .navbar-brand:hover,
.navbar-custom .navbar-brand:focus {
    color: #2c2e31;
}

.navbar-custom .nav li a {
    color: #5c6773;
    font-weight: 600;
    font-size: 14px;
    padding: 20px 15px;
    text-transform: uppercase;
    letter-spacing: 0.5px;
}

.navbar-custom .nav li a:hover,
.navbar-custom .nav li a:focus {
    color: #3eb0ef;
    background-color: transparent;
}

.navbar-custom .nav li.current-menu-item a {
    color: #3eb0ef;
}

/* Mobile menu styles */
@media (max-width: 767px) {
    .navbar-custom .site-header-inside {
        flex-direction: column;
        align-items: flex-start;
    }
    
    .navbar-custom .navbar-header {
        width: 100%;
        display: flex;
        justify-content: space-between;
        align-items: center;
    }
    
    .navbar-custom .nav li a {
        padding: 10px 15px;
    }
}
"""
    
    # Write the custom CSS file
    with open(custom_css_path, 'w') as file:
        file.write(custom_css)
    
    # Update config.toml to use custom CSS
    config_path = os.path.join("site", "config.toml")
    if os.path.exists(config_path):
        with open(config_path, 'r') as file:
            content = file.read()
        
        # Add custom CSS to config if not already there
        if 'custom_css = ["css/custom.css"]' not in content:
            if '[params]' in content:
                # Add to existing params section
                lines = content.split('\n')
                params_index = -1
                
                for i, line in enumerate(lines):
                    if line.strip().startswith('[params]'):
                        params_index = i
                        break
                
                if params_index >= 0:
                    lines.insert(params_index + 1, '  custom_css = ["css/custom.css"]')
                    content = '\n'.join(lines)
            else:
                # Create params section
                content += '\n[params]\n  custom_css = ["css/custom.css"]\n'
            
            # Write updated config
            with open(config_path, 'w') as file:
                file.write(content)
    
    print("Navbar customization completed.")

def add_url_to_posts():
    """Add url field to post metadata, matching the slug field"""
    post_dir = os.path.join("site", "content", "post")
    if not os.path.exists(post_dir):
        print(f"Warning: {post_dir} not found. Cannot update post URLs.")
        return
    
    print("\nAdding URL field to post metadata...")
    
    # Find all markdown files
    md_files = glob.glob(os.path.join(post_dir, "*.md"))
    
    if not md_files:
        print(f"No markdown files found in {post_dir}")
        return
    
    updated_count = 0
    
    for file_path in md_files:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Check if file has frontmatter
        if content.startswith("+++"):
            # Find the end of frontmatter
            frontmatter_end = content.find("+++", 3)
            if frontmatter_end != -1:
                frontmatter = content[3:frontmatter_end]
                rest_of_content = content[frontmatter_end:]
                
                # Check if frontmatter has slug but no url
                if 'slug = ' in frontmatter and 'url = ' not in frontmatter:
                    # Extract slug value
                    slug_match = re.search(r'slug\s*=\s*"([^"]+)"', frontmatter)
                    if slug_match:
                        slug_value = slug_match.group(1)
                        
                        # Add url field after slug
                        modified_frontmatter = re.sub(
                            r'(slug\s*=\s*"[^"]+")(\r?\n)',
                            r'\1\2url = "' + slug_value + r'"\2',
                            frontmatter
                        )
                        
                        # Reassemble the content
                        updated_content = "+++" + modified_frontmatter + rest_of_content
                        
                        # Write updated content back to file
                        with open(file_path, 'w', encoding='utf-8') as f:
                            f.write(updated_content)
                        
                        updated_count += 1
    
    print(f"Added URL field to {updated_count} posts.")

def main():
    # Check command-line arguments
    if len(sys.argv) < 2:
        print("Error: Please provide the path to the JSON file.")
        print("Usage: python script.py <path_to_json_file> [path_to_ghostToHugo_executable]")
        sys.exit(1)
    
    # Get the path to the JSON file from command-line arguments
    json_file_path = sys.argv[1]
    
    # Get the path to the ghostToHugo executable (optional)
    ghost_to_hugo_path = "./ghostToHugo.exe"  # Default path
    if len(sys.argv) >= 3:
        ghost_to_hugo_path = sys.argv[2]
    
    # Check if the JSON file exists
    if not os.path.isfile(json_file_path):
        print(f"Error: The file '{json_file_path}' does not exist.")
        sys.exit(1)
    
    # Construct the command
    command = [ghost_to_hugo_path, "--hugo", "./site", json_file_path]
    
    try:
        # Run the command
        print(f"Running: {ghost_to_hugo_path} --hugo ./site {json_file_path}")
        result = subprocess.run(command, check=True, capture_output=True, text=True)
        
        # Print output
        print("\nOutput:")
        print(result.stdout)
        
        # Clone theme after successful conversion
        clone_theme()
        
        # Update config.toml to use the theme
        update_config_toml()
        
        # Customize navbar to match zainrizvi.io
        customize_navbar()
        
        # Fix unescaped quotes in markdown files
        fix_href_quotes()
        
        # Add URL field to post metadata
        add_url_to_posts()
        
    except subprocess.CalledProcessError as e:
        print(f"Error executing command: {e}")
        print("Standard Error:")
        print(e.stderr)
        sys.exit(1)
    except FileNotFoundError:
        print(f"Error: {ghost_to_hugo_path} not found. Make sure the executable exists at the specified path.")
        sys.exit(1)

if __name__ == "__main__":
    main()