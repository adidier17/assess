import os 

def predict():
    """
    """

    text_extracted = "Text Extracted"
    dir_path = os.path.dirname(os.path.realpath(__file__))
    with open(os.path.join(dir_path, 'SOW-TacCOM.txt')) as f:
        text_extracted = f.read()
    #text_used = [(0,10), (11,20)]
    references = ["ISO/IEC 27032:2012", "ISO/IEC 27039:2015"]
    predictions = [
        {
            "field": "35",
            "group": "030",
            "subgroup": "",
            "standards": [
                {
                    "id": "ISO/IEC 27032:2012",
                    "score": "1.0"
                },
                {
                    "id": "ISO/IEC 27039:2015",
                    "score": "1.0"
                },
                {
                    "id": "ISO/IEC 29147:2014",
                    "score": "1.0"
                }
            ]
        },
        {
            "field": "03",
            "group": "100",
            "subgroup": "70",
            "standards": [
                {
                    "id": "ISO/IEC 27005:2011",
                    "score": "1.0"
                },
                {
                    "id": "ISO/IEC 27002:2013",
                    "score": "1.0"
                }
            ]
        }
    ]

    result = {
        "text_extracted": text_extracted,
        "references": references,
        "predictions": predictions
    }

    return result
