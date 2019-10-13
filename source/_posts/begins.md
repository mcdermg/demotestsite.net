---
title: It begins
date: 2018-10-17 20:17:41
tags: Pi project
cover_image: images/post2/pi.jpg
---
So I am planning on starting a new project. One that is hopefully going to introduce me to some new technologies as well as improve on existing skills. I'm not going to go into too much detail in this post as I'm not sure myself on the exact plan so far but it will be a home monitoring project that is going to use Raspberry Pi's with some sensors. It will probably evolve a bit over the course of the project and I will follow up with a more specific post on my plan of action. For now I need to dust off them Pi's and se what state thy are in and reintroduce myself to them as its been a while.

So I haven't used the Pis for quite some time and of course I have no record of the setup. Usernames, credentials and all the rest. how I configured them is lost to the mists of time. I really need to get better at documenting things. More on that later as well.

On getting the Pis's out to start the ball rolling on this project I spent the best part of half a day messing with Rasbian lite image but had some problems getting it onto WIFI. Not sure what was the problem. Amazing how can forget so much as I have used these in a couple of projects now but I suppose I spent the last 2 years backpacking and that was a pretty low tech affair.

But as history tends to repeat itself I want to take a new tack on this project. So instead of dong bespoke setups I am going to attempt to try and standardise the process. This will help in my next project but also just  mean that I can apply a standardised configuration when I tear down the project and need to set it back u. The whole cattle not pets approach, although I will still name each Pi. The idea is to have a set of basic modules that can be reused or rerun, like setting up WIFI. With this in mind there is a handy (I think new) means of adding a wpa supplicant file onto the boot partition. Also adding a .ssh file and the pi will copy these over to be used. So in effect you get auto WIFI. To think of all the manual messing I did back in university to get the Pi's onto the college network as part of final project. the project was name d Tetralogy and you can [find some details here](http://www.shanefinan.org/visual_art_pages/our_altered_places.html) and the [projects website here](https://frontsquare.scss.tcd.ie/tetralogy/).

So I created a template wpa supplicant file. I did a quick bit of research and found that its a good idea to encrypt your WIFI password. So if anyone is interested [here is the guide I followed.](https://carmalou.com/how-to/2017/08/16/how-to-generate-passcode-for-raspberry-pi.html) just run <code>wpa_passphrase [ssid-name] [password-name]</code>
So you end up with something like:
<code>
network={
	ssid="NetworkName"
	psk=575827beef2c7dbdcf817a9cd0e6b96fb0fd3f54e2c0fbf24a38eb04fb7e9aa3
}
</code>

So I have two Pi zeros and two Pi 3's. Armed with the above I was able to get them all up and running headless and straight onto network with the minimal of hassle. I am looking at using something akin to Packer to build an image that I will use for the project but this might be overkill. One thing that has been a bother in the past is the constant burning of images and modifying and all that. But as I am trying this new DevOps approach of modules and easily repeatable process this shouldn't be too big of an issue. I will probably live to regret thinking that!!
