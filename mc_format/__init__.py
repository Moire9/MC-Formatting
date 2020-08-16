import re, typing

# Essentially, it works like Minecraft. So, no individual resetting. That's for weaklings.
# Setting a color will reset formatting.
# Todo: automatic term detection to enable/disable codes

COLORS: typing.Dict[str, str] = {
	"0": r"\033[0m\033[30m",
	"1": r"\033[0m\033[34m",
	"2": r"\033[0m\033[32m",
	"3": r"\033[0m\033[36m", # Aqua == Cyan
	"4": r"\033[0m\033[31m",
	"5": r"\033[0m\033[35m",
	"6": r"\033[0m\033[33m",
	"7": r"\033[0m\033[37m",
	"8": r"\033[0m\033[90m",
	"9": r"\033[0m\033[94m",
	"a": r"\033[0m\033[92m",
	"b": r"\033[0m\033[96m",
	"c": r"\033[0m\033[91m",
	"d": r"\033[0m\033[95m",
	"e": r"\033[0m\033[93m",
	"f": r"\033[0m\033[97m",
	"k": r"\033[5m", # Obfuscated = Blinking
	"l": r"\033[1m",
	"m": r"\033[8m", # Strikethrough = Password Hidden
	"n": r"\033[4m",
	"o": r"\033[2m", # Italic = Dim because fuck it
	"p": r"\033[7m", # New one - Inverted
	"r": r"\033[0m"
}


section_symbol_regex: typing.Dict[re.Pattern, str] = {
	re.compile("\\\\§"): "§",
	re.compile("^(.*)$"): f"{COLORS['r']}\\1{COLORS['r']}"
}


for x in COLORS.keys():
	section_symbol_regex[re.compile(f"(?<!\\\\)§{x}")]: str = COLORS[x]


def color(string: str) -> str:
	"""Return a string where Minecraft section-symbol codes are replaced with ANSI escape codes."""
	for y in list(section_symbol_regex.keys())[::-1]:
		string: str = re.sub(y, section_symbol_regex[y], string)
	return string


def get_colors() -> str:
	"""Return the color codes that are available for the current Terminal."""
	ret: str = ""
	for a in COLORS.keys():
		ret += f"§{a} : {COLORS[a][(4 if len(COLORS[a]) == 7 else 11):]}\n"
	return ret[:-1]
