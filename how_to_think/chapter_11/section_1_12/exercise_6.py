from how_to_think.chapter_11.section_1_12.SMS_store import SMS_store

my_inbox = SMS_store()

my_inbox.add_new_arrival(1234, 12, "Hello")
print(my_inbox)
print(my_inbox.message_count())