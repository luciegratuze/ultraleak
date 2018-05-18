# ultraleak


Transmits the bytes of a file via beeps, and analyses the record of a file sent, to retrieve it.

## Usage

`ultraleak3.py -f path/to/file -1 freq_ones(Hz) -0 freq_zeros(Hz) -d symbol_duration(ms)`

`analyse.py -f path/to/wav/file -t tolerance(Hz) -1 freq_ones(Hz) -0 freq_zeros(Hz) -d symbol_duration(ms)`

## Examples

All the provided examples were created with a symbol_duration of 1000ms.

**Small_photo.wav** was transmitted at
- 5000Hz for ones
- 500Hz for zeros

`analyse.py -f path/to/Small_photo.wav -t 3 -1 5000 -0 500 -d 1001`

**ultrasound.wav** was transmitted at
- 21700Hz for ones
- 21000Hz for zeros

`analyse.py -f path/to/ultrasounds.wav -t 1 -1 21700 -0 21000 -d 1000`

**Secret_message.wav** was transmitted at 
- 20kHz for ones
- 18kHz for zeros

`analyse.py -f path/to/Secret_message.wav -t 35 -1 20000 -0 18000 -d 1001`
 