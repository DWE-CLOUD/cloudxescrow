from telegram.ext import (
    Updater,
    CommandHandler,
    CallbackQueryHandler,
    ConversationHandler,
    MessageHandler,
    CallbackContext,
)

from telegram.ext import filters
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
list1=["♡ @GirishFr ✿",'♡ @Garvit33 ✿','♡ @EvoHardik ✿','♡ @rdffyt1 ✿']
ESCROW_NUM, NAME, AMOUNT, DESCRIPTION, SELLER, ESCROW, TIME = range(7)
dict1={}
list3=[]
list4=[]
dict2={}
def start1(update: Update, context: CallbackContext):
    if update.effective_chat.type == "private":
        update.message.reply_text("""Welcome to Dwos Escrow Bot :)
        
Following Rules to be followed : 
        
1 ) First make sure to affirm deal then only conclude with escrow , don't waste time 
        
2 ) All deals are secured and registered for best interest of all
         
3 ) A escrow fee would be charged and would be added in the contract as per escrower
        
4 ) Be Timely and prompt . Don't delay and keep the products / services ready
        
5 ) At last be polite and maintain decency while escrowing :) 
        
        
* If you agree to all the above . Use /agree to continue """)

def add_to_esc(update: Update, context: CallbackContext):
    authorized_users = [5994149767, 5457445535]
    user_id = update.effective_user.id

    if user_id in authorized_users:
        username = " ".join(context.args)
        if username:  # check if the username is not empty
            use1='♡ '+username+' ✿'
            if use1 in list1:
                update.message.reply_text(f"Username {username} is already in list.")
            else:
                list1.append('♡ ' + username + ' ✿')
                update.message.reply_text(f"Username {username} has been added to the list.")

        else:
            update.message.reply_text("You didn't provide a username.")
    else:
        update.message.reply_text("You're not entitled to use this command.")
    return ConversationHandler.END


def assigner(update: Update, context: CallbackContext):
    l2=[]
    for i in list1:
        a = i.split()
        l2.append(a[1].lower())
    username = '@' + update.effective_user.username
    if username.lower() in l2:
        if username in dict1:
            update.message.reply_text(f'{username} you are requested to first update the previous case ! ')
        else:
            import random
            a = random.randint(100, 10000)
            dict1[username] = a
            list3.append(a)
            list4.append(a)
            update.message.reply_text(f"Escrower : {username} has started an escrow \n\n Escrow Number : {a}")
    else:
        update.message.reply_text("You're not entitled to use this command.")
    return ConversationHandler.END

def aborter(update: Update, context: CallbackContext):
    l2 = []
    for i in list1:
        a = i.split()
        l2.append(a[1].lower())
    username = '@' + update.effective_user.username
    if username.lower() in l2:
        if username in dict1:
            update.message.reply_text(f"Escrower : {username} has aborted an escrow 🔴 ! \n\nEscrow Number : {dict1.get(username)}")
            list3.remove(dict1.get(username))
            if dict1.get(username) in list4:
                list4.remove(dict1.get(username))
            del dict1[username]
        else:
            update.message.reply_text("You've no escrow ongoing ! ")

    else:
        update.message.reply_text("You're not entitled to use this command.")
    return ConversationHandler.END

def collect_escrow_num(update: Update, context: CallbackContext):
    escrow_num = int(update.message.text)
    if escrow_num in list4:
        context.user_data["escrow_number"] = escrow_num
        list4.remove(escrow_num)
        update.message.reply_text("Escrow number validated. Please enter your username :")
        print(update.effective_user.username)
        dict2[update.effective_user.username]=escrow_num
        print(dict2)
        return NAME
    else:
        update.message.reply_text("Invalid escrow number. Please try again with a valid number:")
        return ESCROW_NUM

def done(update: Update, context: CallbackContext):
    l2 = []
    for i in list1:
        a = i.split()
        l2.append(a[1].lower())
    username = '@' + update.effective_user.username
    if username.lower() in l2:
        if username in dict1:
            update.message.reply_text(
                f"Escrower : {username} has successfully done an escrow ✅ ! \n\nEscrow Number : {dict1.get(username)}")
            list3.remove(dict1.get(username))
            if dict1.get(username) in list4:
                list4.remove(dict1.get(username))
            del dict1[username]
        else:
            update.message.reply_text("You've no escrow ongoing ! ")

    else:
        update.message.reply_text("You're not entitled to use this command.")
    return ConversationHandler.END


