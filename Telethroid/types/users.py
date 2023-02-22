class User(object):
    def ID(message):
        return message.from_user.id if message.from_user else None

    def FIRST(message):
      return message.from_user.first_name if message.from_user else None

    def LAST(message):
      return message.from_user.last_name  if message.from_user else None

    def USERNAME(message):
      return message.from_user.username  if message.from_user else None

    def LANG_CODE(message):
      return message.from_user.language_code if message.from_user else None

    def DC_ID(message):
      return message.from_user.dc_id if message.from_user else None

    def MENTION(message):
      return message.from_user.mention if message.from_user else None
