# Bash
Bash Hints


## Make terminal show the command running as title
Add these two lines (in this order) to the bottom of ~/.bashrc
```bash
PS1="\033]0;\w\007${PS1}"
trap 'echo -ne "\033]0;$BASH_COMMAND\007" > /dev/stderr' DEBUG
```


## Make terminal show the command running as title (path + command)
Add these lines to the bottom of ~/.bashrc
```bash
# Make terminal show the command running as title
# If this is an xterm set the title to user@host:dir
case "$TERM" in
xterm*|rxvt*)
    PROMPT_COMMAND='echo -ne "\033]0;${USER}@${HOSTNAME}: ${PWD}\007"'

    # Show the currently running command in the terminal title:
    # http://www.davidpashley.com/articles/xterm-titles-with-bash.html
    show_command_in_title_bar()
    {
        case "$BASH_COMMAND" in
            *\033]0*)
                # The command is trying to set the title bar as well;
                # this is most likely the execution of $PROMPT_COMMAND.
                # In any case nested escapes confuse the terminal, so don't
                # output them.
                ;;
            *)
                echo -ne "\033]0;${PWD} > ${BASH_COMMAND}\007"
                ;;
        esac
    }
    trap show_command_in_title_bar DEBUG
    ;;
*)
    ;;
esac
```

## Automatically get different terminal colors each time open terminal
Instructions:
The Script considers you're using gnome-terminal, which is the default Ubuntu terminal.
Before running the script, open the gnome-terminal and create some profiles (Edit>Preference>Profiles) with different settings as you wish (background color, text color, ..). You can name them Profile1, Profile2, Profile3 and so on. Create enough Profiles to cover the quantity of Terminals that will be opened, but if a higher number of terminals are opened, the default profile will be used.
The script creates a file ~/.Bash_Color_Changer, which it depends on, since it will tell the script if the terminal was opened regularly or after a call on .bashrc.

Add the script to the end of ~/.bashrc
```bash
# Change color according to the number of Bash shells opened
# Creates the .Bash_Color_Changer file if it's not present
if ! [ -f ~/.Bash_Color_Changer ]; then
    echo ORIGINAL > ~/.Bash_Color_Changer
fi

# Array holding the name of the profiles: Substitute it for the names you're using
Color_counter=(Profile1 Profile2 Profile3)
# Finds out the number of opened bashs counting the lines containing "bash"
# in the pstree function. (-c deactivates compact display to avoid it showing
# lines with "2*[bash]" instead of one for each bash)
Number_of_bashs=$(($(pstree -c | grep "bash" | wc -l)-1))

# Checks if the terminal being opened was opened by the user or by
# the script, and act according to it
if [ $(cat ~/.Bash_Color_Changer) = ORIGINAL ]; then 
    if ((Number_of_bashs < ${#Color_counter[*]})); then
        echo COPY > ~/.Bash_Color_Changer
        gnome-terminal --tab-with-profile-internal-id=${Color_counter[${Number_of_bashs}]} 
        exit
    fi
else 
    echo ORIGINAL > ~/.Bash_Color_Changer
fi
```
