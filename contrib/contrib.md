# Contents of `contrib`

* `GitHub_repos_data.json` is an example response from the `wp2.2_dev` backend saved in JSON. It contains information about various open source hardware GitHub repositories.
* `retrieve_repo_data.py` is an example script, possibly a bit incomplete, that pulls data from the backend.
* `Datasette` includes `read_json.py` and `metadata.yml` to read the JSON file above into an SQLite database that could be served by Datasette.
* `Dockerfile` is an example Dockerfile that can be used to create a container based on this repository. The resulting container image can then be deployed to the web.