class Anonymous(object):
    def id(message):
        return message.from_user.id if message.from_user else None

    def first(message):
      return message.from_user.first_name if message.from_user else None

    def last(message):
      return message.from_user.last_name  if message.from_user else None

    def username(message):
      return message.from_user.username  if message.from_user else None

    def lang_code(message):
      return message.from_user.language_code if message.from_user else None

    def dc_id(message):
      return message.from_user.dc_id if message.from_user else None

    def mention(message):
      return message.from_user.mention if message.from_user else None
