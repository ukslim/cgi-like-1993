#!/bin/sh
echo "Content-type: text/html"
echo ""

name_param=$(echo "$QUERY_STRING" | grep -o "name=[^&]*" | cut -d= -f2)

cat << EOF
<html>
  <h1>Hello $name_param</h1>
  
EOF

echo "<p>Here is my query string</p>"
echo $QUERY_STRING

cat << EOF
</html>
EOF
