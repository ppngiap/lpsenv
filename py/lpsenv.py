import os

def exports(filename):
    lines = open(filename).readlines()
    for line in lines:
        if line.strip().startswith("export "):
            yield line


def removeprefix(str, prefix):
    if str.find(prefix) == 0:
        return str[len(prefix):]
    return str  # no change


libenv = {}
for line in exports("swdepot.bashrc"):
    # [k, v] = line.strip().removeprefix("export ").split("=")
    [k, v] = removeprefix(line.strip(), "export ").split("=")
    libenv[k] = v

try:
    libdir = os.environ['LPS_BASE_LIBDIR']
except KeyError:
    print("LPS_BASE_LIBDIR has not been exported")
    exit(-1)

for (key, val) in libenv.items():
    print(key + "=" + libdir)

#print(libenv)
