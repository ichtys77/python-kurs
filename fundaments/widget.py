class Widget:
  def __init__(self, label):
      self.label = label

class Button(Widget):
  def __init__(self, label, size):
      super().__init__(label)
      self.size = size

  def handle_click(self):
    return('click, click')

button = Button('my button', 'large')
print(button.label, button.size)
print(button.handle_click())