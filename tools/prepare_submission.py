#!/usr/bin/env python3
"""
Automated arXiv Submission Preparation Script
Prepares the Emergent Gravity paper for arXiv submission.
"""

import subprocess
import shutil
import zipfile
from pathlib import Path
import sys


def run_command(cmd, cwd=None, capture_output=True):
    """Run a shell command and return the result."""
    result = subprocess.run(
        cmd, shell=True, cwd=cwd, capture_output=capture_output, text=True
    )
    if result.returncode != 0:
        print(f"❌ Command failed: {cmd}")
        print(f"Error: {result.stderr}")
        return False
    return True


def clean_latex_directory():
    """Clean up any auxiliary files in the latex directory."""
    print("🧹 Cleaning latex directory...")
    latex_dir = Path("latex")

    # Remove auxiliary files that might be in the main directory
    aux_patterns = [
        "*.aux",
        "*.log",
        "*.out",
        "*.toc",
        "*.bcf",
        "*.run.xml",
        "*.synctex.gz",
    ]
    for pattern in aux_patterns:
        for file in latex_dir.glob(pattern):
            file.unlink()
            print(f"   Removed {file.name}")

    print("✅ Latex directory cleaned")
    return True


def compile_document():
    """Compile the LaTeX document using the render script."""
    print("📝 Compiling document...")

    if not run_command("python code/render_all_tex.py"):
        print("❌ Compilation failed!")
        return False

    print("✅ Document compiled successfully")
    return True


def prepare_submission_files():
    """Prepare the files needed for arXiv submission."""
    print("📦 Preparing submission files...")

    latex_dir = Path("latex")
    aux_dir = latex_dir / "auxiliary"

    # Copy the .bbl file from auxiliary to main latex directory
    bbl_source = aux_dir / "main.bbl"
    bbl_dest = latex_dir / "main.bbl"

    if bbl_source.exists():
        shutil.copy2(bbl_source, bbl_dest)
        print("   Copied main.bbl to latex directory")
    else:
        print("❌ Warning: main.bbl not found in auxiliary directory")
        return False

    print("✅ Submission files prepared")
    return True


def create_submission_zip():
    """Create the arXiv submission zip file."""
    print("🗜️  Creating submission zip...")

    zip_name = "emergent_gravity_arxiv_submission.zip"

    # Remove old zip if it exists
    if Path(zip_name).exists():
        Path(zip_name).unlink()

    # Create new zip with only essential files
    with zipfile.ZipFile(zip_name, "w", zipfile.ZIP_DEFLATED) as zipf:
        latex_dir = Path("latex")

        # Essential files to include
        essential_files = [
            "main.tex",
            "main.bbl",
            "references.bib",
            "macros.tex",
            "README_SUBMISSION.md",
        ]

        # Add essential files
        for file_name in essential_files:
            file_path = latex_dir / file_name
            if file_path.exists():
                zipf.write(file_path, f"latex/{file_name}")
                print(f"   Added {file_name}")

        # Add all section files
        sections_dir = latex_dir / "sections"
        if sections_dir.exists():
            for tex_file in sections_dir.glob("*.tex"):
                zipf.write(tex_file, f"latex/sections/{tex_file.name}")
                print(f"   Added sections/{tex_file.name}")

        # Add figure files
        figures_dir = latex_dir / "figures"
        if figures_dir.exists():
            for fig_file in figures_dir.glob("*.pdf"):
                zipf.write(fig_file, f"latex/figures/{fig_file.name}")
                print(f"   Added figures/{fig_file.name}")

    # Check file size
    zip_size = Path(zip_name).stat().st_size / 1024  # KB
    print(f"✅ Created {zip_name} ({zip_size:.0f} KB)")

    if zip_size > 50 * 1024:  # 50MB limit
        print("⚠️  Warning: File size exceeds arXiv's 50MB limit!")
        return False

    return True


def verify_submission():
    """Verify the submission package is ready."""
    print("🔍 Verifying submission package...")

    latex_dir = Path("latex")

    # Check essential files exist
    required_files = [
        latex_dir / "main.tex",
        latex_dir / "main.bbl",
        latex_dir / "references.bib",
        Path("emergent_gravity_arxiv_submission.zip"),
    ]

    missing_files = [f for f in required_files if not f.exists()]

    if missing_files:
        print("❌ Missing required files:")
        for f in missing_files:
            print(f"   - {f}")
        return False

    print("✅ All required files present")
    return True


def test_compilation():
    """Test that the submission package compiles correctly."""
    print("🧪 Testing compilation...")

    # Quick test compilation
    if not run_command("pdflatex -interaction=nonstopmode main.tex", cwd="latex"):
        print("❌ Test compilation failed!")
        return False

    # Clean up test files
    latex_dir = Path("latex")
    for pattern in ["*.aux", "*.log", "*.out", "*.toc"]:
        for file in latex_dir.glob(pattern):
            file.unlink()

    print("✅ Test compilation successful")
    return True


def print_submission_instructions():
    """Print final submission instructions."""
    print("\n🚀 SUBMISSION READY!")
    print("=" * 50)
    print("Your paper is ready for arXiv submission!")
    print()
    print("📁 Submission file: emergent_gravity_arxiv_submission.zip")
    print("📋 Next steps:")
    print("   1. Go to https://arxiv.org/submit")
    print("   2. Upload the zip file")
    print("   3. Choose categories: gr-qc (primary), hep-th, astro-ph.CO")
    print(
        "   4. Add title: 'Emergent Gravity from Entanglement: Unified Derivations and Frameworks'"
    )
    print("   5. Review and submit!")
    print()
    print("📖 See 'submit_to_arxiv.md' for detailed instructions")
    print("=" * 50)


def main():
    """Main submission preparation workflow."""
    print("🎯 Emergent Gravity - arXiv Submission Preparation")
    print("=" * 50)

    steps = [
        ("Clean LaTeX directory", clean_latex_directory),
        ("Compile document", compile_document),
        ("Prepare submission files", prepare_submission_files),
        ("Create submission zip", create_submission_zip),
        ("Test compilation", test_compilation),
        ("Verify submission package", verify_submission),
    ]

    for step_name, step_func in steps:
        print(f"\n📍 {step_name}...")
        if not step_func():
            print(f"\n❌ Failed at step: {step_name}")
            sys.exit(1)

    print_submission_instructions()
    print("\n✅ SUCCESS: Ready for arXiv submission! 🎉")


if __name__ == "__main__":
    main()
