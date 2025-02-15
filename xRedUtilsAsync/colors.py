"""
This module provides terminal colors, styles and async handlers.

### Dataclasses
- `Styles` - ANSI styles (bold, italic, underline)
- `Foreground16` - 4bit text colors
- `Background16` - 4bit background colors
- `Foreground255` - 8bit text colors
- `Background255` - 8bit background colors

Simply import dataclasses and access its globals.
>>> from xRedUtils.colors import Foreground16 as FG
>>> print(FG.RED)
\x1b[31m

`NOTE:` Depending of terminal, some can only display 4bit or even no colors. Please try and see what works for you.

### Functions:
- `manual_color_handler` - Ask the user if they want to see colors.
- `auto_color_handler` - Automatically detects if the terminal/console supports colors.
- `rgb_to_ansi` - Converts RGB values to ANSI colors.
- `rem_colors` - Removes ANSI code from the string.
- `display` - Displays color/style and name of specified dataclass.

### Usage:
```py

import xRedUtilsAsync.colors as colors
or
from xRedUtilsAsync import colors
```
"""

import sys
sys.dont_write_bytecode = True
from dataclasses import dataclass, asdict

from .regexes import ANSI_PATTERN
from .annotations import Literal

__all__: tuple[str, ...] = (
    "Style", "Foreground16", "Background16", "Foreground255", "Background255",
    "manual_color_handler", "auto_color_handler", "rgb_to_ansi", "rem_colors", "display"
)

@dataclass
class Style:
    """Be aware that some terminals don't support all these options."""
    RESET: str = "\x1b[0m"
    BOLD: str = "\x1b[1m"
    DIM: str = "\x1b[2m"
    ITALIC: str = "\x1b[3m"
    UNDERLINE: str = "\x1b[4m"
    BLINK: str = "\x1b[5m"
    INVERSE: str = "\x1b[7m"
    INVISIBLE: str = "\x1b[8m"
    STRIKETHROUGH: str = "\x1b[9m"

@dataclass
class Foreground16:
    """If you cannot see colors, your terminal doesn't support them."""
    
    BLACK: str = "\x1b[30m"
    RED: str = "\x1b[31m"
    GREEN: str = "\x1b[32m"
    YELLOW: str = "\x1b[33m"
    BLUE: str = "\x1b[34m"
    MAGENTA: str = "\x1b[35m"
    CYAN: str = "\x1b[36m"
    WHITE: str = "\x1b[37m"
    
    # these only work on terminals with aixterm specs, use `Styles.BOLD` otherwise
    BRIGHT_BLACK: str = "\x1b[90m"
    BRIGHT_RED: str = "\x1b[91m"
    BRIGHT_GREEN: str = "\x1b[92m"
    BRIGHT_YELLOW: str = "\x1b[93m"
    BRIGHT_BLUE: str = "\x1b[94m"
    BRIGHT_MAGENTA: str = "\x1b[95m"
    BRIGHT_CYAN: str = "\x1b[96m"
    BRIGHT_WHITE: str = "\x1b[97m"

@dataclass
class Background16:
    """If you cannot see colors, your terminal doesn't support them."""
    
    BLACK: str = "\x1b[40m"
    RED: str = "\x1b[41m"
    GREEN: str = "\x1b[42m"
    YELLOW: str = "\x1b[43m"
    BLUE: str = "\x1b[44m"
    MAGENTA: str = "\x1b[45m"
    CYAN: str = "\x1b[46m"
    WHITE: str = "\x1b[47m"
    
    # these only work on terminals with aixterm specs, use `Styles.BOLD` otherwise
    BRIGHT_BLACK: str = "\x1b[100m"
    BRIGHT_RED: str = "\x1b[101m"
    BRIGHT_GREEN: str = "\x1b[102m"
    BRIGHT_YELLOW: str = "\x1b[103m"
    BRIGHT_BLUE: str = "\x1b[104m"
    BRIGHT_MAGENTA: str = "\x1b[105m"
    BRIGHT_CYAN: str = "\x1b[106m"
    BRIGHT_WHITE: str = "\x1b[107m"

