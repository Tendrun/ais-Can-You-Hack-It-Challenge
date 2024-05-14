let immovablePosition = new Array();
solve();
function solve() {
    Tiles = Tiles_getGameBoard()
    immovablePosition = createimmovablePositionTable(Tiles);
    setNumbersInRightOrder(Tiles)
}

function createimmovablePositionTable(Tiles){
    let array = new Array(Tiles.length).fill(false).map(() => new Array(Tiles[0].length).fill(false));
    return array;
}

function setNumbersInRightOrder(array = [[]]) {
    let number = findSmallestNumber(array);
    console.log(number);
    //reachPositon();
}



function findSmallestNumber(array = [[]]){
    let smallestNumber = array[0][0];
    for(let i = 0; i < array[0].length; i++){
        for(let j = 0; j < array.length; j++) {
            if(immovablePosition[i][j] == true) continue;

            if(array[i][j] < smallestNumber){
                smallestNumber = array[i][j];
            }
        }
    }
    return smallestNumber;
}

function findDestinationPosition(){
    for(let i = 0; i < immovablePosition[0].length; i++){
        for(let j = 0; j < immovablePosition.length; j++){
            if(immovablePosition[i][j] == false){
                return [i,j]
            }
        }
    }
}

function findCurrentPosition(array = [[]]){
    for(let i = 0; i < array.length[0]; i++){
        for(let j = 0; j < array.length; j++){
            if(array[i][j] == 'X'){
                return [i,j]
            }
        }
    }
}

function reachPositon(currentPosition = [0,0], destinationPosition = [0,0]){

    while(true){
        let currentPositionX = currentPosition[0];
        let currentPositionY = currentPosition[1];
        let destinationPositionX = destinationPosition[0];
        let destinationPositionY = destinationPosition[1];

        if(currentPositionX < destinationPositionX){
            moveDirection('R')
        }
        else if(currentPositionX > destinationPositionX){
            moveDirection('L')
        }

        if(currentPositionY < destinationPositionY){
            moveDirection('U')
        }
        else if(currentPositionY > destinationPositionY){
            moveDirection('D')
        }

        if(currentPositionX == destinationPositionX && currentPositionY == destinationPositionY){
            break;
        }
    }
}

function moveDirection(direction){
    Tiles_submit(direction);
}