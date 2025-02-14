#!/bin/sh

echo "Content-type: text/html"
echo ""

echo "<html><body>"
cat << EOF
<head>
    <title>Comments in CGI</title>
    <link rel="stylesheet" type="text/css" href="style.css">
</head>
<h1>Comments in CGI</h1>
<p>
  Imagine this is a blog post. You can add comments to it, in an old-fashioned way.
</p>
<form action="new_comment.cgi" method="post">
  <textarea name="comment" rows="4" cols="50"></textarea>
  <br>
  <input type="submit" value="Submit" >
</form>
EOF


cd db
for file in *; do
  if [ -f "$file" ]; then
    timestamp=$(basename "$file" .txt)
    echo "<h3>"
    date -r $file
    echo "</h3>"
    echo "<p>"
    cat "$file"
    echo "</p>"
  fi
done

echo "</body></html>"
