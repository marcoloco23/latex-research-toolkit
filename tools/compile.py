#!/usr/bin/env python3
"""Streamlined LaTeX compilation with automatic file organization."""

import subprocess
import sys
from pathlib import Path
from typing import Optional

import click


def run_command(cmd: list[str], cwd: Path) -> tuple[bool, str]:
    """Run command and return success status with combined output."""
    try:
        result = subprocess.run(
            cmd, cwd=cwd, capture_output=True, text=True, encoding="utf-8"
        )
        output = f"{result.stdout}\n{result.stderr}".strip()
        return result.returncode == 0, output
    except Exception as e:
        return False, str(e)


def compile_tex(tex_file: Path, output_dir: Path, aux_dir: Path) -> bool:
    """Compile LaTeX file with bibliography support."""
    print(f"Compiling {tex_file.name}...")

    # Ensure directories exist
    output_dir.mkdir(exist_ok=True)
    aux_dir.mkdir(exist_ok=True)

    # Compilation chain: pdflatex -> biber -> pdflatex -> pdflatex
    commands = [
        ["pdflatex", "-interaction=nonstopmode", tex_file.name],
        ["biber", tex_file.stem],  # Only if .bcf exists
        ["pdflatex", "-interaction=nonstopmode", tex_file.name],
        ["pdflatex", "-interaction=nonstopmode", tex_file.name],
    ]

    for i, cmd in enumerate(commands):
        # Skip biber if no bibliography
        if (
            cmd[0] == "biber"
            and not (tex_file.parent / f"{tex_file.stem}.bcf").exists()
        ):
            continue

        success, output = run_command(cmd, tex_file.parent)
        if not success:
            print(f"Error in step {i+1} ({cmd[0]}):")
            print(output)
            return False

    # Move files to organized locations
    pdf_file = tex_file.parent / f"{tex_file.stem}.pdf"
    if pdf_file.exists():
        pdf_file.rename(output_dir / pdf_file.name)

    # Move auxiliary files
    aux_extensions = ["aux", "log", "out", "toc", "bbl", "blg", "bcf", "run.xml"]
    for ext in aux_extensions:
        aux_file = tex_file.parent / f"{tex_file.stem}.{ext}"
        if aux_file.exists():
            aux_file.rename(aux_dir / aux_file.name)

    print(f"✓ Successfully compiled {tex_file.name}")
    return True


@click.command()
@click.option("--file", "-f", help="Specific .tex file to compile")
@click.option("--watch", "-w", is_flag=True, help="Watch for changes and recompile")
def main(file: Optional[str], watch: bool) -> None:
    """Compile LaTeX documents with automatic organization."""
    base_dir = Path(__file__).parent.parent / "latex"

    if not base_dir.exists():
        click.echo(f"Error: LaTeX directory not found at {base_dir}")
        sys.exit(1)

    tex_file = base_dir / (file or "main.tex")
    if not tex_file.exists():
        click.echo(f"Error: {tex_file} not found")
        sys.exit(1)

    output_dir = base_dir / "pdfs"
    aux_dir = base_dir / "auxiliary"

    if watch:
        import time

        last_modified = 0
        while True:
            current_modified = tex_file.stat().st_mtime
            if current_modified > last_modified:
                compile_tex(tex_file, output_dir, aux_dir)
                last_modified = current_modified
            time.sleep(1)
    else:
        success = compile_tex(tex_file, output_dir, aux_dir)
        sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()
