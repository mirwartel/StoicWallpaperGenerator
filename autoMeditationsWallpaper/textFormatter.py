class TextFormatter:
    inputString = ''
    length = 0
    maxLength = 0
    maxHeight = 0
    x_start_coordinate = 0
    fontSizeMax = 0
    fontSizeMin = 0
    formatted_lines = []
    total_line_height = 0

    def __init__(self, text, length, maxLenght, max_height, x, fMax, fMin):
        self.inputString = text
        self.length = length
        self.maxLength = maxLenght
        self.maxHeight = max_height
        self.x_start_coordinate = x
        self.fontSizeMax = fMax
        self.fontSizeMin = fMin

    def format_input_string(self):
        length = self.length
        self.total_line_height = 0
        self.formatted_lines = []
        leftover_line = ''
        for line in self.inputString:
            if self.total_line_height > 610 and (length + self.fontSizeMax / 2) < self.maxLength:

                length += self.fontSizeMax / 2
            else:
                length -= self.fontSizeMax / 2

            new_line = ''

            words = line.split()

            for word in words:

                if (len(new_line) * (self.fontSizeMax / 2)) + ((len(word) * (self.fontSizeMax / 2))) >= length:
                    self.formatted_lines.append(new_line)
                    self.total_line_height += (self.fontSizeMax)
                    new_line = ''
                    leftover_line += word + " "

                elif (len(leftover_line) * (self.fontSizeMax / 2)) + ((len(word) * (self.fontSizeMax / 2))) < length:
                    leftover_line += " " + word

                elif (len(leftover_line) * (self.fontSizeMax / 2)) + ((len(word) * (self.fontSizeMax / 2))) > length:
                    new_line += leftover_line
                    self.formatted_lines.append(new_line)
                    self.total_line_height += (self.fontSizeMax)
                    new_line = ''
                    leftover_line = word
            # total_line_height += font_size/2

        if len(leftover_line) > 0:
            self.formatted_lines.append(leftover_line)
            self.total_line_height += (self.fontSizeMax)
            leftover_line = ""

        if self.total_line_height > self.maxHeight:
            try:

                if self.fontSizeMax == self.fontSizeMin and length < self.maxLength:

                    print("Text to long! Reformatting with longer lines")

                    length += self.fontSizeMax * 4

                    self.format_input_string()

                elif self.fontSizeMax > self.fontSizeMin:
                    print("Text to long! Reformatting with smaller font")
                    self.fontSizeMax -= 2
                    if self.fontSizeMax < self.fontSizeMin:
                        self.fontSizeMax = self.fontSizeMin
                    self.format_input_string()
            except RecursionError:
                print("Formatting failed: RecursionError")
                print(self.fontSizeMax)
                print(self.fontSizeMin)
                print(self.length)
                print(self.maxLength)

    def get_formatted_lines(self):
        return self.formatted_lines

    # def stringBreaker(font_size, x, y, input_text):
    #     length = (1920 - x) / (font_size / 2)
    #     formatted_lines = []
    #     leftover_line = ''
    #     total_line_height = y
    #
    #     for line in input_text:
    #         if total_line_height > 610:
    #
    #             length += 1
    #         else:
    #             length -= 1
    #
    #         new_line = ''
    #
    #         words = line.split()
    #
    #         for word in words:
    #
    #             if len(new_line) + len(word) >= length:
    #                 formatted_lines.append(new_line)
    #                 total_line_height += font_size
    #                 new_line = ''
    #                 leftover_line += word + " "
    #
    #             elif len(leftover_line) + len(word) < length:
    #                 leftover_line += " " + word
    #
    #             elif len(leftover_line) + len(word) > length:
    #                 new_line += leftover_line
    #                 formatted_lines.append(new_line)
    #                 total_line_height += font_size
    #                 new_line = ''
    #                 leftover_line = word
    #         # total_line_height += font_size/2
    #
    #     if len(leftover_line) > 0:
    #         formatted_lines.append(leftover_line)
    #         total_line_height += font_size
    #         leftover_line = ""
    #
    #     if total_line_height > 990:
    #         if length < 190 and font_size == 20:
    #             print(length)
    #             print("Text to long! Reformatting with longer lines")
    #
    #             return stringBreaker(font_size, x * 0.9, y, input_text)
    #
    #         print("Text to long! Reformatting with smaller font")
    #         return stringBreaker(20, x, y, input_text)
    #
    #     return formatted_lines