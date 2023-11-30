class Solution(object):
    def interpret(self, command):
        """
        :type command: str
        :rtype: str
        """
        x= "()"
        y="(al)"
        for x in command:
            command=command.replace("()","o")
        for y in command:
            command=command.replace("(al)","al")
        return command

        