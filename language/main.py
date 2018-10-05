import errors_messages
import configuration as config

# todo create a auto - detect user language
if config.DEFAULT_LANGUAGE == "en":
    import language.en as lang
elif config.DEFAULT_LANGUAGE == "fr":
    pass
else:
    raise ValueError(errors_messages.ERROR_LANGUAGE)

TITLE = lang.TITLE
DESCRIPTION = lang.DESCRIPTION
INSTRUCTION_MESSAGE = lang.INSTRUCTION_MESSAGE
INSTRUCTION_MESSAGE2 = lang.INSTRUCTION_MESSAGE2
WORD_MATCH_MSG = lang.WORD_MATCH_MSG
WORD_NOT_MATCH_MSG = lang.WORD_NOT_MATCH_MSG
BUTTON_TEXT = lang.BUTTON_TEXT
