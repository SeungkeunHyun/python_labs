from py_thesaurus import Thesaurus
input_word = "hatred"
new_instance = Thesaurus(input_word)
print(new_instance)
print(new_instance.get_synonym())
print(new_instance.get_synonym(pos='verb'))
print(new_instance.get_synonym(pos='adj'))
print(new_instance.get_definition())
print(new_instance.get_antonym())
