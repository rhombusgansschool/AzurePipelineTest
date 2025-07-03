
import subprocess
import shutil
from pathlib import Path

def copy_documents_from_GL_to_mkdocs():
    # Locations
    base_path = Path(__file__).parent.parent.resolve()
    target_path = (Path(__file__).parent / "1_template" / "docs").resolve()

    # Collect parent folder path (GL.Example) when a StaticDocumentation is found within it via .glob
    for StaticDocumentation in base_path.glob("**/StaticDocumentation"):
        if StaticDocumentation.is_dir():
            shutil.copytree(StaticDocumentation, (target_path / StaticDocumentation.parent.name), dirs_exist_ok=True)
    return

def call_mkdocs(command, directory="."):
    mkdocs_path = shutil.which("mkdocs")  # Find mkdocs in the environment
    if not mkdocs_path:
        print("Error: mkdocs is not installed or not found in the current environment.")
        return

    subprocess.run([mkdocs_path, command], check=True, cwd=directory)

def call_mkdocs_arg(command, arg, directory="."):
    mkdocs_path = shutil.which("mkdocs")  # Find mkdocs in the environment
    if not mkdocs_path:
        print("Error: mkdocs is not installed or not found in the current environment.")
        return

    subprocess.run([mkdocs_path, command, arg], check=True, cwd=directory)

if __name__ == "__main__":
    copy_documents_from_GL_to_mkdocs()
    call_mkdocs("build", "1_template")

    