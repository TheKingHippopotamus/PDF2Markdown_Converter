# Linux-Cheat-Sheet-Sponsored-By-Loggly

*Converted from PDF on 2025-07-06 11:09:49*


## Page 1

### Linux Command Cheat Sheet
### Share This Cheat Sheet
Basic commands File management File Utilities Memory & Processes
| Pipe (redirect) output find search for a file tr -d translate or delete character free -m display free and used system memory
sudo [command] run < command> in superuser ls -a -C -h list content of directory uniq -c -u report or omit repeated lines mode killall stop all process by name
rm -r -f remove files and directory split -l split file into pieces
nohup [command] run < command> immune to sensors CPU temperature
hangup signal locate -i find file, using updatedb(8) wc -w print newline, word, and byte
database counts for each file top display current processes, real
man [command] display help pages of time monitoring
```
< command> cp -a -R -i copy files or directory head -n output the first part of files kill -1 -9 send signal to process
```
```
[command] & run < command> and send task du -s disk usage cut -s remove section from file
```
to background service manage or run sysV init script
file -b -i identify the file type diff -q file compare, line by line [start|stop|restart] >> [fileA] append to fileA, preserving
existing contents mv -f -i move files or directory join -i join lines of two files on a ps aux display current processes, common field snapshot
```
> [fileA] output to fileA, overwriting grep, egrep, fgrep -i -v print lines matching pattern
```
contents more, less view file content, one page at a dmesg -k display system messages time echo -n display a line of text
File compression sort -n sort lines in text file xargs build command line from
### Disk Utilities
previous output comm -3 compare two sorted files, line
tar xvfz create or extract .tar or .tgz by line
1>2& Redirect stdout to stderr files df -h, -i File system usage cat -s concatenate files to the
fg %N go to task N gzip, gunzip, zcat create, extract or view .gz files standard output mkfs -t -V create file system
jobs list task uuencode, uudecode create or extract .Z files tail -f output last part of the file resize2fs update a filesystem, after lvextend*
ctrl-z suspend current task zip, unzip -v create or extract .ZIP files fsck -A -N file system check & repair
rpm create or extract .rpm files Scripting pvcreate create physical volume
bzip2, bunzip2 create or extract .bz2 files File permission
awk, gawk pattern scanning mount -a -t mount a filesystem rar create or extract .rar files
chmod -c -R chmod file read, write and tsh tiny shell fdisk -l edit disk partition executable permission
```
" " anything within double quotes lvcreate create a logical volume
```
touch -a -t modify (or create) file timestamp File Editor is unchanged except \ and $ umount -f -v umount a filesystem
chown -c -R change file ownership ' ' anything within single quote is ex basic editor unchanged
chgrp -c -R change file group permission
vi visual editor python "object-oriented programming
touch -a -t modify (or create) file language" Misc Commands timestamp nano pico clone bash GNU bourne-again SHell
view view file only pwd -P print current working directory ksh korn shell
emacs extensible, customizable editor bc high precision calculator Network php general-purpose scripting
sublime yet another text editor language expr evaluate expression
netstat -r -v print network information, sed stream editor csh, tcsh C shell cal print calender routing and connections
pico simple editor perl Practical Extraction and Report export assign or remove environment
telnet user interface to the TELNET Language variable protocol
source [file] load any functions file into the ` [command] backquote, execute command
tcpdump dump network traffic Directory Utilities current shell, requires the file
to be executable date -d print formatted date ssh -i openSSH client
mkdir create a directory $[variable] if set, access the variable ping -c print routing packet trace to host network rmdir remove a directory Read the Blog Post »
Compiled by Alvin Khoo bit.ly/Linux-Commands
| Linux Command Cheat Sheet
Share This Cheat Sheet |
| --- |
| Basic commands File management File Utilities Memory & Processes
| Pipe (redirect) output find search for a file tr -d translate or delete character free -m display free and used system
memory
sudo [command] run < command> in superuser ls -a -C -h list content of directory uniq -c -u report or omit repeated lines
mode killall stop all process by name
rm -r -f remove files and directory split -l split file into pieces
nohup [command] run < command> immune to sensors CPU temperature
hangup signal locate -i find file, using updatedb(8) wc -w print newline, word, and byte
database counts for each file top display current processes, real
man [command] display help pages of time monitoring
< command> cp -a -R -i copy files or directory head -n output the first part of files
kill -1 -9 send signal to process
[command] & run < command> and send task du -s disk usage cut -s remove section from file
to background service manage or run sysV init script
file -b -i identify the file type diff -q file compare, line by line [start|stop|restart]
>> [fileA] append to fileA, preserving
existing contents mv -f -i move files or directory join -i join lines of two files on a ps aux display current processes,
common field snapshot
> [fileA] output to fileA, overwriting grep, egrep, fgrep -i -v print lines matching pattern
contents more, less view file content, one page at a dmesg -k display system messages
time
echo -n display a line of text
File compression sort -n sort lines in text file
xargs build command line from
Disk Utilities
previous output comm -3 compare two sorted files, line
tar xvfz create or extract .tar or .tgz by line
1>2& Redirect stdout to stderr files df -h, -i File system usage
cat -s concatenate files to the
fg %N go to task N gzip, gunzip, zcat create, extract or view .gz files standard output mkfs -t -V create file system
jobs list task uuencode, uudecode create or extract .Z files tail -f output last part of the file resize2fs update a filesystem, after
lvextend*
ctrl-z suspend current task zip, unzip -v create or extract .ZIP files
fsck -A -N file system check & repair
rpm create or extract .rpm files Scripting
pvcreate create physical volume
bzip2, bunzip2 create or extract .bz2 files
File permission
awk, gawk pattern scanning mount -a -t mount a filesystem
rar create or extract .rar files
chmod -c -R chmod file read, write and tsh tiny shell fdisk -l edit disk partition
executable permission
" " anything within double quotes lvcreate create a logical volume
touch -a -t modify (or create) file timestamp File Editor is unchanged except \ and $
umount -f -v umount a filesystem
chown -c -R change file ownership ' ' anything within single quote is
ex basic editor unchanged
chgrp -c -R change file group permission
vi visual editor python "object-oriented programming
touch -a -t modify (or create) file language" Misc Commands
timestamp nano pico clone
bash GNU bourne-again SHell
view view file only pwd -P print current working directory
ksh korn shell
emacs extensible, customizable editor bc high precision calculator
Network php general-purpose scripting
sublime yet another text editor language expr evaluate expression
netstat -r -v print network information, sed stream editor csh, tcsh C shell cal print calender
routing and connections
pico simple editor perl Practical Extraction and Report export assign or remove environment
telnet user interface to the TELNET Language variable
protocol
source [file] load any functions file into the ` [command] backquote, execute command
tcpdump dump network traffic Directory Utilities current shell, requires the file
to be executable date -d print formatted date
ssh -i openSSH client
mkdir create a directory $[variable] if set, access the variable
ping -c print routing packet trace to
host network rmdir remove a directory
Read the Blog Post » |
| Compiled by Alvin Khoo bit.ly/Linux-Commands |

