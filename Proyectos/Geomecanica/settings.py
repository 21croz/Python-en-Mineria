def to_hex(tup):
    return "#{:02X}{:02X}{:02X}".format(*tup)


COLOR = {
    'BLACK': (0, 0, 0),
    'WHITE': (255, 255, 255),
    'RED': (255, 0, 0),
    'RED0': (255, 200, 200),
    'RED1': (255, 160, 160),
    'RED2': (255, 120, 120),
    'RED3': (255, 80, 80),
    'RED4': (255, 40, 40),
    'RED5': (255, 0, 0),
    'RED6': (200, 0, 0),
    'RED7': (160, 0, 0),
    'RED8': (120, 0, 0),
    'RED9': (80, 0, 0),
    'RED10': (40, 0, 0),
    'GREEN': (0, 255, 0),
    'GREEN0': (200, 255, 200),
    'GREEN1': (160, 255, 160),
    'GREEN2': (120, 255, 120),
    'GREEN3': (80, 255, 80),
    'GREEN4': (40, 255, 40),
    'GREEN5': (0, 255, 0),
    'GREEN6': (0, 200, 0),
    'GREEN7': (0, 160, 0),
    'GREEN8': (0, 120, 0),
    'GREEN9': (0, 80, 0),
    'GREEN10': (0, 40, 0),
    'BLUE': (0, 0, 255),
    'BLUE0': (200, 200, 255),
    'BLUE1': (160, 160, 255),
    'BLUE2': (120, 120, 255),
    'BLUE3': (80, 80, 255),
    'BLUE4': (40, 40, 255),
    'BLUE5': (0, 0, 255),
    'BLUE6': (0, 0, 200),
    'BLUE7': (0, 0, 160),
    'BLUE8': (0, 0, 120),
    'BLUE9': (0, 0, 80),
    'BLUE10': (0, 0, 40),
    'YELLOW': (255, 255, 0),
    'YELLOW0': (255, 255, 200),
    'YELLOW1': (255, 255, 160),
    'YELLOW2': (255, 255, 120),
    'YELLOW3': (255, 255, 80),
    'YELLOW4': (255, 255, 40),
    'YELLOW5': (255, 255, 0),
    'YELLOW6': (200, 200, 0),
    'YELLOW7': (160, 160, 0),
    'YELLOW8': (120, 120, 0),
    'YELLOW9': (80, 80, 0),
    'YELLOW10': (40, 40, 0),
    'ORANGE': (255, 160, 0),
    'PURPLE': (255, 0, 255),
    'CYAN': (0, 255, 255),
    'PINK': (255, 0, 255),
    'BROWN': (150, 75, 0),
    'GRAY': (200, 200, 200),
    'GRAY0': (200, 200, 200),
    'GRAY1': (160, 160, 160),
    'GRAY2': (120, 120, 120),
    'GRAY3': (80, 80, 80),
    'GRAY4': (40, 40, 40)
}

BG_COLOR = to_hex(COLOR['GRAY4'])

style_title = {
    'bg': BG_COLOR,
    'fg': to_hex(COLOR['WHITE']),
    'font': ('Times New Roman', 24, 'bold')
}
style_subtitle = {
    'bg': BG_COLOR,
    'fg': to_hex(COLOR['WHITE']),
    'font': ('Times New Roman', 18, 'bold')
}
style_label_options = {
    'bg': BG_COLOR,
    'fg': to_hex(COLOR['WHITE']),
    'font': ('Helvetica', 10)
}
style_label_result = {
    'bg': BG_COLOR,
    'fg': to_hex(COLOR['WHITE']),
    'font': ('Helvetica', 12, 'bold')
}
style_entry = {
    'bg': to_hex(COLOR['WHITE']),
    'fg': to_hex(COLOR['BLACK']),
    'width': 10,
    'font': ('Helvetica', 10),
    'justify': 'center'
}