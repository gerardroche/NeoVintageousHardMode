# Copyright (C) 2018-2023 The NeoVintageous Team (NeoVintageous).
#
# This file is part of NeoVintageous.
#
# NeoVintageous is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# NeoVintageous is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with NeoVintageous.  If not, see <https://www.gnu.org/licenses/>.

import traceback

import sublime


def plugin_loaded():
    try:
        from NeoVintageous.nv.ex_cmds import do_ex_cmdline
        window = sublime.active_window()

        do_ex_cmdline(window, ':nnoremap h :Noop<CR>')
        do_ex_cmdline(window, ':nnoremap j :Noop<CR>')
        do_ex_cmdline(window, ':nnoremap l :Noop<CR>')
        do_ex_cmdline(window, ':nnoremap k :Noop<CR>')
        do_ex_cmdline(window, ':nnoremap + :Noop<CR>')
        do_ex_cmdline(window, ':nnoremap - :Noop<CR>')

        do_ex_cmdline(window, ':vnoremap h :Noop<CR>')
        do_ex_cmdline(window, ':vnoremap j :Noop<CR>')
        do_ex_cmdline(window, ':vnoremap l :Noop<CR>')
        do_ex_cmdline(window, ':vnoremap k :Noop<CR>')
        do_ex_cmdline(window, ':vnoremap + :Noop<CR>')
        do_ex_cmdline(window, ':vnoremap - :Noop<CR>')
    except Exception:
        traceback.print_exc()
