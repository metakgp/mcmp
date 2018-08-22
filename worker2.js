importScripts('string_score.min.js');

var data;

var fields = ['name', 'field', 'department'];

onmessage = function(e) {
    if (e.data.type === 'data') {
        data = e.data.data;
    } else if (e.data.type === 'query') {
        var query = e.data.query;
        var terms = query.split(/\s+/);
        var fuzz = 0.3;
        console.log('got query: ', query);
        for (var j = 0; j < data.length; ++j) {
            data[j].score = {'name': 0, 'field': 0, 'department': 0, 'total': 1};
            for (var t = 0; t < terms.length; ++t) {
                var maxTermScore = 0, maxField;
                for (var f = 0; f < fields.length; ++f) {
                    var termFieldScore = data[j][fields[f]].score(terms[t], fuzz);
                    if (termFieldScore > maxTermScore) {
                        maxTermScore = termFieldScore;
                        maxField = f;
                    }
                }
                data[j].score[fields[maxField]] += maxTermScore;
            }
            for (var f = 0; f < fields.length; ++f) {
                data[j].score.total += Math.max(data[j].score[fields[f]], 0.2) - 0.2;
            }
        }
        data.sort(function(a, b) {
            return b.score.total - a.score.total;
        });
        var results = data.slice(0, 20);
        console.log('results: ', results);
        postMessage(results);
    }
};
