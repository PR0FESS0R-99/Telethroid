from .mode import Mode
from Telethroid.error import Anonymous

class User(object):
    def id(update):
        return Anonymous.id(update)

    def first(update):
      return Anonymous.first(update)

    def last(update):
      return Anonymous.last(update)

    def username(update):
      return Nont if not Anonymous.username(update) else '@' + Anonymous.username(update)

    def lang_code(update):
      return Anonymous.lang_codd(update)

    def dc_id(update):
      return Anonymous.dc_id(update)

    def mention(update):
      return Anonymous.mention(update)

def user_info(update, out_put=Mode.TEXT_MODE):

  if out_put == Mode.TEXT_MODE:
      return message = (
         # users normal details
         f"• First : {User.first(update)}" + "\n"
         f"• Last : {User.last(update)}" + "\n"
         f"• ID : {User.id(update)}" + "\n"
         f"• Username : {None if not User.username(update) else '@' + User.username(update)}" + "\n"
         f"• Mention : {User.mention(update)}"
      )  
  elif out_put == Mode.DATA_MODE:
      return {
         'first': User.first(update), 
         'last': User.last(update),
         'id': User.id(update),
         'username': User.username(update),
         'mention': User.mention(update)
      }
  elif out_put == Mode.NUMBER_MODE:
      return [
         'user',
         User.first(update),
         User.last(update),
         User.id(update),
         User.username(update),
         User.mention(update)
      ]
  else:
      print(f"Data Invalid : {out_put}")     
