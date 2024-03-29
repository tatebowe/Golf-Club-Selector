## holes will be nodes, values will be par, yardage,  maybe hazards

class Node:
  def __init__(self, name, next_node=None, prev_node=None):
    self.name = name
    self.par = None
    self.yard = None
    self.next_node = next_node
    self.prev_node = prev_node
    
  def set_next_node(self, next_node):
    self.next_node = next_node
    
  def get_next_node(self):
    return self.next_node

  def set_prev_node(self, prev_node):
    self.prev_node = prev_node
    
  def get_prev_node(self):
    return self.prev_node
  
  def get_par(self, value):
    return self.par == value

  def get_yards(self, value):
    return self.yard == value


class DoublyLinkedList:
  def __init__(self, name, num_holes):
    self.name = name
    self.num_holes = num_holes
    self.head_node = None
    self.tail_node = None
  
  def add_to_head(self, new_value):
    new_head = Node(new_value)
    current_head = self.head_node

    if current_head != None:
      current_head.set_prev_node(new_head)
      new_head.set_next_node(current_head)

    self.head_node = new_head

    if self.tail_node == None:
      self.tail_node = new_head

  def add_to_tail(self, new_value):
    new_tail = Node(new_value)
    current_tail = self.tail_node

    if current_tail != None:
      current_tail.set_next_node(new_tail)
      new_tail.set_prev_node(current_tail)

    self.tail_node = new_tail

    if self.head_node == None:
      self.head_node = new_tail

  def remove_head(self):
    removed_head = self.head_node

    if removed_head == None:
      return None

    self.head_node = removed_head.get_next_node()

    if self.head_node != None:
      self.head_node.set_prev_node(None)

    if removed_head == self.tail_node:
      self.remove_tail()

    return removed_head.get_value()

  def remove_tail(self):
    removed_tail = self.tail_node

    if removed_tail == None:
      return None

    self.tail_node = removed_tail.get_prev_node()

    if self.tail_node != None:
      self.tail_node.set_next_node(None)

    if removed_tail == self.head_node:
      self.remove_head()

    return removed_tail.get_value()

  def remove_by_value(self, value_to_remove):
    node_to_remove = None
    current_node = self.head_node

    while current_node != None:
      if current_node.get_value() == value_to_remove:
        node_to_remove = current_node
        break

      current_node = current_node.get_next_node()

    if node_to_remove == None:
      return None

    if node_to_remove == self.head_node:
      self.remove_head()
    elif node_to_remove == self.tail_node:
      self.remove_tail()
    else:
      next_node = node_to_remove.get_next_node()
      prev_node = node_to_remove.get_prev_node()
      next_node.set_prev_node(prev_node)
      prev_node.set_next_node(next_node)

    return node_to_remove
  

class Course(DoublyLinkedList):
  def __init__(self, name = None, holes = None):
    self.name = name
    self.holes = holes
    self.course = None


  def get_course_info(self):
    self.name = input('Which course are you playing? ')
    try:
      self.holes = int(input('How many holes are there? '))
    except ValueError:
      print('Please enter a valid number')
  
    self.course = DoublyLinkedList(self.name, self.holes)
    return self.course
  
  def fill_course(self):

    self.course.add_to_head('Hole 1')

    for i in range(2, self.holes):
      self.course.add_to_head(f'Hole {i}'.format(i))

    return self.course
test_course = Course()
test_course.get_course_info()
test_course.fill_course()
