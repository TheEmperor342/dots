# Created by newuser for 5.9
typeset -U path PATH
path=(~/.local/bin $path)
export PATH

autoload -Uz compinit
compinit

zstyle ':completion:*' menu select

source /usr/share/zsh/plugins/zsh-syntax-highlighting/zsh-syntax-highlighting.zsh
source /usr/share/zsh/plugins/zsh-autosuggestions/zsh-autosuggestions.zsh

PROMPT='%(!.%B%F{red}.%B%F{green}%n@)%m %F{blue}%(!.%1~.%~) %F{blue}%(!.#.$)%k%b%f '
$HOME/.config/colors.py
