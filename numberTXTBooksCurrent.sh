find . -mindepth 1 -type f -name "*.txt" -exec printf x \; | wc -c
