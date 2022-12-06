if vim.g.vscode then
    -- VSCode extension
    require("options")
    require("vscode-bindings")
else
    -- ordinary Neovim
    require("options")
end
