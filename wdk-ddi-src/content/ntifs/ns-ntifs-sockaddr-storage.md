---
UID: NS.ntifs.sockaddr_storage
title: sockaddr_storage
author: windows-driver-content
description: The SOCKADDR_STORAGE structure is a generic structure that specifies a transport address.
old-location: netvista\sockaddr_storage.htm
old-project: netvista
ms.assetid: 27e56c1a-ce11-4cdb-9be8-25ed2f94fb37
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: sockaddr_storage,
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: ntifs.h
req.include-header: Wsk.h
req.target-type: Windows
req.target-min-winverclnt: Available in Windows Vista and later versions of the Windows operating   systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: SOCKADDR_STORAGE
req.alt-loc: ntifs.h
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
---

# sockaddr_storage structure



## -description
<p>The SOCKADDR_STORAGE structure is a generic structure that specifies a transport address.</p>


## -syntax

````
typedef struct sockaddr_storage {
  ADDRESS_FAMILY ss_family;
  CHAR           __ss_pad1[_SS_PAD1SIZE];
  __int64        __ss_align;
  CHAR           __ss_pad2[_SS_PAD2SIZE];
} SOCKADDR_STORAGE, *PSOCKADDR_STORAGE;
````


## -struct-fields
<dl>

### -field <b>ss_family</b>

<dd>
<p>The address family for the transport address. For more information about supported address
     families, see 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff571151">WSK Address Families</a>.</p>
</dd>

### -field <b>__ss_pad1</b>

<dd>
<p>A padding of 6 bytes that puts the 
     <b>__ss_align</b> member on an eight-byte boundary within the structure.</p>
</dd>

### -field <b>__ss_align</b>

<dd>
<p>A 64-bit value that forces the structure to be 8-byte aligned.</p>
</dd>

### -field <b>__ss_pad2</b>

<dd>
<p>A padding of an additional 112 bytes that brings the total size of the SOCKADDR_STORAGE structure
     to 128 bytes.</p>
</dd>
</dl>

## -remarks
<p>A WSK application typically does not directly access any of the members of the SOCKADDR_STORAGE
    structure except for the 
    <b>ss_family</b> member. Instead, a pointer to a SOCKADDR_STORAGE structure is normally cast to a pointer
    to the specific SOCKADDR structure type that corresponds to a particular address family.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Available in Windows Vista and later versions of the Windows operating
   systems.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ntifs.h (include Wsk.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="netvista.sockaddr">SOCKADDR</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20SOCKADDR_STORAGE structure%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
