.DEFAULT_GOAL=git-commit-auto-push

deploy:
	cp boot.py build/boot.py
	cp main.py build/main.py
	mkdir -p build/modules
	cp lib/micropython-lib/uasyncio/uasyncio/__init__.py build/modules/uasyncio.py
	cp lib/micropython-lib/pkg_resources/pkg_resources.py build/modules/pkg_resources.py
	cp lib/microtelnetserver/utelnet/utelnetserver.py build/modules/utelnetserver.py
	cp lib/picoweb/picoweb/__init__.py build/modules/picoweb.py
	cp lib/picoweb/picoweb/utils.py build/modules/utils.py
	cp lib/micropython-adafruit-ssd1306/ssd1306.py build/modules/ssd1306.py

dev:
	git submodule update --init --recursive

update:
	git pull --recurse-submodules

# Git
MESSAGE="Update"
REMOTES=`\
		git branch -a |\
		grep remote   |\
		grep -v HEAD  |\
		grep -v master`  # http://unix.stackexchange.com/a/37316
co: git-checkout-remotes  # Alias
commit: git-commit  # Alias
commit-auto: git-commit-auto-push  # Alias
commit-edit: git-commit-edit-push  # Alias
git-commit: git-commit-auto  # Alias
git-commit-auto-push: git-commit-auto git-push  # Chain
git-commit-edit-push: git-commit-edit git-push  # Chain
push: git-push
git-checkout-remotes:
		-for i in $(REMOTES) ; do \
    git checkout -t $$i ; done
git-commit-auto:
		git commit -a -m $(MESSAGE)
git-commit-edit:
		git commit -a
git-push:
		git push
