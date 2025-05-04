class Subsection:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Subsection: {self.name}"


class Section:
    def __init__(self, name):
        self.name = name
        self.subsections = []

    def add_subsection(self, subsection):
        self.subsections.append(subsection)

    def __str__(self):
        return f"Section: {self.name}"

    def print_sections(self):
        print(f"{self}")
        for subsection in self.subsections:
            print(f"  {subsection}")


class Chapter:
    def __init__(self, name):
        self.name = name
        self.sections = []

    def add_section(self, section):
        self.sections.append(section)

    def __str__(self):
        return f"Chapter: {self.name}"

    def print_chapters(self):
        print(f"{self}")
        for section in self.sections:
            section.print_sections()


class Book:
    def __init__(self, name):
        self.name = name
        self.chapters = []

    def add_chapter(self, chapter):
        self.chapters.append(chapter)

    def __str__(self):
        return f"Book: {self.name}"

    def print_book(self):
        print(f"{self}")
        for chapter in self.chapters:
            chapter.print_chapters()


# Create subsections
sub1 = Subsection("Subsection 1.1")
sub2 = Subsection("Subsection 1.2")
sub3 = Subsection("Subsection 2.1")

# Create sections and add subsections
section1 = Section("Section 1")
section1.add_subsection(sub1)
section1.add_subsection(sub2)

section2 = Section("Section 2")
section2.add_subsection(sub3)

# Create chapters and add sections
chapter1 = Chapter("Chapter 1")
chapter1.add_section(section1)

chapter2 = Chapter("Chapter 2")
chapter2.add_section(section2)

# Create a book and add chapters
book = Book("My Book")
book.add_chapter(chapter1)
book.add_chapter(chapter2)

# Print the tree structure
book.print_book()
