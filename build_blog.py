from pathlib import Path
import os
import shutil

SOURCE_ROOT = "src"
BUILD_ROOT = "build"

TEMPLATE_NAME = "template.html" # One of these can appear at each depth
REPLACE_TAG = "<replace/>" # When this appears we replace with the deeper content

def build_rec(
        path="", # This is the directory we are currently in
        template_markdown="" # This is the existing markup we'll insert into
    ):
        
        # Equal positions in both the src and build directories
        src_current = Path(SOURCE_ROOT + "/" + path)
        build_current = Path(BUILD_ROOT + "/" +  path)

        # Recursively building the markdown 
        next_template_markdown = template_markdown

        # If there is a template.html file here load and replace the sub tag
        template_file_path = Path(SOURCE_ROOT + "/" + path + '/template.html')
        if template_file_path.exists():
            content = template_file_path.read_text(encoding='utf-8')
            if len(template_markdown) == 0: # If it's empty, just set it
                next_template_markdown = content
            else: # Otherwise replace the <replace/> tag with content
                next_template_markdown = template_markdown.replace(REPLACE_TAG, content)

        # If there is a style.css file here load and put it in the head
        style_file_path = Path(SOURCE_ROOT + "/" + path + '/style.css')
        if style_file_path.exists():
            print("  ", style_file_path)
            content = style_file_path.read_text(encoding='utf-8')
            next_template_markdown = next_template_markdown.replace("</head>", f"<style>{content}</style></head>")
            # conjoin adjacent script blocks
            next_template_markdown = next_template_markdown.replace("</style><style>","")

        # For each non-template file generate a final file and put it in build
        for filepath in src_current.glob('*.html'):
            if filepath.name != TEMPLATE_NAME:
                print("  ", filepath)
                # Replace the <replace/> tag with the final files markdown
                new_file_content = next_template_markdown.replace(
                    REPLACE_TAG,
                    filepath.read_text(encoding='utf-8')
                )
                # write the file and build the directories
                new_file_name = BUILD_ROOT + "/" + path + "/" + filepath.name
                os.makedirs(os.path.dirname(new_file_name), exist_ok=True)
                with open(new_file_name, 'w') as f:
                    f.write(new_file_content)

        # TODO: Minify HTML & CSS

        # For each subdirectory repeat this process
        for subdirectory in src_current.iterdir():
            if subdirectory.is_dir():
                build_rec(f"{path}/{subdirectory.name}", next_template_markdown)

if __name__ == '__main__':
    print("Purging previous build directory...")
    shutil.rmtree(BUILD_ROOT) # Delete the build directory
    os.mkdir(BUILD_ROOT) # Create a new build directory
    print("Building latest...")
    build_rec()
    print("Build complete!")