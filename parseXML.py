from xml.etree.ElementTree import XMLParser


class MaxDepth:  # The target object of the parser
    maxDepth = 0
    depth = 0

    def start(self, tag, attrib):  # Called for each opening tag.
        self.depth += 1
        #print(attrib)
        if attrib == {'color': 'red'}:
            color[0] += self.depth
        if attrib == {'color': 'green'}:
            color[1] += self.depth
        if attrib == {'color': 'blue'}:
            color[2] += self.depth
        if self.depth > self.maxDepth:
            self.maxDepth = self.depth

    def end(self, tag):  # Called for each closing tag.
        self.depth -= 1

    def data(self, data):
        pass  # We do not need to do anything with data.

    def close(self):  # Called when all data has been parsed.
        return self.maxDepth

color = [0, 0, 0]
target = MaxDepth()
parser = XMLParser(target=target)
exampleXml = input()
parser.feed(exampleXml)
parser.close()
print(*color)


