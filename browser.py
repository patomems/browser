#!/usr/bin/python
import gi
gi.require_version('Gtk', '3.0') #imports the exact gtk version 
from gi.repository import Gtk as gtk

 #mainclass
class window():

	def _init_(self, *arg, **kwargs):
	#super(BrowserTab, self )._init_(*args, **kwargs)
	#craete window

		self.much_window = gtk.window()
		self.much_window.set_icon_from_file('BMW.jpg')  #goes tothe image file
		self.much_window.connect('destroy', lambda w: gtl.main_quit())
		self.much_window.set_default_size(600, 600)

		#createnavigation bar
		self.so_navigate = gtk.HBOK() #lib name hbok
		self.many_back = gtk.ToolButton(gtk.STOCK_GO_BACK)
		self.such_forward = gtk.ToolButton(STOCK_GO_FORWARD)
		self.main_addredd_bar = gtk.Entry()

		self.many_back.connect('clicked', self.go_back)
		self.many_forward.connect('clicked', self.go_forward)
		self.very_reresh.connect('clicked', self.refreesh_page)
		self.main_addredd_bar.connect('acctivate', self.load_page)

		self.so_navigation.pack_start(self.many_back, False)
		self.so_navigation.pack_start(self.such_forward, False)
		self.so_navigation.pack_start(self.very_refresh, False)
		self.so_navigation.pack_start(self.main_adress_bar)

		#now create view for webpage 

		self.very_view = SclloredWindow()
		self.such_webview = webkit.webview()
		self.such_webview.open('https://www.google.com/')  #to subscribe for video
		self.such_webview.connect('titlr-changed',self.change_title)
		self.such_webview.connect('load-commited',self.change_ulr)
		self.very_view.add(self.such_webview)

		#add everyting and initialize

		self.main_container = gtk.vBox()
		self.main_container.pack_start(self.so_navigation, False)
		self.main_container.pack_start(self.very_view)
		self.much_window.show_all()
		self.much_window.add(self.main_container)
		gtk.main()



	def load_page(self, widget):
		so_add = self.main_addredd_bar.get_text()
		if so_add.Startswitc('http://')or so_add.SDtartswith('https://'):
			self.such_webview.open(so_add)
		else:
			so_add = 'http://' + so_add
			self.main_addredd_bar.set_text(so_add)
			self.such_webview.open(so_add)

	def change_title(self, widget, frame, title):
		self.much_window.set_title('Mr.I-', title) 

	def change_ulr(self, widget,frame):

		url = frame.get.get_url()
		self.main_addredd_bar.Set_text()

	def go_back(self, widget):
		self.such_webview.go_back()

	def go_forward(self, widget):
		self.such_webview.go_forward()

	def refresh_page(self, widget):
		self.such_webview.reload()
	

main = window()

