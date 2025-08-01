schedule_json = {
    "11A": {
        "monday": ["География", "Алгебра", "Русский язык", "Русский язык", "ИП", "Алгебра", "Обществознание", "ДРЯ"],
        "tuesday": ["Физика", "Химия", "Литература", "История", "История", "Физкультура", "Английский", "История"],
        "wednesday": ["Литература", "Английский", "Информатика", "Геометрия", "Физика", "История Церкви"],
        "thursday": ["Русский язык", "Алгебра", "Физкультура", "Литература", "Биология", "Обществознание", "Русский язык", "РВ"],
        "friday": ["Геометрия", "ОПВ", "ОБЖ", "Литература", "Литература", "Английский", "ЦСЯ/Литургика", "География"],
        "saturday": ["История"]
    },
    "11B": {
        "monday": ["Русский язык", "Русский язык", "Алгебра", "Обществознание", "География", "Алгебра", "ИП"],
        "tuesday": ["Химия", "История", "История", "Литература", "Физика", "Английский", "ДРЯ", "История"],
        "wednesday": ["Информатика", "Литература", "Английский", "История Церкви", "Геометрия", "Физкультура", "РВ"],
        "thursday": ["Биология", "Физкультура", "Алгебра", "Физика", "Русский язык", "Литература", "Русский язык"],
        "friday": ["Литература", "ОБЖ", "ОПВ", "Геометрия", "География", "Литература", "Английский", "ЦСЯ/Литургика"],
        "saturday": ["История", "История", "История", "Обществознание"]
    },
    "11V": {
        "monday": ["История", "История", "История", "Физкультура", "Алгебра", "Русский язык", "Русский язык", "География"],
        "tuesday": ["Литература", "Химия", "Информатика", "География", "Физика", "ОПВ"],
        "wednesday": ["Английский", "Английский", "Литература", "ИП", "Физика", "Геометрия", "РВ"],
        "thursday": ["Литература", "Литература", "Алгебра", "Алгебра", "Биология", "Физкультура", "Обществознание", "Русский язык"],
        "friday": ["Английский", "Литература", "Литература", "ОБЖ", "Геометрия", "Обществознание"],
        "saturday": []
    }
}
EN_TO_RU_subjects = {
    "rv": "РВ",
    "obzh": "ОБЖ",
    "geography": "География",
    "fizra": "Физкультура",
    "literature": "Литература",
    "history_of_church": "История Церкви",
    "english": "Английский",
    "ip": "ИП",
    "chemistry": "Химия",
    "dra" : "ДРЯ",
    "russian": "Русский язык",
    "csya_lityrgika": "ЦСЯ/Литургика",
    "biology": "Биология",
    "informatics": "Информатика",
    "society": "Обществознание",
    "history": "История",
    "physics": "Физика",
    "opv": "ОПВ",
    "alg": "Алгебра",
    "geom": "Геометрия"
}
RU_TO_EN_subjects = {v: k for k, v in EN_TO_RU_subjects.items()}
# - class_name
# - schedule - {"weekday" : [subject, subject,...],...}
# - homeworks - {"subject": {"data": ["homework", ...], ...},...}
# - owner
# - admins

def get_schedule_with_class(class_name: str) -> dict:
    array = schedule_json[class_name]
    res = {}
    for i in array.keys():
        subjects = []
        for j in array[i]:
            subjects.append(RU_TO_EN_subjects[j])
        res[i] = subjects
    return res
