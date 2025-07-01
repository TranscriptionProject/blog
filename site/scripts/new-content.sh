#!/bin/bash

# Usage: ./new-content.sh <blog|newsletter> <title-with-dashes>

if [ $# -ne 2 ]; then
    echo "Usage: $0 <blog|newsletter> <title-with-dashes>"
    exit 1
fi

TYPE=$1
TITLE=$2

if [ "$TYPE" != "blog" ] && [ "$TYPE" != "newsletter" ]; then
    echo "Error: Type must be 'blog' or 'newsletter'"
    exit 1
fi

DATE=$(date +%Y-%m-%d)
DATETIME=$(date -u +"%Y-%m-%dT%H:%M:%SZ")
FILENAME="${DATE}_${TITLE}.md"
PATHNAME="content/${TYPE}/${FILENAME}"

# Create front matter based on type
if [ "$TYPE" = "blog" ]; then
    cat > "$PATHNAME" <<EOF
+++
date = "$DATETIME"
description = ""
draft = false
image = ""
slug = "$TITLE"
url = "/blog/$TITLE"
summary = ""
title = ""
+++

EOF
elif [ "$TYPE" = "newsletter" ]; then
    cat > "$PATHNAME" <<EOF
+++
categories = ["Newsletter"]
date = "$DATETIME"
description = ""
draft = false
slug = "$TITLE"
url = "/newsletter/$TITLE"
tags = ["Newsletter"]
title = ""
+++

EOF
fi

echo "Created: $PATHNAME"
