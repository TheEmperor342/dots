# Dotfiles
My configuration for bspwm

# Packages needed
- Xorg: xorg-server xorg-xinit, xorg-xsetroot
- WM and Keybinds: [bspwm (rounded corners)](https://github.com/phuhl/bspwm-rounded) & [sxhkd](https://github.com/baskerville/sxhkd)
- GTK Theme: catppuccin Mocha
- Browser: Firefox
- Wallpaper setter: nitrogen
- Notif daemon: dunst
- Compositor: picom
- Terminal: kitty
- Bar: polybar
- Bluetooth: blueman
- Python3
- Font: JetBrainsMono nerd fonts
- Editor: neovim (with [Lazy.nvim](https://github.com/folke/lazy.nvim))
  - `jq` and `tidy` for [rest.nvim](https://github.com/rest-nvim/rest.nvim)
- lxsession, lxappearance, xdotool
- I have laptop so I also use [gestures](https://aur.archlinux.org/packages/libinput-gestures) and [tlp](https://archlinux.org/packages/extra/any/tlp)
  - Remove their autostarts from bspwmrc if you don't want to use them

___
Command to install dependencies in arch linux:
```
yay -S --needed xorg-server xorg-xinit xorg-xsetroot bspwm-rounded-corners catppuccin-gtk-theme-mocha polybar sxhkd firefox nitrogen dunst picom kitty brightnessctl zsh zsh-autosuggestions zsh-syntax-highlighting blueman python python-pip ttf-jetbrains-mono-nerd lxsession lxappearance xdotool neovim jq tidy rofi alsa-utils
```
Installing gestures stuff
```
yay -S libinput-gestures
sudo gpasswd -a $USER input
```
Reboot after adding your user to input group

TLP
```
sudo pacman -S tlp
```
![image](https://github.com/TheEmperor342/dots/assets/83999665/e6e21847-a3e7-4db5-b7c9-0e816865197b)
![image](https://github.com/TheEmperor342/dots/assets/83999665/d2bdad4e-8dbf-49a2-b3d4-65256d790924)
![image](https://github.com/TheEmperor342/dots/assets/83999665/9ed7ae80-0122-4bc8-92eb-9b5a5b329a0a)
![image](https://github.com/TheEmperor342/dots/assets/83999665/ed4eb185-d7f4-49ba-9e63-a290a9968b43)


