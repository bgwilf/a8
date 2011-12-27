# -*- coding: utf-8 -*- 
# (c) 2005-2011 PIDA Authors
# vim: ft=python sw=2 ts=2 sts=2 tw=80


"""Abominade Monolith."""


from a8 import terminals, files, buffers, vimembed, window


class Abominade(object):
  """Abominade Monolith"""

  def __init__(self):
    self.files = files.FileManager(self)
    self.buffers = buffers.BufferManager(self)
    self.terminals = terminals.TerminalManager(self)
    self.vim = vimembed.VimManager(self)
    self.ui = window.ApplicationWindow(self)

  def start(self):
    """Start a8"""
    self.vim.start()
    self.terminals.execute()
    self.files.browse()
    self.ui.start()

  def stop(self):
    """Stop a8"""
    self.vim.stop()
