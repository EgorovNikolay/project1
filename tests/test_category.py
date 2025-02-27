def test_category_initialization(sample_categories):
    assert sample_categories[0].name == "Смартфоны"
    assert len(sample_categories[0].products) == 3
    assert sample_categories[1].name == "Телевизоры"
    assert len(sample_categories[1].products) == 1
