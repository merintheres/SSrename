from ssrename.filename_generator import FilenameGenerator

def test_filename_not_empty():
    gen = FilenameGenerator()
    name = gen.generate("this is a test document")
    assert name

def test_filename_format():
    gen = FilenameGenerator(max_words=3)
    name = gen.generate("Hello World From Python")
    assert "_" in name
    assert name.islower()
