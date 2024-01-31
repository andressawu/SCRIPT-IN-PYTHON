reverse_list([],[]).
reverse_list([Head|Tail], Reversed):-
     reverse_list(Tail, TailReversed), %reverse the tail of the list
     append(TailReversed, [Head], Reversed). %append the reverse tail and the head to get the reverse list

print_list([]). %this part of the code I used chatgpt to exclude the brackets
print_list([Head|Tail]) :-
    write(Head), write(' '), print_list(Tail).

main :-
     read(InputList), %read input 
     reverse_list(InputList, Reversed), %call reverse_list
     print_list(Reversed).
     



