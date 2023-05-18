# Minimal makefile for Sphinx documentation
# You can set these variables from the command line, and also
# from the environment for the first two.
SPHINXOPTS    ?= -T -j 2
SPHINXBUILD   ?= sphinx-build
SOURCEDIR     = .
BUILDDIR      = _build

sph_user = $(shell find `python3 -m site --user-base` -name sphinx-build || echo "")
sph_def  = $(shell find `python3 -c "import sysconfig; print(sysconfig.get_path('scripts'))"` -name sphinx-build || echo "")
ifneq ($(wildcard $(sph_user)), )
	SPHINXBUILD = $(sph_user)
else
	ifneq ($(wildcard $(sph_def)), )
		SPHINXBUILD = $(sph_def)
	endif
endif

# Catch-all target: route all unknown targets to Sphinx using the new
# "make mode" option.  $(O) is meant as a shortcut for $(SPHINXOPTS).

.PHONY: html
html: clean
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)
	mv $(BUILDDIR)/html docs
	rm -Rf $(BUILDDIR)
	touch docs/.nojekyll

.PHONY: clean
clean:
	rm -Rf $(BUILDDIR)
	rm -Rf docs

.PHONY: pub
pub:
	git checkout pub
	git rm -r docs
	git commit -m "remove old docs"
	git merge -m "merge in main" main
	make
	git add docs
	git commit -m "publish"
	git push
	git checkout main
