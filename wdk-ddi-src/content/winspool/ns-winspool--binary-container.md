---
UID: NS.winspool._BINARY_CONTAINER
title: BINARY_CONTAINER
author: windows-driver-content
description: The BINARY_CONTAINER structure is a container for binary data.
old-location: print\binary_container.htm
old-project: print
ms.assetid: bac960c5-7c29-4550-9b82-5adb6a0cc243
ms.author: windowsdriverdev
ms.date: 11/24/2017
ms.keywords: BINARY_CONTAINER, BINARY_CONTAINER, *PBINARY_CONTAINER
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: winspool.h
req.include-header: Winspool.h
req.target-type: Windows
req.target-min-winverclnt: This structure is available in Windows XP and later operating systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: BINARY_CONTAINER
req.alt-loc: winspool.h
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

# BINARY_CONTAINER structure



## -description
<p>The BINARY_CONTAINER structure is a container for binary data.</p>


## -syntax

````
typedef struct _BINARY_CONTAINER {
  DWORD  cbBuf;
  LPBYTE pData;
} BINARY_CONTAINER, *PBINARY_CONTAINER;
````


## -struct-fields
<dl>

### -field <b>cbBuf</b>

<dd>
<p>Specifies the number of bytes of binary data in the <b>pData</b> member.</p>
</dd>

### -field <b>pData</b>

<dd>
<p>Pointer to a buffer that contains the binary data.</p>
</dd>
</dl>

## -remarks
<p>The BINARY_CONTAINER structure is used in a <a href="..\winspool\ns-winspool--bidi-data.md">BIDI_DATA</a> structure when the bidi data consists of binary data, as opposed to integer, float, or string data.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>This structure is available in Windows XP and later operating systems.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Winspool.h (include Winspool.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\winspool\ns-winspool--bidi-data.md">BIDI_DATA</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [print\print]:%20BINARY_CONTAINER structure%20 RELEASE:%20(11/24/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
