---
UID: NF.winsplp.RouterAllocBidiResponseContainer
title: RouterAllocBidiResponseContainer function
author: windows-driver-content
description: RouterAllocBidiResponseContainer allocates a BIDI_RESPONSE_CONTAINER structure containing a list of bidi responses. The bidi response list is an array of BIDI_RESPONSE_DATA structures.
old-location: print\routerallocbidiresponsecontainer.htm
old-project: print
ms.assetid: ca10f0d5-62d6-451a-96e5-38aca18cf5b0
ms.author: windowsdriverdev
ms.date: 12/9/2017
ms.keywords: RouterAllocBidiResponseContainer
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: winsplp.h
req.include-header: Winsplp.h
req.target-type: Desktop
req.target-min-winverclnt: This function is available in Windows XP and later operating systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: RouterAllocBidiResponseContainer
req.alt-loc: Spoolss.dll
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Spoolss.lib
req.dll: Spoolss.dll
req.irql: 
req.product: Windows 10 or later.
---

# RouterAllocBidiResponseContainer function



## -description
<code>RouterAllocBidiResponseContainer</code> allocates a <a href="print.bidi_response_container">BIDI_RESPONSE_CONTAINER</a> structure containing a list of bidi responses. The bidi response list is an array of <a href="print.bidi_response_data">BIDI_RESPONSE_DATA</a> structures.



## -syntax

````
PBIDI_RESPONSE_CONTAINER RouterAllocBidiResponseContainer(
  _In_ DWORD cSize
);
````


## -parameters

### -param cSize [in]

Specifies the number of BIDI_RESPONSE_DATA structures to be allocated.


## -returns
<code>RouterAllocBidiResponseContainer</code> returns a pointer to the allocated structure, on success. If the function fails to allocate the structure, the caller can obtain the error code from <b>GetLastError</b> (described in the Microsoft Windows SDK documentation).


## -remarks
When the memory allocated by this function is no longer needed, use <a href="print.routerfreebidiresponsecontainer">RouterFreeBidiResponseContainer</a>.


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
This function is available in Windows XP and later operating systems.

</td>
</tr>
<tr>
<th width="30%">
Header

</th>
<td width="70%">
<dl>
<dt>Winsplp.h (include Winsplp.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
Library

</th>
<td width="70%">
<dl>
<dt>Spoolss.lib</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
DLL

</th>
<td width="70%">
<dl>
<dt>Spoolss.dll</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="print.bidi_response_data">BIDI_RESPONSE_DATA</a>
</dt>
<dt>
<a href="print.bidi_response_container">BIDI_RESPONSE_CONTAINER</a>
</dt>
<dt>
<a href="print.routerfreebidiresponsecontainer">RouterFreeBidiResponseContainer</a>
</dt>
<dt>
<a href="print.sendrecvbididatafromport">SendRecvBidiDataFromPort</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [print\print]:%20RouterAllocBidiResponseContainer function%20 RELEASE:%20(12/9/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>

