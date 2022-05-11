from pathlib import Path
from pydantic import BaseSettings
import sys

class Generator(BaseSettings):
    class Config:
        env_prefix = "generator_"
        env_file = ".env"
    cooklang_py_path: Path
    recipes_path: Path



def main():
    cfg = Generator()
    sys.path.append(str(cfg.cooklang_py_path))
    from cooklang.hugo import transform_all_recipes
    transform_all_recipes(cfg.recipes_path, Path("content"))

if __name__ == "__main__":
    main()


