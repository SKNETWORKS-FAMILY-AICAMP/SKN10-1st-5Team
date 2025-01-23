import enum

class INSERT_SQLs(enum.Enum):
  FAQ = (enum.auto(), """
  insert {faq_name}(COMPANY_ID, CATEGORIE, QUESTION, ANSWER)
  values({COMPANY_ID}, '{CATEGORIE}', '{QUESTION}', '{ANSWER}')
  """, 'FAQ 데이터 저장')

class COMPANY(enum.Enum):
  현대 : 0
  기아 : 1