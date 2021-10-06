def exports(filename):
    lines = open(filename).readlines()
    for line in lines:
        if line.strip().startswith("export "):
            yield line

def removeprefix(str, prefix):
    if str.find(prefix) == 0:
        return str[len(prefix):]
    return str # no change


libenv = {}
for line in exports("swdepot.bashrc"):
    # [k, v] = line.strip().removeprefix("export ").split("=")
    [k, v] = removeprefix(line.strip(), "export ").split("=")
    libenv[k] = v

for (key, val) in libenv.items():
    print(key + ":" + val)
print(libenv)
