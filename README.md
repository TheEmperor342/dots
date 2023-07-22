# Dotfiles
My configuration for bspwm

# Packages needed
- Xorg: xorg-server xorg-xinit
- WM and Keybinds: [bspwm (rounded corners)](https://github.com/phuhl/bspwm-rounded) & [sxhkd](https://github.com/baskerville/sxhkd)
- GTK Theme: catppuccin Mocha
- Browser: Firefox
- Wallpaper setter: nitrogen
- Notif daemon: dunst
- Compositor: picom
- Terminal: kitty
- bar: polybar
- Bluetooth: blueman
- python3, python-pip
  - Package: [colorthief](https://github.com/fengsp/color-thief-py)
- Font: JetBrainsMono nerd fonts
- Editor: neovim (with [Lazy.nvim](https://github.com/folke/lazy.nvim))
  - `jq` and `tidy` for [rest.nvim](https://github.com/rest-nvim/rest.nvim)
- lxsession, lxappearance, xdotool
- I have laptop so I also use [gestures](https://aur.archlinux.org/packages/gestures) and [tlp](https://wiki.archlinux.org/title/TLP)
  - Remove their autostarts from bspwmrc if you don't want to use them

___
Command to install dependencies in arch linux:
```
yay -S --needed xorg-server xorg-xinit bspwm-rounded-corners catppuccin-gtk-theme-mocha polybar sxhkd firefox nitrogen dunst picom kitty brightnessctl zsh zsh-autosuggestions zsh-syntax-highlighting blueman python python-pip ttf-jetbrains-mono-nerd lxsession lxappearance xdotool neovim jq tidy rofi alsa-utils
```
Installing gestures stuff
```
yay -S gestures
sudo gpasswd -a $USER input
```
Reboot after adding your user to input group

TLP
```
yay -S tlpui-git
```