@dataclass
class Foreground255:
    """If you cannot see colors, try Foreground16."""

    BLACK: str = "\x1b[38;5;16m"
    STRATOS: str = "\x1b[38;5;17m"
    FUZZY_WUZZY: str = "\x1b[38;5;18m"
    BLUE_GRAY: str = "\x1b[38;5;19m"
    DARK_BLUE: str = "\x1b[38;5;20m"
    BLUE: str = "\x1b[38;5;21m"
    DEEP_FIR: str = "\x1b[38;5;22m"
    DEEP_TEAL: str = "\x1b[38;5;23m"
    MIDNIGHT_BLUE: str = "\x1b[38;5;24m"
    SMALT: str = "\x1b[38;5;25m"
    ABSOLUTE_ZERO: str = "\x1b[38;5;26m"
    CANARY: str = "\x1b[38;5;27m"
    CAMARONE: str = "\x1b[38;5;28m"
    FUN_GREEN: str = "\x1b[38;5;29m"
    BLUE_STONE: str = "\x1b[38;5;30m"
    BAHAMA_BLUE: str = "\x1b[38;5;31m"
    SCIENCE_BLUE: str = "\x1b[38;5;32m"
    BLUE_RIBBON: str = "\x1b[38;5;33m"
    JAPANESE_LAUREL: str = "\x1b[38;5;34m"
    TOMB_BLUE: str = "\x1b[38;5;35m"
    GREEN_HAZE: str = "\x1b[38;5;36m"
    PERSIAN_GREEN: str = "\x1b[38;5;37m"
    PACIFIC_BLUE: str = "\x1b[38;5;38m"
    AZURE_RADIANCE: str = "\x1b[38;5;39m"
    GREEN: str = "\x1b[38;5;40m"
    MALACHITE: str = "\x1b[38;5;41m"
    JADE: str = "\x1b[38;5;42m"
    CARIBBEAN_GREEN: str = "\x1b[38;5;43m"
    EGG_BLUE: str = "\x1b[38;5;44m"
    CYAN: str = "\x1b[38;5;45m"
    GREEN: str = "\x1b[38;5;46m"
    LIGHT_GREEN: str = "\x1b[38;5;47m"
    SPRING_GREEN: str = "\x1b[38;5;48m"
    GREEN_GAS: str = "\x1b[38;5;49m"
    BRIGHT_TURQUOISE: str = "\x1b[38;5;50m"
    AQUA: str = "\x1b[38;5;51m"
    TEMPTRESS: str = "\x1b[38;5;52m"
    BAROSSA: str = "\x1b[38;5;53m"
    CHRISTALLE: str = "\x1b[38;5;54m"
    PIGMENT_INDIGO: str = "\x1b[38;5;55m"
    VIOLET_BLUE: str = "\x1b[38;5;56m"
    ULTRAMARINE: str = "\x1b[38;5;57m"
    MADRAS: str = "\x1b[38;5;58m"
    MINE_SHAFT: str = "\x1b[38;5;59m"
    RHINO: str = "\x1b[38;5;60m"
    COSMIC_COBALT: str = "\x1b[38;5;61m"
    GOVERNOR_BAY: str = "\x1b[38;5;62m"
    LIGHT_ROYAL_BLUE: str = "\x1b[38;5;63m"
    VERDUN_GREEN: str = "\x1b[38;5;64m"
    KILLARNEY: str = "\x1b[38;5;65m"
    CASAL: str = "\x1b[38;5;66m"
    BDAZZLED_BLUE: str = "\x1b[38;5;67m"
    DENIM: str = "\x1b[38;5;68m"
    ULTRAMARINE_BLUE: str = "\x1b[38;5;69m"
    LIMEADE: str = "\x1b[38;5;70m"
    APPLE: str = "\x1b[38;5;71m"
    ILLUMINATING_EMERALD: str = "\x1b[38;5;72m"
    LOCHINVAR: str = "\x1b[38;5;73m"
    MOONSTONE: str = "\x1b[38;5;74m"
    DODGER_BLUE: str = "\x1b[38;5;75m"
    HARLEQUIN: str = "\x1b[38;5;76m"
    DARK_LIME: str = "\x1b[38;5;77m"
    EMERALD: str = "\x1b[38;5;78m"
    SHAMROCK: str = "\x1b[38;5;79m"
    TURQUOISE_PEARL: str = "\x1b[38;5;80m"
    SKY_BLUE: str = "\x1b[38;5;81m"
    POISON_GREEN: str = "\x1b[38;5;82m"
    LIME_LASER: str = "\x1b[38;5;83m"
    SCREAMIN_GREEN: str = "\x1b[38;5;84m"
    EVA_GREEN: str = "\x1b[38;5;85m"
    AURICHALCITE: str = "\x1b[38;5;86m"
    BRIGHT_CYAN: str = "\x1b[38;5;87m"
    LONESTAR: str = "\x1b[38;5;88m"
    TYRIAN_PURPLE: str = "\x1b[38;5;89m"
    POMPADOUR: str = "\x1b[38;5;90m"
    DARK_MAGENTA: str = "\x1b[38;5;91m"
    PURPLE: str = "\x1b[38;5;92m"
    ELECTRIC_VIOLET: str = "\x1b[38;5;93m"
    NUTMEG_WOOD: str = "\x1b[38;5;94m"
    BUCCANEER: str = "\x1b[38;5;95m"
    COSMIC: str = "\x1b[38;5;96m"
    EMINENCE: str = "\x1b[38;5;97m"
    PURPLE_HEART: str = "\x1b[38;5;98m"
    ROYAL_PURPLE: str = "\x1b[38;5;99m"
    MUSTARD: str = "\x1b[38;5;100m"
    JUNGLE: str = "\x1b[38;5;101m"
    GRANITE_GRAY: str = "\x1b[38;5;102m"
    AMETHYST: str = "\x1b[38;5;103m"
    INDIGO: str = "\x1b[38;5;104m"
    BLUEBERRY: str = "\x1b[38;5;105m"
    VENOM_GREEN: str = "\x1b[38;5;106m"
    WASABI: str = "\x1b[38;5;107m"
    HIGHLAND: str = "\x1b[38;5;108m"
    PATINA: str = "\x1b[38;5;109m"
    DANUBE: str = "\x1b[38;5;110m"
    CORNFLOWER_BLUE: str = "\x1b[38;5;111m"
    ALIEN_ARMPIT: str = "\x1b[38;5;112m"
    ATLANTIS: str = "\x1b[38;5;113m"
    MANTIS: str = "\x1b[38;5;114m"
    GREEN_PEARL: str = "\x1b[38;5;115m"
    DOWNY: str = "\x1b[38;5;116m"
    MALIBU: str = "\x1b[38;5;117m"
    BRIGHT_GREEN: str = "\x1b[38;5;118m"
    SPRING_FROST: str = "\x1b[38;5;119m"
    LIME: str = "\x1b[38;5;120m" 
    DRAGON_GREEN: str = "\x1b[38;5;121m"
    AQUAMARINE: str = "\x1b[38;5;122m"
    ELECTRIC_BLUE: str = "\x1b[38;5;123m"
    RED_BERRY: str = "\x1b[38;5;124m"
    PAPRIKA: str = "\x1b[38;5;125m"
    FRESH_EGGPLANT: str = "\x1b[38;5;126m"
    FLIRT: str = "\x1b[38;5;127m"
    DARK_VIOLET: str = "\x1b[38;5;128m"
    PLATINUM_PURPLE: str = "\x1b[38;5;129m"
    OREGON: str = "\x1b[38;5;130m"
    STILETTO: str = "\x1b[38;5;131m"
    ROUGE: str = "\x1b[38;5;132m"
    PLUM: str = "\x1b[38;5;133m"
    NEON_MAGENTA: str = "\x1b[38;5;134m"
    GRAPE: str = "\x1b[38;5;135m"
    CHELSEA_GEM: str = "\x1b[38;5;136m"
    METALLIC_SUNBURST: str = "\x1b[38;5;137m"
    COPPER_ROSE: str = "\x1b[38;5;138m"
    STRIKEMASTER: str = "\x1b[38;5;139m"
    MEDIUM_PURPLE: str = "\x1b[38;5;140m"
    HELIOTROPE: str = "\x1b[38;5;141m"
    SOUP: str = "\x1b[38;5;142m"
    SYNCAMORE: str = "\x1b[38;5;143m"
    AVOCADO: str = "\x1b[38;5;144m"
    QUICK_SILVER: str = "\x1b[38;5;145m"
    BLUE_BELL: str = "\x1b[38;5;146m"
    MELROSE: str = "\x1b[38;5;147m"
    SHEEN_GREEN: str = "\x1b[38;5;148m"
    PEA: str = "\x1b[38;5;149m"
    WILD_WILLOW: str = "\x1b[38;5;150m"
    DE_YORK: str = "\x1b[38;5;151m"
    SINBAD: str = "\x1b[38;5;152m"
    ANAKIWA: str = "\x1b[38;5;153m"
    CHARTREUSE: str = "\x1b[38;5;154m"
    GREEN_YELLOW: str = "\x1b[38;5;155m"
    LIGHT_LIME: str = "\x1b[38;5;156m"
    MINT: str = "\x1b[38;5;157m"
    LIGHT_AQUAMARINE: str = "\x1b[38;5;158m"
    WINTER_WIZARD: str = "\x1b[38;5;159m"
    GUARDSMAN_RED: str = "\x1b[38;5;160m"
    MONZA: str = "\x1b[38;5;161m"
    LIPSTICK: str = "\x1b[38;5;162m"
    HOLLYWOOD_CERISE: str = "\x1b[38;5;163m"
    PURPLE_PIZZA: str = "\x1b[38;5;164m"
    PINK_PURPLE: str = "\x1b[38;5;165m"
    GRENADIER: str = "\x1b[38;5;166m"
    PERSIAN_RED: str = "\x1b[38;5;167m"
    JAZZBERRY_JAM: str = "\x1b[38;5;168m"
    MEDIUM_RED_VIOLET: str = "\x1b[38;5;169m"
    FUCHSIA_PINK: str = "\x1b[38;5;170m"
    NEON_PURPLE: str = "\x1b[38;5;171m"
    ORANGE: str = "\x1b[38;5;172m"
    TUSCANY: str = "\x1b[38;5;173m"
    CHESSNUT_ROSE: str = "\x1b[38;5;174m"
    HOPBRUSH: str = "\x1b[38;5;175m"
    ORCHID: str = "\x1b[38;5;176m"
    JACARANDA_PINK: str = "\x1b[38;5;177m"
    GOLD: str = "\x1b[38;5;178m"
    HOKEY_POKEY: str = "\x1b[38;5;179m"
    ANTIQUE_BRASS: str = "\x1b[38;5;180m"
    EUNRY: str = "\x1b[38;5;181m"
    LILIAC: str = "\x1b[38;5;182m"
    MAUVE: str = "\x1b[38;5;183m"
    CORN: str = "\x1b[38;5;184m"
    EARLS_GREEN: str = "\x1b[38;5;185m"
    KHAKI: str = "\x1b[38;5;186m"
    PINE_GLADE: str = "\x1b[38;5;187m"
    GHOST: str = "\x1b[38;5;188m"
    PERIWINKLE: str = "\x1b[38;5;189m"
    RED: str = "\x1b[38;5;196m"
    TORCH_RED: str = "\x1b[38;5;197m"
    VALENTINE_SKY: str = "\x1b[38;5;198m"
    DEEP_PINK: str = "\x1b[38;5;199m"
    SHOCKING_PINK: str = "\x1b[38;5;200m"
    MAGENTA: str = "\x1b[38;5;201m"
    SCARLET: str = "\x1b[38;5;202m"
    RED_ORANGE: str = "\x1b[38;5;203m"
    RADICAL_RED: str = "\x1b[38;5;204m"
    WILD_STRAWBERRY: str = "\x1b[38;5;205m"
    RAZZLE_DAZZLE: str = "\x1b[38;5;206m"
    PINK_OVERFLOW: str = "\x1b[38;5;207m"
    BLAZE_ORANGE: str = "\x1b[38;5;208m"
    OUTRAGEOUS_ORANGE: str = "\x1b[38;5;209m"
    BITTERSWEET: str = "\x1b[38;5;210m"
    STRAWBERRY: str = "\x1b[38;5;211m"
    HOT_PINK: str = "\x1b[38;5;212m"
    PINK_FLAMINGO: str = "\x1b[38;5;213m"
    ORANGE_PEEL: str = "\x1b[38;5;214m"
    NEON_CARROT: str = "\x1b[38;5;215m"
    ATOMIC_TANGARINE: str = "\x1b[38;5;216m"
    MONA_LISA: str = "\x1b[38;5;217m"
    CORNATION_PINK: str = "\x1b[38;5;218m"
    LAVENDER_ROSE: str = "\x1b[38;5;219m"
    SUPERNOVA: str = "\x1b[38;5;220m"
    SUNGLOW: str = "\x1b[38;5;221m"
    GOLDEN_TAINOI: str = "\x1b[38;5;222m"
    PEACH_ORANGE: str = "\x1b[38;5;223m"
    YOUR_PINK: str = "\x1b[38;5;224m"
    BUBBLE_GUM: str = "\x1b[38;5;225m"
    YELLOW: str = "\x1b[38;5;226m"
    DAFFODIL: str = "\x1b[38;5;227m"
    LASER_LEMON: str = "\x1b[38;5;228m"
    PALE_CANARY: str = "\x1b[38;5;229m"
    CREAM: str = "\x1b[38;5;230m"
    WHITE: str = "\x1b[38;5;231m"
    NEARLY_BLACK: str = "\x1b[38;5;232m"
    EERIE_BLACK: str = "\x1b[38;5;233m" 
    OIL: str = "\x1b[38;5;234m"
    BALTIC_SEA: str = "\x1b[38;5;235m"
    THUNDER: str = "\x1b[38;5;236m"
    IRIDIUM: str = "\x1b[38;5;237m"
    CHARCOAL: str = "\x1b[38;5;238m"
    GRAVEL: str = "\x1b[38;5;239m"
    CARBON_GREY: str = "\x1b[38;5;240m"
    STORM_DUST: str = "\x1b[38;5;241m"
    FLINT: str = "\x1b[38;5;242m"
    BOULDER: str = "\x1b[38;5;243m"
    HURRICANE: str = "\x1b[38;5;244m"
    GUN_SMOKE: str = "\x1b[38;5;245m"
    GREY: str = "\x1b[38;5;246m"
    STAR_DUST: str = "\x1b[38;5;247m"
    ALUMINIUM: str = "\x1b[38;5;248m"
    NOBEL: str = "\x1b[38;5;249m"
    DUST: str = "\x1b[38;5;250m"
    CLOUD: str = "\x1b[38;5;251m"
    LIGHT_SILVER: str = "\x1b[38;5;252m"
    LIGHT_GREY: str = "\x1b[38;5;253m"
    PLATINUM: str = "\x1b[38;5;254m"
    COTTON: str = "\x1b[38;5;255m"

