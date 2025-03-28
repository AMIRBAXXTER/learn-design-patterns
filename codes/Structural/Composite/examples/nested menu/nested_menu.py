from abc import ABC, abstractmethod
from blessings import Terminal

t = Terminal()


# Component: رابط پایه برای آیتم‌های منو
class MenuComponent(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def display(self, indent=0):
        pass

    def add(self, component: "MenuComponent"):
        print(t.red(f"Cannot add to {self.__class__.__name__}"))

    def remove(self, component: "MenuComponent"):
        print(t.red(f"Cannot remove from {self.__class__.__name__}"))


# Leaf: آیتم ساده منو (یک لینک یا عمل خاص)
class MenuItem(MenuComponent):
    def __init__(self, name, action):
        """
        name: نام آیتم منو
        action: عملی که هنگام انتخاب آیتم انجام می‌شود
        """
        super().__init__(name)
        self.action = action

    def display(self, indent=0):
        # نمایش آیتم منو با رنگ سبز
        print(t.green(" " * indent + f"Menu Item: {self.name} --> Action: {self.action}"))


# Composite: منو مرکب که شامل آیتم‌ها یا زیرمنوهای دیگر است
class Menu(MenuComponent):
    def __init__(self, name):
        super().__init__(name)
        self.children = []

    def add(self, component: MenuComponent):
        self.children.append(component)

    def remove(self, component: MenuComponent):
        self.children.remove(component)

    def display(self, indent=0):
        # نمایش منو با رنگ آبی
        print(f'{" " * indent}{t.red("-")}{t.blue(f"Menu: {self.name}")}')
        for child in self.children:
            child.display(indent + 4)


def main():
    # ایجاد آیتم‌های ساده منو
    item1 = MenuItem("Open File", "open_file()")
    item2 = MenuItem("Save File", "save_file()")
    item3 = MenuItem("Exit", "exit_app()")

    # ایجاد زیرمنو
    submenu = Menu("File Operations")
    submenu.add(item1)
    submenu.add(item2)
    submenu.add(item3)

    # آیتم‌های دیگر
    item4 = MenuItem("Copy", "copy()")
    item5 = MenuItem("Paste", "paste()")

    # ایجاد یک منوی اصلی
    main_menu = Menu("Main Menu")
    main_menu.add(submenu)
    main_menu.add(item4)
    main_menu.add(item5)

    # نمایش ساختار منو
    print(t.bold("Menu Structure:"))
    main_menu.display()


if __name__ == "__main__":
    main()
