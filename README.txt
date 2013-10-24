skylog - log skype status changes of your contacts
2013, Laurent Ghigonis <laurent@gouloum.fr>

runskype_skylog.sh:
Run skype and skylog, and shows you skylog output in tmux


Example usage
=============

$ ./runskype_skylog.sh
[-] running skype
[-] waiting for skype to be up
[-] running skylog
cb_attachmentstatus: 0
Started
[-] running skydbg
[-] create tmux skylog watcher
[-] attach to tmux skylog watcher
[detached]
[*] running !


Dependencies
============

pip install Skype4Py
