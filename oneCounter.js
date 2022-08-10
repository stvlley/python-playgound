array = [[0, 1, 1, 1, 0], [0, 1, 0, 1, 0, 1], [1, 0]]

const oneCounter = (array) => {
    let count = 0

    array.forEach(element => {
        element.forEach(node => {
            if(node === 1){
                count ++
            }
        })
    });
    return count
}

console.log(oneCounter(array))