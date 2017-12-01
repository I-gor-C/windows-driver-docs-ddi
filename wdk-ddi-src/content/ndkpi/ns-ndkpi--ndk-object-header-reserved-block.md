---
UID: NS.ndkpi._NDK_OBJECT_HEADER_RESERVED_BLOCK
title: NDK_OBJECT_HEADER_RESERVED_BLOCK
author: windows-driver-content
description: The NDK_OBJECT_HEADER_RESERVED_BLOCK structure specifies reserved information in an NDK object.
old-location: netvista\ndk_object_header_reserved_block.htm
old-project: netvista
ms.assetid: 39D3265C-ED32-420F-9216-EFD0EDC27C84
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: NDK_OBJECT_HEADER_RESERVED_BLOCK, NDK_OBJECT_HEADER_RESERVED_BLOCK
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: ndkpi.h
req.include-header: Ndkpi.h
req.target-type: Windows
req.target-min-winverclnt: None supported,Supported in NDIS 6.30 and later.
req.target-min-winversvr: Windows Server 2012
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: NDK_OBJECT_HEADER_RESERVED_BLOCK
req.alt-loc: ndkpi.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: <=DISPATCH_LEVEL
req.iface: 
---

# NDK_OBJECT_HEADER_RESERVED_BLOCK structure



## -description
<p>The <b>NDK_OBJECT_HEADER_RESERVED_BLOCK</b> structure specifies reserved information in an NDK object.</p>


## -syntax

````
typedef struct _NDK_OBJECT_HEADER_RESERVED_BLOCK {
  PVOID rf[4];
} NDK_OBJECT_HEADER_RESERVED_BLOCK, *PNDK_OBJECT_HEADER_RESERVED_BLOCK;
````


## -struct-fields
<dl>

### -field <b>rf</b>

<dd>
<p>Reserved.</p>
</dd>
</dl>

## -remarks
<p>The <b>NDK_OBJECT_HEADER_RESERVED_BLOCK</b> structure is used in the <a href="..\ndkpi\ns-ndkpi--ndk-object-header.md">NDK_OBJECT_HEADER</a> structure.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Minimum supported client</p>
</th>
<td width="70%">
<p>None supported</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Minimum supported server</p>
</th>
<td width="70%">
<p>Windows Server 2012</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Supported in NDIS 6.30 and later.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ndkpi.h (include Ndkpi.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\ndkpi\ns-ndkpi--ndk-object-header.md">NDK_OBJECT_HEADER</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NDK_OBJECT_HEADER_RESERVED_BLOCK structure%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
