class Category:
    def __init__(self, ident: int, name: str):
        self.id = ident
        self.name = name

    def edit(self, new_name: str) -> None:
        self.name = new_name

    def __repr__(self) -> str:
        return f"Category {self.id}: {self.name}"
