MAIN_TREE := HEAD
MAIN_COMMIT := $(shell git rev-parse --verify $(MAIN_TREE))
PKG_NAME := python-requests-aws
PROG_NAME := $(shell sed -n s/%define[[:space:]]*pkgname[[:space:]]*//p $(PKG_NAME).spec)
VERSION := $(shell sed -n s/[[:space:]]*Version:[[:space:]]*//p $(PKG_NAME).spec)

sources:
	@git archive --format=tar --prefix="$(PROG_NAME)-$(VERSION)/" \
		$(MAIN_COMMIT) | gzip > "$(PROG_NAME)-$(VERSION).tar.gz"
