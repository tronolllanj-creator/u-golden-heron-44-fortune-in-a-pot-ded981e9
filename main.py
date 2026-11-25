"""
# Entry validated: output is 1-120 chars, one line, deterministic.
Entrypoint script that writes a specific dramatic line to entry.txt in the
specified output directory (from MAKEFUN_OUTPUT_DIR or defaulting to /output),
and also attempts a best-effort write to /output/entry.txt if a different
directory is used.
"""

import os

LINE = "Your dramatic afternoon faint means the drama club is missing its star frond."


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    content = LINE + "\n"

    # Validate content according to rules
    if not (1 <= len(content) <= 120 and content.strip()):
        raise ValueError("Content validation failed")

    # Ensure main output directory exists
    os.makedirs(output_dir, exist_ok=True)
    main_path = os.path.join(output_dir, "entry.txt")

    with open(main_path, "w", encoding="utf-8") as f:
        f.write(content)

    # Best effort write to /output/entry.txt if different
    if output_dir != "/output":
        try:
            os.makedirs("/output", exist_ok=True)
            with open("/output/entry.txt", "w", encoding="utf-8") as f:
                f.write(content)
        except Exception:
            pass

    print(main_path)
    print(len(content))


if __name__ == "__main__":
    main()
