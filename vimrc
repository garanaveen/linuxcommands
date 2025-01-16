
"linuxcommands/vimrc start
"Q:How to insert <ESC> character to vim register? A:InsertMode->Ctrl+v->Esc will insert ^[ character which is ESC.

"set ic is
set hls
set tabstop=3
set shiftwidth=3
set scrolloff=30
set expandtab


"If CurtineIncSw.vim plugin is installed,
map <F4> :call CurtineIncSw()<CR>


set tags=./tags;/


"https://vim.fandom.com/wiki/Search_for_visually_selected_text
"Press '//' to search a visually selected pattern
vnoremap // y/<C-R>"<CR>


"This l vim register stores the key sequence to print the Log for every C++ function/method. Need to search for <ClassName::> in vim before using this as this key sequence uses the searched pattern.
"let @l=']]Nyy]]oLog(QString("opo"));kkkJJJ'

colorscheme desert
"Download desert.vim from following link to ~/.vim/colors. 
"https://www.vim.org/scripts/download_script.php?src_id=2038
"Change the following line in desert.vim to the following,
"hi Search cterm=NONE guibg=peru guifg=wheat


"linuxcommands/vimrc end


let @l=']]ologger.logConsole<"%?:%?">("fw00000", __PRETTY_FUNCTION__, __LINE__);'

iab jira https://roku.atlassian.net/browse/


