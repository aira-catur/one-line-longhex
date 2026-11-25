import os

TEXT_PARTS = (
    "I put my resume on a dating app by mistake; ",
    "I've never been rejected so professionally.",
)
TEXT = "".join(TEXT_PARTS)


def write_entry(out_dir, content):
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(content)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    write_entry(out_dir, TEXT)


if __name__ == "__main__":
    main()
