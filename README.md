# Open!Next D2.5 process faciliation dashboard frontend demo

[![Demo frontend](https://img.shields.io/badge/Demo-CLICK%20HERE-green.svg?style=flat)](https://wp22-frontend-demo.herokuapp.com/app/1)
[![Python version](https://img.shields.io/badge/Python-3.10-blue.svg?style=flat&logo=Python&logoColor=white)](https://docs.python.org/3.10)
[![standard-readme compliant](https://img.shields.io/badge/readme%20style-standard-brightgreen.svg?style=flat)](https://github.com/RichardLitt/standard-readme)
[![REUSE status](https://api.reuse.software/badge/github.com/OPEN-NEXT/wp2.2_frontend_dev)](https://api.reuse.software/info/github.com/OPEN-NEXT/wp2.2_frontend_dev)
[![DOI](https://www.zenodo.org/badge/519289691.svg)](https://www.zenodo.org/badge/latestdoi/519289691)

**Example *demonstrator** frontend for an open source development status dashboard*

This repository contains code for an online frontend that visualises various metrics about [open source hardware (OSH)](https://www.oshwa.org/definition/) projects hosted on GitHub. The underlying data used here is retrieved with the backend [REST](https://en.wikipedia.org/wiki/Representational_state_transfer) application programming interface ([API](https://en.wikipedia.org/wiki/API)) implemented in the [Open!Next D2.5 backend repository](https://github.com/OPEN-NEXT/wp2.2_dev).

***This software is not for general consumers to just "double click" on and install on their devices***.

## Background

> Today’s industrial product creation is expensive, risky and unsustainable. At the same time, the process is highly inaccessible to consumers who have very little input in the design and distribution of the finished product. Presently, SMEs and maker communities across Europe are coming together to fundamentally change the way we create, produce, and distribute products.

[OPENNEXT](https://opennext.eu/) is a collaboration between 19 industry and academic partners across Europe. Funded by the [European Union](https://europa.eu/)'s [Horizon 2020](https://ec.europa.eu/programmes/horizon2020/) programme, this project seeks to enable small and medium enterprises (SMEs) to work with consumers, makers, and other communities in rethinking how products are designed and produced. [Open source hardware](https://www.oshwa.org/definition/) is a key enabler of this goal where the design of a physical product is released with the freedoms for anyone to study, modify, share, and redistribute copies. These essential freedoms are based on those of [open source software](https://opensource.org/osd), which is itself derived from [free software](https://www.gnu.org/philosophy/free-sw.en.html) where the word free refers to freedom, *not* free-of-charge. When put in practice, these freedoms could potentially not only reduce proprietary vendor lock-in, planned obsolescence, or waste but also stimulate novel – even disruptive – business models. The SME partners in OPENNEXT are experimenting with producing open source hardware and even opening up the development process to wider community participation. They produce diverse products ranging from [desks](https://stykka.com/), [cargo bike modules](http://www.xyzcargo.com/), to a [digital scientific instrument platform](https://pslab.io/) (and [more](https://opennext.eu/project-team/#sme)).

Work package 2 (WP2) of OPENNEXT is gathering theoretical and practical insights on best practices for company-community collaboration when developing open source hardware. This includes running [Delphi studies](https://www.edelphi.org/) to develop a maturity model to describe the collaboration and developing a precise definition for what the "source" is in open source hardware. In particular, task 2.2 in this work package is developing a demonstration project status dashboard with "health" indicators showing the evolution of a project within the maturity model; design activities; or progress towards success based on project goals. Details of the dashboard's technical architecture are described in the deliverable 2.5 (D2.5) report.

This repository contains the example frontend code for D2.5 and to be clear, this deliverable ***is***: Designed to be deployed on a web server server. This deliverable ***is not***: For general end-users to install on consumer devices and "double click" to open.

The visualisations for this demo frontend is achieved via a [JupyterLab](https://jupyter.org) notebook using the [Plotly](https://plotly.com/python/) plotting library. Interactivity for these visualisations, such as choosing from a list of GitHub repositories to show data for, is done via the [Mercury](https://github.com/mljar/mercury) library.

In addition, this repository aims to follow international standards and good practices in open source development such as, but not limited to: 

* [SDPX 3](https://spdx.dev/) compliance with a [LICENSE](./LICENSE) file (also see [License](#license) section)
* [REUSE 3.0](https://reuse.software/) compliance with appropriate machine-readable SPDX metadata for all files and license texts in [`LICENSES`](./LICENSES/) directory
* README file (this document) conforming to the [Standard Readme Specification](https://github.com/RichardLitt/standard-readme)
* Naming the primary branch of this repository `main` instead of `master` following [modern best practices](https://github.blog/changelog/2020-10-01-the-default-branch-for-newly-created-repositories-is-now-main/)

## Install

This section assumes knowledge of [Python](https://www.python.org/), [Git](https://git-scm.com/), and using a GNU/Linux-based server including installing software from package managers and running a terminal session.

In addition, familiarity with [JupyterLab](https://jupyter.org) and the [Plotly](https://plotly.com/python/) plotting library are helpful when making modifications to the code.

**Note:** This software is designed to be deployed on a server by system administrators or developers, not on generic consumer devices.

This project requires [Python](https://www.python.org/) version 3.10 or later on your server and running it in a [Python virtual environment](https://docs.python.org/3.10/tutorial/venv.html) is optional but recommended. Detailed external library dependencies are listed in the standard-conformant [`requirements.txt`](./requirements.txt) file and also here: 

* [`jupyterlab>=3.4.5`](https://pypi.org/project/jupyterlab/)
* [`mljar-mercury>=1.1.5`](https://pypi.org/project/mljar-mercury/)
* [`pandas>=1.4.3`](https://pypi.org/project/pandas/)
* [`plotly>=5.10`](https://pypi.org/project/plotly/)

In addition to Python and the dependencies listed above, the following programs must be installed and accessible from the command line: 

* [`git`](https://git-scm.com/) (version 2.7.4 or later)
* [`pip`](https://pip.pypa.io/) (version 19.3.1 or later)

### Running locally from source

The code can be run from source and has been tested on updated versions of GNU/Linux server operating systems including [Red Hat Enterprise Linux](https://redhat.com/en/technologies/linux-platforms/enterprise-linux) 8.6. While effort has been made to keep the Python scripts and JupyterLab notebook platform-agnostic, they have not been tested under other operating systems such as [BSD](https://en.wikipedia.org/wiki/Berkeley_Software_Distribution)-derivatives, [Apple macOS](https://www.apple.com/macos/) or [Microsoft Windows](https://www.microsoft.com/windows/) as they - especially the latter two - are rarely used for hosting code such as this.

On your server, with the tools [`git`](https://git-scm.com/) and [`pip`](https://pip.pypa.io/) installed, run the following commands in a terminal session to retrieve the latest version of this repository and prepare it for development and running locally (usually for testing): 

```sh
git clone https://github.com/OPEN-NEXT/wp2.2_frontend_dev.git
pip install --user -r requirements.txt
```

The [`git`](https://git-scm.com/) command will download the files in this repository onto your server into a directory named `wp2.2_frontend_dev`, and [`pip`](https://pip.pypa.io/) will install the Python dependencies listed in [`requirements.txt`](./requirements.txt).

In a terminal window at the root directory of this repository, start the server with the [`mercury`](https://www.uvicorn.org/) command like this: 

```sh
mercury run ./repos.ipynb
```

There will be some output in the terminal. If there are no obvious error messages, this means the demo frontend is up an running, and should be accessible on your local machine on port 8000 at 127.0.0.1 (i.e. `127.0.0.1:8000`).

Note: By default, the JupyterLab notebook `repos.ipynb` will use data contained in `contrib/GitHub_repos_data.json` and visualise them. This [JSON](https://en.wikipedia.org/wiki/JSON) file contains data from various open source hardware repositories hosted on GitHub. It is the same information that the [dashboard backend API](https://github.com/OPEN-NEXT/wp2.2_dev) will provide. 

### Deploy to web

The code in this repository can be directly deployed to a cloud web app hosting provider such as [Fly.io](https://fly.io/) or [Heroku](https://heroku.com/). Here is an example of deplying to Heroku (assuming you already have an Heroku account): 

1. Make sure your terminal prompt is in the root directory of this repository. With the [Heroku commandline interface](https://devcenter.heroku.com/categories/command-line) installed, login with this comamnd: 

```sh
heroku container:login
```

2. Create a new Heroku app where "`your app name`" can be a name of your choosing: 

```sh
heroku create [your app name]
```

3. It may take a couple minutes for the app to come online. You can check your [Heroku account dashboard](https://dashboard.heroku.com/apps) for a status update. Once it is online, you can open the app in your web browser: 

```sh
heroku open
```

A demo of this is hosted on Heroku with this URL: 

```
https://wp22-frontend-demo.herokuapp.com/app/1
```

This demo instance will go into a sleep state after a period of inactivity (approximately 30 minutes at time of writing). This means it may take a while to load the demo instance when you visit it with your web browser.

## Usage

Frontends showing project status metrics from the [dashboard backend API](https://github.com/OPEN-NEXT/wp2.2_dev) could be implemented independently. Such a frontend could show aggregate information about open source hardware projects hosted on GitHub or Wikifactory.

A major component of Open!Next D2.5 is that Wikifactory has implemented various frontend dashboard features. Some of these features are *in production* an viewable on various Wikifactory projects. This will be gradually rolled out to all Wikifactory projects in the coming months.

In addition to that, this repository implements a demo frontend that shows information about open source hardware repositories hosted on GitHub. After deploying this demo per the installation steps above, open it in your web browser. You can also visit a demo instance at: [https://wp22-frontend-demo.herokuapp.com/app/1](https://wp22-frontend-demo.herokuapp.com/app/1)

The following are basic steps for interacting with the demo: 

1. When first loaded, there will be an initial page like this: 

![demo frontend initial page](./assets/frontend%20initial%20page.jpg)

2. Under the "Choose a repository" menu, you can choose from a pre-populated list of GitHub repositories, such as [`nasa-jpl/open-source-rover`](https://github.com/nasa-jpl/open-source-rover): 

![choosing a GitHub repository to visualise](./assets/frontend%20choose%20repo.jpg)

3. Click on the green "Run" button and wait several seconds for the code to run. You should then see a series of visualisations on the right: 

![overview of visualisations](./assets/frontend%20visualisations.jpg)

4. You can scroll down to see graphs of "Commits history", "Issues opened/closed", a list of "Tags" for the repository, and pie chart breakdowns of "File type" and "File editability", followed by "License information". Some of these visualisations are interactive.

5. For graphs such as commit and issue histories, you can use your mouse to click and drag a box to zoom in to: 

![click and drag to zoom in on graphs](./assets/frontend%20drag%20to%20zoom.jpg)

6. Or, when you hover your mouse cursor over a slice in a pie chart, it will display a tool tip. In this screenshot, it is showing that 11.2% of the files in the `nasa-jpl/open-source-rover` repository are "ECAD" (electronics [CAD](https://en.wikipedia.org/wiki/Computer-aided_design)) files: 

![pie chart mouse hover tool tip](./assets/frontend%20pie%20chart%20hover%20tooltip.jpg)

7. For each visualisation, you can hover your mouse cursor over the top right to reveal more controls, such as a "camera" button for downloading a [PNG](https://en.wikipedia.org/wiki/Portable_Network_Graphics) image of the current view: 

![additional visualisation controls](./assets/frontend%20visualisation%20controls.jpg)

8. An additional feature is the blue "Download" button. Clicking this will allow you to download the visualisations as a [PDF](https://en.wikipedia.org/wiki/PDF) or [HTML](https://en.wikipedia.org/wiki/HTML) file for local viewing.

## Maintainers

Dr Pen-Yuan Hsing ([@penyuan](https://github.com/penyuan)) of the [OPENNEXT](https://opennext.eu/) project is the current maintainer.

## Acknowledgements

The maintainer would like to gratefully acknowledge:

* Dr Jérémy Bonvoisin ([@jbon](https://github.com/jbon)) not only for the initial contributions to this work, but also for continued practical and theoretical insight, generosity, and guidance.
* Dr Elies Dekoninck ([@elies30](https://github.com/orgs/OPEN-NEXT/people/elies30)) and Rafaella Antoniou ([@rafaellaantoniou](https://github.com/orgs/OPEN-NEXT/people/rafaellaantoniou)) for valuable feedback and support.
* Max Kampik ([@mkampik](https://github.com/mkampik)), Diego Vaquero, and Andrés Barreiro from Wikifactory for close collaboration, design insights, and technical support throughout the project.
* OPENNEXT internal reviewers Sonika Gogineni ([@GoSFhg](https://github.com/GoSFhg)) and Martin Häuer ([@moedn](https://github.com/moedn)) for constructive criticism.
* OPENNEXT project researchers Robert Mies ([@MIE5R0](https://github.com/MIE5R0)) and Mehera Hassan ([@meherrahassan](https://github.com/meherahassan)) for useful feedback and extensive administrative support.
* The Linux Foundation [CHAOSS](https://chaoss.community/) group for insights on open source community health metrics.
* The following people for their valuable feedback via a survey (see D2.5 report for details) (in alphabetical order of last name): Jean-François Boujut ([@boujut](https://github.com/boujut)), Martin Häuer ([@moedn](https://github.com/moedn)), James Jones (CubeSpawn), Max Kampik ([@mkampik](https://github.com/mkampik)), Johannes Střelka-Petz.

[![EU flag](https://upload.wikimedia.org/wikipedia/commons/thumb/b/b7/Flag_of_Europe.svg/320px-Flag_of_Europe.svg.png)](https://commons.wikimedia.org/wiki/File:Flag_of_Europe.svg)

The work in this repository is supported by a European Union [Horizon 2020](https://ec.europa.eu/programmes/horizon2020/) programme grant (agreement ID [869984](https://cordis.europa.eu/project/id/869984)).

## License

[![GitHub AGPL-3.0-or-later license](https://img.shields.io/github/license/OPEN-NEXT/wp2.2_frontend_dev)](./LICENSE)

The Python code in this repository is licensed under the [GNU AGPLv3 or any later version](./LICENSE) © 2022 Pen-Yuan Hsing

[![CC BY-SA](https://mirrors.creativecommons.org/presskit/buttons/88x31/svg/by-sa.svg)](https://creativecommons.org/licenses/by-sa/4.0/)

This README is licensed under the [Creative Commons Attribution-ShareAlike 4.0 International license (CC BY-SA 4.0)](https://creativecommons.org/licenses/by-sa/4.0/) © 2022 Pen-Yuan Hsing

Details on other files are in the REUSE specification [dep5](./.reuse/dep5) file.