import vpython
import random
import string

WORD_NUMBER_RATIO = 3
ASCII_CVT = 48
ENTER_KEY = 13
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 60
KEYPAD = range(96, 106)
TEXT_BOX_STYLE_LEN = 62
RANDOM_WORD_MAX_LEN = 10
RANDOM_WORD_MIN_LEN = 5
NUMBER_OF_SHAPE = 3
DISTANCE_BETWEEN_SHAPE = 30
SHAPE_SIZE = vpython.vector(25, 25, 25)
SHAPE_AXIS = vpython.vector(0, 1, 0)
SHAPE_ROTATE_ANGLE = 90
COLORS = (vpython.color.white, vpython.color.red, vpython.color.green, vpython.color.blue, vpython.color.yellow,
          vpython.color.orange)
COLORS_TO_CODE = {"<1, 0, 0>": "red", "<0, 1, 0>": "green", "<0, 0, 1>": "blue", "<1, 1, 0>": "yellow",
                  "<1, 0.6, 0>": "orange", "<1, 1, 1>": "white"}
DELETE_KEYS = ("delete", "backspace")
DESCRIPTION_OF_KEYS = ("right", "left", "up", "down", "alt", "ctrl", "shift", "caps lock", "tab", "esc", "home", "end",
                       "pageup", "pagedown", "insert", "backspace", "delete")
SHAPE_TYPES = ("box", "cone", "cylinder", "pyramid", "sphere")
TEXTURES = (vpython.textures.flower, vpython.textures.granite, vpython.textures.gravel, vpython.textures.earth,
            vpython.textures.metal, vpython.textures.rock, vpython.textures.rough, vpython.textures.rug,
            vpython.textures.stones, vpython.textures.stucco, vpython.textures.wood, vpython.textures.wood_old)
TITLE = "Are you Human?"
DESCRIPTION = "Right button drag or Ctrl-drag to rotate 'camera' to view scene.\n" \
              "To zoom, drag with middle button or Alt/Option depressed, or use scroll wheel.\n" \
              "On a two-button mouse, middle is left + right.\n" \
              "Shift-drag to pan left/right and up/down.\n" \
              "Touch screen: pinch/extend to zoom, swipe or two-finger rotate."
INSTRUCTION_MESSAGE = "please enter the word in the "
INSTRUCTION_MESSAGE2 = " with color "
TEXT_BOX_STYLE = "<p style='width:150px; border:20px solid Tomato; color:blue;'>"
WORD_MATCH_MSG = "Word Match!"
WORD_NOT_MATCH_MSG = "Word NOT Match!"
BUTTON_TEXT = "submit!"
KEY_RECOGNIZE_BY = "keydown"
ALIGN = "center"
ERROR_SHAPE = "a chosen shape not supported"
ERROR_CONVERT_COLOR = "error with convert color code to color"


def get_random_word():
    """
    creating the captcha word
    :return: a random word
    """
    word_length = random.randint(RANDOM_WORD_MIN_LEN, RANDOM_WORD_MAX_LEN)
    rand_word = list()
    i = 0
    while i < word_length:
        if random.choice([True] * WORD_NUMBER_RATIO + [False]):
            rand_word.append(random.choice(string.ascii_letters))
        else:
            rand_word.append(random.choice(string.digits))
        i += 1
    return "".join(rand_word)


def get_random_shape():
    """
    :return: a created random shape
    """
    shape_type = random.choice(SHAPE_TYPES)
    if shape_type == SHAPE_TYPES[0]:
        return vpython.box(size=SHAPE_SIZE, axis=SHAPE_AXIS)
    elif shape_type == SHAPE_TYPES[1]:
        return vpython.cone(size=SHAPE_SIZE, axis=SHAPE_AXIS)
    elif shape_type == SHAPE_TYPES[2]:
        return vpython.cylinder(size=SHAPE_SIZE, axis=SHAPE_AXIS)
    elif shape_type == SHAPE_TYPES[3]:
        return vpython.pyramid(size=SHAPE_SIZE, axis=SHAPE_AXIS)
    elif shape_type == SHAPE_TYPES[4]:
        return vpython.sphere(size=SHAPE_SIZE, axis=SHAPE_AXIS)
    else:
        raise ValueError(ERROR_SHAPE)


def get_random_color():
    """
    :return: a random color
    """
    return random.choice(COLORS)


def check_color_used(color_use):
    """
    :param color_use: list of color that already been used
    :return: a random color that hasn't used
    """
    color = get_random_color()
    while color in color_use:
        color = get_random_color()
    return color


def get_random_texture():
    """
    :return: a random texture
    """
    return random.choice(TEXTURES)


