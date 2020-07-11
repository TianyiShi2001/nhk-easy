# `nhk-easy`

An API for [NHK News Web Easy](https://www3.nhk.or.jp/news/easy/).

It includes a command-line application that supports download of audio (as `.m3u8` playlists or `.mp3`) and text (with or without furigana, in plain text or HTML) of today's top news articles displayed on the homepage of [NHK News Web Easy](https://www3.nhk.or.jp/news/easy/).

# Installation

```
pip install nhk-easy
```

# Synopsis

```
usage: nhk-easy [-h] [-M] [-d DIRECTORY] [-F] [-H]

optional arguments:
  -h, --help            show this help message and exit
  -M, --mp3             Download mp3 audio instead of m3u8 playlist (ffmpeg required)
  -d DIRECTORY, --directory DIRECTORY
                        output directory
  -F, --furigana        enable furigana
  -H, --html            HTML output (default is txt)
```

# Usage

To start with, try `nhk-easy` alone (with default options):

```
nhk-easy
```

This downloads:
  1. plain text without furigana in `.txt` files, and
  2. the `.m3u8` playlist file of the audio

of all top articles currectly shown on https://www3.nhk.or.jp/news/easy/

`m3u8` playlists can be streamed by VLC, for example, to play audio.

If you want furigana, use the flag `--furigana` (`-F`). If you want HTML output instead of plain text, use the flag `--html` (`-F`). In plain text, furigana guides are shown in parentheses; in HTML output, they are contained within `ruby` tags.

If you have [**ffmpeg**](https://ffmpeg.org) installed, you may use the `--mp3` (`-M`) flag to download `.mp3` audio files instead of `.m3u8` playlists.

You can use the `--directory` (`-d`) flag to specify the output directory (defaults to the currect directory).

Example output:

```
$ mkdir outdir && nhk-easy -MFH -d outdir && ls outdir
2020-07-08-避難所でコロナウイルスがうつらないように気をつけること.mp3
2020-07-08-避難所でコロナウイルスがうつらないように気をつけること.html
2020-07-09-コロナウイルスのアプリ　うつったことを知らせた人は３人.mp3
2020-07-09-コロナウイルスのアプリ　うつったことを知らせた人は３人.html
......
```

# Copyright Notice

You should abide by [NHK's copyright notice](https://www.nhk.or.jp/toppage/nhk_info/copyright.html):

> NHKホームページはすべてNHKの著作物です。次の点にご注意いただいた上でご利用下さい。
> - NHKのホームページの画面あるいは内容を
>   - 自分のホームページに取り込んではいけません。
>   - 著作権法で許された範囲を超えて複製してはいけません。
>   - 著作権法で許された範囲内で複製する場合でも、その複製物を目的外に利用してはいけません。
>   - 著作権法で許された範囲内で複製する場合でも、改変するなど手を加えてはいけません。
>   - 電子透かしについて
> - NHKのホームページではNHKおよびNHKに素材を提供していただいている他の著作権保有者の権利を守るために、電子透かしを用いています。

# Troubleshooting

## Fail to Download mp3

### `ffmpeg` freezes due to unstable internet connection

- `ctrl+C` and/or `ctrl+D` to exit.
- Delete any incomplete file(s).
- Make sure you have a good connection, then re-run `nhk-easy` with the same argument(s). Files already downloaded will be skipped.

### `ffmpeg` error

#### `dyld: Library not loaded: /usr/local/opt/libffi/lib/libffi.6.dylib`

See https://github.com/platformio/platform-lattice_ice40/issues/7 . This is the most widely accepted solution:

```
cd /usr/local/opt/libffi/lib
ln -s libffi.7.dylib libffi.6.dylib
```

# Licence

```
The MIT License (MIT)

Copyright (c) 2020 石天熠

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```