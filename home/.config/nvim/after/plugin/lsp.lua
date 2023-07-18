local lsp = require('lsp-zero').preset({})

lsp.on_attach(function(client, bufnr)
	lsp.default_keymaps({ buffer = bufnr })
	local opts = { buffer = bufnr, remap = false }
	vim.keymap.set("n", "gd", function() vim.lsp.buf.definition() end, opts)

end)

-- (Optional) Configure lua language server for neovim
require('lspconfig').lua_ls.setup(lsp.nvim_lua_ls())

local cmp = require("cmp")
local cmp_select = { behavior = cmp.SelectBehavior.Select }
local cmp_mappings = lsp.defaults.cmp_mappings({
	['<C-Space>'] = cmp.mapping.complete(),
	['<C-Tab>'] = cmp.mapping.confirm({ select = true }),
})

lsp.setup()
