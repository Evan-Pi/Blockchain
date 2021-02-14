from django.shortcuts import render, redirect
import hashlib

def hash_functions(request):

    algorithms = [i for i in hashlib.algorithms_available if i not in ['shake_128','shake_256']]
    message = ""
    algorithm = "sha256"

    h = hashlib.new(algorithm)
    h.update(bytes(message,'utf-8'))

    # hexadecimal
    hash_value = h.hexdigest()

    # decimal
    hex_as_int = int(hash_value, 16)

    # binary
    end_length = len(hash_value) * 4
    hex_as_binary = bin(hex_as_int)[2:].zfill(end_length)


    context = {'algorithms':algorithms,'hash_value':hash_value,'hex_as_int':hex_as_int,'hex_as_binary':hex_as_binary,'message':message}
    return render(request, 'basic_concepts/hash_functions.html', context)


def ajax_hash_functions(request):

    algorithms = [i for i in hashlib.algorithms_available if i not in ['shake_128','shake_256']]

    if request.method == 'POST':
        message = request.POST['message']

        algorithm = request.POST['algorithm']
        h = hashlib.new(algorithm)
        h.update(bytes(message,'utf-8'))

        # hexadecimal
        hash_value = h.hexdigest()

        # decimal
        hex_as_int = int(hash_value, 16)

        # binary
        end_length = len(hash_value) * 4
        hex_as_binary = bin(hex_as_int)[2:].zfill(end_length)

    context = {'algorithms':algorithms,'hash_value':hash_value,'hex_as_int':hex_as_int,'hex_as_binary':hex_as_binary,'message':message}
    return render(request, 'basic_concepts/ajax_hash_functions.html', context)