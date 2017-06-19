from yattag import Doc

doc, tag, text = Doc(
    defaults = {'ingredient': ['chocolate', 'coffee']}
).tagtext()

with tag('form', action = ""):
    with tag('label'):
        text("Select one or more ingredients")
    with doc.select(name = 'ingredient', multiple = "multiple"):
        for value, description in (
            ("chocolate", "Dark chocolate"),
            ("almonds", "Roasted almonds"),
            ("honey", "Acacia honey"),
            ("coffee", "Ethiopian coffee")
        ):
            with doc.option(value = value):
                text(description)
    doc.stag('input', type = "submit", value = "Validate")

print(doc.getvalue())