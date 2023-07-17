# Goal
A universal music to RGB light sync device. 

It should be easy to set up and leave running for a long period of time, and ideally, it should be simple to control from my phone. It should have different parameters to change how responsive it is to the ambient music, and, ideally, it should be able to have pre-set “moods” that might limit things like the range of available colors, maximum and minimum light intensities and similar. 

In terms of what kinds of music it can understand, I want it to be able to use a combination of:
1. A local microphone
2. A microphone connected through the network
3. Connecting to a music player API like spotify or soundcloud

In terms of what kinds of lights I want it to control, I want it to be able to use a combination of:
1. A local LED strip
2. An LED connected through the network
3. Smart lights such as phillips hue

## Phases
### Phase 1 - Get the lights working
1. Set up the Raspberry PI
2. Connect it to LEDs
3. Come up with some reasonable libraries for programming the neo-pixels
4. Step back and think of a reasonable abstraction layer that could encapsulate other kinds of lights (e.g. Phillips Hue or anything generally connected to the google home API, definitely dig into what options there are for that)

### Phase 2 - Get a microphone working
1. Start capturing audio input
2. Figure out a way to create a real time loop that samples music at a responsive interval
3. Figure out cool ways to model the analog input that could then map to rgb values
4. Might be fun to see if there are any ML models out there for this kind of thing
    1. Being able to hook into spotify or soundcloud would be super cool as would be hooking into the google home mics if that is possible?

### Phase 3 - Connect the dots
1. Figure out how to pipe the audio data to the lights routine and get the light to respond to simple inputs like my voice
2. Start figuring out cool ways to modulate and weight that data.

### Phase 4 - Make it useable
1. Need to wrap the library in a light weight web framework (probably flask?)
    1. Let's do some due diligence on how to secure this too - don't want to accidentally let people just listen into my house (creepy)
2. Need to create a really simple app (maybe play around with android?) to connect with that app