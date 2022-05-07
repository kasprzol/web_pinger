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

    def test_invalid_certificate(self):
        """Test that/ping endpoint handles invalid ssl certificates."""
        client = Client()
        body = {"url": "https://expired.badssl.com"}
        response = client.post(
            "/ping", data=json.dumps(body), content_type="application/json"
        )

        expected = {
            "response": """<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="shortcut icon" href="/icons/favicon-red.ico"/>
  <link rel="apple-touch-icon" href="/icons/icon-red.png"/>
  <title>expired.badssl.com</title>
  <link rel="stylesheet" href="/style.css">
  <style>body { background: red; }</style>
</head>
<body>
<div id="content">
  <h1 style="font-size: 12vw;">
    expired.<br>badssl.com
  </h1>
</div>

</body>
</html>
"""
        }
        self.assertJSONEqual(response.content, expected)
