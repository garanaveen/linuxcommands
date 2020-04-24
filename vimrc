
"linuxcommands/vimrc start
"Q:How to insert <ESC> character to vim register? A:InsertMode->Ctrl+v->Esc will insert ^[ character which is ESC.

"set ic is
set hls
set shiftwidth=3

"If CurtineIncSw.vim plugin is installed,
map <F4> :call CurtineIncSw()<CR>


set tags=./tags;/


"Temporary
nnoremap <C-b> iThe beneficiary will <Esc>
inoremap <C-b> The beneficiary will <Esc>

nnoremap <C-k> <Esc>0iSkip <Esc>
inoremap <C-k> Skip <Esc>



"https://vim.fandom.com/wiki/Search_for_visually_selected_text
"Press '//' to search a visually selected pattern
vnoremap // y/<C-R>"<CR>


"This l vim register stores the key sequence to print the Log for every C++ function/method. Need to search for <ClassName::> in vim before using this as this key sequence uses the searched pattern.
"let @l=']]Nyy]]oLog(QString("opo"));kkkJJJ'

colorscheme desert

"linuxcommands/vimrc end

