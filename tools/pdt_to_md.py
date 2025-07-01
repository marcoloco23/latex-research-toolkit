import os
import pathlib
import pymupdf4llm


def convert_pdfs_to_markdown(references_dir: str) -> None:
    """
    Converts all PDF files in the given directory to Markdown using pymupdf4llm,
    extracting images as well. The output .md files are saved alongside the PDFs,
    and images are saved in a dedicated images subdirectory.
    """
    # Create images directory if it doesn't exist
    images_dir = os.path.join(references_dir, "images")
    os.makedirs(images_dir, exist_ok=True)

    for entry in os.scandir(references_dir):
        if entry.is_file() and entry.name.lower().endswith(".pdf"):
            input_path = os.path.abspath(entry.path)  # Use absolute path
            output_path = os.path.splitext(entry.path)[0] + ".md"

            # Change to the images directory so pymupdf4llm saves images there
            original_cwd = os.getcwd()
            os.chdir(images_dir)

            try:
                md_text = pymupdf4llm.to_markdown(
                    input_path, write_images=True, dpi=150
                )
                # Update image paths in markdown to reference the images directory
                md_text = md_text.replace("![](", f"![](images/")

                # Write the markdown file from the original directory
                os.chdir(original_cwd)
                pathlib.Path(output_path).write_bytes(md_text.encode("utf-8"))
                print(f"Converted {entry.name} -> {os.path.basename(output_path)}")

            finally:
                # Always restore original directory
                os.chdir(original_cwd)


if __name__ == "__main__":
    convert_pdfs_to_markdown("references")
