#!/usr/bin/env bash
set -euo pipefail

# This script deploys the blog, there are 4 steps all done over ssh
# 0. Clone the repo if it's not there
# 1. Pull changes to blog repo
# 2. Pull changes to smol build repo
# 3. Build new site
# 4. Trigger a reset of Caddy

ssh -A root@dollar-box 'bash -s' <<EOF
	set -euxo pipefail;

	# If the "smol_blog" directory doesn't exist then pull the repos first
	if [ ! -d smol_blog ]; then
	  	git clone git@github.com:co-0p/smol_blog.git;
		cd smol_blog && git clone git@github.com:co-0p/smol_build.sh.git;
	fi

	# Pull and reset the smol blog and smol build repos
	cd /root/smol_blog                && git fetch origin && git reset --hard origin/main;
	cd /root/smol_blog/smol_build.sh  && git fetch origin && git reset --hard origin/main;
	cd /root/smol_blog                && ./smol_build.sh/smol_build.sh src /var/www/html;
	systemctl reload caddy; # Reset caddy
EOF



