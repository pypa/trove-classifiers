from models import ClassifierRoot, ClassifierNode

classifiers = ClassifierRoot(
    children=[
        ClassifierNode(
            "Development Status",
            skip=True,
            children=[
                ClassifierNode("1 - Planning"),
                ClassifierNode("2 - Pre-Alpha"),
                ClassifierNode("3 - Alpha"),
                ClassifierNode("4 - Beta"),
                ClassifierNode("5 - Production/Stable"),
                ClassifierNode("6 - Mature"),
                ClassifierNode("7 - Inactive"),
            ],
        ),
        ClassifierNode(
            "Environment",
            skip=True,
            children=[
                ClassifierNode(
                    "Console",
                    children=[
                        ClassifierNode("Curses"),
                        ClassifierNode("Framebuffer"),
                        ClassifierNode("Newt"),
                        ClassifierNode("svgalib"),
                    ],
                ),
                ClassifierNode("Handhelds/PDA's"),
                ClassifierNode(
                    "MacOS X",
                    children=[
                        ClassifierNode("Aqua"),
                        ClassifierNode("Carbon"),
                        ClassifierNode("Cocoa"),
                    ],
                ),
                ClassifierNode("No Input/Output (Daemon)"),
                ClassifierNode("OpenStack"),
                ClassifierNode("Other Environment"),
                ClassifierNode("Plugins"),
                ClassifierNode(
                    "Web Environment",
                    children=[
                        ClassifierNode("Buffet"),
                        ClassifierNode("Mozilla"),
                        ClassifierNode("ToscaWidgets"),
                    ],
                ),
                ClassifierNode("Win32 (MS Windows)"),
                ClassifierNode(
                    "X11 Applications",
                    children=[
                        ClassifierNode("Gnome"),
                        ClassifierNode("GTK"),
                        ClassifierNode("KDE"),
                        ClassifierNode("Qt"),
                    ],
                ),
            ],
        ),
        ClassifierNode(
            "Framework",
            skip=True,
            children=[
                ClassifierNode("AiiDA"),
                ClassifierNode("AsyncIO"),
                ClassifierNode("BEAT"),
                ClassifierNode("BFG"),
                ClassifierNode("Bob"),
                ClassifierNode("Bottle"),
                ClassifierNode(
                    "Buildout",
                    children=[ClassifierNode("Extension"), ClassifierNode("Recipe")],
                ),
                ClassifierNode("CastleCMS", children=[ClassifierNode("Theme")]),
                ClassifierNode("Chandler"),
                ClassifierNode("CherryPy"),
                ClassifierNode("CubicWeb"),
                ClassifierNode("Dash"),
                ClassifierNode(
                    "Django",
                    children=[
                        ClassifierNode("1.10"),
                        ClassifierNode("1.11"),
                        ClassifierNode("1.4"),
                        ClassifierNode("1.5"),
                        ClassifierNode("1.6"),
                        ClassifierNode("1.7"),
                        ClassifierNode("1.8"),
                        ClassifierNode("1.9"),
                        ClassifierNode("2.0"),
                        ClassifierNode("2.1"),
                        ClassifierNode("2.2"),
                        ClassifierNode("3.0"),
                    ],
                ),
                ClassifierNode(
                    "Django CMS",
                    children=[
                        ClassifierNode("3.4"),
                        ClassifierNode("3.5"),
                        ClassifierNode("3.6"),
                        ClassifierNode("3.7"),
                    ],
                ),
                ClassifierNode("Flake8"),
                ClassifierNode("Flask"),
                ClassifierNode("Hypothesis"),
                ClassifierNode("IDLE"),
                ClassifierNode("IPython"),
                ClassifierNode("Jupyter"),
                ClassifierNode("Lektor"),
                ClassifierNode("Masonite"),
                ClassifierNode("Matplotlib"),
                ClassifierNode("Nengo"),
                ClassifierNode("Odoo"),
                ClassifierNode("Opps"),
                ClassifierNode("Paste"),
                ClassifierNode(
                    "Pelican",
                    children=[ClassifierNode("Plugins"), ClassifierNode("Themes")],
                ),
                ClassifierNode(
                    "Plone",
                    children=[
                        ClassifierNode("3.2"),
                        ClassifierNode("3.3"),
                        ClassifierNode("4.0"),
                        ClassifierNode("4.1"),
                        ClassifierNode("4.2"),
                        ClassifierNode("4.3"),
                        ClassifierNode("5.0"),
                        ClassifierNode("5.1"),
                        ClassifierNode("5.2"),
                        ClassifierNode("5.3"),
                        ClassifierNode("6.0"),
                        ClassifierNode("Addon"),
                        ClassifierNode("Core"),
                        ClassifierNode("Theme"),
                    ],
                ),
                ClassifierNode("Pylons"),
                ClassifierNode("Pyramid"),
                ClassifierNode("Pytest"),
                ClassifierNode("Review Board"),
                ClassifierNode(
                    "Robot Framework",
                    children=[ClassifierNode("Library"), ClassifierNode("Tool")],
                ),
                ClassifierNode("Scrapy"),
                ClassifierNode("Setuptools Plugin"),
                ClassifierNode(
                    "Sphinx",
                    children=[ClassifierNode("Extension"), ClassifierNode("Theme")],
                ),
                ClassifierNode("tox"),
                ClassifierNode("Trac"),
                ClassifierNode("Trio"),
                ClassifierNode("Tryton"),
                ClassifierNode(
                    "TurboGears",
                    children=[
                        ClassifierNode("Applications"),
                        ClassifierNode("Widgets"),
                    ],
                ),
                ClassifierNode("Twisted"),
                ClassifierNode(
                    "Wagtail", children=[ClassifierNode("1"), ClassifierNode("2")]
                ),
                ClassifierNode("ZODB"),
                ClassifierNode(
                    "Zope",
                    children=[
                        ClassifierNode("2"),
                        ClassifierNode("3"),
                        ClassifierNode("4"),
                        ClassifierNode("5"),
                    ],
                ),
                ClassifierNode("Zope2"),
                ClassifierNode("Zope3"),
            ],
        ),
        ClassifierNode(
            "Intended Audience",
            skip=True,
            children=[
                ClassifierNode("Customer Service"),
                ClassifierNode("Developers"),
                ClassifierNode("Education"),
                ClassifierNode("End Users/Desktop"),
                ClassifierNode("Financial and Insurance Industry"),
                ClassifierNode("Healthcare Industry"),
                ClassifierNode("Information Technology"),
                ClassifierNode("Legal Industry"),
                ClassifierNode("Manufacturing"),
                ClassifierNode("Other Audience"),
                ClassifierNode("Religion"),
                ClassifierNode("Science/Research"),
                ClassifierNode("System Administrators"),
                ClassifierNode("Telecommunications Industry"),
            ],
        ),
        ClassifierNode(
            "License",
            skip=True,
            children=[
                ClassifierNode("Aladdin Free Public License (AFPL)"),
                ClassifierNode("CC0 1.0 Universal (CC0 1.0) Public Domain Dedication"),
                ClassifierNode("CeCILL-B Free Software License Agreement (CECILL-B)"),
                ClassifierNode("CeCILL-C Free Software License Agreement (CECILL-C)"),
                ClassifierNode("DFSG approved"),
                ClassifierNode("Eiffel Forum License (EFL)"),
                ClassifierNode("Free For Educational Use"),
                ClassifierNode("Free For Home Use"),
                ClassifierNode("Free for non-commercial use"),
                ClassifierNode("Freely Distributable"),
                ClassifierNode("Free To Use But Restricted"),
                ClassifierNode("Freeware"),
                ClassifierNode("GUST Font License 1.0"),
                ClassifierNode("GUST Font License 2006-09-30"),
                ClassifierNode("Netscape Public License (NPL)"),
                ClassifierNode("Nokia Open Source License (NOKOS)"),
                ClassifierNode(
                    "OSI Approved",
                    children=[
                        ClassifierNode("Academic Free License (AFL)"),
                        ClassifierNode("Apache Software License"),
                        ClassifierNode("Apple Public Source License"),
                        ClassifierNode("Artistic License"),
                        ClassifierNode("Attribution Assurance License"),
                        ClassifierNode("Boost Software License 1.0 (BSL-1.0)"),
                        ClassifierNode("BSD License"),
                        ClassifierNode(
                            "CEA CNRS Inria Logiciel Libre License, version 2.1 (CeCILL-2.1)"
                        ),  # noqa
                        ClassifierNode(
                            "Common Development and Distribution License 1.0 (CDDL-1.0)"
                        ),
                        ClassifierNode("Common Public License"),
                        ClassifierNode("Eclipse Public License 1.0 (EPL-1.0)"),
                        ClassifierNode("Eclipse Public License 2.0 (EPL-2.0)"),
                        ClassifierNode("Eiffel Forum License"),
                        ClassifierNode("European Union Public Licence 1.0 (EUPL 1.0)"),
                        ClassifierNode("European Union Public Licence 1.1 (EUPL 1.1)"),
                        ClassifierNode("European Union Public Licence 1.2 (EUPL 1.2)"),
                        ClassifierNode("GNU Affero General Public License v3"),
                        ClassifierNode(
                            "GNU Affero General Public License v3 or later (AGPLv3+)"
                        ),
                        ClassifierNode("GNU Free Documentation License (FDL)"),
                        ClassifierNode("GNU General Public License (GPL)"),
                        ClassifierNode("GNU General Public License v2 (GPLv2)"),
                        ClassifierNode(
                            "GNU General Public License v2 or later (GPLv2+)"
                        ),
                        ClassifierNode("GNU General Public License v3 (GPLv3)"),
                        ClassifierNode(
                            "GNU General Public License v3 or later (GPLv3+)"
                        ),
                        ClassifierNode("GNU Lesser General Public License v2 (LGPLv2)"),
                        ClassifierNode(
                            "GNU Lesser General Public License v2 or later (LGPLv2+)"
                        ),
                        ClassifierNode("GNU Lesser General Public License v3 (LGPLv3)"),
                        ClassifierNode(
                            "GNU Lesser General Public License v3 or later (LGPLv3+)"
                        ),
                        ClassifierNode(
                            "GNU Library or Lesser General Public License (LGPL)"
                        ),
                        ClassifierNode(
                            "Historical Permission Notice and Disclaimer (HPND)"
                        ),
                        ClassifierNode("IBM Public License"),
                        ClassifierNode("Intel Open Source License"),
                        ClassifierNode("ISC License (ISCL)"),
                        ClassifierNode("Jabber Open Source License"),
                        ClassifierNode("MirOS License (MirOS)"),
                        ClassifierNode("MIT License"),
                        ClassifierNode(
                            "MITRE Collaborative Virtual Workspace License (CVW)"
                        ),
                        ClassifierNode("Motosoto License"),
                        ClassifierNode("Mozilla Public License 1.0 (MPL)"),
                        ClassifierNode("Mozilla Public License 1.1 (MPL 1.1)"),
                        ClassifierNode("Mozilla Public License 2.0 (MPL 2.0)"),
                        ClassifierNode("Nethack General Public License"),
                        ClassifierNode("Nokia Open Source License"),
                        ClassifierNode("Open Group Test Suite License"),
                        ClassifierNode("Open Software License 3.0 (OSL-3.0)"),
                        ClassifierNode("PostgreSQL License"),
                        ClassifierNode("Python License (CNRI Python License)"),
                        ClassifierNode("Python Software Foundation License"),
                        ClassifierNode("Qt Public License (QPL)"),
                        ClassifierNode("Ricoh Source Code Public License"),
                        ClassifierNode("SIL Open Font License 1.1 (OFL-1.1)"),
                        ClassifierNode("Sleepycat License"),
                        ClassifierNode("Sun Industry Standards Source License (SISSL)"),
                        ClassifierNode("Sun Public License"),
                        ClassifierNode("Universal Permissive License (UPL)"),
                        ClassifierNode(
                            "University of Illinois/NCSA Open Source License"
                        ),
                        ClassifierNode("Vovida Software License 1.0"),
                        ClassifierNode("W3C License"),
                        ClassifierNode("X.Net License"),
                        ClassifierNode("zlib/libpng License"),
                        ClassifierNode("Zope Public License"),
                    ],
                ),
                ClassifierNode("Other/Proprietary License"),
                ClassifierNode("Public Domain"),
                ClassifierNode("Repoze Public License"),
            ],
        ),
        ClassifierNode(
            "Natural Language",
            skip=True,
            children=[
                ClassifierNode("Afrikaans"),
                ClassifierNode("Arabic"),
                ClassifierNode("Basque"),
                ClassifierNode("Bengali"),
                ClassifierNode("Bosnian"),
                ClassifierNode("Bulgarian"),
                ClassifierNode("Cantonese"),
                ClassifierNode("Catalan"),
                ClassifierNode("Chinese (Simplified)"),
                ClassifierNode("Chinese (Traditional)"),
                ClassifierNode("Croatian"),
                ClassifierNode("Czech"),
                ClassifierNode("Danish"),
                ClassifierNode("Dutch"),
                ClassifierNode("English"),
                ClassifierNode("Esperanto"),
                ClassifierNode("Finnish"),
                ClassifierNode("French"),
                ClassifierNode("Galician"),
                ClassifierNode("German"),
                ClassifierNode("Greek"),
                ClassifierNode("Hebrew"),
                ClassifierNode("Hindi"),
                ClassifierNode("Hungarian"),
                ClassifierNode("Icelandic"),
                ClassifierNode("Indonesian"),
                ClassifierNode("Irish"),
                ClassifierNode("Italian"),
                ClassifierNode("Japanese"),
                ClassifierNode("Javanese"),
                ClassifierNode("Korean"),
                ClassifierNode("Latin"),
                ClassifierNode("Latvian"),
                ClassifierNode("Lithuanian"),
                ClassifierNode("Macedonian"),
                ClassifierNode("Malay"),
                ClassifierNode("Marathi"),
                ClassifierNode("Nepali"),
                ClassifierNode("Norwegian"),
                ClassifierNode("Panjabi"),
                ClassifierNode("Persian"),
                ClassifierNode("Polish"),
                ClassifierNode("Portuguese"),
                ClassifierNode("Portuguese (Brazilian)"),
                ClassifierNode("Romanian"),
                ClassifierNode("Russian"),
                ClassifierNode("Serbian"),
                ClassifierNode("Slovak"),
                ClassifierNode("Slovenian"),
                ClassifierNode("Spanish"),
                ClassifierNode("Swedish"),
                ClassifierNode("Tamil"),
                ClassifierNode("Telugu"),
                ClassifierNode("Thai"),
                ClassifierNode("Tibetan"),
                ClassifierNode("Turkish"),
                ClassifierNode("Ukrainian"),
                ClassifierNode(
                    "Ukranian",
                    deprecated=True,
                    deprecated_by=["Natural Language :: Ukrainian"],
                ),  # noqa
                ClassifierNode("Urdu"),
                ClassifierNode("Vietnamese"),
            ],
        ),
        ClassifierNode(
            "Operating System",
            skip=True,
            children=[
                ClassifierNode("Android"),
                ClassifierNode("BeOS"),
                ClassifierNode("iOS"),
                ClassifierNode(
                    "MacOS",
                    children=[ClassifierNode("MacOS 9"), ClassifierNode("MacOS X")],
                ),
                ClassifierNode(
                    "Microsoft",
                    children=[
                        ClassifierNode("MS-DOS"),
                        ClassifierNode(
                            "Windows",
                            children=[
                                ClassifierNode("Windows 10"),
                                ClassifierNode("Windows 3.1 or Earlier"),
                                ClassifierNode("Windows 7"),
                                ClassifierNode("Windows 8"),
                                ClassifierNode("Windows 8.1"),
                                ClassifierNode("Windows 95/98/2000"),
                                ClassifierNode("Windows CE"),
                                ClassifierNode("Windows NT/2000"),
                                ClassifierNode("Windows Server 2003"),
                                ClassifierNode("Windows Server 2008"),
                                ClassifierNode("Windows Vista"),
                                ClassifierNode("Windows XP"),
                            ],
                        ),
                    ],
                ),
                ClassifierNode("OS/2"),
                ClassifierNode("OS Independent"),
                ClassifierNode("Other OS"),
                ClassifierNode("PalmOS"),
                ClassifierNode("PDA Systems"),
                ClassifierNode(
                    "POSIX",
                    children=[
                        ClassifierNode("AIX"),
                        ClassifierNode(
                            "BSD",
                            children=[
                                ClassifierNode("BSD/OS"),
                                ClassifierNode("FreeBSD"),
                                ClassifierNode("NetBSD"),
                                ClassifierNode("OpenBSD"),
                            ],
                        ),
                        ClassifierNode("GNU Hurd"),
                        ClassifierNode("HP-UX"),
                        ClassifierNode("IRIX"),
                        ClassifierNode("Linux"),
                        ClassifierNode("Other"),
                        ClassifierNode("SCO"),
                        ClassifierNode("SunOS/Solaris"),
                    ],
                ),
                ClassifierNode("Unix"),
            ],
        ),
        ClassifierNode(
            "Programming Language",
            skip=True,
            children=[
                ClassifierNode("Ada"),
                ClassifierNode("APL"),
                ClassifierNode("ASP"),
                ClassifierNode("Assembly"),
                ClassifierNode("Awk"),
                ClassifierNode("Basic"),
                ClassifierNode("C"),
                ClassifierNode("C#"),
                ClassifierNode("C++"),
                ClassifierNode("Cold Fusion"),
                ClassifierNode("Cython"),
                ClassifierNode("Delphi/Kylix"),
                ClassifierNode("Dylan"),
                ClassifierNode("Eiffel"),
                ClassifierNode("Emacs-Lisp"),
                ClassifierNode("Erlang"),
                ClassifierNode("Euler"),
                ClassifierNode("Euphoria"),
                ClassifierNode("F#"),
                ClassifierNode("Forth"),
                ClassifierNode("Fortran"),
                ClassifierNode("Haskell"),
                ClassifierNode("Java"),
                ClassifierNode("JavaScript"),
                ClassifierNode("Lisp"),
                ClassifierNode("Logo"),
                ClassifierNode("ML"),
                ClassifierNode("Modula"),
                ClassifierNode("Objective C"),
                ClassifierNode("Object Pascal"),
                ClassifierNode("OCaml"),
                ClassifierNode("Other"),
                ClassifierNode("Other Scripting Engines"),
                ClassifierNode("Pascal"),
                ClassifierNode("Perl"),
                ClassifierNode("PHP"),
                ClassifierNode("Pike"),
                ClassifierNode("Pliant"),
                ClassifierNode("PL/SQL"),
                ClassifierNode("PROGRESS"),
                ClassifierNode("Prolog"),
                ClassifierNode(
                    "Python",
                    children=[
                        ClassifierNode(
                            "2", children=[ClassifierNode("Only", children=[])]
                        ),
                        ClassifierNode("2.3"),
                        ClassifierNode("2.4"),
                        ClassifierNode("2.5"),
                        ClassifierNode("2.6"),
                        ClassifierNode("2.7"),
                        ClassifierNode(
                            "3", children=[ClassifierNode("Only", children=[])]
                        ),
                        ClassifierNode("3.0"),
                        ClassifierNode("3.1"),
                        ClassifierNode("3.2"),
                        ClassifierNode("3.3"),
                        ClassifierNode("3.4"),
                        ClassifierNode("3.5"),
                        ClassifierNode("3.6"),
                        ClassifierNode("3.7"),
                        ClassifierNode("3.8"),
                        ClassifierNode("3.9"),
                        ClassifierNode(
                            "Implementation",
                            children=[
                                ClassifierNode("CPython"),
                                ClassifierNode("IronPython"),
                                ClassifierNode("Jython"),
                                ClassifierNode("MicroPython"),
                                ClassifierNode("PyPy"),
                                ClassifierNode("Stackless"),
                            ],
                        ),
                    ],
                ),
                ClassifierNode("R"),
                ClassifierNode("REBOL"),
                ClassifierNode("Rexx"),
                ClassifierNode("Ruby"),
                ClassifierNode("Rust"),
                ClassifierNode("Scheme"),
                ClassifierNode("Simula"),
                ClassifierNode("Smalltalk"),
                ClassifierNode("SQL"),
                ClassifierNode("Tcl"),
                ClassifierNode("Unix Shell"),
                ClassifierNode("Visual Basic"),
                ClassifierNode("XBasic"),
                ClassifierNode("YACC"),
                ClassifierNode("Zope"),
            ],
        ),
        ClassifierNode(
            "Topic",
            skip=True,
            children=[
                ClassifierNode("Adaptive Technologies"),
                ClassifierNode("Artistic Software"),
                ClassifierNode(
                    "Communications",
                    children=[
                        ClassifierNode("BBS"),
                        ClassifierNode(
                            "Chat",
                            children=[
                                ClassifierNode(
                                    "AOL Instant Messenger", deprecated=True
                                ),
                                ClassifierNode("ICQ"),
                                ClassifierNode("Internet Relay Chat"),
                                ClassifierNode("Unix Talk"),
                            ],
                        ),
                        ClassifierNode("Conferencing"),
                        ClassifierNode(
                            "Email",
                            children=[
                                ClassifierNode("Address Book"),
                                ClassifierNode("Email Clients (MUA)"),
                                ClassifierNode("Filters"),
                                ClassifierNode("Mailing List Servers"),
                                ClassifierNode("Mail Transport Agents"),
                                ClassifierNode(
                                    "Post-Office",
                                    children=[
                                        ClassifierNode("IMAP"),
                                        ClassifierNode("POP3"),
                                    ],
                                ),
                            ],
                        ),
                        ClassifierNode("Fax"),
                        ClassifierNode("FIDO"),
                        ClassifierNode(
                            "File Sharing",
                            children=[
                                ClassifierNode("Gnutella"),
                                ClassifierNode("Napster"),
                            ],
                        ),
                        ClassifierNode("Ham Radio"),
                        ClassifierNode("Internet Phone"),
                        ClassifierNode("Telephony"),
                        ClassifierNode("Usenet News"),
                    ],
                ),
                ClassifierNode(
                    "Database",
                    children=[
                        ClassifierNode("Database Engines/Servers"),
                        ClassifierNode("Front-Ends"),
                    ],
                ),
                ClassifierNode(
                    "Desktop Environment",
                    children=[
                        ClassifierNode("File Managers"),
                        ClassifierNode("Gnome"),
                        ClassifierNode("GNUstep"),
                        ClassifierNode(
                            "K Desktop Environment (KDE)",
                            children=[ClassifierNode("Themes")],
                        ),
                        ClassifierNode(
                            "PicoGUI",
                            children=[
                                ClassifierNode("Applications"),
                                ClassifierNode("Themes"),
                            ],
                        ),
                        ClassifierNode("Screen Savers"),
                        ClassifierNode(
                            "Window Managers",
                            children=[
                                ClassifierNode(
                                    "Afterstep", children=[ClassifierNode("Themes")]
                                ),
                                ClassifierNode("Applets"),
                                ClassifierNode(
                                    "Blackbox", children=[ClassifierNode("Themes")]
                                ),
                                ClassifierNode(
                                    "CTWM", children=[ClassifierNode("Themes")]
                                ),
                                ClassifierNode(
                                    "Enlightenment",
                                    children=[
                                        ClassifierNode("Epplets"),
                                        ClassifierNode("Themes DR15"),
                                        ClassifierNode("Themes DR16"),
                                        ClassifierNode("Themes DR17"),
                                    ],
                                ),
                                ClassifierNode(
                                    "Fluxbox", children=[ClassifierNode("Themes")]
                                ),
                                ClassifierNode(
                                    "FVWM", children=[ClassifierNode("Themes")]
                                ),
                                ClassifierNode(
                                    "IceWM", children=[ClassifierNode("Themes")]
                                ),
                                ClassifierNode(
                                    "MetaCity", children=[ClassifierNode("Themes")]
                                ),
                                ClassifierNode(
                                    "Oroborus", children=[ClassifierNode("Themes")]
                                ),
                                ClassifierNode(
                                    "Sawfish",
                                    children=[
                                        ClassifierNode("Themes 0.30"),
                                        ClassifierNode("Themes pre-0.30"),
                                    ],
                                ),
                                ClassifierNode(
                                    "Waimea", children=[ClassifierNode("Themes")]
                                ),
                                ClassifierNode(
                                    "Window Maker",
                                    children=[
                                        ClassifierNode("Applets"),
                                        ClassifierNode("Themes"),
                                    ],
                                ),
                                ClassifierNode(
                                    "XFCE", children=[ClassifierNode("Themes")]
                                ),
                            ],
                        ),
                    ],
                ),
                ClassifierNode("Documentation", children=[ClassifierNode("Sphinx")]),
                ClassifierNode(
                    "Education",
                    children=[
                        ClassifierNode("Computer Aided Instruction (CAI)"),
                        ClassifierNode("Testing"),
                    ],
                ),
                ClassifierNode(
                    "Games/Entertainment",
                    children=[
                        ClassifierNode("Arcade"),
                        ClassifierNode("Board Games"),
                        ClassifierNode("First Person Shooters"),
                        ClassifierNode("Fortune Cookies"),
                        ClassifierNode("Multi-User Dungeons (MUD)"),
                        ClassifierNode("Puzzle Games"),
                        ClassifierNode("Real Time Strategy"),
                        ClassifierNode("Role-Playing"),
                        ClassifierNode("Side-Scrolling/Arcade Games"),
                        ClassifierNode("Simulation"),
                        ClassifierNode("Turn Based Strategy"),
                    ],
                ),
                ClassifierNode("Home Automation"),
                ClassifierNode(
                    "Internet",
                    children=[
                        ClassifierNode("File Transfer Protocol (FTP)"),
                        ClassifierNode("Finger"),
                        ClassifierNode("Log Analysis"),
                        ClassifierNode("Name Service (DNS)"),
                        ClassifierNode("Proxy Servers"),
                        ClassifierNode("WAP"),
                        ClassifierNode(
                            "WWW/HTTP",
                            children=[
                                ClassifierNode("Browsers"),
                                ClassifierNode(
                                    "Dynamic Content",
                                    children=[
                                        ClassifierNode("CGI Tools/Libraries"),
                                        ClassifierNode("Content Management System"),
                                        ClassifierNode("Message Boards"),
                                        ClassifierNode("News/Diary"),
                                        ClassifierNode("Page Counters"),
                                        ClassifierNode("Wiki"),
                                    ],
                                ),
                                ClassifierNode("HTTP Servers"),
                                ClassifierNode("Indexing/Search"),
                                ClassifierNode("Session"),
                                ClassifierNode(
                                    "Site Management",
                                    children=[ClassifierNode("Link Checking")],
                                ),
                                ClassifierNode(
                                    "WSGI",
                                    children=[
                                        ClassifierNode("Application"),
                                        ClassifierNode("Middleware"),
                                        ClassifierNode("Server"),
                                    ],
                                ),
                            ],
                        ),
                        ClassifierNode("XMPP"),
                        ClassifierNode("Z39.50"),
                    ],
                ),
                ClassifierNode(
                    "Multimedia",
                    children=[
                        ClassifierNode(
                            "Graphics",
                            children=[
                                ClassifierNode("3D Modeling"),
                                ClassifierNode("3D Rendering"),
                                ClassifierNode(
                                    "Capture",
                                    children=[
                                        ClassifierNode("Digital Camera"),
                                        ClassifierNode("Scanners"),
                                        ClassifierNode("Screen Capture"),
                                    ],
                                ),
                                ClassifierNode(
                                    "Editors",
                                    children=[
                                        ClassifierNode("Raster-Based"),
                                        ClassifierNode("Vector-Based"),
                                    ],
                                ),
                                ClassifierNode("Graphics Conversion"),
                                ClassifierNode("Presentation"),
                                ClassifierNode("Viewers"),
                            ],
                        ),
                        ClassifierNode(
                            "Sound/Audio",
                            children=[
                                ClassifierNode("Analysis"),
                                ClassifierNode("Capture/Recording"),
                                ClassifierNode(
                                    "CD Audio",
                                    children=[
                                        ClassifierNode("CD Playing"),
                                        ClassifierNode("CD Ripping"),
                                        ClassifierNode("CD Writing"),
                                    ],
                                ),
                                ClassifierNode("Conversion"),
                                ClassifierNode("Editors"),
                                ClassifierNode("MIDI"),
                                ClassifierNode("Mixers"),
                                ClassifierNode(
                                    "Players", children=[ClassifierNode("MP3")]
                                ),
                                ClassifierNode("Sound Synthesis"),
                                ClassifierNode("Speech"),
                            ],
                        ),
                        ClassifierNode(
                            "Video",
                            children=[
                                ClassifierNode("Capture"),
                                ClassifierNode("Conversion"),
                                ClassifierNode("Display"),
                                ClassifierNode("Non-Linear Editor"),
                            ],
                        ),
                    ],
                ),
                ClassifierNode(
                    "Office/Business",
                    children=[
                        ClassifierNode(
                            "Financial",
                            children=[
                                ClassifierNode("Accounting"),
                                ClassifierNode("Investment"),
                                ClassifierNode("Point-Of-Sale"),
                                ClassifierNode("Spreadsheet"),
                            ],
                        ),
                        ClassifierNode("Groupware"),
                        ClassifierNode("News/Diary"),
                        ClassifierNode("Office Suites"),
                        ClassifierNode("Scheduling"),
                    ],
                ),
                ClassifierNode("Other/Nonlisted Topic"),
                ClassifierNode("Printing"),
                ClassifierNode("Religion"),
                ClassifierNode(
                    "Scientific/Engineering",
                    children=[
                        ClassifierNode("Artificial Intelligence"),
                        ClassifierNode("Artificial Life"),
                        ClassifierNode("Astronomy"),
                        ClassifierNode("Atmospheric Science"),
                        ClassifierNode("Bio-Informatics"),
                        ClassifierNode("Chemistry"),
                        ClassifierNode("Electronic Design Automation (EDA)"),
                        ClassifierNode("GIS"),
                        ClassifierNode("Human Machine Interfaces"),
                        ClassifierNode("Hydrology"),
                        ClassifierNode("Image Recognition"),
                        ClassifierNode("Information Analysis"),
                        ClassifierNode("Interface Engine/Protocol Translator"),
                        ClassifierNode("Mathematics"),
                        ClassifierNode("Medical Science Apps."),
                        ClassifierNode("Physics"),
                        ClassifierNode("Visualization"),
                    ],
                ),
                ClassifierNode("Security", children=[ClassifierNode("Cryptography")]),
                ClassifierNode(
                    "Sociology",
                    children=[ClassifierNode("Genealogy"), ClassifierNode("History")],
                ),
                ClassifierNode(
                    "Software Development",
                    children=[
                        ClassifierNode("Assemblers"),
                        ClassifierNode("Bug Tracking"),
                        ClassifierNode("Build Tools"),
                        ClassifierNode("Code Generators"),
                        ClassifierNode("Compilers"),
                        ClassifierNode("Debuggers"),
                        ClassifierNode("Disassemblers"),
                        ClassifierNode("Documentation"),
                        ClassifierNode("Embedded Systems"),
                        ClassifierNode("Internationalization"),
                        ClassifierNode("Interpreters"),
                        ClassifierNode(
                            "Libraries",
                            children=[
                                ClassifierNode("Application Frameworks"),
                                ClassifierNode("Java Libraries"),
                                ClassifierNode("Perl Modules"),
                                ClassifierNode("PHP Classes"),
                                ClassifierNode("Pike Modules"),
                                ClassifierNode("pygame"),
                                ClassifierNode("Python Modules"),
                                ClassifierNode("Ruby Modules"),
                                ClassifierNode("Tcl Extensions"),
                            ],
                        ),
                        ClassifierNode("Localization"),
                        ClassifierNode(
                            "Object Brokering", children=[ClassifierNode("CORBA")]
                        ),
                        ClassifierNode("Pre-processors"),
                        ClassifierNode("Quality Assurance"),
                        ClassifierNode(
                            "Testing",
                            children=[
                                ClassifierNode("Acceptance"),
                                ClassifierNode("BDD"),
                                ClassifierNode("Mocking"),
                                ClassifierNode("Traffic Generation"),
                                ClassifierNode("Unit"),
                            ],
                        ),
                        ClassifierNode("User Interfaces"),
                        ClassifierNode(
                            "Version Control",
                            children=[
                                ClassifierNode("Bazaar"),
                                ClassifierNode("CVS"),
                                ClassifierNode("Git"),
                                ClassifierNode("Mercurial"),
                                ClassifierNode("RCS"),
                                ClassifierNode("SCCS"),
                            ],
                        ),
                        ClassifierNode("Widget Sets"),
                    ],
                ),
                ClassifierNode(
                    "System",
                    children=[
                        ClassifierNode(
                            "Archiving",
                            children=[
                                ClassifierNode("Backup"),
                                ClassifierNode("Compression"),
                                ClassifierNode("Mirroring"),
                                ClassifierNode("Packaging"),
                            ],
                        ),
                        ClassifierNode("Benchmark"),
                        ClassifierNode("Boot", children=[ClassifierNode("Init")]),
                        ClassifierNode("Clustering"),
                        ClassifierNode("Console Fonts"),
                        ClassifierNode("Distributed Computing"),
                        ClassifierNode("Emulators"),
                        ClassifierNode("Filesystems"),
                        ClassifierNode(
                            "Hardware",
                            children=[
                                ClassifierNode("Hardware Drivers"),
                                ClassifierNode("Mainframes"),
                                ClassifierNode("Symmetric Multi-processing"),
                            ],
                        ),
                        ClassifierNode("Installation/Setup"),
                        ClassifierNode("Logging"),
                        ClassifierNode("Monitoring"),
                        ClassifierNode(
                            "Networking",
                            children=[
                                ClassifierNode("Firewalls"),
                                ClassifierNode(
                                    "Monitoring",
                                    children=[ClassifierNode("Hardware Watchdog")],
                                ),
                                ClassifierNode("Time Synchronization"),
                            ],
                        ),
                        ClassifierNode("Operating System"),
                        ClassifierNode(
                            "Operating System Kernels",
                            children=[
                                ClassifierNode("BSD"),
                                ClassifierNode("GNU Hurd"),
                                ClassifierNode("Linux"),
                            ],
                        ),
                        ClassifierNode("Power (UPS)"),
                        ClassifierNode("Recovery Tools"),
                        ClassifierNode("Shells"),
                        ClassifierNode("Software Distribution"),
                        ClassifierNode(
                            "Systems Administration",
                            children=[
                                ClassifierNode(
                                    "Authentication/Directory",
                                    children=[
                                        ClassifierNode("LDAP"),
                                        ClassifierNode("NIS"),
                                    ],
                                )
                            ],
                        ),
                        ClassifierNode("System Shells"),
                    ],
                ),
                ClassifierNode(
                    "Terminals",
                    children=[
                        ClassifierNode("Serial"),
                        ClassifierNode("Telnet"),
                        ClassifierNode("Terminal Emulators/X Terminals"),
                    ],
                ),
                ClassifierNode(
                    "Text Editors",
                    children=[
                        ClassifierNode("Documentation"),
                        ClassifierNode("Emacs"),
                        ClassifierNode("Integrated Development Environments (IDE)"),
                        ClassifierNode("Text Processing"),
                        ClassifierNode("Word Processors"),
                    ],
                ),
                ClassifierNode(
                    "Text Processing",
                    children=[
                        ClassifierNode("Filters"),
                        ClassifierNode("Fonts"),
                        ClassifierNode("General"),
                        ClassifierNode("Indexing"),
                        ClassifierNode("Linguistic"),
                        ClassifierNode(
                            "Markup",
                            children=[
                                ClassifierNode("HTML"),
                                ClassifierNode("LaTeX"),
                                ClassifierNode("SGML"),
                                ClassifierNode("VRML"),
                                ClassifierNode("XML"),
                            ],
                        ),
                    ],
                ),
                ClassifierNode("Utilities"),
            ],
        ),
        ClassifierNode("Typing", skip=True, children=[ClassifierNode("Typed")]),
    ]
)
