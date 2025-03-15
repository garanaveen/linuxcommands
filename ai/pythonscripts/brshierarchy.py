"""
In brightscript programming, for every component there is xml file and its corresponding brs file.

If there is a brs file without xml file, that means its not a component on its own and needs to be included in another xml file.

The syntax for including a brs file in it's xml file is as follows (CustomComponent is the name of the component).

CustomComponent.xml:
    <script type="text/brightscript" uri="CustomComponent.brs" />
    <script type="text/brightscript" uri="Utils.brs" />

Here CustomComponent.brs is the brs exclusively for CustomComponent and it won't be included in any other xml files.

However, Utils.brs could be more of a general utility and might be included in other xml files.

I want you to write a python script which walks all the directories from the directory it is executed from and finds all the xml files and creates a tree diagram as follows,

CustomComponent.xml
  |
  ____ CustomComponent.brs
  ____ Utils.brs

This isn't an exact format to follow but more of an idea. Use the best possible graphs that is suited for this usecase.
"""
