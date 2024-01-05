from typing import List

from project.category import Category
from project.document import Document
from project.topic import Topic


class Storage:

    def __init__(self):
        self.categories: List[Category] = []
        self.topics: List[Topic] = []
        self.documents: List[Document] = []

    def add_category(self, category: Category) -> None:
        if category not in self.categories:
            self.categories.append(category)

    def add_topic(self, topic: Topic) -> None:
        if topic not in self.topics:
            self.topics.append(topic)

    def add_document(self, document: Document) -> None:
        if document not in self.documents:
            self.documents.append(document)

    def edit_category(self, category_id: int, new_name: str) -> None:
        category = [c for c in self.categories if category_id == c.id][0]
        category.edit(new_name)

    def edit_topic(self, topic_id: int, new_topic: str, new_storage_folder: str) -> None:
        topic = [t for t in self.topics if topic_id == t.id][0]
        topic.edit(new_topic, new_storage_folder)

    def edit_document(self, document_id: int, new_file_name: str) -> None:
        document = [d for d in self.documents if document_id == d.id][0]
        document.edit(new_file_name)

    def delete_category(self, category_id) -> None:
        category = [c for c in self.categories if category_id == c.id][0]
        self.categories.remove(category)

    def delete_topic(self, topic_id: int) -> None:
        topic = [t for t in self.topics if topic_id == t.id][0]
        self.topics.remove(topic)

    def delete_document(self, document_id: int) -> None:
        document = [d for d in self.documents if document_id == d.id][0]
        self.documents.remove(document)

    def get_document(self, document_id) -> Document:
        return [d for d in self.documents if document_id == d.id][0]

    def __repr__(self):
        res = ''
        for c in self.documents:
            res += f'{c}\n'

        return res
