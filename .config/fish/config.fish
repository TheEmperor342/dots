#! /usr/bin/env fish

if status is-interactive
    # Commands to run in interactive sessions can go here
    set fish_greeting ""

    python3 $HOME/.config/fish/colors.py

    # === ALIASES === #
    # alias neofetch "neofetch --backend kitty --source $HOME/.config/neofetch/EndeavourOS_Logo.svg --size '200px'"
    alias update "yay -Syu"
    alias install "sudo pacman -S"
    alias aurinstall "yay -S"
    alias remove "sudo pacman -Rs"

end
fish_add_path /home/emperor/.spicetify
