#!/bin/zsh
typeset -U path PATH
path=(~/.local/bin $path)
export PATH

autoload -Uz compinit
compinit

zstyle ':completion:*' menu select

source /usr/share/zsh/plugins/zsh-syntax-highlighting/zsh-syntax-highlighting.zsh
source /usr/share/zsh/plugins/zsh-autosuggestions/zsh-autosuggestions.zsh

PROMPT='%(!.%B%F{red}.%B%F{green}%n@)%m %F{blue}%(!.%1~.%~) %F{blue}%(!.#.$)%k%b%f '
#$HOME/.config/colors.py
colorscript -r

# VIM MODE
bindkey -v
export KEYTIMEOUT=1

# ALIASES
alias v="nvim"
alias \
	cp="cp -iv" \
	mv="mv -iv" \
	rm="rm -vI"

alias \
	ls="ls -hN --color=auto --group-directories-first" \
	grep="grep --color=auto" \
	diff="diff --color=auto" \
	ccat="highlight --out-format=ansi" \
	ip="ip -color=auto"

alias \
	p="sudo pacman" \
	y="yay" \
	mount="sudo mount" \
	umount="sudo umount" \
	systemctl="sudo systemctl" \

alias \
	cfg="nvim ~/.dotfiles" \
	cfb="nvim ~/.config/bspwm" \
	cfd="nvim ~/.config/dunst" \
	cfe="nvim ~/.config/eww" \
	cfk="nvim ~/.config/kitty" \
	cfn="nvim ~/.config/nvim" \
	cfp="nvim ~/.config/polybar" \
	cfq="nvim ~/.config/qtile" \
	cfr="nvim ~/.config/rofi" \
	cfs="nvim ~/.config/sxhkd" \
	cfx="nvim ~/.config/X11" \
	cfz="nvim ~/.config/zsh"
