def list_benefits():
    return ["More organized code", "More readable code", "Easier code reuse",
            "Allowing programmers to share and connect code together"]


def build_sentence(info):
    return info + " is a benefit of functions!"


print(list_benefits())
print(build_sentence("Organization"))
