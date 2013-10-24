#!/bin/sh

LOGDIR=$HOME/skylog/
EXEDIR=$(dirname $0)

if [ ! -d $LOGDIR ]; then
    mkdir $LOGDIR
fi

echo "[-] running skype"
skype &

echo "[-] waiting for skype to be up"
sleep 5 # XXX

if [ $(pgrep -x skype| wc -l) = 0 ]; then
    echo "[!] skype startup failed"
    exit 1
fi

echo "[-] running skylog"
$EXEDIR/skylog.py >> $LOGDIR/skylog.csv &
sleep 2

echo "[-] running skydbg"
$EXEDIR/skydbg.py >> $LOGDIR/skydbg.csv &

echo "[-] create tmux skylog watcher"
tmux new-session -d -s skylog "tail -f $LOGDIR/skydbg.csv"
tmux new-window -t skylog "tail -f $LOGDIR/skylog.csv"

echo "[-] attach to tmux skylog watcher"
tmux attach-session -t skylog

echo "[*] running !"
