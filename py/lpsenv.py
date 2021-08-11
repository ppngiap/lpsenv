def exports(filename):
    lines = open(filename).readlines()
    for line in lines:
        if line.strip().startswith("export "):
            yield line
    return None


libenv = {}
for line in exports("swdepot.bashrc"):
    [k, v] = line.strip().removeprefix("export ").split("=")
    libenv[k] = v

print(libenv)
