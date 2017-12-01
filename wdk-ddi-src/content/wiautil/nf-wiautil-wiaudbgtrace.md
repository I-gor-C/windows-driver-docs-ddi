---
UID: NF.wiautil.wiauDbgTrace
title: wiauDbgTrace
author: windows-driver-content
description: The wiauDbgTrace function logs a trace message.
old-location: image\wiaudbgtrace.htm
old-project: image
ms.assetid: c3cdb5c9-b43d-443b-8d04-d30eb74f39da
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: wiauDbgTrace
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
req.alt-api: wiauDbgTrace
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
req.iface: 
req.product: Windows 10 or later.
---

# wiauDbgTrace function



## -description
<p>The <b>wiauDbgTrace</b> function logs a trace message.</p>


## -syntax

````
inline void __stdcall wiauDbgTrace(
   LPCSTR   fname,
   LPCSTR   fmt, ...
);
````


## -parameters
<dl>

### -param <i>fname</i> 

<dd>
<p>Pointer to a string containing the name of the function or method into which the call to <b>wiauDbgTrace</b> is inserted.</p>
</dd>

### -param <i>fmt, ...</i> 

<dd>
<p>Pointer to a format string that specifies a variable argument list, which starts with an ANSI format string containing the trace message and any conversion specifiers. The ellipsis (...) specifies a variable number of arguments that are to be output.</p>
</dd>
</dl>

## -returns
<p>None</p>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Target platform</p>
</th>
<td width="70%">
<dl>
<dt>Desktop</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Available in Windows XP and later.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
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
<a href="..\wiautil\nf-wiautil-wiaudbgdump.md">wiauDbgDump</a>
</dt>
<dt>
<a href="..\wiautil\nf-wiautil-wiaudbgerror.md">wiauDbgError</a>
</dt>
<dt>
<a href="..\wiautil\nf-wiautil-wiaudbgerrorhr.md">wiauDbgErrorHr</a>
</dt>
<dt>
<a href="..\wiautil\nf-wiautil-wiaudbgwarning.md">wiauDbgWarning</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [image\image]:%20wiauDbgTrace function%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
