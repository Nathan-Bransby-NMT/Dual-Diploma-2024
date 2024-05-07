> Ref: [https://git-scm.com/book/en/v2/Git-Tools-Submodules](https://git-scm.com/book/en/v2/Git-Tools-Submodules)

# Git Submodule Support _(Guide)

## Adding an existing Git repository as a submodule

```git
$ git submodule add https://github.com/chaconinc/DbConnector
```

## Cloning a Project with Submodules

```git
$ git clone https://github.com/chaconinc/MainProject
```
The DbConnector directory is there, but empty. You must run two commands: git submodule init to initialize your local configuration file, and git submodule update to fetch all the data from that project and check out the appropriate commit listed in your superproject:
