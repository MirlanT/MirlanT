def article_validate(title, author, content, status):
    errors = {}
    if not title:
        errors["title"] = "Поле обязательное символов"
    elif len(title) > 50:
        errors["title"] = "Поле должно быть меньше 50 символов"
    if not author:
        errors["author"] = "Поле обязательное"
    elif len("author") > 50:
        errors["author"] = "Поле должно быть меньше 50 символов"
    if not content:
        errors["content"] = "Поле обязательное"
    elif len(author) > 2000:
        errors["content"] = "Поле должно быть меньше 50 символов"
    if not status:
        errors["status"] = "Поле обязательное"
    return errors