def build_text(shape_number):
    """
    creating a text's shape
    :param shape_number: the index number of the shape that the text will be inside it
    :return: a text's shape object
    """
    text = vpython.text(text=get_random_word(), color=get_random_color(),
                        pos=vpython.vector(-DISTANCE_BETWEEN_SHAPE + shape_number * DISTANCE_BETWEEN_SHAPE, 0, 0),
                        billboard=True, align=ALIGN)
    return text


def convert_code_to_color(color_code):
    """
    convert rgb color's code to color name
    :param color_code: rgb color's code
    :return: a color name
    """
    try:
        return COLORS_TO_CODE[color_code]
    except KeyError:
        raise ValueError(ERROR_CONVERT_COLOR)


def create_all_shapes():
    """
    create the all shapes & texts on the canvas
    :return: the captcha text object, shape type that the text in it, and the color of that shape
    """
    shape_list = [get_random_shape() for i in range(NUMBER_OF_SHAPE)]
    color_use = list()
    start_position = -DISTANCE_BETWEEN_SHAPE
    for shape in shape_list:
        if type(shape) in (vpython.pyramid, vpython.cone, vpython.cylinder):
            shape.pos = vpython.vector(start_position, -12, 0)  # fixing shapes align to be the same line
        else:
            shape.pos = vpython.vector(start_position, 0, 0)
        shape.rotate(angle=SHAPE_ROTATE_ANGLE)
        shape_random_color = check_color_used(color_use)
        shape.color = shape_random_color
        color_use.append(shape_random_color)
        shape.texture = get_random_texture()
        start_position += DISTANCE_BETWEEN_SHAPE
    text_list = [build_text(pos) for pos in range(NUMBER_OF_SHAPE)]
    random_choice = random.randint(0, NUMBER_OF_SHAPE - 1)
    # get the shape and color name to display msg
    shape_type = str(type(shape_list[random_choice])).split(".")[2]
    shape_type = shape_type.split("'")[0]
    shape_type = shape_type.replace('"', "")
    color = convert_code_to_color(str(shape_list[random_choice].color))

    return text_list[random_choice].text, shape_type, color


def word_valid_do():
    """
    your function to do when the user enter correct answer
    :return:
    """
    pass


def word_invalid_do():
    """
    your function to do when the user enter incorrect answer
    :return:
    """
    pass


def word_checker():
    """
    this function check if the word that the user enter are in/correct
    :return: None
    """
    if word == text_box.text[TEXT_BOX_STYLE_LEN:]:
        result.text = WORD_MATCH_MSG
        word_valid_do()
    else:
        result.text = WORD_NOT_MATCH_MSG
        word_invalid_do()


def key_input(event):
    """
    recognize the key that the user been press.
    keys that in DESCRIPTION_OF_KEYS are ignore.
    also it not allow to write a word with more then RANDOM_WORD_MAX_LEN length
    :param event: event that accrue due the key press
    :return: None
    """
    key_press = event.key
    key_location = event.which
    if key_location is ENTER_KEY:
        word_checker()
    elif (key_press in DELETE_KEYS) and len(text_box.text) > TEXT_BOX_STYLE_LEN:
        text_box.text = text_box.text[:-1]  # erase a letter
    elif key_press in DESCRIPTION_OF_KEYS:
        pass  # ignore "saved words"
    elif len(text_box.text) > TEXT_BOX_STYLE_LEN + RANDOM_WORD_MAX_LEN:
        pass
    elif key_location in KEYPAD:
        text_box.text += (chr(key_location - ASCII_CVT))
    else:
        text_box.text += key_press


# main part
scene = vpython.canvas(title=TITLE,
                       width=WINDOW_WIDTH, height=WINDOW_HEIGHT,
                       background=vpython.color.black)
scene.append_to_caption(DESCRIPTION)
info = create_all_shapes()
word = info[0]
chosen_shape = info[1]
shape_color = info[2]

# msg part
message = vpython.text(text=INSTRUCTION_MESSAGE, color=vpython.color.red, pos=vpython.vector(-25, 25, 0),
                       height=3)
text1 = vpython.text(text=chosen_shape + INSTRUCTION_MESSAGE2 + str(shape_color),
                     color=vpython.color.red,
                     pos=vpython.vector(-25, 20, 0), height=3)

# answer part
text_box = vpython.wtext()
result = vpython.wtext()
text_box.text = TEXT_BOX_STYLE
scene.bind(KEY_RECOGNIZE_BY, key_input)

button = vpython.button(bind=word_checker, text=BUTTON_TEXT)
