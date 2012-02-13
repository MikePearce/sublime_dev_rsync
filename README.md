### Usage

This plugin requires a dev_rsync.json file at the root of your project to define your rsync parameters and options.

```javascript
{
    // Must be able to ssh to this server. Easiest to set this up in ~/.ssh/config
    "host": "devserver.com",
  
    // Must have write access to this directory
    "target_dir": "/var/www/devsite.com",
    
    // Any files and/or directories you'd like to exclude from the rsync
    "exclude":
    [
        ".git",
        ".svn",
        ".DS_Store"
    ],
  
    // Any rsync options you'd like to use
    // http://ss64.com/bash/rsync_options.html
    "option":
    [
        "verbose",
        "delete",
        "archive"
    ]
}
```

I suggest you ignore your `dev_rsync.json` file so each developer on your project can have their own setup. And version a `dev_rsync.json.dist` file to provide a template for devs to get started with.

### License

All of Sublime Dev Rsync is licensed under the MIT license.