vim.g.mapleader = " "
vim.keymap.set("n", "<leader>pv", vim.cmd.Ex)
vim.api.nvim_set_keymap('n', '<leader>rr', '<Cmd>lua require("rest-nvim").run()<CR>', { noremap = true, silent = true })
vim.api.nvim_set_keymap('n', '<leader>lf', '<Cmd>lua vim.lsp.buf.format({timeout_ms = 10000})<CR>',
	{ noremap = true, silent = true })

vim.opt.nu = true
vim.opt.rnu = true

vim.opt.tabstop = 2
vim.opt.softtabstop = 2
vim.opt.shiftwidth = 2
vim.opt.expandtab = false

vim.opt.smartindent = true
vim.opt.wrap = false

vim.opt.swapfile = false
vim.opt.backup = false

vim.opt.hlsearch = false
vim.opt.incsearch = true

vim.opt.scrolloff = 8
