local lazypath = vim.fn.stdpath("data") .. "/lazy/lazy.nvim"
if not vim.loop.fs_stat(lazypath) then
	vim.fn.system({
		"git",
		"clone",
		"--filter=blob:none",
		"https://github.com/folke/lazy.nvim.git",
		"--branch=stable", -- latest stable release
		lazypath,
	})
end
vim.opt.rtp:prepend(lazypath)

require("lazy").setup(
	{
		{ "catppuccin/nvim", name = "catppuccin" },
		{ 'nvim-treesitter/nvim-treesitter', build = ':TSUpdate' },
		{
			'nvim-lualine/lualine.nvim',
			dependencies = { 'kyazdani42/nvim-web-devicons', name = "weebdevicons" }
		},
		{
			'nvim-tree/nvim-tree.lua',
			dependencies = {
				'nvim-tree/nvim-web-devicons', -- optional, for file icons
			},
		},
		{
			'VonHeikemen/lsp-zero.nvim',
			branch = 'v2.x',
			dependencies = {
				-- LSP Support
				{ 'neovim/nvim-lspconfig' }, -- Required
				{ 'prabirshrestha/vim-lsp' },
				{ -- Optional
					'williamboman/mason.nvim',
					build = function()
						pcall(vim.cmd, 'MasonUpdate')
					end,
				},
				{ 'williamboman/mason-lspconfig.nvim' }, -- Optional

				-- Autocompletion
				{ 'hrsh7th/nvim-cmp' }, -- Required
				{ 'hrsh7th/cmp-nvim-lsp' }, -- Required
				{ 'L3MON4D3/LuaSnip' }, -- Required
			}
		},
		'andweeb/presence.nvim',
		{
			"rest-nvim/rest.nvim",
			dependencies = { "nvim-lua/plenary.nvim" },
		},
		{
			"jose-elias-alvarez/null-ls.nvim",
			dependencies = { "nvim-lua/plenary.nvim" }
		},
    {
    'nvim-telescope/telescope.nvim', tag = '0.1.2',
      dependencies = { 'nvim-lua/plenary.nvim' }
    }

	}
	, {})
