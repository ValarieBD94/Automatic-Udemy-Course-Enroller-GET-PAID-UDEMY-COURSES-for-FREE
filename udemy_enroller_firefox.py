# Install all the requirements by running requirements.py in IDLE or follow the alternate instructions at
# https://github.com/aapatre/Automatic-Udemy-Course-Enroller-GET-PAID-UDEMY-COURSES-for-FREE/ Make sure you have
# cleared all saved payment details on your Udemy account & the browser! For firefox you need to manually install the
# driver on Arch Linux (sudo pacman -S geckodriver). Untested on other platforms.
from udemy_enroller import run, parse_args


if __name__ == "__main__":
    args = parse_args("firefox")
    run(args.browser, args.max_pages)
