for file in *.md; do
   python convert_front_matter.py "$file" >> output.md;
done
