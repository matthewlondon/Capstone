# Colors for dark mode
COLORS = {
    'primary': '#569cd6',  # Skyblue-like color for dark mode
    'secondary': '#dcdcaa',  # Light yellow for accents
    'highlight': '#c586c0',  # Purple for highlights
    'grid': '#2d2d2d',       # Dark gray for gridlines
    'background': '#1e1e1e', # VSCode dark mode background
    'text': '#d4d4d4',       # Light gray text
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
    'linestyle': '--',
    'linewidth': 0.5,
    'alpha': 0.7
}

# Default figure size
FIGURE_SIZE = (10, 6)

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
