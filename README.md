"# Obsidian_nt" 
#command ```
#!/bin/bash

gstatus=`git status --porcelain`

if [ ${#gstatus} -ne 0 ]
then

    git add .
    git commit -m "$gstatu"
	git push

fi
```
