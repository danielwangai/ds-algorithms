var Stack = function () {
	/**
	* store stack items into as string data structure.
	*/
	this.storage = "";
}

/**
* Add item to stack
*/
Stack.prototype.push = function (val) {
	if (val.length) {
		if (this.storage.length === 0) {
			return this.storage = val;
		}
		// concatenate to existing stack
		this.storage = this.storage.concat("-" + val);
		return this.storage;
	}
	return "Cannot push an empty value to stack";
}

/**
	* remove item from stack
	* latest item added(concatenated) - removed FIRST
*/
Stack.prototype.pop = function () {
	if (this.storage.length) {
		// remove last item if storage is not empty
		let stackElements = this.storage.split("-");
		stackElements.pop();
		this.storage = stackElements.join("-")
		return this.storage;
	}
	return "Cannot pop from an empty stack.";
}

/**
* Get the total number of items in the stack
*/
Stack.prototype.size = function () {
	let stackElements = this.storage.split("-");
	if (stackElements.length == 1) {
		return stackElements[0].length == 0 ? 0 : 1
	}
	return stackElements.length;
}

/**
* Get the first element in the stack
*/
Stack.prototype.head = function () {
	let stackSize = this.size();
	let stackElements = this.storage.split("-");
	if(stackSize == 0) {
		return "The stack is empty.";
	}
	if(stackSize >= 1) {
		return stackElements[0]
	}
}
/**
* Get the last element in the stack
*/
Stack.prototype.tail = function () {
	let stackSize = this.size();
	let stackElements = this.storage.split("-");
	if(stackSize == 0) {
		return "The stack is empty.";
	}
	if(stackSize >= 1) {
		return stackElements[stackElements.length - 1]
	}
}

module.exports = Stack
