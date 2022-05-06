import json

from django.test import Client, TestCase


# Create your tests here.
class RestAppTest(TestCase):
    def test_info(self):
        client = Client()
        response = client.get("/info")
        self.assertJSONEqual(response.content, {"Receiver": "Cisco is the best!"})

    def test_ping(self):
        client = Client()
        body = {"url": "https://raw.githubusercontent.com/torvalds/linux/master/README"}
        response = client.post(
            "/ping", data=json.dumps(body), content_type="application/json"
        )

        expected = {
            "response": """Linux kernel
============

There are several guides for kernel developers and users. These guides can
be rendered in a number of formats, like HTML and PDF. Please read
Documentation/admin-guide/README.rst first.

In order to build the documentation, use ``make htmldocs`` or
``make pdfdocs``.  The formatted documentation can also be read online at:

    https://www.kernel.org/doc/html/latest/

There are various text files in the Documentation/ subdirectory,
several of them using the Restructured Text markup notation.

Please read the Documentation/process/changes.rst file, as it contains the
requirements for building and running the kernel, and information about
the problems which may result by upgrading your kernel.
"""
        }
        self.assertJSONEqual(response.content, expected)
