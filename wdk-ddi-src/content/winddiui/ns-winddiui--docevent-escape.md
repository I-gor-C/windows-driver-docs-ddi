---
UID: NS.winddiui._DOCEVENT_ESCAPE
title: DOCEVENT_ESCAPE
author: windows-driver-content
description: The DOCEVENT_ESCAPE structure is a container for values used as parameters for the ExtEscape function.
old-location: print\docevent_escape.htm
old-project: print
ms.assetid: 54ac7c45-63a1-4003-8250-524e6f9e8d06
ms.author: windowsdriverdev
ms.date: 11/24/2017
ms.keywords: DOCEVENT_ESCAPE, DOCEVENT_ESCAPE, *PDOCEVENT_ESCAPE
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: winddiui.h
req.include-header: Winddiui.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: DOCEVENT_ESCAPE
req.alt-loc: winddiui.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: 
req.iface: 
req.product: Windows 10 or later.
---

# DOCEVENT_ESCAPE structure



## -description
<p>The DOCEVENT_ESCAPE structure is a container for values used as parameters for the <b>ExtEscape</b> function.</p>


## -syntax

````
typedef struct _DOCEVENT_ESCAPE {
  int   iEscape;
  int   cjInput;
  PVOID pvInData;
} DOCEVENT_ESCAPE, *PDOCEVENT_ESCAPE;
````


## -struct-fields
<dl>

### -field <b>iEscape</b>

<dd>
<p>Specifies the value of the <b>ExtEscape</b> function's <i>nEscape</i> parameter.</p>
</dd>

### -field <b>cjInput</b>

<dd>
<p>Specifies the value of the <b>ExtEscape</b> function's <i>cbInput</i> parameter.</p>
</dd>

### -field <b>pvInData</b>

<dd>
<p>Specifies the value of the <b>ExtEscape</b> function's <i>lpszInData</i> parameter.</p>
</dd>
</dl>

## -remarks
<p>The DOCEVENT_ESCAPE structure is defined for Windows XP and later.</p>

<p>This structure is used in conjunction with a call to <a href="..\winddiui\nf-winddiui-drvdocumentevent.md">DrvDocumentEvent</a> or <a href="print.iprintoemui2_documentevent">IPrintOemUI2::DocumentEvent</a>, in which the <i>iEsc</i> parameter is set to DOCUMENTEVENT_ESCAPE. Before calling either of these functions, the caller must fill in the members of this structure.</p>

<p>Refer to the Microsoft Windows SDK documentation for a description of the <b>ExtEscape</b> function and the three parameters that correspond to the members of this structure. </p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Winddiui.h (include Winddiui.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\winddiui\nf-winddiui-drvdocumentevent.md">DrvDocumentEvent</a>
</dt>
<dt>
<a href="print.iprintoemui2_documentevent">IPrintOemUI2::DocumentEvent</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [print\print]:%20DOCEVENT_ESCAPE structure%20 RELEASE:%20(11/24/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
