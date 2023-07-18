local null_ls = require("null-ls")

null_ls.setup({
	sources = {
		null_ls.builtins.formatting.prettier.with({
			args = { "--tab-width", "2", "--use-tabs" },
		}),
		null_ls.builtins.formatting.autopep8
	},
})
