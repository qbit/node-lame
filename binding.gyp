{
  'targets': [
  ],
  'conditions': [
    ['OS=="openbsd"', {
      'targets': [
        {
          'target_name': 'bindings',
          'include_dirs': [
            '<!(node -e "require(\'nan\')")',
            '/usr/local/include',
            '/usr/local/include/lame',
          ],
          'sources': [
            'src/bindings.cc',
            'src/node_lame.cc',
            'src/node_mpg123.cc'
          ],
        },
      ],
    }],
    ['OS!="openbsd"', {
      'targets': [
        {
          'target_name': 'bindings',
          'sources': [
            'src/bindings.cc',
            'src/node_lame.cc',
            'src/node_mpg123.cc'
          ],
          "include_dirs" : [
            '<!(node -e "require(\'nan\')")'
          ],
          'dependencies': [
            'deps/lame/libmp3lame.gyp:mp3lame',
            'deps/mpg123/mpg123.gyp:mpg123'
          ],
          'conditions':[
            ['OS=="win"', {
              'defines':[
                'NOMINMAX'
              ],
            }],
	  ],
        },
      ],
    }],
  ],
}
