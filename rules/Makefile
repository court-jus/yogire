all: pdf html

pdf: rules.rst
	rst2pdf rules.rst

html: rules.rst
	pandoc rules.rst > rules.html
