bot_name = "RaptorTaskBot"

texts = {
    'help': "Use\n"
            f"/do [title] - Assign a task (First Line)\n"
            f"[Description] (Start Description from the Second line, CTRL+Enter) \n"
            f"(private chat with the bot only)\n"
            f"/tasks - to list your duties\n"
            f"/stats - to list some numbers about your work\n"
            f"/feedback [your message] - to report issues or get in contact with the Raptor-team\n"
            f"/help - to show this info\n\n"
            f"Note: All tasks from groups that you leave will be deleted!\n\n",
    'announcement-prefix': "Hi, there is an announcement from the Raptor-team:",
    'feedback-thanks': "Thanks for your feedback, the Raptor-team will have a look and might get back to you.",
    'feedback-reply-prefix': "Hi, there is a reply from the Raptor-team to your feedback:",
    'user-welcome': lambda chat_title, name: f"Welcome in the {chat_title}'s realm of productivity, {name}!",
    'user-goodbye': lambda name: f"Farewell, my exhausted busy Raptor {name}!",
}
