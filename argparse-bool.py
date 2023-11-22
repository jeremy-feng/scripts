import argparse
from distutils.util import strtobool

parser = argparse.ArgumentParser("test")
parser.add_argument("--yesorno", type=lambda x: bool(strtobool(str(x))), default=True)

args = parser.parse_args()
yesorno = args.yesorno

print(type(yesorno))
print(yesorno)
