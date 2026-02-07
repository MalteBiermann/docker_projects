import os
os.environ["GMT_USERDIR"] = "/workspaces/gmt-docker/data"

import pygmt
fig = pygmt.Figure()
pygmt.config(DIR_CACHE = '/workspaces/gmt-docker/data', DIR_GSHHG = '/workspaces/gmt-docker/data')

fig.coast(projection="H10c", region="g", frame=True, land="gray")
outputfilename = "app/out/out.pdf"
fig.savefig(outputfilename)