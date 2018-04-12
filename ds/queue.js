/**
 * 
 * @param capacity - max number of elements in the queue
 */
function Queue(capacity) {
	// determine queue store structure
	this.capacity = capacity || Infinity;
	this.storage = {}
	this.head = 0
	this.tail = 0
	this.count = 0
}

/**
 * operation carried out after dequeueing
 * RULES
 *  - head = 1
 * 	- tail = this.count
*/
Queue.prototype.reorderElements = function () {
	if (this.count == 0) {
		return this.count
	}
	Object.keys(this.storage).map((element) => {
		let value = this.storage[element]
		this.storage[element - 1] = value
		delete this.storage[element]
	})
	return this.storage
}

/**
 * Adds an element to the back of the queue
 * @param value - element to be added to the queue
 * reject attempts to add to a full queue
*/
Queue.prototype.enqueue = function (value) {
	if (this.count == this.capacity) {
		return "Queue already full. Could not enqueue."
	}
	if (value == undefined) {
		return "Add a valid element to the queue."
	}
	if (typeof value == "string") {
		if (!value.length) {
			return "String elements must not be empty."
		}
	}
	if (this.count == 0) {
		this.tail = 1
	}
	this.storage[++this.count] = value
	this.tail = this.count + 1
	return this.count
};
// Time complexity:

/**
 * Remove from queue
*/
Queue.prototype.dequeue = function () {
	if (this.count == 0) {
		return "Queue is already empty. Cannot delete from empty queue."
	}
	delete this.storage[1]
	--this.count
	this.reorderElements()
	return this.count
};
// Time complexity:

Queue.prototype.peek = function () {
	// implement me...
};

Queue.prototype.count = function () {
	// implement me...
	return Object.keys(this.storage).length
};

Queue.prototype.contains = function (value) {
	return (value == undefined || value == null) ?
		"Input the value to search. =="
		:
		(typeof value == "string" && value.length == 0) ?
			"Input the value to search."
			:
			Object.values(this.storage).filter((i) => (i == value)).length > 0
}

module.exports = Queue
