import vpython
import random
import string
import errors_messages
import configuration as config
import language.main as lang

FIXING_POSITION = -12
ASCII_CVT = 48
ENTER_KEY = 13
KEYPAD = range(96, 106)

SHAPE_ROTATE_ANGLE = 90
COLORS = (vpython.color.white, vpython.color.red, vpython.color.green, vpython.color.blue, vpython.color.yellow,
          vpython.color.orange)
COLORS_TO_CODE = {"<1, 0, 0>": "red", "<0, 1, 0>": "green", "<0, 0, 1>": "blue", "<1, 1, 0>": "yellow",
                  "<1, 0.6, 0>": "orange", "<1, 1, 1>": "white"}
DELETE_KEYS = ("delete", "backspace")
KEY_RECOGNIZE_BY = "keydown"
DESCRIPTION_OF_KEYS = ("right", "left", "up", "down", "alt", "ctrl", "shift", "caps lock", "tab", "esc", "home", "end",
                       "pageup", "pagedown", "insert", "backspace", "delete")
SHAPE_TYPES = ("box", "cone", "cylinder", "pyramid", "sphere")
TEXTURES = (vpython.textures.flower, vpython.textures.granite, vpython.textures.gravel, vpython.textures.earth,
            vpython.textures.metal, vpython.textures.rock, vpython.textures.rough, vpython.textures.rug,
            vpython.textures.stones, vpython.textures.stucco, vpython.textures.wood, vpython.textures.wood_old)
TEXT_BOX_STYLE = "<p style='width:150px; border:20px solid Tomato; color:blue;'>"
ALIGN = "center"


def get_random_word():
    """
    creating the captcha word
    :return: a random word
    """
    word_length = random.randint(config.RANDOM_WORD_MIN_LEN, config.RANDOM_WORD_MAX_LEN)
    rand_word = list()
    i = 0
    while i < word_length:
        if random.choice([True] * config.WORD_NUMBER_RATIO + [False]):
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
        return vpython.box(size=config.SHAPE_SIZE, axis=config.SHAPE_AXIS)
    elif shape_type == SHAPE_TYPES[1]:
        return vpython.cone(size=config.SHAPE_SIZE, axis=config.SHAPE_AXIS)
    elif shape_type == SHAPE_TYPES[2]:
        return vpython.cylinder(size=config.SHAPE_SIZE, axis=config.SHAPE_AXIS)
    elif shape_type == SHAPE_TYPES[3]:
        return vpython.pyramid(size=config.SHAPE_SIZE, axis=config.SHAPE_AXIS)
    elif shape_type == SHAPE_TYPES[4]:
        return vpython.sphere(size=config.SHAPE_SIZE, axis=config.SHAPE_AXIS)
    else:
        raise ValueError(errors_messages.ERROR_SHAPE)


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
    text = vpython.text(text=get_random_word(), color=get_random_color(), pos=vpython.vector(
        -config.DISTANCE_BETWEEN_SHAPE + shape_number * config.DISTANCE_BETWEEN_SHAPE, 0, 0),
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
        raise ValueError(errors_messages.ERROR_CONVERT_COLOR)


def create_all_shapes():
    """
    create the all shapes & texts on the canvas
    :return: the captcha text object, shape type that the text in it, and the color of that shape
    """
    shape_list = [get_random_shape() for i in range(config.NUMBER_OF_SHAPE)]
    color_use = list()
    start_position = -config.DISTANCE_BETWEEN_SHAPE
    for shape in shape_list:
        if type(shape) in (vpython.pyramid, vpython.cone, vpython.cylinder):
            shape.pos = vpython.vector(start_position, FIXING_POSITION, 0)
        else:
            shape.pos = vpython.vector(start_position, 0, 0)
        shape.rotate(angle=SHAPE_ROTATE_ANGLE)
        shape_random_color = check_color_used(color_use)
        shape.color = shape_random_color
        color_use.append(shape_random_color)
        shape.texture = get_random_texture()
        start_position += config.DISTANCE_BETWEEN_SHAPE
    text_list = [build_text(pos) for pos in range(config.NUMBER_OF_SHAPE)]
    random_choice = random.randint(0, config.NUMBER_OF_SHAPE - 1)
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
    if word == text_box.text[config.TEXT_BOX_STYLE_LEN:]:
        result.text = lang.WORD_MATCH_MSG
        word_valid_do()
    else:
        result.text = lang.WORD_NOT_MATCH_MSG
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
    elif (key_press in DELETE_KEYS) and len(text_box.text) > config.TEXT_BOX_STYLE_LEN:
        text_box.text = text_box.text[:-1]  # erase a letter
    elif key_press in DESCRIPTION_OF_KEYS:
        pass  # ignore "saved words"
    elif len(text_box.text) > config.TEXT_BOX_STYLE_LEN + config.RANDOM_WORD_MAX_LEN:
        pass  # don't allow to use more chars then RANDOM_WORD_MAX_LEN
    elif key_location in KEYPAD:
        text_box.text += (chr(key_location - ASCII_CVT))
    else:
        text_box.text += key_press


def show_instruction():
    """
    show the instruction massage to user: which shape's type and color to pick
    :return: None
    """
    vpython.text(text=lang.INSTRUCTION_MESSAGE, color=vpython.color.red, pos=vpython.vector(-25, 25, 0),
                 height=3)
    vpython.text(text=chosen_shape + lang.INSTRUCTION_MESSAGE2 + str(shape_color),
                 color=vpython.color.red,
                 pos=vpython.vector(-25, 20, 0), height=3)


def form_box():
    """
    this function handle the form box
    :return: None
    """
    text_box.text = TEXT_BOX_STYLE
    scene.bind(KEY_RECOGNIZE_BY, key_input)
    vpython.button(bind=word_checker, text=lang.BUTTON_TEXT)


# main part
scene = vpython.canvas(title=lang.TITLE,
                       width=config.WINDOW_WIDTH, height=config.WINDOW_HEIGHT,
                       background=vpython.color.black)
scene.append_to_caption(lang.DESCRIPTION)
info = create_all_shapes()
word = info[0]
chosen_shape = info[1]
shape_color = info[2]
text_box = vpython.wtext()
result = vpython.wtext()
show_instruction()
form_box()