def group_form(update: Update, context: CallbackContext):
    chat_id = update.effective_chat.id
    message_id = update.message.message_id
    message_text = """ғɪʟʟ ᴛʜᴇ ʙᴇʟᴏᴡ ғᴏʀᴍ 

▫️ʙᴜʏᴇʀ's username - 

▫️sᴇʟʟᴇʀ's username- 

▫️ᴅᴇᴀʟ ᴅᴇᴛᴀɪʟs - 

▫️ᴅᴇᴀʟ ᴡᴏʀᴛʜ - 

▫️ᴇsᴄʀᴏᴡ ᴛɪʟʟ - 

▫️ʜᴏᴡ ᴍᴜᴄʜ ᴛɪᴍᴇ ᴅᴇᴀʟ ᴡɪʟʟ ᴛᴀᴋᴇ -

Fɪʟʟ ᴛʜɪs ғᴏʀᴍ ᴀɴᴅ ᴛᴀɢ ᴀᴅᴍɪɴs

Escrow group Link will be given to you by admins

Rᴇɢᴀʀᴅs :- Hʏᴘᴇʀ Esᴄʀᴏᴡ Sᴇʀᴠɪᴄᴇ"""
    reply_markup = InlineKeyboardMarkup(
        [[InlineKeyboardButton("Start Bot in Private", url=f"t.me/{context.bot.username}?start=startform")]])
    context.bot.send_message(chat_id=chat_id, text=message_text, reply_markup=reply_markup, reply_to_message_id=message_id)

def group_escrow(update: Update, context: CallbackContext):
    chat_id = update.effective_chat.id
    txt1 = '\n'.join(list1)
    message_text = f'𝐕𝐞𝐫𝐢𝐟𝐢𝐞𝐝 𝐄𝐬𝐜𝐫𝐨𝐰𝐞𝐫 𝐋𝐢𝐬𝐭 ✔️\n{txt1}\nFill The Form For Escrow \n Use [ /Form ]'
    context.bot.send_message(chat_id=chat_id, text=message_text)


def start_form(update: Update, context: CallbackContext):
    if update.effective_chat.type == "private":
        if context.user_data.get("submitted", False):
            context.user_data["submitted"] = False
            context.user_data["escrow_number"] = None

            if update.message:
                update.message.reply_text("Please enter your escrow number:")
            elif update.callback_query:
                update.callback_query.message.reply_text("Please enter your escrow number:")
            return ESCROW_NUM
        else:
            context.user_data["submitted"] = False
            context.user_data["escrow_number"] = None

            if update.message:
                update.message.reply_text("Please enter your escrow number:")
            elif update.callback_query:
                update.callback_query.message.reply_text("Please enter your escrow number:")
            return ESCROW_NUM
    else:
        if update.effective_user.is_bot:
            update.message.reply_text("Please enter your escrow number:")
            return ESCROW_NUM
        else:
            return ESCROW_NUM

def collect_name(update: Update, context: CallbackContext):
    print("Form detected")
    context.user_data["name"] = update.message.text
    update.message.reply_text("Enter the amount:")
    return AMOUNT



def collect_amount(update: Update, context: CallbackContext):
    context.user_data["amount"] = update.message.text
    update.message.reply_text("Please provide a description:")
    return DESCRIPTION


def collect_description(update: Update, context: CallbackContext):
    context.user_data["description"] = update.message.text
    update.message.reply_text("Please enter the seller's details:")
    return SELLER


def collect_seller(update: Update, context: CallbackContext):
    context.user_data["seller"] = update.message.text
    update.message.reply_text("Enter the escrow till time:")
    return ESCROW


def collect_escrow(update: Update, context: CallbackContext):
    context.user_data["escrow"] = update.message.text
    update.message.reply_text("Enter the time the deal would take:")
    return TIME


def collect_time(update: Update, context: CallbackContext):

    jal=update.effective_user.username
    print("1",dict2)
    if  jal in dict2:
        context.user_data["time"] = update.message.text
        reply_keyboard = [[InlineKeyboardButton("Submit", callback_data="submit")]]
        print(dict2)
        update.message.reply_text(
            "Thank you for submitting the form! Press 'Submit' to finalize your submission.",
            reply_markup=InlineKeyboardMarkup(reply_keyboard),
        )
        return ConversationHandler.END
    else:
        update.message.reply_text(
            "Form was already submitted ! "
        )


