# Save as lex.py
import re

patterns = {
    "KEYWORD": r"\b(int|main|if|begin|end|printf)\b",
    "IDENTIFIER": r"\b[a-zA-Z_][a-zA-Z0-9_]*\b",
    "OPERATOR": r"(==|!=|<=|>=|<|>|=)",
    "LITERAL": r"\b\d+\b",
    "PUNCTUATION": r"[\(\);,]",
    "EXPR": r"\bexpr\b",
    "RELOP": r"\brelop\b"
}

token_spec = "|".join(f"(?P<{k}>{v})" for k, v in patterns.items())
token_regex = re.compile(token_spec)

from collections import defaultdict

def lex():
    summary = defaultdict(list)
    with open("input.txt") as src, open("tokens.txt", "w") as tf:
        tf.write("{:<20} {:<20} {:<20}\n".format("Token", "Lexeme", "Type"))
        tf.write("-" * 60 + "\n")

        for line in src:
            for mo in re.finditer(token_regex, line):
                kind = mo.lastgroup
                lexeme = mo.group()
                summary[kind].append(lexeme)

                tf.write("{:<20} {:<20} {:<20}\n".format(
                    kind, lexeme,
                    "Keyword" if kind == "KEYWORD"
                    else "Identifier" if kind == "IDENTIFIER"
                    else "Number" if kind == "LITERAL"
                    else "Operator" if kind == "OPERATOR"
                    else "Punctuation" if kind == "PUNCTUATION"
                    else "Expression" if kind == "EXPR"
                    else "Relational Operator"
                ))

    with open("token_summary.txt", "w") as sf:
        sf.write("Summary of Analysis:\n")
        sf.write("-" * 60 + "\n")
        sf.write("{:<22} {:<12} {}\n".format("Category", "Count", "Elements"))
        sf.write("-" * 60 + "\n")
        for k, values in summary.items():
            sf.write("{:<22} {:<12} {}\n".format(k.capitalize(), len(values), "\t".join(set(values))))

if __name__ == "__main__":
    lex()
