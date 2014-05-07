(function(){

	// ----- BACKBONE.JS ACTION -----
	window.App = {
		Models: {},
		Collections: {},
		Views: {}
	};
	
	window.template = function(id){
		return _.template( $('#' + id).html());
	};

	//The model for the data
	App.Models.Race = Backbone.Model.extend({
		defaults: {
			results: 'stuff',
			pre_reporting: '24/50'
		}
	});

	// A List of races
	App.Collections.Races = Backbone.Collection.extend({
		model: App.Models.Race
	});

	// View for all Races
	App.Views.AllRaces = Backbone.View.extend({
	  tagName: 'div',
	  el: '#content',

	  render: function(){
		  this.collection.each(function(race){
			  var raceView = new App.Views.Race({ model: race });
			  this.$el.append(raceView.render().el); // adding all the person objects.
		  }, this);
		  return this;
	  }
	});

	// The View for a race
	App.Views.Race = Backbone.View.extend({
	  tagName: 'div',
	  className: 'race',
	  template: template('depTemplate'),
	  render: function(){
		  this.$el.html( this.template(this.model.toJSON()));
		  return this;  // returning this from render method.
	  }
	});

	var raceCollection = new App.Collections.Races(results);

	var all_races = new App.Views.AllRaces({collection: raceCollection})
	
	$('#container').append(all_races.render().el);
	// -------- END BACKBONE ------
	
})();
