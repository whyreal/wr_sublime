import sublime
import sublime_plugin

FORMAT = ""

class TemplateCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		global FORMAT
		sels = self.view.sel()
		FORMAT = self.view.substr(sels[0])

class FormatCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		global FORMAT
		sels = self.view.sel()
		self.view.insert(edit, self.view.size(), "\n")
		for line in self.view.substr(sels[0]).splitlines():
			self.view.insert(edit, self.view.size(), FORMAT.format(*line.split()))
		