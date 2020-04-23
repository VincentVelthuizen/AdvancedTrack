from how_to_think.chapter_11.section_1_12.SMS_store import SMS_store

my_inbox = SMS_store()

my_inbox.add_new_arrival(1234, 12, "Hello")
my_inbox.add_new_arrival(1234, 13, "World")
my_inbox.add_new_arrival(1234, 15, "Please don't send one word messages...")

print(my_inbox)
print(my_inbox.message_count())

print(my_inbox.get_message(1))

print(my_inbox.get_unread_indexes())
