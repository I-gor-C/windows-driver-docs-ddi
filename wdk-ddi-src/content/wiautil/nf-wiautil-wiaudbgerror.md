---
UID: NF.wiautil.wiauDbgError
title: wiauDbgError
author: windows-driver-content
description: The wiauDbgError function logs an error message.
old-location: image\wiaudbgerror.htm
ms.assetid: 112d6f90-33b3-446b-943c-8995e6ec3378
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
req.alt-api: wiauDbgError
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
ms.keywords: wiauDbgError
req.iface: 
req.product: Windows 10 or later.
---

# wiauDbgError function



## -description
<p>The <b>wiauDbgError</b> function logs an error message.</p>


## -syntax

````
inline void __stdcall wiauDbgError(
   LPCSTR   fname,
   LPCSTR   fmt, ...
);
````


## -parameters
<dl>

### -param <i>fname</i> 

<dd>
<p>Pointer to a string containing the name of the function or method into which the call to <b>wiauDbgDump</b> is inserted.</p>
</dd>

### -param <i>fmt, ...</i> 

<dd>
<p>Pointer to a format string that specifies a variable argument list, which starts with an ANSI format string containing the message and any conversion specifiers. The ellipsis (...) specifies a variable number of arguments that are to be output. </p>
</dd>
</dl>

## -returns
<p>None</p>

## -remarks
<p>The <b>wiauDbgError</b> typically is used to display an error message with no data, such as in the following example:</p>

<p>The <b>wiauDbgError</b> typically is used to display an error message with no data, such as in the following example:</p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff549637">wiauDbgErrorHr</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff550161">wiauDbgTrace</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff550163">wiauDbgWarning</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [image\image]:%20wiauDbgError function%20 RELEASE:%20(10/24/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
