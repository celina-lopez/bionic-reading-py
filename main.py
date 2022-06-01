import ebooklib
from ebooklib import epub

def return_num_of_bolded_letters(word):
  length_of_word = len(word)
  if length_of_word <= 1:
    return 0
  elif length_of_word == 2:
    return 1
  elif length_of_word == 3: 
    return 2
  elif length_of_word > 6:
    return 3
  else:
    return length_of_word - 2


def chapter_to_str(chapter):
  soup = BeautifulSoup(chapter.get_body_content(), "html.parser")
  text = [para.get_text() for para in soup.find_all("p")]
  return " ".join(text)


def read_epub(book):
  items = list(book.get_items_of_type(ebooklib.ITEM_DOCUMENT))
  chapters = {}
  for item in items:
    item_id = item.get_id()
    chapters[item_id] = chapter_to_str(item)
  return chapters


def bionic_word(word):
  end = return_num_of_bolded_letters(word)
  return "<b>" + word[0:end] + "</b>" + word[end:len(word)]


def create_bionic_text(text):
  words = text.split(' ')
  bionic_words = []
  for word in words: 
    bionic_words.append(bionic_word(word))
  return " ".join(bionic_words)


def create_bionic_book(file_name):
  book = epub.read_epub(file_name)
  chapter_by_id = read_epub(book)
  for chapter_id in chapter_by_id:
    content = create_bionic_text(chapter_by_id[chapter_id])
    book.get_item_with_id(chapter_id).set_content(content)
  # saves to path
  epub.write_epub(file_name + '_bionic.epub', book, {})

  
# file_name = "path/to/file"
# create_bionic_book(file_name)
