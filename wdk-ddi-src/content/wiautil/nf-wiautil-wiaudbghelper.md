---
UID: NF.wiautil.wiauDbgHelper
title: wiauDbgHelper
author: windows-driver-content
description: The wiauDbgHelper function formats a message and writes it to a log file, or debugger, or both.
old-location: image\wiaudbghelper.htm
ms.assetid: 5be1ede7-13a0-4ef4-93bd-8a1adc5baa9e
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
req.alt-api: wiauDbgHelper
req.alt-loc: wiautil.h
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
ms.keywords: wiauDbgHelper
req.iface: 
req.product: Windows 10 or later.
---

# wiauDbgHelper function



## -description
<p>The <b>wiauDbgHelper</b> function formats a message and writes it to a log file, or debugger, or both.</p>


## -syntax

````
void __stdcall wiauDbgHelper(
  _In_ LPCSTR  prefix,
  _In_ LPCSTR  fname,
  _In_ LPCSTR  fmt,
       va_list marker
);
````


## -parameters
<dl>

### -param <i>prefix</i> [in]

<dd>
<p>Pointer to a string containing a prefix (such as "ERROR " or "WARN ") associated with the message. </p>
</dd>

### -param <i>fname</i> [in]

<dd>
<p>Pointer to a string containing the name of the function or method into which the call to <b>wiauDbgHelper</b> is inserted.</p>
</dd>

### -param <i>fmt</i> [in]

<dd>
<p>Pointer to a string that controls how an item or items in a variable argument list is to be formatted.</p>
</dd>

### -param <i>marker</i> 

<dd>
<p>Marks the beginning of a variable argument list.</p>
</dd>
</dl>

## -returns
<p>None</p>

## -remarks
<p>The <b>wiauDbgHelper</b> function is a general-purpose function that is used internally by many of the other <b>wiauDbg</b><b><i>Xxx</i></b> functions. While it can be used in WIA minidrivers, there are other limited-purpose functions provided that are more convenient to use.</p>

<p>The <b>wiauDbgHelper</b> function is a general-purpose function that is used internally by many of the other <b>wiauDbg</b><b><i>Xxx</i></b> functions. While it can be used in WIA minidrivers, there are other limited-purpose functions provided that are more convenient to use.</p>

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
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [image\image]:%20wiauDbgHelper function%20 RELEASE:%20(10/24/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