def submit_form(update: Update, context: CallbackContext):
    context.user_data["submitted"] = True
    user_data = context.user_data
    if update.effective_user.username in dict2:
        send_form_to_channel(update, context)
        if update.message:
            update.message.reply_text("Form submitted successfully! Thank you.")
            print(dict2)
            dict2.pop(update.effective_user.username)
            return ConversationHandler.END
        elif update.callback_query:
            update.callback_query.message.reply_text("Form submitted successfully! Thank you.")
            dict2.pop(update.effective_user.username)
            return ConversationHandler.END
        else:
            update.message.reply_text("Form was already submitted ! ")
    else:
        update.message.reply_text("Form was already submitted ! ")


def send_form_to_channel(update: Update, context: CallbackContext):
    user_data = context.user_data
    form_data = f"\n▫️ʙᴜʏᴇʀ's username - {user_data['name']}\n\n▫️sᴇʟʟᴇʀ's username- {user_data['seller']}\n\n▫️ᴅᴇᴀʟ ᴅᴇᴛᴀɪʟs -: {user_data['description']}\n\n▫️ᴅᴇᴀʟ ᴡᴏʀᴛʜ - {user_data['amount']}\n\n▫️ᴇsᴄʀᴏᴡ ᴛɪʟʟ - {user_data['escrow']}\n\n▫️ʜᴏᴡ ᴍᴜᴄʜ ᴛɪᴍᴇ ᴅᴇᴀʟ ᴡɪʟʟ ᴛᴀᴋᴇ - {user_data['time']}\n\n Rᴇɢᴀʀᴅs :- Hʏᴘᴇʀ Esᴄʀᴏᴡ Sᴇʀᴠɪᴄᴇ"
    context.bot.send_message(chat_id='-1001802284454', text=form_data)
    return ConversationHandler.END


def cancel(update: Update, context: CallbackContext):
    context.user_data["submitted"] = False
    update.message.reply_text("Form submission cancelled.")
    return ConversationHandler.END



def button_callback(update: Update, context: CallbackContext):
    query = update.callback_query
    if query.data == "submit":
        if query.message.chat.type == 'private':
            return submit_form(update, context)


def main():
    updater = Updater("______________", use_context=True)

    dispatcher = updater.dispatcher

    conv_handler = ConversationHandler(
        entry_points=[
            CommandHandler("agree", start_form, filters.private),
            MessageHandler(filters.regex("^Submit$") & filters.private, submit_form),
            CommandHandler("form", group_form, filters=filters.group),
            CommandHandler("escrow", group_escrow, filters=filters.group),
            CommandHandler("egen", assigner, filters=filters.group),
            CommandHandler("abort", aborter, filters=filters.group),
            CommandHandler("done", done, filters=filters.group),
        ],

        states={
            ESCROW_NUM: [MessageHandler(filters.text & ~filters.command & filters.private, collect_escrow_num)],
            NAME: [MessageHandler(filters.text & ~filters.command & filters.private, collect_name)],
            AMOUNT: [MessageHandler(filters.text & ~filters.command & filters.private, collect_amount)],
            DESCRIPTION: [MessageHandler(filters.text & ~filters.command & filters.private, collect_description)],
            SELLER: [MessageHandler(filters.text & ~filters.command & filters.private, collect_seller)],
            ESCROW: [MessageHandler(filters.text & ~filters.command & filters.private, collect_escrow)],
            TIME: [MessageHandler(filters.text & ~filters.command & filters.private, collect_time)],
        },
        fallbacks=[CommandHandler("cancel", cancel, filters.private)],
    )
    dispatcher.add_handler(conv_handler)
    dispatcher.add_handler(CommandHandler("start", start1))
    dispatcher.add_handler(CommandHandler("esc", add_to_esc))

    dispatcher.add_handler(CallbackQueryHandler(button_callback, pattern='^submit$'))

    #polling start kardi dekh raha girish ?

    updater.start_polling()
    updater.idle()




if __name__ == "__main__":
    main()
