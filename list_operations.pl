% 1. myFirst:

myFirst([Head|_], Head).
 
 
% 2. myLast:

myLast([Head], Head).
myLast([_|Tail], Result):-
	myLast(Tail, Result).


% 3. myInit

myInit([_], []).
myInit([Head|Tail], [Head|Rest]):-
	myInit(Tail, Rest).

% 4. myAppend:

myAppend([], List, List).
myAppend([L1H|L1T], L2, [L1H|Result]):-
	myAppend(L1T, L2, Result).


% 5. myLength:

myLength([], 0).
myLength([Head|Tail], Length):-
	myLength(Tail, NewLength),
	Length is 1 + NewLength.


% 6. myFlatten: 

myFlatten([], []).
myFlatten([Head|Tail], Result):-
	Head = [];
	Head = [_|_],
	myFlatten(Head, HR),
	myFlatten(Tail, TR),
	myAppend(HR, TR, Result).
myFlatten([Head|Tail], [Head|TailR]):-
	Head \= [],
	Head \= [_|_],
	myFlatten(Tail, TailR).

	
% 7. insertPosition

insertPosition(List, Element, 0, [Element|List]).
insertPosition([Head|Tail], Element, Index, [Head|NewResult]):-
	NewIndex is Index - 1,
	insertPosition(Tail, Element, NewIndex, NewResult).


% 8. insertSorted

insertSorted([], Element, [Element]).
insertSorted([Head|Tail], Element, Result):-
	Element < Head,
	myAppend([Element], [Head | Tail], Result).
insertSorted([Head|Tail], Element, Result):-
	insertSorted(Tail, Element, Rest),
	myAppend([Head], Rest, Result).
	

% 9. insertionSort:

insertionSort([], []).
insertionSort([Head|Tail], Result):-
	insertionSort(Tail, R1),
	insertSorted(R1, Head, Result).






