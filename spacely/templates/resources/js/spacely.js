Game = {
	// This defines our grid's size and the size of each of its tiles
	map_grid: {
		width:  800,
		height: 600
	},

	// The total width of the game screen. Since our grid takes up the entire screen
	//  this is just the width of a tile times the width of the grid
	width: function() {
		return this.map_grid.width;
	},

	// The total height of the game screen. Since our grid takes up the entire screen
	//  this is just the height of a tile times the height of the grid
	height: function() {
		return this.map_grid.height;
	},

	// Initialize and start our game
	start: function() {
		// Start crafty and set a background color so that we can see it's working
		Crafty.init(Game.width(), Game.height());
		//Crafty.background('black');

		// Simply start the "Loading" scene to get things going
		Crafty.scene('Loading');
	}
}

// Models!

Crafty.c('Ship', {
	init: function() {
		this.requires('2D, Color, Canvas, Mouse');
		this.attr({
			zone: 0,
			size: 10,
			id:0,
    		name: 'LOL',
		})
	},

});

Crafty.c('Zone', {
	init: function() {
		this.requires('2D, Canvas, Color, Mouse');
		this.attr({
			size: 1000,
    		name: 'Null',
		})
	},

});

// Loading scene
// -------------
// Handles the loading of binary assets such as images and audio files
Crafty.scene('Loading', function(){
	var main;

	zone = Crafty.e('Zone').color('black').attr({w:Game.map_grid.width, h:Game.map_grid.height});

	player = Crafty.e('Ship').color("blue").attr({w:50, h:50, x:100});
	player.bind('Click', function(e) {
		console.log(e);
		console.log('Selected Ship ['+e+']');
	});

	zone.bind('Click', function(e) {
		console.log(e);
		target_x = e.realX;
		target_y = e.realY;

		console.log('Creating route towards ('+target_x+','+target_y+')')
		//Make a new event for this
		socket.send(new Event('MOVE', {'current_x':player.x, 'x':target_x, 'current_y':player.y, 'y':target_y}), 'zone-2');

	})


});

