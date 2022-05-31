# Database columns.
COLUMNS = {
    "QUESTION_ADD": ("category", "level", "question", "option1", "option2", "option3", "option4", "answer", "explanation","id"),
    "QUESTION_GET": ("mode", "num", "userid"),
    "DEFINITION_ADD": ("item", "definition", "aliases"),
    "DEFINITION_GET": ("input",),
    "ADD_CORRECT_QUESTION": ("userid", "questionid"),
}