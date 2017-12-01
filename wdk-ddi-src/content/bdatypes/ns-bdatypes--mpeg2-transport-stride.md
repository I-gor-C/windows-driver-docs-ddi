---
UID: NS.bdatypes._MPEG2_TRANSPORT_STRIDE
title: MPEG2_TRANSPORT_STRIDE
author: windows-driver-content
description: The MPEG2_TRANSPORT_STRIDE structure describes the format block of the MPEG2 transport stride.
old-location: stream\mpeg2_transport_stride.htm
old-project: stream
ms.assetid: 5756bb06-8fd3-4124-b3c8-35d5ed0bd57b
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: MPEG2_TRANSPORT_STRIDE, MPEG2_TRANSPORT_STRIDE, *PMPEG2_TRANSPORT_STRIDE
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: bdatypes.h
req.include-header: Bdatypes.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: MPEG2_TRANSPORT_STRIDE
req.alt-loc: bdatypes.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: PASSIVE_LEVEL
req.iface: 
---

# MPEG2_TRANSPORT_STRIDE structure



## -description
<p>The MPEG2_TRANSPORT_STRIDE structure describes the format block of the MPEG2 transport stride. </p>


## -syntax

````
typedef struct _MPEG2_TRANSPORT_STRIDE {
  DWORD dwOffset;
  DWORD dwPacketLength;
  DWORD dwStride;
} MPEG2_TRANSPORT_STRIDE, *PMPEG2_TRANSPORT_STRIDE;
````


## -struct-fields
<dl>

### -field <b>dwOffset</b>

<dd>
<p>Offset in bytes into a packet.</p>
</dd>

### -field <b>dwPacketLength</b>

<dd>
<p>Size in bytes of a packet.</p>
</dd>

### -field <b>dwStride</b>

<dd>
<p>Stride of data in a packet. </p>
</dd>
</dl>

## -remarks
<p>The MPEG2 transport stride format block is associated with the MEDIATYPE_Stream/MEDIASUBTYPE_MPEG2_TRANSPORT_STRIDE media type. Format blocks that are associated with this media type must start with the MPEG2_TRANSPORT_STRIDE structure.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Bdatypes.h (include Bdatypes.h)</dt>
</dl>
</td>
</tr>
</table>