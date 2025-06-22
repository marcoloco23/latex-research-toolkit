import subprocess
from pathlib import Path


def compile_latex_files(
    latex_dir: Path, pdf_dir: Path, aux_dir: Path, engine: str = "pdflatex"
) -> None:
    """
    Compile standalone .tex files using LaTeX engine and Biber for bibliography.

    Follows the standard chain: pdflatex → biber → pdflatex → pdflatex.
    PDFs are moved to pdf_dir, and auxiliary files to aux_dir for organization.
    """
    # Explicitly list standalone files to compile
    standalone_files: list[str] = ["main.tex"]  # Add more if needed
    tex_files: list[Path] = [latex_dir / fname for fname in standalone_files]
    pdf_dir.mkdir(exist_ok=True)
    aux_dir.mkdir(exist_ok=True)

    def safe_decode(output_bytes: bytes) -> str:
        """Safely decode subprocess output with fallback encodings."""
        for encoding in ['utf-8', 'latin-1', 'cp1252', 'ascii']:
            try:
                return output_bytes.decode(encoding)
            except UnicodeDecodeError:
                continue
        # If all else fails, decode with errors='replace'
        return output_bytes.decode('utf-8', errors='replace')

    for tex_file in tex_files:
        print(f"Compiling {tex_file.name}...")

        # 1. First pdflatex pass
        result = subprocess.run(
            [engine, "-interaction=nonstopmode", tex_file.name],
            cwd=latex_dir,
            capture_output=True,
        )
        if result.returncode != 0:
            print(f"Error in first pdflatex pass for {tex_file.name}:")
            print(safe_decode(result.stdout))
            print(safe_decode(result.stderr))
            continue

        # 2. Biber pass (only if .bcf file exists)
        bcf_file = latex_dir / f"{tex_file.stem}.bcf"
        if bcf_file.exists():
            result = subprocess.run(
                ["biber", tex_file.stem],
                cwd=latex_dir,
                capture_output=True,
            )
            if result.returncode != 0:
                print(f"Error in biber pass for {tex_file.name}:")
                print(safe_decode(result.stdout))
                print(safe_decode(result.stderr))
                continue
        else:
            print(f"No bibliography found in {tex_file.name}, skipping biber.")

        # 3. Second pdflatex pass
        result = subprocess.run(
            [engine, "-interaction=nonstopmode", tex_file.name],
            cwd=latex_dir,
            capture_output=True,
        )
        if result.returncode != 0:
            print(f"Error in second pdflatex pass for {tex_file.name}:")
            print(safe_decode(result.stdout))
            print(safe_decode(result.stderr))
            continue

        # 4. Third pdflatex pass
        result = subprocess.run(
            [engine, "-interaction=nonstopmode", tex_file.name],
            cwd=latex_dir,
            capture_output=True,
        )
        if result.returncode != 0:
            print(f"Error in third pdflatex pass for {tex_file.name}:")
            print(safe_decode(result.stdout))
            print(safe_decode(result.stderr))
            continue

        print(f"Successfully compiled {tex_file.name}.")

        # Move PDF
        pdf_file = latex_dir / f"{tex_file.stem}.pdf"
        if pdf_file.exists():
            pdf_file.rename(pdf_dir / pdf_file.name)

        # Move auxiliary files
        for ext in [
            "aux",
            "log",
            "out",
            "toc",
            "bbl",
            "blg",
            "lof",
            "lot",
            "bcf",
            "run.xml",
        ]:
            aux_file = latex_dir / f"{tex_file.stem}.{ext}"
            if aux_file.exists():
                aux_file.rename(aux_dir / aux_file.name)


if __name__ == "__main__":
    """
    Compile standalone LaTeX files in ../latex directory.

    Moves PDFs to ../latex/pdfs and auxiliary files to ../latex/auxiliary.
    Uses pdflatex → biber → pdflatex → pdflatex chain for biblatex/biber.
    """
    base = Path(__file__).parent.parent / "latex"
    compile_latex_files(
        latex_dir=base, pdf_dir=base / "pdfs", aux_dir=base / "auxiliary"
    )
