# Introduction

In Day 27, we're building a daily habit app.

With this app, we'll track our daily habit activity.  It looks like we use Pixela.

This is the URL:

https://pixe.la/

I see these commands to get us started.

```bash
curl -X POST https://pixe.la/v1/users -d '{"token":"thisissecret", "username":"a-know", "agreeTermsOfService":"yes", "notMinor":"yes"}'
```

I'll run a command similar to that for me with my username and secret.  I also see we agree to the TOS and state we're not a minor.

Next, we create a graph definition with this command:

```bash
curl -X POST https://pixe.la/v1/users/a-know/graphs -H 'X-USER-TOKEN:thisissecret' -d '{"id":"test-graph","name":"graph-name","unit":"commit","type":"int","color":"shibafu"}'

```

- I use my user token (and not my id).
- It looks like I specify my desired name.
- Also a color
- I have to figure out what the unit of "commit" means.

