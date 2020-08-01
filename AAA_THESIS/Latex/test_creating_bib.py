import pytest
from get_cite_bib import replace_article_id_with_label


def test_replace_article_id_with_label_1():
    exported_citation = "@ARTICLE{sdf:w34243, }"

    data = dict(label= "FixMatch",
                exported_citation=exported_citation)

    expected_output= "@ARTICLE{FixMatch, }"

    result = replace_article_id_with_label(**data)
    assert expected_output == result

def test_replace_article_id_with_label():
    exported_citation = """@ARTICLE{2020arXiv200107685S,
                        author = {{Sohn}, Kihyuk and {Berthelot}, David and {Li}, Chun-Liang and
                        {Zhang}, Zizhao and {Carlini}, Nicholas and {Cubuk}, Ekin D. and
                        {Kurakin}, Alex and {Zhang}, Han and {Raffel}, Colin},
                        title = "{FixMatch: Simplifying Semi-Supervised Learning with Consistency and Confidence}",
                        journal = {arXiv e-prints},
                        keywords = {Computer Science - Machine Learning, Computer Science - Computer Vision and Pattern Recognition, Statistics - Machine Learning},
                        year = 2020,
                        month = jan,
                        eid = {arXiv:2001.07685},
                        pages = {arXiv:2001.07685},
                        archivePrefix = {arXiv},
                        eprint = {2001.07685},
                        primaryClass = {cs.LG},
                        adsurl = {https://ui.adsabs.harvard.edu/abs/2020arXiv200107685S},
                        adsnote = {Provided by the SAO/NASA Astrophysics Data System}}""" 

    data = dict(label= "FixMatch",
                exported_citation=exported_citation)

    expected_output= """@ARTICLE{FixMatch,
                        author = {{Sohn}, Kihyuk and {Berthelot}, David and {Li}, Chun-Liang and
                        {Zhang}, Zizhao and {Carlini}, Nicholas and {Cubuk}, Ekin D. and
                        {Kurakin}, Alex and {Zhang}, Han and {Raffel}, Colin},
                        title = "{FixMatch: Simplifying Semi-Supervised Learning with Consistency and Confidence}",
                        journal = {arXiv e-prints},
                        keywords = {Computer Science - Machine Learning, Computer Science - Computer Vision and Pattern Recognition, Statistics - Machine Learning},
                        year = 2020,
                        month = jan,
                        eid = {arXiv:2001.07685},
                        pages = {arXiv:2001.07685},
                        archivePrefix = {arXiv},
                        eprint = {2001.07685},
                        primaryClass = {cs.LG},
                        adsurl = {https://ui.adsabs.harvard.edu/abs/2020arXiv200107685S},
                        adsnote = {Provided by the SAO/NASA Astrophysics Data System}}""" 
    result = replace_article_id_with_label(**data)
    assert expected_output == result 
