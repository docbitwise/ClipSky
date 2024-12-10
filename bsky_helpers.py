from typing import List
from atproto import Client, models
from atproto_client.models import AppBskyRichtextFacet as rtf
import os


class BskyEasyClient(Client):
    def __init__(self, username: str = os.environ['BSKY_USERNAME'], password: str = os.environ['BSKY_PASSWORD']):
        super().__init__()
        self.login(username, password)

    def postWithImages(self, text: str, images: List[bytes], tags: List[str] = None) -> None:
        """
        Sends an image to the BlueSky API.

        Args:
            text (str): The text of the post to send.
            image (bytes): The image to send.

        Returns:
            None
        """
        facets = []
        if tags:
            for tag in tags:
                # Find the starting index
                start_index = text.find(tag)

                if start_index != -1:
                    # Calculate the ending index
                    end_index = start_index + len(tag)
                    print(f"Substring '{tag}' found at index {
                          start_index} to {end_index}")
                else:
                    print(f"Substring '{tag}' not found")
                    continue

                facets.append(rtf.Main(index=rtf.ByteSlice(byte_start=start_index, byte_end=end_index), features=[
                              {"$type": "app.bsky.richtext.facet#tag", "tag": tag[1:]}]))
        # if links:
        #     for link in links:
        #         facets.append(models.AppBskyRichtextFacet.Main(features=[
        #         ], index=models.AppBskyRichtextFacet.ByteSlice(byte_start=link["start"], byte_end=link["end"]), link=link))
        self.send_images(text=text, images=images[:4], facets=facets)
        print("Sent post to BlueSky!")
