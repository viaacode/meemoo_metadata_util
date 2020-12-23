import re
datatypes = {
    # cm/s
    "RECORD_SPEED": {
        "regex": r"^[+-]?([0-9]*[.])?[0-9]+\s+cm\/s$",
        "pos_test": [
            "3 cm/s",
            "03 cm/s",
            "3.4 cm/s",
            "4.75 cm/s",
            "04.75 cm/s"
        ],
        "neg_test": [
            "4",
            "s",
            "word",
            "4,5",
            "4.5",
            "4,5 cm/s",
            "4,5cm/s",
        ]
    },

    "FREE_TEXT": {
        "regex": r"[\s\S]*"
    },

    "DATE": {
        "regex": r"^([0-9]{4})(-?)(1[0-2]|0[1-9])\2(3[01]|0[1-9]|[12][0-9])$"
    },

    "TIME": {
        "regex": r"^(2[0-3]|[01][0-9]):?([0-5][0-9]):?([0-5][0-9])(Z|[+-](?:2[0-3]|[01][0-9])(?::?(?:[0-5][0-9]))?)$"
    },

    "DATETIME": {
        "regex": r"^([0-9]{4})(-)?(1[0-2]|0[1-9])(?(2)-)(3[01]|0[1-9]|[12][0-9])(2[0-3]|[01][0-9])(?(2):)([0-5][0-9])(?(2):)([0-5][0-9])$"
    },

    "DURATION": {
        "regex": r"^(([01]\d|2[0-4])(?::([0-5]\d)(?::((?:[0-5]\d|60))(.\d{1,9})?)?)?)?$"
    },

    "FLOAT": {
        "regex": r"^[+-]?([0-9]*[.])?[0-9]+$"
    },

    "INT": {
        "regex": r"^[-+]?[0-9]+$"
    },

    "IEC60094": {
        "value_set": ["I", "II", "III", "IV"]
    },

    "LANGUAGE": {
        "value_set": ["nl", "fr", "de", "it", "en", "es", "aa", "ab", "ae", "af", "ak", "am", "an", "ar", "as", "av", "ay", "az", "ba", "be", "bg", "bh", "bi", "bm", "bn", "bo", "br", "bs", "ca", "ce", "ch", "co", "cr", "cs", "cu", "cv", "cy", "da", "dv", "dz", "ee", "el", "eo", "et", "eu", "fa", "ff", "fi", "fj", "fo", "fy", "ga", "gd", "gl", "gn", "gu", "gv", "ha", "he", "hi", "ho", "hr", "ht", "hu", "hy", "hz", "ia", "id", "ie", "ig", "ii", "ik", "io", "is", "iu", "ja", "jv", "ka", "kg", "ki", "kj", "kk", "kl", "km", "kn", "ko", "kr", "ks", "ku", "kv", "kw", "ky", "la", "lb", "lg", "li", "ln", "lo", "lt", "lu", "lv", "mg", "mh", "mi", "mk", "ml", "mn", "mo", "mr", "ms", "mt", "my", "na", "nb", "nd", "ne", "ng", "nn", "no", "nr", "nv", "ny", "oc", "oj", "om", "or", "os", "pa", "pi", "pl", "ps", "pt", "qu", "rm", "rn", "ro", "ru", "rw", "sa", "sc", "sd", "se", "sg", "sh", "si", "sk", "sl", "sm", "sn", "so", "sq", "sr", "ss", "st", "su", "sv", "sw", "ta", "te", "tg", "th", "ti", "tk", "tl", "tn", "to", "tr", "ts", "tt", "tw", "ty", "ug", "uk", "ur", "uz", "ve", "vi", "vo", "wa", "wo", "xh", "yi", "yo", "za", "zh", "zu"]
    },

    "SUCCEEDED": {
        "value_set": ["OK", "NOT OK"]
    },


    "ASPECT_RATIO": {
        "regex": r"[0-9]+x[0-9]+$"
    },

    "MD5": {
        "regex": r"^[a-fA-F0-9]{32}$",
        "flags": [re.I]
    },

    "ISO_DURATION": {
        "regex": r"^(-?)P(?=.)((\d+)Y)?((\d+)M)?((\d+)D)?(T(?=.)((\d+)H)?((\d+)M)?(\d*(\.\d+)?S)?)?$"
    },

    "VIAA_LICENSE": {
        "value_set": [
            "VIAA-ONDERWIJS",
            "VIAA-ONDERZOEK",
            "VIAA-BIBLIOTHEKEN",
            "VIAA-INTRAMUROS",
            "VIAA-INTRA_CP-CONTENT",
            "VIAA-INTRA_CP-METADATA-ALL",
            "VIAA-PUBLIEK-METADATA-LTD",
            "VIAA-PUBLIEK-METADATA-ALL",
            "VIAA-PUBLIEK-CONTENT",
            "Publiek domein",
            "CC-BY-SA-METADATA",
            "CC-BY-SA-CONTENT",
            "CC BY-ND-METADATA",
            "CC BY-ND-CONTEN",
            "CC BY-NC-METADATA",
            "CC BY-NC-CONTENT",
            "CC BY-NC-ND-METADATA",
            "CC BY-NC-ND-CONTENT",
            "CC BY-NC-SA-METADATA",
            "CC BY-NC-SA-CONTENT"]
    },

    "XML_DATETIME": {
        "regex": r"^(-?(?:[1-9][0-9]*)?[0-9]{4})-(1[0-2]|0[1-9])-(3[01]|0[1-9]|[12][0-9])T(2[0-3]|[01][0-9]):([0-5][0-9]):([0-5][0-9])(\.[0-9]+)?(Z|[+-](?:2[0-3]|[01][0-9]):[0-5][0-9])?$"
    },

    "CORE_REEL": {
        "value_set": ["kern", "spoel"]
    },

    "TIME_CODE": {
        "regex": r"^(?:(?:[0-1][0-9]|[0-2][0-3]):)(?:[0-5][0-9]:){2}(?:[0-2][0-9])$"
    },

    "PRESERVATION_PROBLEMS": {
        "value_set": [
            "perforation damage"
            "Edge Damage",
            "Emulsion Scratching",
            "Base Scratching",
            "Image Fading",
            "vinegar",
            "% of shrinking",
            "Warpage",
            "splices",
            "worn",
            "glue remains",
            "mold",
            "nitrate-degradation",
            "deformation",
            "Other",
            "None"
        ]
    },

    "FORMAT": {
        "value_set": [
            "ACC Audiocassette",
            "AKF Andere Kleine Formaten(Golf 6)",
            "BMX Betamax",
            "BSP Betacam SP",
            "BSX Betacam SX",
            "BTC Betacam oxide",
            "CDR cd-r",
            "DBE Digital betacam",
            "ORV Open Spoel video",
            "QIA Kwartduim audiotape",
            "SLD Shellac - en Lakplaat",
            "UMA U-matic",
            "VCR VCR",
            "VHS VHS",
            "WCL wax cylinder",
            "WRE wire recording"
        ]
    }
}
