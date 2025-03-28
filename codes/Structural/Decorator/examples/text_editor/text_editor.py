from abc import ABC, abstractmethod


# Component
class TextEditor(ABC):
    @abstractmethod
    def render(self, text):
        pass


# ConcreteComponent
class SimpleTextEditor(TextEditor):
    def render(self, text):
        return text


# Decorator
class TextEditorDecorator(TextEditor):
    def __init__(self, editor: TextEditor):
        self._editor = editor

    def render(self, text):
        return self._editor.render(text)


# ConcreteDecoratorA: add line numbers
class LineNumberingDecorator(TextEditorDecorator):
    def render(self, text):
        rendered_text = self._editor.render(text)
        lines = rendered_text.split("\n")
        numbered_lines = [f"{i + 1}: {line}" for i, line in enumerate(lines)]
        return "\n".join(numbered_lines)


# ConcreteDecoratorB: uppercase
class UpperCaseDecorator(TextEditorDecorator):
    def render(self, text):
        rendered_text = self._editor.render(text)
        return rendered_text.upper()


# ConcreteDecoratorC: add border
class BorderDecorator(TextEditorDecorator):
    def __init__(self, editor: TextEditor, border_height=1, border_char="*"):
        super().__init__(editor)
        self._border_height = border_height
        self._border_char = border_char

    def render(self, text):

        rendered_text = self._editor.render(text)
        max_char_in_line = max(map(len, rendered_text.split("\n")))
        border = self._border_char * (max_char_in_line + self._border_height * 4 + 1)
        bordered_text = f"{border}\n" * self._border_height
        for line in rendered_text.split("\n"):
            if len(line) < max_char_in_line:
                line += " " * (max_char_in_line - len(line))
            bordered_text += f"{(self._border_char + " ") * self._border_height} {line} {(self._border_char + " ") * self._border_height}\n"
        bordered_text += f"{border}\n" * self._border_height
        return bordered_text


def main():
    text = "hi, my name is amir\ni am 27\ni love programming\ni love my job"

    basic_editor = SimpleTextEditor()

    editor_with_lines = LineNumberingDecorator(basic_editor)

    editor_with_lines_and_uppercase = UpperCaseDecorator(editor_with_lines)

    fully_decorated_editor = BorderDecorator(editor_with_lines_and_uppercase, 2, "+")
    print(fully_decorated_editor.render(text))


if __name__ == "__main__":
    main()
