---
UID: NF.wiautil.wiauDbgHelper2
title: wiauDbgHelper2
author: windows-driver-content
description: The wiauDbgHelper2 function writes a message to a log file, or debugger, or both.
old-location: image\wiaudbghelper2.htm
ms.assetid: 577ce93a-5a90-4e85-afc6-3791f402c238
ms.author: windowsdriverdev
ms.date: 10/24/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: image
req.header: wiautil.h
req.include-header: Wiautil.h
req.target-type: Desktop
req.target-min-winverclnt: Available in Windows XP and later.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: wiauDbgHelper2
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
ms.keywords: wiauDbgHelper2
req.iface: 
req.product: Windows 10 or later.
---

# wiauDbgHelper2 function



## -description
<p>The <b>wiauDbgHelper2</b> function writes a message to a log file, or debugger, or both. </p>


## -syntax

````
void __stdcall wiauDbgHelper2(
   LPCSTR   prefix,
   LPCSTR   fname,
   LPCSTR   fmt, ...
);
````


## -parameters
<dl>

### -param <i>prefix</i> 

<dd>
<p>Pointer to a string containing a prefix (such as "ERROR " or "WARN ") associated with the message. </p>
</dd>

### -param <i>fname</i> 

<dd>
<p>Pointer to a string containing the name of the function or method into which the call to <b>wiauDbgHelper2</b> is inserted.</p>
</dd>

### -param <i>fmt, ...</i> 

<dd>
<p>Pointer to a format string that specifies a variable argument list, which starts with an ANSI format string containing the message and any conversion specifiers. The ellipsis (...) specifies a variable number of arguments that are to be output. The text should be prefixed with the full name of the method or function generating the message in the format of "class::method, message-text". </p>
</dd>
</dl>

## -returns
<p>None</p>

## -remarks
<p>The <b>wiauDbgHelper2</b> function enables those using it to write <b>printf</b>-style messages, with variable argument lists, to a log file or debugger. The following example demonstrates how this function might be used:</p>

<p>The <b>wiauDbgHelper2</b> function enables those using it to write <b>printf</b>-style messages, with variable argument lists, to a log file or debugger. The following example demonstrates how this function might be used:</p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff549627">wiauDbgDump</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff549633">wiauDbgError</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff549637">wiauDbgErrorHr</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff550161">wiauDbgTrace</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff550163">wiauDbgWarning</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff549649">wiauDbgHelper</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [image\image]:%20wiauDbgHelper2 function%20 RELEASE:%20(10/24/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
