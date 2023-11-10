
# if having trouble visualizing how it works, use this link:
# https://pythontutor.com/render.html#code=numbers%20%3D%20%5B6,%202,%205,%206,%202,%207,%201,%209,%201,%207,%206,%204,%202,%206%5D%0A%0Amost_common_number%20%3D%200%0Amost_common_number_counter%20%3D%200%0A%0A%23%20if%20number%20has%20already%20been%20counted,%20skip%20it%0Achecked_numbers%20%3D%20%5B%5D%0A%0Afor%20number%20in%20numbers%3A%0A%20%20%20%20%23%20if%20number%20has%20not%20been%20counted,%20run%20this%0A%20%20%20%20if%20number%20not%20in%20checked_numbers%3A%0A%0A%20%20%20%20%20%20%20%20%23%20counting%20how%20many%20times%20the%20number%20appears%20in%20the%20list%0A%20%20%20%20%20%20%20%20repetition%20%3D%200%0A%20%20%20%20%20%20%20%20for%20count%20in%20numbers%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20if%20number%20%3D%3D%20count%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20repetition%20%2B%3D%201%0A%0A%20%20%20%20%20%20%20%20%23%20updating%20most%20common%20number%20and%20how%20many%20times%20it%20appears%0A%20%20%20%20%20%20%20%20if%20repetition%20%3E%20most_common_number_counter%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20most_common_number_counter%20%3D%20repetition%0A%20%20%20%20%20%20%20%20%20%20%20%20most_common_number%20%3D%20number%0A%0A%20%20%20%20%20%20%20%20checked_numbers.append%28number%29%0A%0Aprint%28f%22most_common_number%3A%20%7Bmost_common_number%7D%22%29%0Aprint%28f%22repeats%20%7Bmost_common_number_counter%7D%20times%22%29&cumulative=false&curInstr=0&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=311&rawInputLstJSON=%5B%5D&textReferences=false

numbers = [6, 2, 5, 6, 2, 7, 1, 9, 1, 7, 6, 4, 2, 6]

most_common_number = 0
most_common_number_counter = 0

# if number has already been counted, skip it
checked_numbers = []

for number in numbers:
    # if number has not been counted, run this
    if number not in checked_numbers:

        # counting how many times the number appears in the list
        repetition = 0
        for count in numbers:
            if number == count:
                repetition += 1

        # updating most common number and how many times it appears
        if repetition > most_common_number_counter:
            most_common_number_counter = repetition
            most_common_number = number

        checked_numbers.append(number)

print(f"Most common number: {most_common_number}")
print(f"Occurs {most_common_number_counter} times")
