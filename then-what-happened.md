= Then what happened?

CGI seemed like (and probably was) a great idea at the time. You could write
dynamic content in C, shell, anything that could produce an executable. It was
limitless.

== Security

Security was a concern, but that can't really be pinned on CGI itself. CGI
supplied request data robustly -- it's up to the script itself to properly
use that. 

But, doing it wrong was all too easy in C and Shell (for different reasons), 
resulting in SQL injection, data leaks, remote execution exploits, etc.

People began to use Perl for their CGI, along with Perl modules which would
reliably parse requests data as supplied by CGI. For coders coming from a 
Shell background, though, it was all too tempting to write shell-like scripts
in Perl, using `system` and `exec` to invoke shell commands, bringing back
all the same injection possibilities as Shell.

Properly written Perl CGI scripts would use Perl library functions to interact with
the system, and gradually people got used to doing this properly. We still
have vulnerabilities, even today, but at least they're more subtle.

== Expressivity

Writing code that outputs HTML is OK. It's fairly easy to make mistakes and
produce invalid HTML, but browsers were always very forgiving of things like
unclosed tags.

But it wasn't long until techniques arrived in all languages to facilitate more
expressive ways of working. Templating languages, sometimes home-brewed were one
common approach.

Even with basic Shell commands, this fairly is easy to achieve:

```
cat blogpage.html.template | sed "s/__CONTENT__/$content/; s/__TITLE__/$title/; s/__AUTHOR__/$author/"
```

== Performance

The core mechanism of CGI is to spawn a whole new process for each request, 
launch an executable, which initialises, works on the request, outputs its
response, then terminates. 

This is consistent with UNIX philosophy, and UNIX systems are designed to efficiently spawn processes. But nonetheless, this didn't perform well for
high-volume web servers.

Every single request, not only would a process have to be spawned, its environment
populated, but also the executable would have to initialise. In the case of a
script (Perl, Shell, other) it would have to interpret the source code each
time. It wouldn't be able to reuse initialised resources such as database 
connections.

Fairly early on, Apache HTTPd pioneered process pooling, in which processes were
spawned in advance, used for a task, and replaced to the pool. This helped, but
with no foreknowledge of what task a process would execute, large parts of the
task still had to happen when the request arrived. 

(Aside: it was services like HTTPd that stoked demand for threads -- lightweight
processes -- in operating systems)

So various solutions were developed to address this, often taking advantage of
Apache HTTPd's modular architecture. 

 - FastCGI demands that you write executables which remain alive and process a sequence of requests. This allows things like database handles to be reused. The module spawns a pool of processes and manages the routing of requests to these.
 - `mod_perl` embeds a Perl runtime into the HTTPd's execution space, and supplies
   an API to the Perl programs it loads and runs. Recompilation is avoided, and resources can be reused from one request to the next.
 - `mod_php` takes the same approach as `mod_perl` , but uses the fancy new language
   PHP, designed specifically for producing dynamic HTML.

Only quite a lot later did it become popular to flip the responsibilities. Instead
of embedding a language runtime in an HTTP server like Apache, embed an HTTP server 
in the language runtime, or write the HTTP server in the language itself. Examples 
of this include Java containers like Tomcat, and theJavascript runtime Node.js.
