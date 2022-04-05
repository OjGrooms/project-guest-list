from threading import Timer

class ButtonTimeout():
  def __init__(self, time, callbackFunction):
    self.time = time
    self.callbackFunction = callbackFunction
    self.thread = Timer(self.time, self.handle_function)

  def handle_function(self):
    self.callbackFunction()

  def start(self):
    self.thread = Timer(self.time, self.handle_function)
    self.thread.start()

  def cancel(self):
    self.thread.cancel()
