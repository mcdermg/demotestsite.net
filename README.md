# demotestsite.net

My initial attempt at a blog site. i was more interested inhostinc a static site and leaning automated build and deployment process that actually writing blog articles so this has not really been kept up tp date.

The technical side is but choice of Hexo might not have been the best.

Pushes to the repo trigger a CircleCI piepline that builds the static elelemtns, these ar ethen copied to an AWS S3 storage bucket. The bucket is fronted by AWS CDN and there is some Terrafrom managing the DNS.

Its all a good setup but I need to go back ad flip over to GitHub actions from CircleCI, I dont think Actions were availabele when I created all this.

Also need to switch over to a different static blog framework as well.

But like many projects I may leave it half finsihed and underloved.......
