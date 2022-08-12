let string = "minimum"


const nonDuplicates = (string) => {

    let hashTable = {};

    for (let i = 0; i < string.length; i ++) {
        if (hashTable[string[i]]) {
            hashTable[string[i]] ++ ;
        } else {
            hashTable[string[i]] = 1;
        }
        for (let j = 0; j < string.length; j ++ ) {
            hashTable.searchFuncton('1')
        }
    }
}

console.log(nonDuplicates(string))