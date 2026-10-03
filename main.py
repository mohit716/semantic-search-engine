from langchain_core.documents import Document

documents = [
    Document(
        page_content="Dogs are great companions, known for their loyalty and friendliness.",
        metadata={"source": "mammal-pets-doc"},
    ),
    Document(
        page_content="Cats are independent pets that often enjoy their own space.",
        metadata={"source": "mammal-pets-doc"},
    ),
]


documetns2 = [
    Document(
        page_content="a great studnet and a great person",
        metadata={"source": "student-doc"},
    )
    Document(
        page_content="a great teacher and a great person",
        metadata={"source": "teacher-doc"},
    )
]

document3= [
    Document(
        page_content="the constitution guarantees right to equality""
        metadata={source: "constitution-doc"},
    )
]