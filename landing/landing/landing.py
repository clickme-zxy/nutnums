"""Welcome to Reflex! This file outlines the steps to create a basic app."""
from rxconfig import config

import reflex as rx

docs_url = "https://reflex.dev/docs/getting-started/introduction"
filename = f"{config.app_name}/{config.app_name}.py"


class State(rx.State):
    """The app state."""

    pass


def index() -> rx.Component:
    return rx.fragment(
        rx.color_mode_button(rx.color_mode_icon(), float="right"),
        # 小标题
        rx.hstack(
            rx.text("About",font_size = "2em",width="25%"),
            rx.text("How it works",font_size = "2em",width="25%"),
            rx.text("Join us",font_size = "2em",width="25%"),
            rx.text("The team",font_size = "2em",width="25%"),
            bg = "darkgray",
            as_="b",
        ),
        # header
        rx.hstack(
            rx.vstack(
                rx.text("Nutnums, streamlines your collecting experience, treasure hunting made easy",font_size="3em",as_="b",padding_left="3em",),
                rx.text("",font_size= "3em"),
                rx.text("For fans by fans",as_="i",font_size="3em",padding_right="9em",),
                width = "70%"
            ),
            rx.image(src="head_image.png",width="30%"),
            bg="lightgray",
        ),

        rx.vstack(
            rx.markdown(
                """ ### Why we’re doing this & What we want to tackle"""
            ),
            rx.markdown(
                """
As a nerd who’s been obsessed with lots of different IPs ever since I was a kid, after talking to lots of people I found that there are 3 problems common and not limited to collectors: 

1.There are too many editions or series or other nuanced info, it’s hard to keep up with all, which can be discouraging to MANY of us. [1]</br>
2.Even with comprehensive information, it’s still challenging to browse through different markets accordingly, track across multiple social media platforms to find listings for the exact item you want, which may take hours, days and even months of effort.</br> 
3.Hard to manage and keep track of what we have and what we want.</br>

All of which become even more painful for someone with both ADHD and OCD like me, our hobby and our obsession should be our joy not burden, so an idea to solve this came naturally to me when shopping for photo cards while anxiety was building up.

[1] Nevertheless, there are some altruistic people in the community making well-designed templates, but they need to be updated constantly and conform to different standards, not to mention it takes great effort on their part and sometimes it breaks our heart when they discontinue their accounts.
"""
            ),
            padding_left = "10%",
            padding_right = "10%",
        ),
        rx.vstack(
            rx.markdown(
                """### How it works:"""
            ),
            rx.markdown(
                """1.Curated overview and info for your collection, specific to issue dates, series, nicknames, and more;</br>
2.Find specific listings whenever an item catches your eyes. You can link your listings from eBay, Mercari, or other marketplaces and social media platforms to specific entries [2];</br>
3.Spot an incomplete template or inaccurate information? Edit it, get credit and rewarded for every piece of information you contribute;</br>
4.Easily track your collections, you can save an entire template or make a wish list of your own, mark what you already have and don’t have yet.</br>
5.Utilised machine learning to identify each item from your post, streamlining your listing and collection tracking experience.</br>
                """
            ),
            rx.markdown(
            """We will be updating the above features one by one, while we are building a minimum working version outside of our busy school and work, your support will help us ensure that we’re making something people really want."""
            ),
            padding_left = "10%",
            padding_right = "10%",
        ),
        
        rx.vstack(
            rx.markdown(
            """### Ways to do that:"""
            ),
            rx.image(src="email_image.png"),
            rx.markdown(
            """Join our discord and telegram group, we’d love for you to share your own struggles with collecting merch to improve our approach: []</br> 
            Share on social media: [Social media logos and outward links]</br>"""
            ),
            padding_left = "10%",
            padding_right = "10%",
        ),

        rx.vstack(
            rx.markdown(
            """### Have advices or questions and wanna reach us personally? 
            """
            ),
            rx.markdown(
            """You can either pin us through the discord or telegram group above, or email us at [email]</br>
            To take it further, make a booking to talk with us directly: [Calendly Link]</br>"""
            ),
            padding_lef = "10%",
            padding_right = "10%",
        ),

        rx.stack(
            rx.markdown("""
            ### About the team
            """
            ),
            padding_left = "10%",
            padding_right = "10%",
        ),
    )


# Add state and page to the app.
app = rx.App(state=State)
app.add_page(index)
app.compile()

