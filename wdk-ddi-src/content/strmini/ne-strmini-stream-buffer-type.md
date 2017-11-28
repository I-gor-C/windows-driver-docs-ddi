---
UID: NE.strmini.STREAM_BUFFER_TYPE
title: STREAM_BUFFER_TYPE
author: windows-driver-content
description: This enumeration defines the buffer types for StreamClassGetPhysicalAddress.
old-location: stream\stream_buffer_type.htm
old-project: stream
ms.assetid: 7C9E1D94-BF59-4302-BEE8-24546C8AE7E6
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: PST_PARAMETER_DATA, ST_PARAMETER_DATA, *PST_PARAMETER_DATA
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: strmini.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: STREAM_BUFFER_TYPE
req.alt-loc: Strmini.h
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

# STREAM_BUFFER_TYPE enumeration



## -description
<p>This enumeration defines the buffer types for <a href="https://msdn.microsoft.com/library/windows/hardware/ff568247">StreamClassGetPhysicalAddress</a>.</p>


## -syntax

````
typedef enum  { 
  PerRequestExtension,
  DmaBuffer,
  SRBDataBuffer
} STREAM_BUFFER_TYPE;
````


## -enum-fields
<dl>

### -field <a id="PerRequestExtension"></a><a id="perrequestextension"></a><a id="PERREQUESTEXTENSION"></a><b>PerRequestExtension</b>

<dd>
<p>Indicates the physical address of the SRB extension.</p>
</dd>

### -field <a id="DmaBuffer"></a><a id="dmabuffer"></a><a id="DMABUFFER"></a><b>DmaBuffer</b>

<dd>
<p>Indicates the physical address of the DMA buffer.</p>
</dd>

### -field <a id="SRBDataBuffer"></a><a id="srbdatabuffer"></a><a id="SRBDATABUFFER"></a><b>SRBDataBuffer</b>

<dd>
<p>Indicates the physical address of a data buffer.</p>
</dd>
</dl>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Strmini.h</dt>
</dl>
</td>
</tr>
</table>