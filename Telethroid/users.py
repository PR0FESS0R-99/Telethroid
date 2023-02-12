def anonymous_id(message):
  return message.from_user.id if message.from_user else None

def anonymous_first_name(message):
  return message.from_user.first_name if message.from_user else None

def anonymous_last_name(message):
  return message.from_user.last_name  if message.from_user else None

def anonymous_username (message):
  return message.from_user.username  if message.from_user else None

def anonymous_language_codemessage):
  return message.from_user.language_code if message.from_user else None

def anonymous_dc_id(message):
  return message.from_user.dc_id if message.from_user else None

def anonymous_mention(message):
  return message.from_user.mention if message.from_user else None
