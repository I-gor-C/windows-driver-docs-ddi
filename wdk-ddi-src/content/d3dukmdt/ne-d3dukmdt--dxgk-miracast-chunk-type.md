---
UID: NE.d3dukmdt._DXGK_MIRACAST_CHUNK_TYPE
title: DXGK_MIRACAST_CHUNK_TYPE
author: windows-driver-content
description: Specifies the types of wireless display (Miracast) chunk info that is to be processed.
old-location: display\dxgk_miracast_chunk_type.htm
old-project: display
ms.assetid: 6C44EFD1-9366-4119-945E-688176D9F5D5
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: D3DKMT_PRESENT_MULTIPLANE_OVERLAY, D3DKMT_PRESENT_MULTIPLANE_OVERLAY
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: d3dukmdt.h
req.include-header: D3dukmdt.h, D3dkmddi.h
req.target-type: Windows
req.target-min-winverclnt: Windows 8.1
req.target-min-winversvr: Windows Server 2012 R2
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: DXGK_MIRACAST_CHUNK_TYPE
req.alt-loc: D3dukmdt.h
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

# DXGK_MIRACAST_CHUNK_TYPE enumeration



## -description
<p>Specifies the types of wireless display (Miracast) chunk info that is to be processed.</p>


## -syntax

````
typedef enum _DXGK_MIRACAST_CHUNK_TYPE { 
  DXGK_MIRACAST_CHUNK_TYPE_UNKNOWN                  = 0,
  DXGK_MIRACAST_CHUNK_TYPE_COLOR_CONVERT_COMPLETE   = 1,
  DXGK_MIRACAST_CHUNK_TYPE_ENCODE_COMPLETE          = 2,
  DXGK_MIRACAST_CHUNK_TYPE_FRAME_START              = 3,
  DXGK_MIRACAST_CHUNK_TYPE_FRAME_DROPPED            = 4,
  DXGK_MIRACAST_CHUNK_TYPE_ENCODE_DRIVER_DEFINED_1  = 0x80000000,
  DXGK_MIRACAST_CHUNK_TYPE_ENCODE_DRIVER_DEFINED_2  = 0x80000001
} DXGK_MIRACAST_CHUNK_TYPE;
````


## -enum-fields
<dl>

### -field DXGK_MIRACAST_CHUNK_TYPE_UNKNOWN

<dd>
<p>An unknown or undefined chunk type.</p>
</dd>

### -field DXGK_MIRACAST_CHUNK_TYPE_COLOR_CONVERT_COMPLETE

<dd>
<p>Color conversion has completed on the chunk.</p>
</dd>

### -field DXGK_MIRACAST_CHUNK_TYPE_ENCODE_COMPLETE

<dd>
<p>Encoding has completed on the chunk.</p>
</dd>

### -field DXGK_MIRACAST_CHUNK_TYPE_FRAME_START

<dd>
<p>The chunk is at the start of the Wi-Fi frame.</p>
</dd>

### -field DXGK_MIRACAST_CHUNK_TYPE_FRAME_DROPPED

<dd>
<p>The chunk is in a dropped Wi-Fi frame.</p>
</dd>

### -field DXGK_MIRACAST_CHUNK_TYPE_ENCODE_DRIVER_DEFINED_1

<dd>
<p>Encoding is driver-defined, of type 1.</p>
</dd>

### -field DXGK_MIRACAST_CHUNK_TYPE_ENCODE_DRIVER_DEFINED_2

<dd>
<p>Encoding is driver-defined, of type 2.</p>
</dd>
</dl>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Minimum supported client</p>
</th>
<td width="70%">
<p>Windows 8.1</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Minimum supported server</p>
</th>
<td width="70%">
<p>Windows Server 2012 R2</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>D3dukmdt.h (include D3dukmdt.h or D3dkmddi.h)</dt>
</dl>
</td>
</tr>
</table>