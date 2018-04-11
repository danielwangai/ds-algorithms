const chai = require('chai')
const Stack = require('../ds/stack')
var assert = chai.assert

var stackFixture = new Stack()
stackFixture.storage = "one-two-three-four";

describe('Stack', function () {
	beforeEach(function() {
		stackFixture.storage = "one-two-three-four";
	})
	
	it('should reject pushing empty values to stack', function () {
		var stack = new Stack()
		assert.equal(stack.push(''), 'Cannot push an empty value to stack')
		assert.equal(stack.size(), 0)
	})

	it('should return size 1 if one element is pushed to empty stack', function () {
		var stack = new Stack()
		stack.push('test')
		assert.equal(stack.size(), 1)

	})

	it('should append more elements to the stack', function () {
		stackFixture.push('five')
		stackFixture.push('six')
		assert.equal(stackFixture.size(), 6)
	})

	it('should pop elements from the stack', function () {
		stackFixture.pop()
		assert.equal(stackFixture.size(), 3)
	})

	it('should reject pop elements from empty stack', function () {
		var stack = new Stack();
		assert.equal(stack.pop(), 'Cannot pop from an empty stack.')
	})

	it('should get head element from stack', function () {
		chai.expect(stackFixture.head()).to.equals('one')
		// empty stack
		var stack = new Stack()
		chai.expect(stack.head()).to.equals('The stack is empty.')
	})

	it('should get tail element from stack', function () {
		chai.expect(stackFixture.tail()).to.equals('four')
		// empty stack
		var stack = new Stack()
		chai.expect(stack.tail()).to.equals('The stack is empty.')
	})
	
})
