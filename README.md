# CGI like it's 1993

A colleague mentioned to me that he'd had a conversation along the lines of:

> Hey! What if instead of a single page and the browser doing all the work, 
> we had something on the server that produces the page and all it's content.

I realised that we have a generation who perhaps don't know how we used to write
dynamic web pages.

This tiny project goes right back to basics: the Common Gateway Interface. It's
just to demonstrate how things like this used to work. You can reason about why
things changed.

Yeah, in 1993 we really would write CGI scripts in Shell.

One script produces a page of HTML by reading comment files from `db/`

Another script reads form data from stdin, creates a file in `db/` and redirects you
to the first script to see the outcome.

Don't deploy this anywhere real - it has security holes. Some of them I've left in
deberately as a talking point (shell vars aren't properly quoted).
Maybe there are ones I don't know about...

Try including a `!` in your comment. Try including a `*` . Oops. How would you fix it?
Use Perl next time ; ) 

CSS wasn't around at the time we were working this way, but I succumbed to temptation.

# Try it

To try this for yourself, install Apache HTTP -- I did it in a VirtualBox VM running Debian Linux.
You could run it in a VM, in Docker, or natively.

Put this `public_html` in your home directory and configure userdir support. You should be able
to view `index.html` at `http://<your VM's IP address>/~<your username>/index.html`

Configure Apache to execute the file extension .cgi as CGI and `chmod a+x *.cgi`

There are too many variants of this to document here -- ask your favourite LLM AI Chatbot, 
they'll know.
