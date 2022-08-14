import re

def run(_filepath):
    with open(_filepath, "rb") as rf:
        hexstr = rf.read().hex()
        lines = re.sub(r"(.{79})", r"\1\r\n", hexstr)
        with open(_filepath+".txt", "w", encoding="utf-8") as wf:
            wf.write(lines)
            wf.close()

