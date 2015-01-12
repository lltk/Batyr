var item = {};
var mode = 'input';

$(document).ready(function() { init(); });

function init() {

	if (language == undefined) {
		var language = 'de';
	}
	next(language);

	$('img#play-input').click(function() { play(); focus(); })
	$('img#play-answer').click(function() { play(); focus(); })
	$('img#tatoeba').click(function() { tatoeba(); })

};

function next() {
	$.getJSON('/items/random/' + language, function(data) {
		item = data;
		play(language);
		$('input#question').val('');
		$('div#answer').html(item['text']);
		$('div#question-block').show();
		$('div#answer-block').hide();
		$('input#question').focus();
		mode = 'input';
	});
};

function play() {
	var audioElement = document.createElement('audio');
	audioElement.setAttribute('src', item['audio']);
	audioElement.setAttribute('preload', 'auto');
	audioElement.setAttribute('autoplay', 'true');
	$(audioElement).appendTo($('body')).css('display','none');
};

function focus() {
	$('input#question').focus();
};

function tatoeba() {
	window.open('http://tatoeba.org/eng/sentences/show/' + item['id']);
}

function okay() {

	score = distance(item['text'], $('input#question').val());
	console.log('Distance: ' + score);
	$('div#question-block').hide();
	$('div#answer-block').show();
	if (score > 0.3) {
		$('div#answer').removeClass('correct incorrect').addClass('incorrect');
	}
	else {
		$('div#answer').removeClass('correct incorrect').addClass('correct');
	}
	mode = 'answer';

}

function distance(a, b) {
	value = new Levenshtein(a, b);
	return (value.distance / a.length);
}

$(document).keydown(function(e) {

	switch(e.which) {

		/* Enter */
		case 13: if (mode == 'input') { okay(); } else { next(); };
		break;
	}

});
