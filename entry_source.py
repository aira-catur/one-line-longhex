import os
from pathlib import Path

FINAL_LINE = "I put my resume on a dating app by mistake; I've never been rejected so professionally."


def emit_line(destination: Path) -> None:
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text(FINAL_LINE, encoding="utf-8")


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    emit_line(out_dir / "entry.txt")


if __name__ == "__main__":
    main()
