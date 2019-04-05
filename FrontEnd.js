var config = {
    type: Phaser.AUTO,
    width: 800,
    height: 600,
    scene: {
        preload: preload,
        create: create,
        move: move
    }
};

var game = new Phaser.Game(config);
var player;

function preload () {
    this.load.image('background', 'images/trivia-background.jpg');
    this.load.image('Question', 'images/Question.png');
    this.load.image('o', 'images/letter-o-block-capitals.png');
    this.load.image('x','images/LETTERS_x.jpg');
    this.load.image('player', 'images/pcircle.png');
}

function create () {
    this.add.image(400, 300, 'background');
    this.add.image(200,200, 'Question');
    this.add.image(150, 150, 'o');
    this.add.image(150, 150, 'x');
    this.input.setDefaultCursor('url(images/pcircle.png), pointer');
    player = this.add.sprite(400, 300, 'player').setInteractive({ cursor: 'url(images/pcircle.png), pointer' });
    //the cursor is the player for each individual
}

function move(){
    player.body
    //set player to the corner or the bottom of the screen

    //if player-cursor moves up, have it move up, vice versa

}

