import os

def add_username_segment():
    if powerline.args.shell == 'bash':
        user_prompt = ' \\u'
    elif powerline.args.shell == 'zsh':
        user_prompt = ' %n'
    else:
        user_prompt = ' %s' % os.getenv('USER')

    bg = Color.USERNAME_BG
    if os.geteuid() == 0:
        bg = 1
    powerline.append(user_prompt, Color.USERNAME_FG, bg)

add_username_segment()