@dataclass
class Background255:
    """If you cannot see colors, try Background16."""

    BLACK: str = "\x1b[48;5;16m"
    STRATOS: str = "\x1b[48;5;17m"
    FUZZY_WUZZY: str = "\x1b[48;5;18m"
    BLUE_GRAY: str = "\x1b[48;5;19m"
    DARK_BLUE: str = "\x1b[48;5;20m"
    BLUE: str = "\x1b[48;5;21m"
    DEEP_FIR: str = "\x1b[48;5;22m"
    DEEP_TEAL: str = "\x1b[48;5;23m"
    MIDNIGHT_BLUE: str = "\x1b[48;5;24m"
    SMALT: str = "\x1b[48;5;25m"
    ABSOLUTE_ZERO: str = "\x1b[48;5;26m"
    CANARY: str = "\x1b[48;5;27m"
    CAMARONE: str = "\x1b[48;5;28m"
    FUN_GREEN: str = "\x1b[48;5;29m"
    BLUE_STONE: str = "\x1b[48;5;30m"
    BAHAMA_BLUE: str = "\x1b[48;5;31m"
    SCIENCE_BLUE: str = "\x1b[48;5;32m"
    BLUE_RIBBON: str = "\x1b[48;5;33m"
    JAPANESE_LAUREL: str = "\x1b[48;5;34m"
    TOMB_BLUE: str = "\x1b[48;5;35m"
    GREEN_HAZE: str = "\x1b[48;5;36m"
    PERSIAN_GREEN: str = "\x1b[48;5;37m"
    PACIFIC_BLUE: str = "\x1b[48;5;38m"
    AZURE_RADIANCE: str = "\x1b[48;5;39m"
    GREEN: str = "\x1b[48;5;40m"
    MALACHITE: str = "\x1b[48;5;41m"
    JADE: str = "\x1b[48;5;42m"
    CARIBBEAN_GREEN: str = "\x1b[48;5;43m"
    EGG_BLUE: str = "\x1b[48;5;44m"
    CYAN: str = "\x1b[48;5;45m"
    GREEN: str = "\x1b[48;5;46m"
    LIGHT_GREEN: str = "\x1b[48;5;47m"
    SPRING_GREEN: str = "\x1b[48;5;48m"
    GREEN_GAS: str = "\x1b[48;5;49m"
    BRIGHT_TURQUOISE: str = "\x1b[48;5;50m"
    AQUA: str = "\x1b[48;5;51m"
    TEMPTRESS: str = "\x1b[48;5;52m"
    BAROSSA: str = "\x1b[48;5;53m"
    CHRISTALLE: str = "\x1b[48;5;54m"
    PIGMENT_INDIGO: str = "\x1b[48;5;55m"
    VIOLET_BLUE: str = "\x1b[48;5;56m"
    ULTRAMARINE: str = "\x1b[48;5;57m"
    MADRAS: str = "\x1b[48;5;58m"
    MINE_SHAFT: str = "\x1b[48;5;59m"
    RHINO: str = "\x1b[48;5;60m"
    COSMIC_COBALT: str = "\x1b[48;5;61m"
    GOVERNOR_BAY: str = "\x1b[48;5;62m"
    LIGHT_ROYAL_BLUE: str = "\x1b[48;5;63m"
    VERDUN_GREEN: str = "\x1b[48;5;64m"
    KILLARNEY: str = "\x1b[48;5;65m"
    CASAL: str = "\x1b[48;5;66m"
    BDAZZLED_BLUE: str = "\x1b[48;5;67m"
    DENIM: str = "\x1b[48;5;68m"
    ULTRAMARINE_BLUE: str = "\x1b[48;5;69m"
    LIMEADE: str = "\x1b[48;5;70m"
    APPLE: str = "\x1b[48;5;71m"
    ILLUMINATING_EMERALD: str = "\x1b[48;5;72m"
    LOCHINVAR: str = "\x1b[48;5;73m"
    MOONSTONE: str = "\x1b[48;5;74m"
    DODGER_BLUE: str = "\x1b[48;5;75m"
    HARLEQUIN: str = "\x1b[48;5;76m"
    DARK_LIME: str = "\x1b[48;5;77m"
    EMERALD: str = "\x1b[48;5;78m"
    SHAMROCK: str = "\x1b[48;5;79m"
    TURQUOISE_PEARL: str = "\x1b[48;5;80m"
    SKY_BLUE: str = "\x1b[48;5;81m"
    POISON_GREEN: str = "\x1b[48;5;82m"
    LIME_LASER: str = "\x1b[48;5;83m"
    SCREAMIN_GREEN: str = "\x1b[48;5;84m"
    EVA_GREEN: str = "\x1b[48;5;85m"
    AURICHALCITE: str = "\x1b[48;5;86m"
    BRIGHT_CYAN: str = "\x1b[48;5;87m"
    LONESTAR: str = "\x1b[48;5;88m"
    TYRIAN_PURPLE: str = "\x1b[48;5;89m"
    POMPADOUR: str = "\x1b[48;5;90m"
    DARK_MAGENTA: str = "\x1b[48;5;91m"
    PURPLE: str = "\x1b[48;5;92m"
    ELECTRIC_VIOLET: str = "\x1b[48;5;93m"
    NUTMEG_WOOD: str = "\x1b[48;5;94m"
    BUCCANEER: str = "\x1b[48;5;95m"
    COSMIC: str = "\x1b[48;5;96m"
    EMINENCE: str = "\x1b[48;5;97m"
    PURPLE_HEART: str = "\x1b[48;5;98m"
    ROYAL_PURPLE: str = "\x1b[48;5;99m"
    MUSTARD: str = "\x1b[48;5;100m"
    JUNGLE: str = "\x1b[48;5;101m"
    GRANITE_GRAY: str = "\x1b[48;5;102m"
    AMETHYST: str = "\x1b[48;5;103m"
    INDIGO: str = "\x1b[48;5;104m"
    BLUEBERRY: str = "\x1b[48;5;105m"
    VENOM_GREEN: str = "\x1b[48;5;106m"
    WASABI: str = "\x1b[48;5;107m"
    HIGHLAND: str = "\x1b[48;5;108m"
    PATINA: str = "\x1b[48;5;109m"
    DANUBE: str = "\x1b[48;5;110m"
    CORNFLOWER_BLUE: str = "\x1b[48;5;111m"
    ALIEN_ARMPIT: str = "\x1b[48;5;112m"
    ATLANTIS: str = "\x1b[48;5;113m"
    MANTIS: str = "\x1b[48;5;114m"
    GREEN_PEARL: str = "\x1b[48;5;115m"
    DOWNY: str = "\x1b[48;5;116m"
    MALIBU: str = "\x1b[48;5;117m"
    BRIGHT_GREEN: str = "\x1b[48;5;118m"
    SPRING_FROST: str = "\x1b[48;5;119m"
    LIME: str = "\x1b[48;5;120m" 
    DRAGON_GREEN: str = "\x1b[48;5;121m"
    AQUAMARINE: str = "\x1b[48;5;122m"
    ELECTRIC_BLUE: str = "\x1b[48;5;123m"
    RED_BERRY: str = "\x1b[48;5;124m"
    PAPRIKA: str = "\x1b[48;5;125m"
    FRESH_EGGPLANT: str = "\x1b[48;5;126m"
    FLIRT: str = "\x1b[48;5;127m"
    DARK_VIOLET: str = "\x1b[48;5;128m"
    PLATINUM_PURPLE: str = "\x1b[48;5;129m"
    OREGON: str = "\x1b[48;5;130m"
    STILETTO: str = "\x1b[48;5;131m"
    ROUGE: str = "\x1b[48;5;132m"
    PLUM: str = "\x1b[48;5;133m"
    NEON_MAGENTA: str = "\x1b[48;5;134m"
    GRAPE: str = "\x1b[48;5;135m"
    CHELSEA_GEM: str = "\x1b[48;5;136m"
    METALLIC_SUNBURST: str = "\x1b[48;5;137m"
    COPPER_ROSE: str = "\x1b[48;5;138m"
    STRIKEMASTER: str = "\x1b[48;5;139m"
    MEDIUM_PURPLE: str = "\x1b[48;5;140m"
    HELIOTROPE: str = "\x1b[48;5;141m"
    SOUP: str = "\x1b[48;5;142m"
    SYNCAMORE: str = "\x1b[48;5;143m"
    AVOCADO: str = "\x1b[48;5;144m"
    QUICK_SILVER: str = "\x1b[48;5;145m"
    BLUE_BELL: str = "\x1b[48;5;146m"
    MELROSE: str = "\x1b[48;5;147m"
    SHEEN_GREEN: str = "\x1b[48;5;148m"
    PEA: str = "\x1b[48;5;149m"
    WILD_WILLOW: str = "\x1b[48;5;150m"
    DE_YORK: str = "\x1b[48;5;151m"
    SINBAD: str = "\x1b[48;5;152m"
    ANAKIWA: str = "\x1b[48;5;153m"
    CHARTREUSE: str = "\x1b[48;5;154m"
    GREEN_YELLOW: str = "\x1b[48;5;155m"
    LIGHT_LIME: str = "\x1b[48;5;156m"
    MINT: str = "\x1b[48;5;157m"
    LIGHT_AQUAMARINE: str = "\x1b[48;5;158m"
    WINTER_WIZARD: str = "\x1b[48;5;159m"
    GUARDSMAN_RED: str = "\x1b[48;5;160m"
    MONZA: str = "\x1b[48;5;161m"
    LIPSTICK: str = "\x1b[48;5;162m"
    HOLLYWOOD_CERISE: str = "\x1b[48;5;163m"
    PURPLE_PIZZA: str = "\x1b[48;5;164m"
    PINK_PURPLE: str = "\x1b[48;5;165m"
    GRENADIER: str = "\x1b[48;5;166m"
    PERSIAN_RED: str = "\x1b[48;5;167m"
    JAZZBERRY_JAM: str = "\x1b[48;5;168m"
    MEDIUM_RED_VIOLET: str = "\x1b[48;5;169m"
    FUCHSIA_PINK: str = "\x1b[48;5;170m"
    NEON_PURPLE: str = "\x1b[48;5;171m"
    ORANGE: str = "\x1b[48;5;172m"
    TUSCANY: str = "\x1b[48;5;173m"
    CHESSNUT_ROSE: str = "\x1b[48;5;174m"
    HOPBRUSH: str = "\x1b[48;5;175m"
    ORCHID: str = "\x1b[48;5;176m"
    JACARANDA_PINK: str = "\x1b[48;5;177m"
    GOLD: str = "\x1b[48;5;178m"
    HOKEY_POKEY: str = "\x1b[48;5;179m"
    ANTIQUE_BRASS: str = "\x1b[48;5;180m"
    EUNRY: str = "\x1b[48;5;181m"
    LILIAC: str = "\x1b[48;5;182m"
    MAUVE: str = "\x1b[48;5;183m"
    CORN: str = "\x1b[48;5;184m"
    EARLS_GREEN: str = "\x1b[48;5;185m"
    KHAKI: str = "\x1b[48;5;186m"
    PINE_GLADE: str = "\x1b[48;5;187m"
    GHOST: str = "\x1b[48;5;188m"
    PERIWINKLE: str = "\x1b[48;5;189m"
    RED: str = "\x1b[48;5;196m"
    TORCH_RED: str = "\x1b[48;5;197m"
    VALENTINE_SKY: str = "\x1b[48;5;198m"
    DEEP_PINK: str = "\x1b[48;5;199m"
    SHOCKING_PINK: str = "\x1b[48;5;200m"
    MAGENTA: str = "\x1b[48;5;201m"
    SCARLET: str = "\x1b[48;5;202m"
    RED_ORANGE: str = "\x1b[48;5;203m"
    RADICAL_RED: str = "\x1b[48;5;204m"
    WILD_STRAWBERRY: str = "\x1b[48;5;205m"
    RAZZLE_DAZZLE: str = "\x1b[48;5;206m"
    PINK_OVERFLOW: str = "\x1b[48;5;207m"
    BLAZE_ORANGE: str = "\x1b[48;5;208m"
    OUTRAGEOUS_ORANGE: str = "\x1b[48;5;209m"
    BITTERSWEET: str = "\x1b[48;5;210m"
    STRAWBERRY: str = "\x1b[48;5;211m"
    HOT_PINK: str = "\x1b[48;5;212m"
    PINK_FLAMINGO: str = "\x1b[48;5;213m"
    ORANGE_PEEL: str = "\x1b[48;5;214m"
    NEON_CARROT: str = "\x1b[48;5;215m"
    ATOMIC_TANGARINE: str = "\x1b[48;5;216m"
    MONA_LISA: str = "\x1b[48;5;217m"
    CORNATION_PINK: str = "\x1b[48;5;218m"
    LAVENDER_ROSE: str = "\x1b[48;5;219m"
    SUPERNOVA: str = "\x1b[48;5;220m"
    SUNGLOW: str = "\x1b[48;5;221m"
    GOLDEN_TAINOI: str = "\x1b[48;5;222m"
    PEACH_ORANGE: str = "\x1b[48;5;223m"
    YOUR_PINK: str = "\x1b[48;5;224m"
    BUBBLE_GUM: str = "\x1b[48;5;225m"
    YELLOW: str = "\x1b[48;5;226m"
    DAFFODIL: str = "\x1b[48;5;227m"
    LASER_LEMON: str = "\x1b[48;5;228m"
    PALE_CANARY: str = "\x1b[48;5;229m"
    CREAM: str = "\x1b[48;5;230m"
    WHITE: str = "\x1b[48;5;231m"
    NEARLY_BLACK: str = "\x1b[48;5;232m"
    EERIE_BLACK: str = "\x1b[48;5;233m" 
    OIL: str = "\x1b[48;5;234m"
    BALTIC_SEA: str = "\x1b[48;5;235m"
    THUNDER: str = "\x1b[48;5;236m"
    IRIDIUM: str = "\x1b[48;5;237m"
    CHARCOAL: str = "\x1b[48;5;238m"
    GRAVEL: str = "\x1b[48;5;239m"
    CARBON_GREY: str = "\x1b[48;5;240m"
    STORM_DUST: str = "\x1b[48;5;241m"
    FLINT: str = "\x1b[48;5;242m"
    BOULDER: str = "\x1b[48;5;243m"
    HURRICANE: str = "\x1b[48;5;244m"
    GUN_SMOKE: str = "\x1b[48;5;245m"
    GREY: str = "\x1b[48;5;246m"
    STAR_DUST: str = "\x1b[48;5;247m"
    ALUMINIUM: str = "\x1b[48;5;248m"
    NOBEL: str = "\x1b[48;5;249m"
    DUST: str = "\x1b[48;5;250m"
    CLOUD: str = "\x1b[48;5;251m"
    LIGHT_SILVER: str = "\x1b[48;5;252m"
    LIGHT_GREY: str = "\x1b[48;5;253m"
    PLATINUM: str = "\x1b[48;5;254m"
    COTTON: str = "\x1b[48;5;255m"

