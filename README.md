# Smol Blog (and site)

Here lies the code for [c0-0p.io](https://c0-0p.io).

## Building
This blog depends on my [smol_build.sh](https://github.com/co-0p/smol_build.sh) tool. In fact, this blog basically just
exists because i wanted to create such a tool.

1. `cd` into the root of this cloned repo
2. `git clone` the smol_build.sh repo into the root of this blogs repo
3. run `./smol_build.sh/smol_build.sh src build` to build the site.

Then you can view the build in the browser by running a server such as `python3 -m http.server 8000 -d build`

## Deploying
If you're not me, then you're not going to be able to deploy using my script. But if you are me,
and I'm on a laptop on my tailnet, then simply run the `deploy_blog.sh` script which will connect over ssh to your cheap
server, pull any code changes, build the blog, and refresh the web server.