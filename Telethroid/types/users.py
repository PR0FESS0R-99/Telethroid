from .mode import Mode

class User(object):
    def id(update):
        return update.from_user.id

    def first(update):
      return update.from_user.first_name

    def last(update):
      return update.from_user.last_name

    def username(update):
      return update.from_user.username

    def lang_code(update):
      return update.from_user.language_code

    def dc_id(update):
      return update.from_user.dc_id

    def mention(update):
      return update.from_user.mention

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
