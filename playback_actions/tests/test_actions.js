var playback_actions = require('../playback_actions.js')
var assert = require('assert')

describe('test getUsers function regular behaviour' , function(){
    it('works', () => {
        let users = playback_actions.getUsers(playback_actions.db_records, "start", 700, 900)
        assert.equal( users.length, 1 )
        assert.equal( users[0], 3 )
    });
});


describe('test getPlaybackTime function regular behaviour' , function(){
    it('works', () => {
        let playbackTime = playback_actions.getPlaybackTime(1, playback_actions.db_records)
        assert.equal( playbackTime, 310 )
    });
});
