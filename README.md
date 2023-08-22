# Dotfiles
My configuration for QTile and bspwm
<details>
  <summary>QTile</summary>

  ## Packages needed
  - Xorg: xorg-server xorg-xinit, xorg-xsetroot, xorg-xrandr
  - WM: QTile
      - Python3
      - QTile Extras
      - python-psutil
  - Wallpaper setter: QTile
  - Bar: QTile bar
  - Catppuccin
    - GTK Theme: catppuccin Mocha
    - Cursor Theme: catppuccin cursors
  - Gruvbox
    - gruvbox-dark-gtk
  - Browser: Firefox
  - Notif daemon: dunst
  - Compositor: picom
  - Terminal: kitty
  - Tray:
    - NetworkManager Applet
    - cbatticon
    - Blueman
  - Bluetooth: blueman
  - Font: JetBrainsMono nerd fonts
  - Editor: neovim (with [Lazy.nvim](https://github.com/folke/lazy.nvim))
    - `jq` and `tidy` for [rest.nvim](https://github.com/rest-nvim/rest.nvim)
    - xclip
  - lxsession, lxappearance, xdotool, unclutter


  Command to install dependencies in Arch Linux:
  ```
  yay -S --needed xorg-server xorg-xinit xorg-xsetroot xorg-xrandr qtile qtile-extras python-psutil network-manager-applet cbatticon firefox dunst picom kitty brightnessctl zsh zsh-autosuggestions zsh-syntax-highlighting blueman python ttf-jetbrains-mono-nerd lxsession-gtk3 lxappearance xdotool neovim jq tidy xclip rofi alsa-utils
  ```
  ### Gruvbox
  ```
  yay -S --needed gruvbox-dark-gtk
  ```
  ### Catppuccin
  ```
  yay -S --needed catppuccin-cursors-mocha catppuccin-gtk-theme-mocha
  ```

  ## Gallery (Gruvbox)
  ![image](https://github.com/TheEmperor342/dots/assets/83999665/a7388977-7b84-43d2-8c7d-046277f77be1)
  ![image](https://github.com/TheEmperor342/dots/assets/83999665/df1f45b0-2cd8-4e9b-9180-1e75adb3851b)
  ![image](https://github.com/TheEmperor342/dots/assets/83999665/9b475beb-1f68-42ab-9a96-90959a709f9f)

  
  ## Gallery (Catppuccin)
  ![image](https://github.com/TheEmperor342/dots/assets/83999665/ed69db26-04e4-4297-9883-9f11d6580e44)
  ![image](https://github.com/TheEmperor342/dots/assets/83999665/7ec6e118-7d97-4796-a926-f48f9344aa86)
  ![image](https://github.com/TheEmperor342/dots/assets/83999665/70fc3629-b209-4c8f-98b8-7caba8566c31)

</details>

<details>
  <summary>bspwm</summary>

  ## Packages needed
  - Xorg: xorg-server xorg-xinit, xorg-xsetroot, xorg-xrandr
  - WM and Keybinds: [bspwm (rounded corners)](https://github.com/phuhl/bspwm-rounded) & [sxhkd](https://github.com/baskerville/sxhkd)
  - GTK Theme: catppuccin Mocha
  - Cursor Theme: catppuccin cursors
  - Browser: Firefox
  - Wallpaper setter: nitrogen
  - Notif daemon: dunst
  - Compositor: picom
  - Terminal: kitty
  - Bar: polybar OR eww (There are configs for both in `home/.config`)
  - Tray:
    - NetworkManager Applet
    - Blueman
  - Python3
  - Font: JetBrainsMono nerd fonts
  - Editor: neovim (with [Lazy.nvim](https://github.com/folke/lazy.nvim))
    - `jq` and `tidy` for [rest.nvim](https://github.com/rest-nvim/rest.nvim)
    - xclip
  - lxsession, lxappearance, xdotool

  Command to install dependencies in Arch Linux:
  ```
  yay -S --needed xorg-server xorg-xinit xorg-xsetroot xorg-xrandr bspwm-rounded-corners network-manager-applet catppuccin-gtk-theme-mocha catppuccin-cursors-mocha sxhkd firefox nitrogen dunst picom kitty brightnessctl zsh zsh-autosuggestions zsh-syntax-highlighting blueman python ttf-jetbrains-mono-nerd lxsession-gtk3 lxappearance xdotool neovim jq tidy xclip rofi alsa-utils
  ```
  ### Polybar
  ```
  sudo pacman -S polybar
  ```
  ### eww
  - Compile eww from source.
    - [Link to repo](https://github.com/elkowar/eww)
    
  After installation:
  ```
  yay -S playerctl python-colorthief
  ```
  ## Gallery (With eww)
  ![image](https://github.com/TheEmperor342/dots/assets/83999665/c8868352-8616-4813-9bef-01b51be321cb)
  ## Gallery (With Polybar)
  ![image](https://github.com/TheEmperor342/dots/assets/83999665/d4388466-34be-4ea5-a834-7d835f62fcdb)
  ![image](https://github.com/TheEmperor342/dots/assets/83999665/76ee1867-b5ce-4478-b8d9-46b783259150)
  ![image](https://github.com/TheEmperor342/dots/assets/83999665/484e7404-28c5-4426-9418-db872cb9cb8a)
  ![image](https://github.com/TheEmperor342/dots/assets/83999665/fe5ca0e2-ed0e-4a44-9abe-b7012c922a11)
  
</details>

___
Optional: Install `fzf` for a script in `home/.local/bin/`

____
I have laptop so I also use [libinput-gestures](https://aur.archlinux.org/packages/libinput-gestures) and [auto-cpufreq](https://github.com/AdnanHodzic/auto-cpufreq)
  - Remove their autostarts from bspwmrc or qtile autostarts if you don't want to use them

Installing gestures stuff
```
yay -S libinput-gestures
sudo gpasswd -a $USER input
```
Reboot after adding your user to input group

If you don't have an nvidia GPU, I [envy](https://github.com/bayasdev/envycontrol) you (pun intended).
- remove xrandr commands from `.xinitrc` located at `home/.config/X11/`

