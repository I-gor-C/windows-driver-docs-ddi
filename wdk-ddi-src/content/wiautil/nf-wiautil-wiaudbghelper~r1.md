---
UID: NF.wiautil.wiauDbgHelper~r1
title: wiauDbgHelper macro
author: windows-driver-content
description: The wiauDbgHelper function formats a message and writes it to a log file, or debugger, or both.
old-location: image\wiaudbghelper.htm
old-project: Image
ms.assetid: 5be1ede7-13a0-4ef4-93bd-8a1adc5baa9e
ms.author: windowsdriverdev
ms.date: 12/14/2017
ms.keywords: wiauDbgHelper
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: macro
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
req.product: Windows 10 or later.
---

# wiauDbgHelper macro



## -description
The <b>wiauDbgHelper</b> function formats a message and writes it to a log file, or debugger, or both.



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

### -param prefix [in]

Pointer to a string containing a prefix (such as "ERROR " or "WARN ") associated with the message. 


### -param fname [in]

Pointer to a string containing the name of the function or method into which the call to <b>wiauDbgHelper</b> is inserted.


### -param fmt [in]

Pointer to a string that controls how an item or items in a variable argument list is to be formatted.


### -param marker 

Marks the beginning of a variable argument list.


## -remarks
The <b>wiauDbgHelper</b> function is a general-purpose function that is used internally by many of the other <b>wiauDbg</b><b><i>Xxx</i></b> functions. While it can be used in WIA minidrivers, there are other limited-purpose functions provided that are more convenient to use.


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
<a href="image.wiaudbgerrorhr">wiauDbgErrorHr</a>
</dt>
<dt>
<a href="image.wiaudbgtrace">wiauDbgTrace</a>
</dt>
<dt>
<a href="image.wiaudbgwarning">wiauDbgWarning</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [Image\image]:%20wiauDbgHelper function%20 RELEASE:%20(12/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>

