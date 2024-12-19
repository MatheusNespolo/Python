#Titulo

def title(F):
  """Converte uma string para o formato de título.

  Args:
    text: A string a ser convertida.

  Returns:
    A string convertida para o formato de título.
  """
  return F.title()

F = str(input())
titled_text = title(F)
print(titled_text)
