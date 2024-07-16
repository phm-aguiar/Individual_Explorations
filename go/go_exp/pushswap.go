package main


type LikedList struct {
	value int
	next *LikedList
}

func newLikedList(value int) *LikedList {
	return &LikedList{value: value}
}

func (l *LikedList) push(value int) {
	if l.value == 0 {
		l.value = value
		return
	}
	for l.next != nil {
		l = l.next
	}
	l.next = &LikedList{value: value}
}

func (l *LikedList) pop() int {
	if l.next == nil {
		return l.value
	}
	for l.next.next != nil {
		l = l.next
	}
	value := l.next.value
	l.next = nil
	return value
}


func (l *LikedList) print() {
	for l != nil {
		println(l.value)
		l = l.next
	}
}

func (l *LikedList) rotate() {
	if l.next == nil {
		return
	}
	aux := l.value
	for l.next != nil {
		l.value = l.next.value
		l = l.next
	}
	l.value = aux
}

func (l *LikedList) swap() {
	if l.next == nil {
		return
	}
	aux := l.value
	l.value = l.next.value
	l.next.value = aux
}

func (l *LikedList) reverse() {
	if l.next == nil {
		return
	}
	aux := l.value
	for l.next != nil {
		l.value = l.next.value
		l = l.next
	}
	l.value = aux
}

func (l *LikedList) pushtolinkedlist(l2 *LikedList) {
	for l.next != nil {
		l = l.next
	}
	l.next = l2
}

func (l *LikedList) pushfromlinkedlist(l2 *LikedList) {
	for l2 != nil {
		l2 = l2.next
	}
	l.push(l2.value)
}