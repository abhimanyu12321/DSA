/**
 * @param {integer} init
 * @return { increment: Function, decrement: Function, reset: Function }
 */
var createCounter = function(init) {
    let trackIncrementValue = init
    
        return {
        increment:()=> {
            trackIncrementValue+=1
            return trackIncrementValue
            },
        decrement:()=> {
            trackIncrementValue-=1
            return trackIncrementValue
            },
        reset:()=> {
            trackIncrementValue = init
            return trackIncrementValue
            }
    }
};

/**
 * const counter = createCounter(5)
 * counter.increment(); // 6
 * counter.reset(); // 5
 * counter.decrement(); // 4
 */