async def _delete_colors() -> None:
    """Helper function to delete colors, do not modify unless you know what you are doing!"""
    for datacls in [Foreground16, Background16, Foreground255, Background255]:
        for color in asdict(datacls).keys():
            setattr(datacls, color, "")

async def manual_color_handler() -> None:
    """
    Ask the user if they want to see colors.
    """
    ask: str = input("Display colours (y/Y or n/N)? (Your console/terminal needs to support ANSI colours): ").lower()
    while True:   
        if ask == "y":
            return 
        elif ask == "n":
            return await _delete_colors()
        else:
            ask = input(f"`{ask}` is not a valid argument. Write only 'y/Y' or 'n/N'. Display colours?: ").lower()  

async def auto_color_handler() -> None:
    """
    Automatically detects if the terminal/console supports colors.
    ### Sometimes `stdout.isatty` can be wrong.
    """
    if not sys.stdout.isatty():
        return await _delete_colors()

async def rgb_to_ansi(r: int = 0, g: int = 0, b: int = 0, option: Literal["fg", "bg"] = "fg") -> str:
    """
    Converts RGB values to ANSI colors.
    ### This requires terminal that supports `Truecolor` (24-bit RGB)
    
    ### Parameters:
    - `r` - value for `RED` (0-255). Defaults to `0`.
    - `g` - value for `GREEN` (0-255). Defaults to `0`.
    - `b` - value for `BLUE` (0-255). Defaults to `0`.
    - `option` - Either "bg" (background) or "fg" (foreground). Defaults to "fg".

    ### Returns:
    - ANSI `string` representing that color.
    """
    return f"\x1b[{"38" if option == "fg" else "48"};2;{r};{g};{b}m"

async def rem_colors(s: str) -> str:
    """
    Removes ANSI code from the string.

    ### Parameters:
    - `s` - String that needs removal of ANSI code.

    ### Returns:
    - `String` without ANSI code
    """
    return ANSI_PATTERN.sub("", s)

async def display(cls: Style | Foreground16 | Foreground255 | Background16 | Background255) -> None:
    """
    Displays color/style and name of specified dataclass.
    """
    if isinstance(cls, type):
        cls = cls()
    
    for style, value in asdict(cls).items():
        print(f"{value}{style:^25}{Style.RESET}")
