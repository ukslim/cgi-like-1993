#!/bin/sh

# CGI script accepts form data containing a "comment" field, and writes it to a file with timestamp in the
# filename.

# I have deliberately failed to follow best practices for quoting, to demonstrate how easy it is to do.
# The code still appears to work, but it has serious security flaws -- see if you can identify an exploit.

echo "Content-type: text/html"
echo ""

read -r post_data

# Extract the comment from the form data (assuming field name is 'comment')
comment=$(echo $post_data | sed 's/comment=//' | sed 's/+/ /g' | sed 's/%20/ /g' | sed 's/%0D%0A/\n/g')

filename="db/$(date +%s)-$$.txt"
echo $comment > $filename

# Redirect back to main page
echo "<html>"
echo "<head>"
echo "<link rel='stylesheet' type='text/css' href='style.css'>"
echo "<meta http-equiv='refresh' content='0;url=comments.cgi'>"
echo "</head>"
echo "<body>"
echo "Saving comment..."
# echo "<pre>"
# echo $post_data
# echo "</pre>"
echo "</body>"
echo "</html>" 