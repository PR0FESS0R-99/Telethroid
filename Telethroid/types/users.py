class User(object):
    def id(message):
        return message.from_user.id

    def first(message):
      return message.from_user.first_name

    def last(message):
      return message.from_user.last_name

    def username(message):
      return message.from_user.username

    def lang_code(message):
      return message.from_user.language_code

    def dc_id(message):
      return message.from_user.dc_id

    def mention(message):
      return message.from_user.mention
