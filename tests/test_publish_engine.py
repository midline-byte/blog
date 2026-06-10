import os
import unittest

from src.publish_engine import build_post_payload, publish_post


class PublishEngineTest(unittest.TestCase):
    def test_builds_draft_payload(self):
        payload = build_post_payload("Title", "Content", ["tag"], "draft")

        self.assertEqual(payload["status"], "draft")
        self.assertEqual(payload["title"], "Title")

    def test_fails_without_blog_credentials(self):
        old_url = os.environ.pop("BLOG_API_URL", None)
        old_token = os.environ.pop("BLOG_API_TOKEN", None)
        try:
            result = publish_post(build_post_payload("Title", "Content", []), max_attempts=1)
        finally:
            if old_url is not None:
                os.environ["BLOG_API_URL"] = old_url
            if old_token is not None:
                os.environ["BLOG_API_TOKEN"] = old_token

        self.assertEqual(result.status, "fail")


if __name__ == "__main__":
    unittest.main()
