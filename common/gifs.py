import random

gifs = [
    '<iframe src="https://giphy.com/embed/1xXaGFtQjvW6I" width="270" height="150" frameBorder="0" class="giphy-embed" allowFullScreen></iframe>',
    '<iframe src="https://giphy.com/embed/Xd3xIZ9XHO5uE" width="270" height="150" frameBorder="0" class="giphy-embed" allowFullScreen></iframe>',
    '<iframe src="https://giphy.com/embed/oP1wXfmRFxBTO" width="270" height="150" frameBorder="0" class="giphy-embed" allowFullScreen></iframe>',
    '<iframe src="https://giphy.com/embed/4Kpqhw1Pu3HQk" width="270" height="150" frameBorder="0" class="giphy-embed" allowFullScreen></iframe>',
    '<iframe src="https://giphy.com/embed/12mykE9f4gnNOo" width="270" height="150" frameBorder="0" class="giphy-embed" allowFullScreen></iframe>',
    '<iframe src="https://giphy.com/embed/229rpnGFx8lXUxISC3" width="270" height="150" frameBorder="0" class="giphy-embed" allowFullScreen></iframe>',
    '<iframe src="https://giphy.com/embed/oF3bOtVhGe2Oc" width="270" height="150" frameBorder="0" class="giphy-embed" allowFullScreen></iframe>'
]


def get_random_gif():
    return gifs[random.randint(0, len(gifs) - 1)]
