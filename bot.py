from pyrogram import Client, Filters
app = Client("745460463:AAEiAf0M0cMZSRWXFrgotuZETEx-mJYZIYA",814511,"44462f0f278503255d5cc30941b617a9")
bullet = -1001157455913
ferrari = -1001274887387 
k = -1001306730083

@app.on_message(Filters.chat(ferrari) & ~ Filters.edited)
def main(client, message):
 mes = client.send_message( k, "**" + message.text + "**" )
 fille = open("ids.txt","r")
 n = fille.readlines()
 fille.close()
 for t in n:
  fie = open("ids.txt","w")
  fie.write(t +" " + str(message.message_id) + " " + str(mes.message_id))
  fie.close()

@app.on_message(Filters.chat(bullet) & ~ Filters.edited)
def main(client, message):
 mes = client.send_message( k, "**" + message.text + "**" )
 fille = open("ids.txt","r")
 n = fille.readlines()
 fille.close()
 for t in n:
   fie = open("ids.txt","w")
   fie.write(t +" " + str(message.message_id) + " " + str(mes.message_id))
   fie.close()

@app.on_message(Filters.chat(ferrari) & Filters.edited)
def main(client, message):
   files = open("ids.txt" , "r")
   d = files.readlines()
   files.close()
   for c in d:
    x = c.split()
    id = str(message.message_id)
    if id in x:
      client.edit_message_text(k,int(x[x.index(id)+1]), "**" + message.text + "**" )

     
@app.on_message(Filters.chat(bullet) & Filters.edited)
def main(client, message):
 files = open("ids.txt" , "r")
 d = files.readlines()
 files.close()
 for c in d:
  x = c.split()
  id = str(message.message_id)
  if id in x:
   client.edit_message_text(k , int(x[x.index(id)+1]), "**" + message.text + "**" )
     


@app.on_message(Filters.command('clear') & Filters.user(491634139))
def forward(client, message):
 fie = open("ids.txt","w")
 fie.write("001 002")
 fie.close()
 message.reply("☢️ Done, Editing data cleared ✅✅")


@app.on_message(Filters.command('get') & Filters.user(491634139) )
def forward(client, message):
 if len(message.text.split(' ')) > 1:
  if len(message.text.split(' ')[1]) == 14:
      x = client.get_chat(int(message.text.split(' ')[1])).title
      message.reply("📶 This chat name is - "+str(x)+" ✅")
  else:
    message.reply("💼 Please write a valid chat id. ✅✅ ")
 else:
    message.reply("💼 Please write a valid chat id. ✅✅ ")

@app.on_message(Filters.command("start"))
def forward(client, message):
 if message.from_user.id == 491634139:
   message.reply("♻️ Welcome to your LineBot . ✅✅")
 else:
   message.reply("♻️ You need admins permission to use my functions. ✅✅")

@app.on_message(Filters.private)
def forward(client, message):
 if not message.from_user.id == 491634139:
   message.reply("♻️ You need admins permission to use my functions. ✅✅")

app.run()
