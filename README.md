# launch-tray

Menu bar for Mac that launches the specified process in the background.

Prepare the following configuration file.

~/.launch-tray.json

```
[
    {
        "name": "Notify",
        "exec": "sleep 3; osascript -e 'on run argv display notification item 1 of argv end run' -- 'xxx'"
    },
    ....
]
```
