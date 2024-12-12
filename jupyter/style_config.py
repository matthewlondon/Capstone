# Colors for dark mode
COLORS = {
    'primary': '#569cd6',
    'secondary': '#dcdcaa',
    'highlight': '#c586c0',
    'grid': '#2d2d2d',
    'background': '#1e1e1e',
    'text': '#d4d4d4',
}

# Font sizes
FONT_SIZES = {
    'title': 16,
    'axes': 12,
    'ticks': 10,
    'annotations': 9
}

# Gridline style
GRID_STYLE = {
    'color': COLORS['grid'],
}

# Default figure size
FIGURE_SIZE = (12, 8)

# Apply the dark mode style globally
def apply_dark_mode_style():
    import matplotlib.pyplot as plt

    plt.rcParams.update({
        'figure.facecolor': COLORS['background'],
        'axes.facecolor': COLORS['background'],
        'axes.edgecolor': COLORS['text'],
        'axes.labelcolor': COLORS['text'],
        'xtick.color': COLORS['text'],
        'ytick.color': COLORS['text'],
        'grid.color': COLORS['grid'],
        'text.color': COLORS['text'],
        'legend.frameon': False,
        'legend.facecolor': 'inherit',
        'legend.edgecolor': 'inherit',
        'lines.color': COLORS['primary'],
        'patch.edgecolor': COLORS['background'],
        'font.size': 12
    })
