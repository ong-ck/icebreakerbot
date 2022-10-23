<div id="top"></div>

<br />
<div align="center">

<h3 align="center">IceBreakerBot</h3>

  <p align="center">
    Find a friend through this telegram bot, create a group chat with them and the bot and let the ice breaking begin!
    <br />
    <a href="https://github.com/ong-ck/icebreakerbot"><strong>Explore the docs »</strong></a>

</div>

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li>
      <a href="#roadmap">Roadmap</a>
      <ul>
        <li><a href="#features">Features</a></li>
      </ul>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details><br>


<!-- ABOUT THE PROJECT -->
<div id = "about-the-project"></div>

## About The Project

<div id = "built-with"></div>

### Built With

* [Python](https://www.python.org/)
* [Telegram API](https://core.telegram.org/api)
* [python-telegram-bot](python-telegram-bot.org)
* [libretranslate](libretranslate.com)

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- GETTING STARTED -->
<div id = "getting-started"></div>

## Getting Started

  Kindly follow the instructions below to get started.

<div id = "prerequisites"></div>

### Prerequisites

* pip
  ```sh
  pip install python-telegram-bot
  pip install pymongo
  pip install libretranslatepy
  ```
<div id = "installation"></div>

### Installation

1. Get a free API Key from Telegram from BotFather https://core.telegram.org/bots

2. Create a free account from MongoDB https://www.mongodb.com/

3. Clone the repo
   ```sh
   git clone https://github.com/ong-ck/icebreakerbot
   ```

4. Enter your API key for each of the APIs above in `config.py`

4. Run `main.py`

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
<div id = "usage"></div>

## Usage

  DISCLAIMER: Using this telegram bot requires the collection of personal information. PLEASE MAKE SURE TO DRAFT A PRIVACY STATEMENT BEFORE ATTEMPTING TO EMULATE THIS PROJECT AND INFORM THE USER ABOUT THE COLLECTION OF ANY PERSONAL DATA.

  1. Type /find to answers some questions about yourself.

  2. Username of matched user will be sent to you by the bot.

  3. Proceed to create a telegram group chat with said matched user and this bot.

  4. In case matched user and yourself speak different languages, this bot will attempt to auto translate any non-command texts in the group chat (by default from "en" to "de", with "en", "de" and "es" currently available for selection).

  5. To set translation languages, type /setlang

  6. To toggle auto translation on/off, type /toggle_translation

  7. To BREAK SOME ICE, type /breakice


<p align="right">(<a href="#top">back to top</a>)</p>



<!-- ROADMAP -->
<div id = "roadmap"></div>

## Roadmap

<div id = "features"></div>

### Features
- Finding like-minded individuals
- Auto translation for better connectivity
- Ice Breaker features

<p align="right">(<a href="#top">back to top</a>)</p>


<!-- ACKNOWLEDGMENTS -->
<div id = "acknowledgments"></div>

## Acknowledgments

* [Starter python code for a telegram bot using the library python-telegram-bot by liuhh02](https://gist.github.com/liuhh02/193bb28aab9a4efe08962c5b78c3b5da)
* [python-telegram-bot](python-telegram-bot.org)
* [libretranslate](libretranslate.com)

<p align="right">(<a href="#top">back to top</a>)</p>