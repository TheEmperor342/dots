" STARTER COMMANDS
" ===========================
set clipboard=unnamed
set number
syntax on
set ruler
set mouse=a

" FONT
" ===========================

let s:fontsize = 12
function! AdjustFontSize(amount)
  let s:fontsize = s:fontsize+a:amount
endfunction

noremap <C-ScrollWheelUp> :call AdjustFontSize(1)<CR>
noremap <C-ScrollWheelDown> :call AdjustFontSize(-1)<CR>
inoremap <C-ScrollWheelUp> <Esc>:call AdjustFontSize(1)<CR>a
inoremap <C-ScrollWheelDown> <Esc>:call AdjustFontSize(-1)<CR>a

" CHANGE TAB SIZE TO 2 
" ===========================
set tabstop=2
set shiftwidth=2

" PLUGINS
" ===========================
call plug#begin()
Plug 'preservim/nerdtree'
Plug 'catppuccin/nvim', {'as': 'catppuccin'}
Plug 'andweeb/presence.nvim'
Plug 'mxw/vim-jsx'
Plug 'pangloss/vim-javascript'
Plug 'ap/vim-css-color'
Plug 'vim-airline/vim-airline'
Plug 'vim-airline/vim-airline-themes'
call plug#end()

" CHANGE THEME
" ===========================
colorscheme catppuccin-mocha
let g:airline_theme='dracula'

autocmd VimEnter * NERDTree
