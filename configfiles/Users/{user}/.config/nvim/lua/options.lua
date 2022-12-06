local opt = vim.opt
opt.relativenumber = true -- relative line numbers
opt.cursorline = true -- highlights the current line
opt.conceallevel = 0 -- to show text normally
opt.signcolumn = "yes" -- always show the sign column
opt.undofile = true -- persistent undo
opt.clipboard:append { 'unnamedplus' }

-- sync wsl2 vim clipboard with windows
vim.cmd([[
  if system('uname -r') =~ "microsoft"
    augroup Yank
    autocmd!
    autocmd TextYankPost * :call system('/mnt/c/windows/system32/clip.exe ',@")
    augroup END
  endif
]])
