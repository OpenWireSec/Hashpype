HashPype
======

HashPype is a script that utilizes Core Security Labs Impacket module and psexec script to perform large scale pass the hash attacks.

A single target or an entire subnet can be scanned using either a username/password or username/hash combination. Alternatively an input file can be included with a list of username/password and username/hash combinations, they can be mixed in any order but must be limited to one set per line.

HashPype is multithreaded, the number of threads spawned will determine the number of hosts concurrently tested.

exit the program at any time during execution by typing exit and hitting enter, it may take several moments to close the threads.
