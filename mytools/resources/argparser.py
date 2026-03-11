import sys

def parse_args(argv=None):
    """
    Lightweight argument parser.

    Returns:
        args: list of positional arguments
        opts: dict of options / flags
    """
    if argv is None:
        argv = sys.argv[1:]

    args = []
    opts = {}

    i = 0
    while i < len(argv):
        token = argv[i]

        # --key=value
        if token.startswith("--") and "=" in token:
            key, value = token[2:].split("=", 1)
            opts[key.replace("-", "_")] = value

        # --flag or --key value
        elif token.startswith("--"):
            key = token[2:].replace("-", "_")

            # value follows
            if i + 1 < len(argv) and not argv[i + 1].startswith("-"):
                opts[key] = argv[i + 1]
                i += 1
            else:
                opts[key] = True

        # -abc or -v
        elif token.startswith("-") and len(token) > 1:
            for ch in token[1:]:
                opts[ch] = True

        # positional
        else:
            args.append(token)

        i += 1

    return args, opts
