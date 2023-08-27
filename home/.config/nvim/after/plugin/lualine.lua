--require('lualine').setup {
--options = {
--    icons_enabled = true,
--    theme = 'auto',
--    component_separators = { left = '', right = ''},
--    section_separators = { left = '', right = ''},
--    disabled_filetypes = {
--      statusline = {},
--      winbar = {},
--    },
--    ignore_focus = {},
--    always_divide_middle = true,
--    globalstatus = false,
--    refresh = {
--      statusline = 1000,
--      tabline = 1000,
--      winbar = 1000,
--    }
--  },
--  sections = {
--    lualine_a = {'mode'},
--    lualine_b = {'branch', 'diff', 'diagnostics'},
--    lualine_c = {'filename'},
--    lualine_x = {'encoding', 'fileformat', 'filetype'},
--    lualine_y = {'progress'},
--    lualine_z = {'location'}
--  },
--  inactive_sections = {
--    lualine_a = {},
--    lualine_b = {},
--    lualine_c = {'filename'},
--    lualine_x = {'location'},
--    lualine_y = {},
--    lualine_z = {}
--  },
--  tabline = {},
--  winbar = {},
--  inactive_winbar = {},
--  extensions = {}
--}
-- local colorsCatppuccin = {
-- 	blue   = '#89b4fa',
-- 	cyan   = '#94e2d5',
-- 	black  = '#181825',
-- 	white  = '#cdd6f4',
-- 	red    = '#f38ba8',
-- 	violet = '#cba6f7',
-- 	grey   = '#313244',
-- }
-- 
-- local colorsSolarized = {
-- 	blue   = '#268bd2',
-- 	cyan   = '#2aa198',
-- 	black  = '#002b36',
-- 	white  = '#fdf6e3',
-- 	red    = '#dc322f',
-- 	violet = '#6c71c4',
-- 	grey   = '#073642',
-- }
-- 
-- local colorsGruvbox = {
-- 	blue   = '#458588',
-- 	cyan   = '#83a598',
-- 	black  = '#1d2021',
-- 	white  = '#ebdbb2',
-- 	red    = '#cc241d',
-- 	violet = '#b16286',
-- 	grey   = '#928374',
-- }

require('lualine').setup {
  options = {
    icons_enabled = true,
    theme = 'auto',
    component_separators = { left = '', right = ''},--
    section_separators = { left = '', right = ''},
    disabled_filetypes = {
      statusline = {},
      winbar = {},
    },
    ignore_focus = {},
    always_divide_middle = true,
    globalstatus = true,
    refresh = {
      statusline = 1000,
      tabline = 1000,
      winbar = 1000,
    }
  },
  sections = {
    lualine_a = {'mode'},
    lualine_b = {'branch', 'diff', 'diagnostics'},
    lualine_c = {'filename'},
    lualine_x = {'encoding', 'fileformat', 'filetype'},
    lualine_y = {'progress'},
    lualine_z = {'location'}
  },
  inactive_sections = {
    lualine_a = {},
    lualine_b = {},
    lualine_c = {'filename'},
    lualine_x = {'location'},
    lualine_y = {},
    lualine_z = {}
  },
  tabline = {},
  winbar = {},
  inactive_winbar = {},
  extensions = {}
}
