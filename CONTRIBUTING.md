# How to contribute

So you've written a blocklet for i3blocks and would like to share it with the 
community, great! Let's just set a few ground rules in order to get your
blocklet included. 

The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD", 
"SHOULD NOT", "RECOMMENDED", "MAY", and "OPTIONAL" in this document are to be 
interpreted as described in [RFC 2119](https://www.ietf.org/rfc/rfc2119.txt).

# Directory guidelines

1. A blocklet MUST be confined to a single directory and the name of the 
   directory MUST be relevant to the blocklet's purpose or core feature.
2. A blocklet MUST be human readable.
3. A blocklet MUST contain a `README.md` explaining what the blocklet does,
   what its dependencies are, and any special instruction or setup required to
   use it.
4. A suggested i3blocks configuration MUST be included in an `i3blocks.conf` 
   file or within the `README.md`.
5. Any non-obvious assumptions required to make the configuration work SHOULD 
   be included either in the `README.md` or as comments in the configuration.
6. A blocklet's suggested command SHOULD be of the form
   `command=$SCRIPT_DIR/myscript [args...]` even
   if the script is a single line. The [args...] SHOULD be empty, in favor of
   using injected properties.
7. The command file (`myscript` above) SHOULD be the entirety of the
   executable part of your blocklet, i.e. your code is a single script.
8. The command file's name, SHOULD match the name of the 
   containing directory. E.g. `myscript/myscript`
   is a good name, but `myscript/yourscript` is not.
9. A blocklet SHOULD NOT have a separate non `i3blocks.conf` configuration
   file. Any extra configuration (e.g. default colors, paths, etc.) SHOULD be 
   injected properties.
10. A blocklet MUST include at least one screenshot of what it looks like in
   action.
11. A blocklet MAY require building/compiling, but if it does the build process SHOULD be
   as simple as possible (preferably nothing more than running `make`)
12. A blocklet SHOULD include a `LICENSE` file.
13. A blocklet MAY include a `.gitignore` file.

# Dependency guidelines

1. Listing standard utilities as dependencies is OPTIONAL.
2. If a blocklet requires a specific minimum version of a program, that program
   SHOULD be listed as a dependency, and the minimum version SHOULD be listed
   as well.

# Pull request guidelines

1. Every commit being merged in a pull request MUST begin with the name of the 
   blocklet it concerns, .e.g. `myscript: update colors`
2. A contributor with write access MUST NOT merge any pull request that he or
   she created, unless there are no other contributors with write access 
   currently active.
3. Commit messages SHOULD be written in imperative form. E.g. 
   `myscript: add option to configure colors`, instead of
   `myscript: added option to configure colors`.
4. Commit message first lines SHOULD be 72 characters or less but descriptive, 
   and details MAY be added to subsequent lines.
5. Commit details SHOULD write `Fixes: [issue]` or `Closes: [issue]` if
   the commit is meant to fix/close an issue on the issues page.
6. A pull request SHOULD contribute significant change to exactly one
   blocklet. A bug fix or new injected property will usually be considered 
   a significant change.

# Example workflow

In case you have never made a pull request before, here is an example workflow.

1. You write and test your blocklet called `myscript`.
2. You write a `README.md` and `i3blocks.conf` to go with your script, make a 
   `screenshot.png` and put `myscript`, `README.md`, `i3blocks.conf`, 
   `screenshot.png`, and your favorite `LICENSE` into a
   directory called `myscript`.
3. You fork the i3blocks-contrib repository on github, and clone your fork of
   i3blocks-contrib onto your computer with `git clone [your fork here]`.
4. You copy your `myscript` directory to the top level of the cloned
   i3blocks-contrib directory and `cd` to the top level directory.
5. You `git add myscript` to tell git to track your blocklet's directory, you 
   will need to do this before every commit.
6. You `git commit` and leave a commit message of the form
   `myscript: add myscript, a short description of myscript`
7. Perhaps you make a few last minute changes, and add another commit.
8. You squash your commits into one with `git rebase -i` and follow the
   instructions, leaving only your first commit and commits that were already 
   there unsquashed.
9. You push your changes to your fork on github with `git push`.
10. You navigate to vivien's i3blocks-contrib, click "pull requests" and
   "New pull request". You click "compare across forks", then select the base 
   as vivien's i3blocks-contrib and the head fork as yours. You click 
   "Create pull request".
11. The community makes some comments and suggests some things to improve before 
   your blocklet is accepted.
12. You add and commit changes to your local copy, and then squash them as before, so 
   that there are only two commits besides those that were there when you first
   forked, your initial commit and one representing all the changes made to 
   address community concerns.
13. You push to your remote fork of i3blocks-contrib, and the changes 
   automatically get incorporated into the pull request process.
14. A maintainer with write access to vivien's i3blocks-contrib decides your
   script is ready to be merged and merges it in, possibly making minor changes
   of their own in the process.

Whenever you make a significant change to your blocklet or fix a bug,
squash your local commits since your last pull request and replace the commit
message with something of the form

    myscript: what has changed since last pull request
    
    More detailed description of changes, perhaps including:
        Change 1
        Change 2
        Change 3

Then push to your remote fork, navigate to vivien's, and make a new pull
request.
