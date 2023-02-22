class Chats(object):
    def id(message):
      return message.chat.id

    def type(message):
      return message.chat.type

    def title(message):
      return message.chat.title

    def username(message):
      return message.chat.username

    def photo(message):
      return message.chat.photo

    def description(message):
      return message.chat.description

    def dc_id(message):
      return message.chat.dc_id

    def has_protected_content(message):
      return message.chat.has_protected_content

    def invite_link(message):
      return message.chat.invite_link

    def pinned_message(message):
      return message.chat.pinned_message

    def members_count(message):
      return message.chat.members_count
