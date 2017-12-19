---
UID: NF.wiautil.wiauDbgDump
title: wiauDbgDump function
author: windows-driver-content
description: The wiauDbgDump function logs a message containing one or more data values.
old-location: image\wiaudbgdump.htm
old-project: Image
ms.assetid: 5df074ff-572d-47f7-9c5c-4423b200cddc
ms.author: windowsdriverdev
ms.date: 12/14/2017
ms.keywords: wiauDbgDump
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
req.alt-api: wiauDbgDump
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

# wiauDbgDump function



## -description
The <b>wiauDbgDump</b> function logs a message containing one or more data values.



## -syntax

````
inline void __stdcall wiauDbgDump(
   LPCSTR   fname,
   LPCSTR   fmt, ...
);
````


## -parameters

### -param fname 

Pointer to a string containing the name of the function or method into which the call to <b>wiauDbgDump</b> is inserted.


### -param fmt, ... 

Pointer to a format string that specifies a variable argument list, which starts with an ANSI format string containing the message and any conversion specifiers. The ellipsis (...) specifies a variable number of arguments that are to be output. 


## -returns
None


## -remarks
The <b>wiauDbgDump</b> function typically is used to log a message along with one or more data values, as in the following example:

This example, which would be placed in a function named <i>SetBuffer</i>, causes the function name and a string describing the size of a buffer to be logged. 


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
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [Image\image]:%20wiauDbgDump function%20 RELEASE:%20(12/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>

