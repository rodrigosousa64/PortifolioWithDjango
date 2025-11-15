
TAILWIND_INPUT = core/assets/css/input.css
TAILWIND_OUTPUT = core/static/css/output.css

css-watch:
	./tailwindcss -i $(TAILWIND_INPUT) -o $(TAILWIND_OUTPUT) --watch

css-build:
	./tailwindcss -i $(TAILWIND_INPUT) -o $(TAILWIND_OUTPUT) --minify

