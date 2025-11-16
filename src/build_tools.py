import pathlib
import shutil
import subprocess
import tomllib

from setuptools.command.build_py import build_py


class NPMBuild(build_py):
    """Custom setuptools command to run NPM and copy JS assets."""

    def run(self):
        project_root = pathlib.Path(__file__).resolve().parent

        # Load config from pyproject.toml
        pyproject = project_root / "pyproject.toml"
        with pyproject.open("rb") as f:
            config = tomllib.load(f)

        jsdeps = config.get("tool", {}).get("myapp", {}).get("js_dependencies", {})
        copy_list = jsdeps.get("copy", [])

        # 1. Run npm install (only if package.json exists)
        if (project_root / "package.json").exists():
            print("Running npm install…")
            subprocess.check_call(["npm", "install"], cwd=project_root)

        # 2. Copy configured files from node_modules → static folder
        static_dir = project_root / "src" / "myapp" / "static"
        static_dir.mkdir(parents=True, exist_ok=True)

        for item in copy_list:
            src = project_root / item["src"]
            dst = static_dir / item["dst"]

            if not src.exists():
                raise FileNotFoundError(f"Configured file not found: {src}")

            dst.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy(src, dst)
            print(f"Copied {src} → {dst}")

        # 3. Continue the normal Python build
        super().run()