| Basic commands |
| --- |
| | Pipe (redirect) output
sudo [command] run < command> in superuser
mode
nohup [command] run < command> immune to
hangup signal
man [command] display help pages of
< command>
[command] & run < command> and send task
to background
>> [fileA] append to fileA, preserving
existing contents
> [fileA] output to fileA, overwriting
contents
echo -n display a line of text
xargs build command line from
previous output
1>2& Redirect stdout to stderr
fg %N go to task N
jobs list task
ctrl-z suspend current task |

| File management |
| --- |
| find search for a file
ls -a -C -h list content of directory
rm -r -f remove files and directory
locate -i find file, using updatedb(8)
database
cp -a -R -i copy files or directory
du -s disk usage
file -b -i identify the file type
mv -f -i move files or directory
grep, egrep, fgrep -i -v print lines matching pattern |

| File Utilities |
| --- |
| tr -d translate or delete character
uniq -c -u report or omit repeated lines
split -l split file into pieces
wc -w print newline, word, and byte
counts for each file
head -n output the first part of files
cut -s remove section from file
diff -q file compare, line by line
join -i join lines of two files on a
common field
more, less view file content, one page at a
time
sort -n sort lines in text file
comm -3 compare two sorted files, line
by line
cat -s concatenate files to the
standard output
tail -f output last part of the file |

| Memory & Processes |
| --- |
| free -m display free and used system
memory
killall stop all process by name
sensors CPU temperature
top display current processes, real
time monitoring
kill -1 -9 send signal to process
service manage or run sysV init script
[start|stop|restart]
ps aux display current processes,
snapshot
dmesg -k display system messages |

| File compression |
| --- |
| tar xvfz create or extract .tar or .tgz
files
gzip, gunzip, zcat create, extract or view .gz files
uuencode, uudecode create or extract .Z files
zip, unzip -v create or extract .ZIP files
rpm create or extract .rpm files
bzip2, bunzip2 create or extract .bz2 files
rar create or extract .rar files |

| Disk Utilities |
| --- |
| df -h, -i File system usage
mkfs -t -V create file system
resize2fs update a filesystem, after
lvextend*
fsck -A -N file system check & repair
pvcreate create physical volume
mount -a -t mount a filesystem
fdisk -l edit disk partition
lvcreate create a logical volume
umount -f -v umount a filesystem |

| Scripting |
| --- |
| awk, gawk pattern scanning
tsh tiny shell
" " anything within double quotes
is unchanged except \ and $
' ' anything within single quote is
unchanged
python "object-oriented programming
language"
bash GNU bourne-again SHell
ksh korn shell
php general-purpose scripting
language
csh, tcsh C shell
perl Practical Extraction and Report
Language
source [file] load any functions file into the
current shell, requires the file
to be executable |

| File permission |
| --- |
| chmod -c -R chmod file read, write and
executable permission
touch -a -t modify (or create) file timestamp
chown -c -R change file ownership
chgrp -c -R change file group permission
touch -a -t modify (or create) file
timestamp |

| File Editor |
| --- |
| ex basic editor
vi visual editor
nano pico clone
view view file only
emacs extensible, customizable editor
sublime yet another text editor
sed stream editor
pico simple editor |

| Misc Commands |
| --- |
| pwd -P print current working directory
bc high precision calculator
expr evaluate expression
cal print calender
export assign or remove environment
variable
` [command] backquote, execute command
date -d print formatted date
$[variable] if set, access the variable |

| Network |
| --- |
| netstat -r -v print network information,
routing and connections
telnet user interface to the TELNET
protocol
tcpdump dump network traffic
ssh -i openSSH client
ping -c print routing packet trace to
host network |

| Directory Utilities |
| --- |
| mkdir create a directory
rmdir remove a directory |

| Read the Blog Post » |
| --- |
| bit.ly/Linux-Commands |
