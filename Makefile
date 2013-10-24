PREFIX=/usr/local
BINDIR=$(PREFIX)/bin

BINARIES=skylog.py skydbg.py runskype_skylog.sh

all:

install:
	install -m 0755 $(BINARIES) $(BINDIR)
