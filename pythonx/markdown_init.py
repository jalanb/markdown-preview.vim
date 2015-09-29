#!/usr/bin/env python
# encoding: utf-8
import os, vim, platform, commands

def init():
    if vim.eval("exists('g:MarkDownCssDir')") == '1':
        cssDir = vim.eval('g:MarkDownCssDir')
    else:
        if platform.system() == 'Windows':
            cssDir = os.path.join(vim.eval('$HOME'), 'vimfiles', 'MarkDownCSS')
        elif vim.eval("has('nvim')") == '1':
            cssDir = os.path.join(vim.eval('$HOME'),'.nvim', 'MarkDownCSS')
        else:
            cssDir = os.path.join(vim.eval('$HOME'), '.vim', 'MarkDownCSS')

    if not os.path.exists(cssDir):
        vim.command('!pip install mistune')

        cssFile = "h1,\n" + "h2,\n" + "h3,\n" + "h4,\n" + "h5,\n" + "h6,\n" + "p,\n" + "blockquote {\n" + "    margin: 0;\n" + "    padding: 0;\n" + "}\n" + "body {\n" + "    font-family: \"Helvetica Neue\", Helvetica, \"Hiragino Sans GB\", Arial, sans-serif;\n" + "    font-size: 13px;\n" + "    line-height: 18px;\n" + "    color: #737373;\n" + "    background-color: white;\n" + "    margin: 10px 13px 10px 13px;\n" + "}\n" + "table {\n" + "    margin: 10px 0 15px 0;\n" + "    border-collapse: collapse;\n" + "}\n" + "td,th {\n" + "    border: 1px solid #ddd;\n" + "    padding: 3px 10px;\n" + "}\n" + "th {\n" + "    padding: 5px 10px;\n" + "}\n" + "\n" + "a {\n" + "    color: #0069d6;\n" + "}\n" + "a:hover {\n" + "    color: #0050a3;\n" + "    text-decoration: none;\n" + "}\n" + "a img {\n" + "    border: none;\n" + "    max-width:400px;\n" + "    max-height:400px;\n" + "}\n" + "p {\n" + "    margin-bottom: 9px;\n" + "}\n" + "h1,\n" + "h2,\n" + "h3,\n" + "h4,\n" + "h5,\n" + "h6 {\n" + "    color: #404040;\n"
        cssFile = cssFile + "    line-height: 36px;\n" + "}\n" + "h1 {\n" + "    margin-bottom: 18px;\n" + "    font-size: 30px;\n" + "}\n" + "h2 {\n" + "    font-size: 24px;\n" + "}\n" + "h3 {\n" + "    font-size: 18px;\n" + "}\n" + "h4 {\n" + "    font-size: 16px;\n" + "}\n" + "h5 {\n" + "    font-size: 14px;\n" + "}\n" + "h6 {\n" + "    font-size: 13px;\n" + "}\n" + "hr {\n" + "    margin: 0 0 19px;\n" + "    border: 0;\n" + "    border-bottom: 1px solid #ccc;\n" + "}\n" + "blockquote {\n" + "    padding: 13px 13px 21px 15px;\n" + "    margin-bottom: 18px;\n" + "    font-family:georgia,serif;\n" + "    font-style: italic;\n" + "}\n" + "blockquote:before {\n" + "    content:\"\\201C\";\n" + "    font-size:40px;\n" + "    margin-left:-10px;\n" + "    font-family:georgia,serif;\n" + "    color:#eee;\n" + "}\n" + "blockquote p {\n" + "    font-size: 14px;\n" + "    font-weight: 300;\n" + "    line-height: 18px;\n" + "    margin-bottom: 0;\n" + "    font-style: italic;\n" + "}\n" + "code, pre {\n" + "    font-family: Monaco, Andale Mono, Courier New, monospace;\n" + "}\n" + "code {\n" + "    background-color: #fee9cc;\n"
        cssFile = cssFile + "    color: rgba(0, 0, 0, 0.75);\n" + "    padding: 1px 3px;\n" + "    font-size: 12px;\n" + "    -webkit-border-radius: 3px;\n" + "    -moz-border-radius: 3px;\n" + "    border-radius: 3px;\n" + "}\n" + "pre {\n" + "    display: block;\n" + "    padding: 14px;\n" + "    margin: 0 0 18px;\n" + "    line-height: 16px;\n" + "    font-size: 11px;\n" + "    border: 1px solid #d9d9d9;\n" + "    white-space: pre-wrap;\n" + "    word-wrap: break-word;\n" + "}\n" + "pre code {\n" + "    background-color: #fff;\n" + "    color:#737373;\n" + "    font-size: 11px;\n" + "    padding: 0;\n" + "}\n" + "sup {\n" + "    font-size: 0.83em;\n" + "    vertical-align: super;\n" + "    line-height: 0;\n" + "}\n" + "* {\n" + "    -webkit-print-color-adjust: exact;\n" + "}\n" + "@media screen and (min-width: 914px) {\n" + "    body {\n" + "        width: 854px;\n" + "        margin:10px auto;\n" + "    }\n" + "}\n" + "@media print {\n" + "    body,code,pre code,h1,h2,h3,h4,h5,h6 {\n" + "        color: black;\n" + "    }\n" + "    table, pre {\n" + "        page-break-inside: avoid;\n" + "    }\n" + "}"
        file = open(os.path.join(cssDir, 'default.css'), 'w+')
        file.write(cssFile)
        file.close()

        cssFile = "*{margin:0;padding:0;}\n" + "body {\n" + "    font:13.34px helvetica,arial,freesans,clean,sans-serif;\n" + "    color:black;\n" + "    line-height:1.4em;\n" + "    background-color: #F8F8F8;\n" + "    padding: 0.7em;\n" + "}\n" + "p {\n" + "    margin:1em 0;\n" + "    line-height:1.5em;\n" + "}\n" + "table {\n" + "    font-size:inherit;\n" + "    font:100%;\n" + "    margin:1em;\n" + "}\n" + "table th{border-bottom:1px solid #bbb;padding:.2em 1em;}\n" + "table td{border-bottom:1px solid #ddd;padding:.2em 1em;}\n" + "input[type=text],input[type=password],input[type=image],textarea{font:99% helvetica,arial,freesans,sans-serif;}\n" + "select,option{padding:0 .25em;}\n" + "optgroup{margin-top:.5em;}\n" + "pre,code{font:12px Monaco,\"Courier New\",\"DejaVu Sans Mono\",\"Bitstream Vera Sans Mono\",monospace;}\n" + "pre {\n" + "    margin:1em 0;\n" + "    font-size:12px;\n" + "    background-color:#eee;\n" + "    border:1px solid #ddd;\n" + "    padding:5px;\n" + "    line-height:1.5em;\n"
        cssFile = cssFile + "    color:#444;\n" + "    overflow:auto;\n" + "    -webkit-box-shadow:rgba(0,0,0,0.07) 0 1px 2px inset;\n" + "    -webkit-border-radius:3px;\n" + "    -moz-border-radius:3px;border-radius:3px;\n" + "}\n" + "pre code {\n" + "    padding:0;\n" + "    font-size:12px;\n" + "    background-color:#eee;\n" + "    border:none;\n" + "}\n" + "code {\n" + "    font-size:12px;\n" + "    background-color:#f8f8ff;\n" + "    color:#444;\n" + "    padding:0 .2em;\n" + "    border:1px solid #dedede;\n" + "}\n" + "img{border:0;max-width:100%;}\n" + "abbr{border-bottom:none;}\n" + "a{color:#4183c4;text-decoration:none;}\n" + "a:hover{text-decoration:underline;}\n" + "a code,a:link code,a:visited code{color:#4183c4;}\n" + "h2,h3{margin:1em 0;}\n" + "h1,h2,h3,h4,h5,h6{border:0;}\n" + "h1{font-size:170%;border-top:4px solid #aaa;padding-top:.5em;margin-top:1.5em;}\n" + "h1:first-child{margin-top:0;padding-top:.25em;border-top:none;}\n" + "h2{font-size:150%;margin-top:1.5em;border-top:4px solid #e0e0e0;padding-top:.5em;}\n"
        cssFile = cssFile + "h3{margin-top:1em;}\n" + "hr{border:1px solid #ddd;}\n" + "ul{margin:1em 0 1em 2em;}\n" + "ol{margin:1em 0 1em 2em;}\n" + "ul li,ol li{margin-top:.5em;margin-bottom:.5em;}\n" + "ul ul,ul ol,ol ol,ol ul{margin-top:0;margin-bottom:0;}\n" + "blockquote{margin:1em 0;border-left:5px solid #ddd;padding-left:.6em;color:#555;}\n" + "dt{font-weight:bold;margin-left:1em;}\n" + "dd{margin-left:2em;margin-bottom:1em;}\n" + "sup {\n" + "    font-size: 0.83em;\n" + "    vertical-align: super;\n" + "    line-height: 0;\n" + "}\n" + "* {\n" + "    -webkit-print-color-adjust: exact;\n" + "}\n" + "@media screen and (min-width: 914px) {\n" + "    body {\n" + "        width: 854px;\n" + "        margin:0 auto;\n" + "    }\n" + "}\n" + "@media print {\n" + "    table, pre {\n" + "        page-break-inside: avoid;\n" + "    }\n" + "    pre {\n" + "        word-wrap: break-word;\n" + "    }\n" + "}\n"
        file = open(os.path.join(cssDir, 'GitHub.css'), 'w+')
        file.write(cssFile)
        file.close()
