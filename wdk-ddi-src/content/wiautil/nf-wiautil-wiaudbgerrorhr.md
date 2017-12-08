---
UID: NF.wiautil.wiauDbgErrorHr
title: wiauDbgErrorHr function
author: windows-driver-content
description: The wiauDbgErrorHr function logs a message containing an HRESULT and its error message string.
old-location: image\wiaudbgerrorhr.htm
old-project: image
ms.assetid: 18d248d9-d447-4d3e-9eaa-f6befb4bef58
ms.author: windowsdriverdev
ms.date: 12/6/2017
ms.keywords: wiauDbgErrorHr
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: wiautil.h
req.include-header: Wiautil.h
req.target-type: Desktop
req.target-min-winverclnt: Available in Windows XP and later.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: wiauDbgErrorHr
req.alt-loc: Wiautil.h
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
req.product: Windows 10 or later.
---

# wiauDbgErrorHr function



## -description
The <b>wiauDbgErrorHr</b> function logs a message containing an HRESULT and its error message string.


## -syntax

````
inline void __stdcall wiauDbgErrorHr(
   HRESULT  hr,
   LPCSTR   fname,
   LPCSTR   fmt, ...
);
````


## -parameters

### -param hr 

Specifies the HRESULT that is to be logged.

### -param fname 

Pointer to a string containing the name of the function or method into which the call to <b>wiauDbgDump</b> is inserted.

### -param fmt, ... 

Pointer to a format string that specifies a variable argument list, which starts with an ANSI format string containing the message and any conversion specifiers. The ellipsis (...) specifies a variable number of arguments that are to be output. 

## -returns
None

## -remarks
The <b>wiauDbgErrorHr</b> function typically logs two lines to the log file, or debugger, or both. The first line contains the text of the <i>fmt</i> parameter, including data, if provided. The second line contains the HRESULT and the message string associated with that HRESULT. The following example shows how this function might be called:

## -requirements
<table>
<tr>
<th width="30%">
Target platform
</th>
<td width="70%">
<dl>
<dt>Desktop</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
Version
</th>
<td width="70%">
Available in Windows XP and later.
</td>
</tr>
<tr>
<th width="30%">
Header
</th>
<td width="70%">
<dl>
<dt>Wiautil.h (include Wiautil.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="image.wiaudbgdump">wiauDbgDump</a>
</dt>
<dt>
<a href="image.wiaudbgerror">wiauDbgError</a>
</dt>
<dt>
<a href="image.wiaudbgtrace">wiauDbgTrace</a>
</dt>
<dt>
<a href="image.wiaudbgwarning">wiauDbgWarning</a>
</dt>
</dl>
 
 
<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [image\image]:%20wiauDbgErrorHr function%20 RELEASE:%20(12/6/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>
