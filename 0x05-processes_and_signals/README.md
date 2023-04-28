# 0x05. Processes and signals

# Resources
**Read or watch:**
- [Linux PID](https://intranet.alxswe.com/rltoken/zh33PXDR6w_qyu7zXUezmw)
- [Linux process](https://intranet.alxswe.com/rltoken/px2TdWSjVO8i9SB5gHchAw)
- [Linux signal](https://intranet.alxswe.com/rltoken/qQSGz9CN52PVF3IPCuaRiw)
- [Process management in linux](https://intranet.alxswe.com/rltoken/XlYrlghzNZ6Z1cbI_IPaiA)

**man or help:**
- `ps`
- `pgrep`
- `pkill`
- `kill`
- `exit`
- `trap`

# Learning Objectives
## General
- What is a PID
- What is a process
- How to find a process’ PID
- How to kill a process
- What is a signal
- What are the 2 signals that cannot be ignored

# More Info
For those who want to know more and learn about all signals, check out [this article](https://intranet.alxswe.com/rltoken/BOU-KVNMqfKEIBo_VOI26A).

## Tasks
### 0. What is my PID
- `0-what-is-my-pid` - a Bash script that displays its own PID.

### 1. List your processes
- `1-list_your_processes` - a Bash script that displays a list of currently running processes.

### 2. Show your Bash PID
- `2-show_your_bash_pid` -  a Bash script that displays lines containing the `bash` word, thus allowing you to easily get the PID of your Bash process.

### 3. Show your Bash PID made easy
- `3-show_your_bash_pid_made_easy` - a Bash script that displays the PID, along with the process name, of processes whose name contain the word `bash`.

### 4. To infinity and beyond
- `4-to_infinity_and_beyond` - a Bash script that displays `To infinity and beyond` indefinitely.

### 5. Don't stop me now!
- `5-dont_stop_me_now` - a Bash script that stops `4-to_infinity_and_beyond` process.

### 6. Stop me if you can
- `6-stop_me_if_you_can` - a Bash script that stops `4-to_infinity_and_beyond` process.

### 7. Highlander
- `7-highlander` - a Bash script that displays `To infinity and beyond` indefinitely, With a `sleep 2` in between each iteration and `I am invincible!!!` when receiving a `SIGTERM` signal.

### 8-beheaded_process
- `8-beheaded_process` - a Bash script that kills the process `7-highlander`.

### 9. Process and PID file
- `100-process_and_pid_file`
        - Creates the file `/var/run/myscript.pid` containing its PID
        - Displays `To infinity and beyond` indefinitely
        - Displays `I hate the kill command` when receiving a SIGTERM signal
        - Displays `Y U no love me?!` when receiving a SIGINT signal
        - Deletes the file `/var/run/myscript.pid` and terminates itself when receiving a SIGQUIT or SIGTERM signal

### 10. Manage my process
- `101-manage_my_process`
- `manage_my_process`

### 11. Zombie
- `102-zombie.c` - a C program that creates 5 zombie processes.
