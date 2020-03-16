import os
import logging

from thug.ThugAPI.ThugAPI import ThugAPI

log = logging.getLogger("Thug")


class TestMiscSamplesIE(object):
    thug_path = os.path.dirname(os.path.realpath(__file__)).split("thug")[0]
    misc_path = os.path.join(thug_path, "thug", "samples/misc")

    def do_perform_test(self, caplog, sample, expected):
        thug = ThugAPI()

        thug.set_useragent('win7ie100')
        thug.set_events('click,storage')
        thug.set_connect_timeout(2)
        thug.disable_cert_logging()
        thug.set_file_logging()
        thug.set_features_logging()
        thug.set_ssl_verify()
        thug.log_init(sample)
        thug.run_local(sample)

        records = [r.message for r in caplog.records]

        matches = 0

        for e in expected:
            for record in records:
                if e in record:
                    matches += 1

        assert matches >= len(expected)

    def test_plugindetect1(self, caplog):
        sample   = os.path.join(self.misc_path, "PluginDetect-0.7.6.html")
        expected = ['AdobeReader version: 9.1.0.0',
                    'Flash version: 10.0.64.0']

        self.do_perform_test(caplog, sample, expected)

    def test_plugindetect2(self, caplog):
        sample   = os.path.join(self.misc_path, "PluginDetect-0.7.8.html")
        expected = ['AdobeReader version: 9,1,0,0',
                    'Flash version: 10,0,64,0',
                    'Java version: 1,6,0,32',
                    'ActiveXObject: javawebstart.isinstalled.1.6.0.0',
                    'ActiveXObject: javaplugin.160_32']

        self.do_perform_test(caplog, sample, expected)

    def test_test1(self, caplog):
        sample   = os.path.join(self.misc_path, "test1.html")
        expected = ['[Window] Alert Text: one']
        self.do_perform_test(caplog, sample, expected)

    def test_test2(self, caplog):
        sample   = os.path.join(self.misc_path, "test2.html")
        expected = ['[Window] Alert Text: Java enabled: true']
        self.do_perform_test(caplog, sample, expected)

    def test_test3(self, caplog):
        sample   = os.path.join(self.misc_path, "test3.html")
        expected = ['[Window] Alert Text: foo']
        self.do_perform_test(caplog, sample, expected)

    def test_testAppendChild(self, caplog):
        sample   = os.path.join(self.misc_path, "testAppendChild.html")
        expected = ['Don\'t care about me',
                    'Just a sample',
                    'Attempt to append a null element failed',
                    'Attempt to append an invalid element failed',
                    'Attempt to append a text element failed',
                    'Attempt to append a read-only element failed']

        self.do_perform_test(caplog, sample, expected)

    def test_testClipboardData(self, caplog):
        sample   = os.path.join(self.misc_path, "testClipboardData.html")
        expected = ['Test ClipboardData']
        self.do_perform_test(caplog, sample, expected)

    def test_testCloneNode(self, caplog):
        sample   = os.path.join(self.misc_path, "testCloneNode.html")
        expected = ['<div id="cloned"><q>Can you copy <em>everything</em> I say?</q></div>']
        self.do_perform_test(caplog, sample, expected)

    def test_testCloneNode2(self, caplog):
        sample   = os.path.join(self.misc_path, "testCloneNode2.html")
        expected = ['[Window] Alert Text: [object HTMLButtonElement]',
                    '[Window] Alert Text: Clone node',
                    '[Window] Alert Text: None',
                    '[Window] Alert Text: [object Attr]',
                    '[Window] Alert Text: True']

        self.do_perform_test(caplog, sample, expected)

    def test_testCreateHTMLDocument(self, caplog):
        sample   = os.path.join(self.misc_path, "testCreateHTMLDocument.html")
        expected = ['[object HTMLDocument]',
                    '[object HTMLBodyElement]',
                    '<p>This is a new paragraph.</p>']

        self.do_perform_test(caplog, sample, expected)

    def test_testCreateStyleSheet(self, caplog):
        sample   = os.path.join(self.misc_path, "testCreateStyleSheet.html")
        expected = ['[Window] Alert Text: style1.css',
                    '[Window] Alert Text: style2.css',
                    '[Window] Alert Text: style3.css',
                    '[Window] Alert Text: style4.css']

        self.do_perform_test(caplog, sample, expected)

    def test_testDocumentAll(self, caplog):
        sample   = os.path.join(self.misc_path, "testDocumentAll.html")
        expected = ["http://www.google.com"]
        self.do_perform_test(caplog, sample, expected)

    def test_testDocumentWrite1(self, caplog):
        sample   = os.path.join(self.misc_path, "testDocumentWrite1.html")
        expected = ['Foobar',
                    "Google</a><script>alert('foobar');</script><script language=\"VBScript\">alert('Gnam');</script><script>alert('Aieeeeee');</script></body>"]
        self.do_perform_test(caplog, sample, expected)

    def test_testExternalSidebar(self, caplog):
        sample   = os.path.join(self.misc_path, "testExternalSidebar.html")
        expected = ['[Window] Alert Text: Internet Explorer >= 7.0 or Chrome']
        self.do_perform_test(caplog, sample, expected)

    def test_testGetElementsByClassName(self, caplog):
        sample   = os.path.join(self.misc_path, "testGetElementsByClassName.html")
        expected = ['First',
                    'Hello World!',
                    'Second']
        self.do_perform_test(caplog, sample, expected)

    def test_testInnerHTML(self, caplog):
        sample   = os.path.join(self.misc_path, "testInnerHTML.html")
        expected = ['dude', 'Fred Flinstone']
        self.do_perform_test(caplog, sample, expected)

    def test_testInsertBefore(self, caplog):
        sample   = os.path.join(self.misc_path, "testInsertBefore.html")
        expected = ["<div>Just a sample</div><div>I'm your reference!</div></body></html>",
                    "[ERROR] Attempting to insert null element",
                    "[ERROR] Attempting to insert an invalid element",
                    "[ERROR] Attempting to insert using an invalid reference element",
                    "[ERROR] Attempting to insert a text node using an invalid reference element"]

        self.do_perform_test(caplog, sample, expected)

    def test_testLocalStorage(self, caplog):
        sample   = os.path.join(self.misc_path, "testLocalStorage.html")
        expected = ["Alert Text: Fired",
                    "Alert Text: bar",
                    "Alert Text: south"]
        self.do_perform_test(caplog, sample, expected)

    def test_testPlugins(self, caplog):
        sample   = os.path.join(self.misc_path, "testPlugins.html")
        expected = ["Shockwave Flash 10.0.64.0",
                    "Windows Media Player 7",
                    "Adobe Acrobat"]
        self.do_perform_test(caplog, sample, expected)

    def test_testMetaXUACompatibleEdge(self, caplog):
        sample   = os.path.join(self.misc_path, "testMetaXUACompatibleEdge.html")
        expected = ["[Window] Alert Text: 10"]
        self.do_perform_test(caplog, sample, expected)

    def test_testMetaXUACompatibleEmulateIE(self, caplog):
        sample   = os.path.join(self.misc_path, "testMetaXUACompatibleEmulateIE.html")
        expected = ["[Window] Alert Text: 8"]
        self.do_perform_test(caplog, sample, expected)

    def test_testMetaXUACompatibleIE(self, caplog):
        sample   = os.path.join(self.misc_path, "testMetaXUACompatibleIE.html")
        expected = ["[Window] Alert Text: 10"]
        self.do_perform_test(caplog, sample, expected)

    def test_testNode(self, caplog):
        sample   = os.path.join(self.misc_path, "testNode.html")
        expected = ["thelink",
                    "thediv"]
        self.do_perform_test(caplog, sample, expected)

    def test_testNode2(self, caplog):
        sample   = os.path.join(self.misc_path, "testNode2.html")
        expected = ["thelink",
                    "thediv2"]
        self.do_perform_test(caplog, sample, expected)

    def test_testQuerySelector(self, caplog):
        sample   = os.path.join(self.misc_path, "testQuerySelector.html")
        expected = ["Alert Text: Have a Good life.",
                    "CoursesWeb.net"]
        self.do_perform_test(caplog, sample, expected)

    def test_testQuerySelector2(self, caplog):
        sample   = os.path.join(self.misc_path, "testQuerySelector2.html")
        expected = ['CoursesWeb.net',
                    "MarPlo.net",
                    'php.net']
        self.do_perform_test(caplog, sample, expected)

    def test_testScope(self, caplog):
        sample   = os.path.join(self.misc_path, "testScope.html")
        expected = ["foobar",
                    "foo",
                    "bar",
                    "True",
                    "3",
                    "2012-10-07 11:13:00",
                    "3.14159265359",
                    "/foo/i"]
        self.do_perform_test(caplog, sample, expected)

    def test_testSessionStorage(self, caplog):
        sample   = os.path.join(self.misc_path, "testSessionStorage.html")
        expected = ["key1",
                    "key2",
                    "value1",
                    "value3"]
        self.do_perform_test(caplog, sample, expected)

    def test_testSetInterval(self, caplog):
        sample   = os.path.join(self.misc_path, "testSetInterval.html")
        expected = ["[Window] Alert Text: Hello"]
        self.do_perform_test(caplog, sample, expected)

    def test_testText(self, caplog):
        sample   = os.path.join(self.misc_path, "testText.html")
        expected = ['<p id="p1">First line of paragraph.<br/> Some text added dynamically. </p>']
        self.do_perform_test(caplog, sample, expected)

    def test_testWindowOnload(self, caplog):
        sample   = os.path.join(self.misc_path, "testWindowOnload.html")
        expected = ["[Window] Alert Text: Fired"]
        self.do_perform_test(caplog, sample, expected)

    def test_test_click(self, caplog):
        sample   = os.path.join(self.misc_path, "test_click.html")
        expected = ["[window open redirection] about:blank -> https://buffer.github.io/thug/"]
        self.do_perform_test(caplog, sample, expected)

    def test_testInsertAdjacentHTML1(self, caplog):
        sample   = os.path.join(self.misc_path, "testInsertAdjacentHTML1.html")
        expected = ['<div id="five">five</div><div id="one">one</div>']
        self.do_perform_test(caplog, sample, expected)

    def test_testInsertAdjacentHTML2(self, caplog):
        sample   = os.path.join(self.misc_path, "testInsertAdjacentHTML2.html")
        expected = ['<div id="two"><div id="six">six</div>two</div>']
        self.do_perform_test(caplog, sample, expected)

    def test_testInsertAdjacentHTML3(self, caplog):
        sample   = os.path.join(self.misc_path, "testInsertAdjacentHTML3.html")
        expected = ['<div id="three">three<div id="seven">seven</div></div>']
        self.do_perform_test(caplog, sample, expected)

    def test_testInsertAdjacentHTML4(self, caplog):
        sample   = os.path.join(self.misc_path, "testInsertAdjacentHTML4.html")
        expected = ['<div id="four">four</div><div id="eight">eight</div>']
        self.do_perform_test(caplog, sample, expected)

    def test_testInsertAdjacentHTML5(self, caplog):
        sample   = os.path.join(self.misc_path, "testInsertAdjacentHTML5.html")
        expected = ['insertAdjacentHTML does not support notcorrect operation']
        self.do_perform_test(caplog, sample, expected)

    def test_testCurrentScript(self, caplog):
        sample   = os.path.join(self.misc_path, "testCurrentScript.html")
        expected = ["[Window] Alert Text: This page has scripts",
                    "[Window] Alert Text: text/javascript",
                    "[Window] Alert Text: Just a useless script"]
        self.do_perform_test(caplog, sample, expected)

    def test_testCCInterpreter(self, caplog):
        sample   = os.path.join(self.misc_path, "testCCInterpreter.html")
        expected = ['JavaScript version: 10',
                    'Running on the 32-bit version of Windows']
        self.do_perform_test(caplog, sample, expected)

    def test_testTextNode(self, caplog):
        sample   = os.path.join(self.misc_path, "testTextNode.html")
        expected = ['nodeName: #text',
                    'nodeType: 3',
                    'Object: [object Text]',
                    'nodeValue: Hello World',
                    'Length: 11',
                    'Substring(2,5): llo W',
                    'New nodeValue (replace): HelloAWorld',
                    'New nodeValue (delete 1): HelloWorld',
                    'Index error (delete 2)',
                    'New nodeValue (delete 3): Hello',
                    'New nodeValue (append): Hello Test',
                    'Index error (insert 1)',
                    'New nodeValue (insert 2): Hello New Test',
                    'New nodeValue (reset): Reset']

        self.do_perform_test(caplog, sample, expected)

    def test_testCommentNode(self, caplog):
        sample   = os.path.join(self.misc_path, "testCommentNode.html")
        expected = ['nodeName: #comment',
                    'nodeType: 8',
                    'Object: [object Comment]',
                    'nodeValue: <!--Hello World-->',
                    'Length: 18',
                    'Substring(2,5): --Hel',
                    'New nodeValue (replace): <!--HAllo World-->',
                    'New nodeValue (delete 1): <!--Hllo World-->',
                    'Index error (delete 2)',
                    'New nodeValue (delete 3): <!--H',
                    'New nodeValue (append): <!--H Test',
                    'Index error (insert 1)',
                    'New nodeValue (insert 2): <!--H New Test',
                    'New nodeValue (reset): Reset']

        self.do_perform_test(caplog, sample, expected)

    def test_testDOMImplementation(self, caplog):
        sample   = os.path.join(self.misc_path, "testDOMImplementation.html")
        expected = ["hasFeature('core'): true", ]

        self.do_perform_test(caplog, sample, expected)

    def test_testAttrNode(self, caplog):
        sample   = os.path.join(self.misc_path, "testAttrNode.html")
        expected = ['Object: [object Attr]',
                    'nodeName: test',
                    'nodeType: 2',
                    'nodeValue: foo',
                    'Length: undefined',
                    'New nodeValue: test2',
                    'Parent: null',
                    'Owner: null',
                    'Name: test',
                    'Specified: true',
                    'childNodes length: 0']

        self.do_perform_test(caplog, sample, expected)

    def test_testReplaceChild(self, caplog):
        sample   = os.path.join(self.misc_path, "testReplaceChild.html")
        expected = ['firstChild: Old child',
                    'lastChild: Old child',
                    'innerText: Old child',
                    '[ERROR] Attempting to replace with a null element',
                    '[ERROR] Attempting to replace a null element',
                    '[ERROR] Attempting to replace with an invalid element',
                    '[ERROR] Attempting to replace an invalid element',
                    '[ERROR] Attempting to replace on a read-only element failed',
                    'Alert Text: New child',
                    '<div id="foobar"><!--Just a comment--></div>']

        self.do_perform_test(caplog, sample, expected)

    def test_testCookie(self, caplog):
        sample   = os.path.join(self.misc_path, "testCookie.html")
        expected = ["Alert Text: favorite_food=tripe; name=oeschger", ]

        self.do_perform_test(caplog, sample, expected)

    def test_testDocumentFragment1(self, caplog):
        sample   = os.path.join(self.misc_path, "testDocumentFragment1.html")
        expected = ["<div><p>Test</p></div>", ]

        self.do_perform_test(caplog, sample, expected)

    def test_testDocumentFragment2(self, caplog):
        sample   = os.path.join(self.misc_path, "testDocumentFragment2.html")
        expected = ["<div id=\"foobar\"><b>This is B</b></div>", ]

        self.do_perform_test(caplog, sample, expected)

    def test_testDocumentFragment3(self, caplog):
        sample   = os.path.join(self.misc_path, "testDocumentFragment3.html")
        expected = ["foo:bar", ]

        self.do_perform_test(caplog, sample, expected)

    def test_testClassList1(self, caplog):
        sample   = os.path.join(self.misc_path, "testClassList1.html")
        expected = ['[Initial value] <div class="foo"></div>',
                    '[After remove and add] <div class="anotherclass"></div>',
                    '[Item] anotherclass',
                    '[Empty item] null',
                    '[Toggle visible] true',
                    '[After toggle] <div class="anotherclass"></div>']

        self.do_perform_test(caplog, sample, expected)

    def test_testClassList4(self, caplog):
        sample   = os.path.join(self.misc_path, "testClassList4.html")
        expected = ['[After remove and add] <div class="anotherclass"></div>', ]

        self.do_perform_test(caplog, sample, expected)

    def test_testDocumentType(self, caplog):
        sample   = os.path.join(self.misc_path, "testDocumentType.html")
        expected = ['Doctype: [object DocumentType]',
                    'Doctype name: html',
                    'Doctype nodeName: html',
                    'Doctype nodeType: 10',
                    'Doctype nodeValue: null',
                    'Doctype publicId: ',
                    'Doctype systemId: ',
                    'Doctype textContent: null']

        self.do_perform_test(caplog, sample, expected)

    def test_testRemoveChild(self, caplog):
        sample   = os.path.join(self.misc_path, "testRemoveChild.html")
        expected = ['<div>Don\'t care about me</div>',
                    '[ERROR] Attempting to remove null element',
                    '[ERROR] Attempting to remove an invalid element',
                    '[ERROR] Attempting to remove a read-only element',
                    '[ERROR] Attempting to remove an element not in the tree',
                    '[ERROR] Attempting to remove from a read-only element']

        self.do_perform_test(caplog, sample, expected)

    def test_testNamedNodeMap(self, caplog):
        sample   = os.path.join(self.misc_path, "testNamedNodeMap.html")
        expected = ['hasAttributes (before removal): true',
                    'hasAttribute(\'id\'): true',
                    'First test: id->p1',
                    'Second test: id->p1',
                    'Third test: id->p1',
                    'Fourth test: id->p1',
                    'Fifth test failed',
                    'Not existing: null',
                    'hasAttributes (after removal): false',
                    'Sixth test: foo->bar',
                    'Seventh test: foo->bar2',
                    'Final attributes length: 1']

        self.do_perform_test(caplog, sample, expected)

    def test_testEntityReference(self, caplog):
        sample   = os.path.join(self.misc_path, "testEntityReference.html")
        expected = ['node: [object EntityReference]',
                    'name: &',
                    'nodeName: &',
                    'nodeType: 5',
                    'nodeValue: null']

        self.do_perform_test(caplog, sample, expected)

    def test_getElementsByTagName(self, caplog):
        sample   = os.path.join(self.misc_path, "testGetElementsByTagName.html")
        expected = ['[object HTMLHtmlElement]',
                    '[object HTMLHeadElement]',
                    '[object HTMLBodyElement]',
                    '[object HTMLParagraphElement]',
                    '[object HTMLScriptElement]']

        self.do_perform_test(caplog, sample, expected)

    def test_testDocumentElement(self, caplog):
        sample   = os.path.join(self.misc_path, "testDocumentElement.html")
        expected = ['<a href="http://www.google.com">Google</a>']

        self.do_perform_test(caplog, sample, expected)

    def test_testSetAttribute1(self, caplog):
        sample   = os.path.join(self.misc_path, "testSetAttribute1.html")
        expected = ['Attribute: bar',
                    'Attribute (after removal): null']

        self.do_perform_test(caplog, sample, expected)

    def test_testSetAttribute3(self, caplog):
        sample   = os.path.join(self.misc_path, "testSetAttribute3.html")
        expected = ['Alert Text: foo',
                    'Alert Text: bar',
                    'Alert Text: test',
                    'Alert Text: foobar']

        self.do_perform_test(caplog, sample, expected)

    def test_testCDATASection(self, caplog):
        sample   = os.path.join(self.misc_path, "testCDATASection.html")
        expected = ['nodeName: #cdata-section',
                    'nodeType: 4',
                    '<xml>&lt;![CDATA[Some &lt;CDATA&gt; data &amp; then some]]&gt;</xml>']

        self.do_perform_test(caplog, sample, expected)

    def test_testHTMLCollection(self, caplog):
        sample   = os.path.join(self.misc_path, "testHTMLCollection.html")
        expected = ['<div id="odiv1">Page one</div>',
                    '<div name="odiv2">Page two</div>']

        self.do_perform_test(caplog, sample, expected)

    def test_testApplyElement(self, caplog):
        sample   = os.path.join(self.misc_path, "testApplyElement.html")
        expected = ['<div id="outer"><div id="test"><div>Just a sample</div></div></div>',
                    '<div id="outer"><div>Just a div<div id="test"><div>Just a sample</div></div></div></div>']

        self.do_perform_test(caplog, sample, expected)

    def test_testProcessingInstruction(self, caplog):
        sample   = os.path.join(self.misc_path, "testProcessingInstruction.html")
        expected = ['[object ProcessingInstruction]',
                    'nodeName: xml-stylesheet',
                    'nodeType: 7',
                    'nodeValue: href="mycss.css" type="text/css"',
                    'target: xml-stylesheet']

        self.do_perform_test(caplog, sample, expected)

    def test_testWindow(self, caplog):
        sample   = os.path.join(self.misc_path, "testWindow.html")
        expected = ['window: [object Window]',
                    'self: [object Window]',
                    'top: [object Window]',
                    'length: 0',
                    'history: [object History]',
                    'pageXOffset: 0',
                    'pageYOffset: 0',
                    'screen: [object Screen]',
                    'screenLeft: 0',
                    'screenX: 0',
                    'confirm: true']

        self.do_perform_test(caplog, sample, expected)

    def test_testObject1(self, caplog):
        sample   = os.path.join(self.misc_path, "testObject1.html")
        expected = ['[object data redirection] about:blank -> https://github.com/buffer/thug/raw/master/tests/test_files/sample.swf']

        self.do_perform_test(caplog, sample, expected)

    def test_testReplaceChild2(self, caplog):
        sample   = os.path.join(self.misc_path, "testReplaceChild2.html")
        expected = ['<div id="foobar"><div id="test"></div></div>']

        self.do_perform_test(caplog, sample, expected)

    def test_testNavigator(self, caplog):
        sample   = os.path.join(self.misc_path, "testNavigator.html")
        expected = ['window: [object Window]',
                    'appCodeName: Mozilla',
                    'appName: Microsoft Internet Explorer',
                    'appVersion: 5.0 (compatible; MSIE 10.0; Windows NT 6.1; Trident/6.0; rv: 10.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E)',
                    'cookieEnabled: true',
                    'onLine: true',
                    'platform: Win32']

        self.do_perform_test(caplog, sample, expected)

    def test_testAdodbStream(self, caplog):
        sample   = os.path.join(self.misc_path, "testAdodbStream.html")
        expected = ['[Microsoft MDAC RDS.Dataspace ActiveX] CreateObject (Adodb.Stream)',
                    '[Window] Alert Text: Stream content: Test',
                    '[Window] Alert Text: Stream content (first 2 chars): Te',
                    '[Window] Alert Text: Stream size: 4',
                    '[Adodb.Stream ActiveX] SaveToFile(test.txt, 2)',
                    '[Adodb.Stream ActiveX] LoadFromFile(test1234.txt)',
                    '[Window] Alert Text: Attempting to load from a not existing file',
                    '[Adodb.Stream ActiveX] LoadFromFile(test.txt)',
                    '[Window] Alert Text: ReadText: Test',
                    '[Window] Alert Text: ReadText(3): Tes',
                    '[Window] Alert Text: ReadText(10): Test',
                    '[Adodb.Stream ActiveX] Changed position in fileobject to: (2)',
                    '[Window] Alert Text: stTest2',
                    '[Adodb.Stream ActiveX] Close']

        self.do_perform_test(caplog, sample, expected)

    def test_testScriptingFileSystemObject(self, caplog):
        sample   = os.path.join(self.misc_path, "testScriptingFileSystemObject.html")
        expected = ['[Microsoft MDAC RDS.Dataspace ActiveX] CreateObject (Scripting.FileSystemObject)',
                    '[Script.FileSystemObject ActiveX] Returning C:\\WINDOWS for GetSpecialFolder("0")',
                    '[Script.FileSystemObject ActiveX] Returning C:\\WINDOWS\\system32 for GetSpecialFolder("1")',
                    '[WScript.Shell ActiveX] Expanding environment string "%TEMP%"',
                    '[Window] Alert Text: FolderExists(\'C:\\Windows\\System32\'): true',
                    '[Window] Alert Text: FileExists(\'\'): true',
                    '[Window] Alert Text: FileExists(\'C:\\Windows\\System32\\drivers\\etc\\hosts\'): true',
                    '[Window] Alert Text: FileExists(\'C:\\Windows\\System32\\test.txt\'): true',
                    '[Window] Alert Text: GetExtensionName("C:\\Windows\\System32\\test.txt"): .txt',
                    '[Window] Alert Text: FileExists(\'C:\\Windows\\System32\\test.txt\'): true',
                    '[Window] Alert Text: [After CopyFile] FileExists(\'C:\\Windows\\System32\\test2.txt\'): true',
                    '[Window] Alert Text: [After MoveFile] FileExists(\'C:\\Windows\\System32\\test2.txt\'): false',
                    '[Window] Alert Text: [After MoveFile] FileExists(\'C:\\Windows\\System32\\test3.txt\'): true']

        self.do_perform_test(caplog, sample, expected)

    def test_testHTMLOptionsCollection(self, caplog):
        sample   = os.path.join(self.misc_path, "testHTMLOptionsCollection.html")
        expected = ['length: 4',
                    'item(0): Volvo',
                    'namedItem(\'audi\'): Audi',
                    'namedItem(\'mercedes\').value: mercedes',
                    '[After remove] item(0): Saab',
                    '[After first add] length: 4',
                    '[After first add] item(3): foobar',
                    '[After second add] length: 5',
                    '[After second add] item(3): test1234',
                    'Not found error']

        self.do_perform_test(caplog, sample, expected)

    def test_testTextStream(self, caplog):
        sample   = os.path.join(self.misc_path, "testTextStream.html")
        expected = ['[Microsoft MDAC RDS.Dataspace ActiveX] CreateObject (Scripting.FileSystemObject)',
                    '[Script.FileSystemObject ActiveX] CreateTextFile("test.txt", "False", "False")',
                    '[After first write] ReadAll: foobar',
                    '[After first write] Line: 1',
                    '[After first write] Column: 7',
                    '[After first write] AtEndOfLine: true',
                    '[After first write] AtEndOfStream: true',
                    '[After second write] Line: 2',
                    '[After second write] Column: 1',
                    '[After second write] AtEndOfLine: false',
                    '[After second write] AtEndOfStream: false',
                    '[After third write] Line: 5',
                    '[After third write] Column: 16',
                    '[After third write] AtEndOfLine: false',
                    '[After third write] AtEndOfStream: false',
                    '[After fourth write] Line: 6',
                    '[After fourth write] Column: 1',
                    '[After fourth write] AtEndOfLine: false',
                    '[After fourth write] AtEndOfStream: false',
                    '[After fourth write] First char: s',
                    '[After fourth write] Second char: o',
                    '[After fourth write] Third char: m',
                    '[After fourth write] Line: some other textnext line',
                    '[After skip] Read(5): ttest']

        self.do_perform_test(caplog, sample, expected)

    def test_testHTMLAnchorElement(self, caplog):
        sample   = os.path.join(self.misc_path, "testHTMLAnchorElement.html")
        expected = ['a.protocol: https:',
                    'a.host: www.example.com:1234',
                    'a.hostname: www.example.com',
                    'a.port: 1234',
                    'b.protocol: :',
                    'b.host: ',
                    'b.hostname: ',
                    'b.port: ',
                    'c.protocol: https:',
                    'c.host: www.example.com',
                    'c.hostname: www.example.com',
                    'c.port: ']

        self.do_perform_test(caplog, sample, expected)

    def test_testHTMLTableElement3(self, caplog):
        sample   = os.path.join(self.misc_path, "testHTMLTableElement3.html")
        expected = ['tHead: [object HTMLTableSectionElement]',
                    'tFoot: [object HTMLTableSectionElement]',
                    'caption: [object HTMLTableCaptionElement]',
                    'row: [object HTMLTableRowElement]',
                    'tBodies: [object HTMLCollection]',
                    'cell: [object HTMLTableCellElement]',
                    'cell.innerHTML: New cell 1',
                    'row.deleteCell(10) failed',
                    'row.deleteCell(20) failed']

        self.do_perform_test(caplog, sample, expected)

    def test_testTextArea(self, caplog):
        sample   = os.path.join(self.misc_path, "testTextArea.html")
        expected = ['type: textarea',
                    'cols: 100',
                    'rows: 25']

        self.do_perform_test(caplog, sample, expected)

    def test_testHTMLDocument(self, caplog):
        sample   = os.path.join(self.misc_path, "testHTMLDocument.html")
        expected = ['document.title: Test',
                    'document.title: Foobar',
                    'anchors: [object HTMLCollection]',
                    'anchors length: 1',
                    'anchors[0].name: foobar',
                    'applets: [object HTMLCollection]',
                    'applets length: 2',
                    'applets[0].code: HelloWorld.class',
                    'links: [object HTMLCollection]',
                    'links length: 1',
                    'links[0].href: https://github.com/buffer/thug/',
                    'images: [object HTMLCollection]',
                    'images length: 1',
                    'images[0].href: test.jpg',
                    'disabled: false',
                    'head: [object HTMLHeadElement]',
                    'referrer: ',
                    'URL: about:blank',
                    'Alert Text: Hello, world']

        self.do_perform_test(caplog, sample, expected)

    def test_testHTMLFormElement(self, caplog):
        sample   = os.path.join(self.misc_path, "testHTMLFormElement.html")
        expected = ['[object HTMLFormElement]',
                    'f.elements: [object HTMLFormControlsCollection]',
                    'f.length: 4',
                    'f.name: [object HTMLFormControlsCollection]',
                    'f.acceptCharset: ',
                    'f.action: /cgi-bin/test',
                    'f.enctype: application/x-www-form-urlencoded',
                    'f.encoding: application/x-www-form-urlencoded',
                    'f.method: POST',
                    'f.target: ']

        self.do_perform_test(caplog, sample, expected)

    def test_testFile(self, caplog):
        sample   = os.path.join(self.misc_path, "testFile.html")
        expected = ['[Microsoft MDAC RDS.Dataspace ActiveX] CreateObject (Scripting.FileSystemObject)',
                    '[Script.FileSystemObject ActiveX] GetFile("D:\\ Program Files\\ Common Files\\test.txt")',
                    '[File ActiveX] Path = D:\\ Program Files\\ Common Files\\test.txt, Attributes = 32',
                    'Drive (test.txt): D:',
                    'ShortPath (test.txt): D:\\\\ Progr~1\\\\ Commo~1\\\\test.txt',
                    'ShortName (test.txt): test.txt',
                    'Attributes: 1',
                    '[Script.FileSystemObject ActiveX] GetFile("test2.txt")',
                    '[File ActiveX] Path = test2.txt, Attributes = 32',
                    'Drive (test2.txt): C:',
                    'ShortPath (test2.txt): test2.txt',
                    'ShortName (test2.txt): test2.txt',
                    'Copy(test3.txt, True)',
                    'Move(test4.txt)',
                    'Delete(False)',
                    'OpenAsTextStream(ForReading, 0)']

        self.do_perform_test(caplog, sample, expected)

    def test_testWScriptNetwork(self, caplog):
        sample   = os.path.join(self.misc_path, "testWScriptNetwork.html")
        expected = ['[WScript.Network ActiveX] Got request to PrinterConnections',
                    '[WScript.Network ActiveX] Got request to EnumNetworkDrives',
                    '[WScript.Shell ActiveX] Expanding environment string "%USERDOMAIN%"',
                    '[WScript.Shell ActiveX] Expanding environment string "%USERNAME%"',
                    '[WScript.Shell ActiveX] Expanding environment string "%COMPUTERNAME%"']

        self.do_perform_test(caplog, sample, expected)

    def test_testApplet(self, caplog):
        sample   = os.path.join(self.misc_path, "testApplet.html")
        expected = ['[applet redirection]']

        self.do_perform_test(caplog, sample, expected)

    def test_testHTMLImageElement(self, caplog):
        sample   = os.path.join(self.misc_path, "testHTMLImageElement.html")
        expected = ['src (before changes): test.jpg',
                    'src (after first change): test2.jpg',
                    'onerror handler fired']

        self.do_perform_test(caplog, sample, expected)

    def test_testTitle(self, caplog):
        sample   = os.path.join(self.misc_path, "testTitle.html")
        expected = ['New title: Foobar']

        self.do_perform_test(caplog, sample, expected)

    def test_testCSSStyleDeclaration(self, caplog):
        sample   = os.path.join(self.misc_path, "testCSSStyleDeclaration.html")
        expected = ['style: [object CSSStyleDeclaration]',
                    'length: 1',
                    'cssText: color: blue;',
                    'color: blue',
                    'item(0): color',
                    'item(100):',
                    'getPropertyValue(\'color\'): blue',
                    'length (after removeProperty): 0',
                    'cssText: foo: bar;']

        self.do_perform_test(caplog, sample, expected)

    def test_testFormProperty(self, caplog):
        sample   = os.path.join(self.misc_path, "testFormProperty.html")
        expected = ['[object HTMLFormElement]',
                    'formA']

        self.do_perform_test(caplog, sample, expected)

    def test_testVBScript(self, caplog):
        sample   = os.path.join(self.misc_path, "testVBScript.html")
        expected = ['[VBS embedded URL redirection]',
                    'http://192.168.1.100/putty.exe']

        self.do_perform_test(caplog, sample, expected)

    def test_testFontFaceRule1(self, caplog):
        sample   = os.path.join(self.misc_path, "testFontFaceRule1.html")
        expected = ['[font face redirection]',
                    'http://192.168.1.100/putty.exe']

        self.do_perform_test(caplog, sample, expected)

    def test_testFontFaceRule2(self, caplog):
        sample   = os.path.join(self.misc_path, "testFontFaceRule2.html")
        expected = ['[font face redirection]',
                    'https://mdn.mozillademos.org/files/2468/VeraSeBd.ttf']

        self.do_perform_test(caplog, sample, expected)

    def test_testSilverLight(self, caplog):
        sample   = os.path.join(self.misc_path, "testSilverLight.html")
        expected = ['[SilverLight] isVersionSupported(\'4.0\')',
                    'Version 4.0 supported: true']

        self.do_perform_test(caplog, sample, expected)

    def test_testMSXML2Document(self, caplog):
        sample   = os.path.join(self.misc_path, "testMSXML2Document.html")
        expected = ['[MSXML2.DOMDocument] Microsoft XML Core Services MSXML Uninitialized Memory Corruption',
                    'CVE-2012-1889']

        self.do_perform_test(caplog, sample, expected)
