import re
import sys


def _get_input():
    return sys.stdin.read()
    # TODO: read from paste-bin
    # return "tags: #metadata,#social,#share,#tags,#whatsapp,#facebook,#twitter,#debug,#tools"


def _extract_tags(raw_data):
    tags = re.split(r"\W+", raw_data)
    return [tag for tag in tags if tag != "tags"]


def _format_tags(tags):
    output = ""
    for tag in tags:
        output += f"    - {tag}\n"
    return output


def _print_output(output):
    print(f"tags:\n{output}")


def main():
    raw_data = _get_input()
    tags = _extract_tags(raw_data)
    output = _format_tags(tags)
    _print_output(output)


if __name__ == "__main__":
    main()
