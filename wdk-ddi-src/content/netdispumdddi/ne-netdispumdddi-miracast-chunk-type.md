---
UID: NE.netdispumdddi.MIRACAST_CHUNK_TYPE
title: MIRACAST_CHUNK_TYPE
author: windows-driver-content
description: Specifies the types of wireless display (Miracast) chunk info that is to be processed.
old-location: display\miracast_chunk_type.htm
old-project: display
ms.assetid: 39911172-f916-4ca2-8d98-9d53fbc30807
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: NDK_SRQ, NDK_SRQ
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: netdispumdddi.h
req.include-header: Netdispumdddi.h
req.target-type: Windows
req.target-min-winverclnt: Windows 8.1
req.target-min-winversvr: Windows Server 2012 R2
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: MIRACAST_CHUNK_TYPE
req.alt-loc: Netdispumdddi.h
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

# MIRACAST_CHUNK_TYPE enumeration



## -description
<p>Specifies the types of wireless display (Miracast) chunk info that is to be processed.</p>


## -syntax

````
typedef enum  { 
  MIRACAST_CHUNK_TYPE_UNKNOWN                  = 0,
  MIRACAST_CHUNK_TYPE_COLOR_CONVERT_COMPLETE   = 1,
  MIRACAST_CHUNK_TYPE_ENCODE_COMPLETE          = 2,
  MIRACAST_CHUNK_TYPE_FRAME_START              = 3,
  MIRACAST_CHUNK_TYPE_FRAME_DROPPED            = 4,
  MIRACAST_CHUNK_TYPE_ENCODE_DRIVER_DEFINED_1  = 0x80000000,
  MIRACAST_CHUNK_TYPE_ENCODE_DRIVER_DEFINED_2  = 0x80000001,
  MIRACAST_CHUNK_TYPE_ENCODE_FORCE_UINT32      = 0xffffffff
} MIRACAST_CHUNK_TYPE;
````


## -enum-fields
<dl>

### -field <a id="MIRACAST_CHUNK_TYPE_UNKNOWN"></a><a id="miracast_chunk_type_unknown"></a><b>MIRACAST_CHUNK_TYPE_UNKNOWN</b>

<dd>
<p>An unknown or undefined chunk type.</p>
</dd>

### -field <a id="MIRACAST_CHUNK_TYPE_COLOR_CONVERT_COMPLETE"></a><a id="miracast_chunk_type_color_convert_complete"></a><b>MIRACAST_CHUNK_TYPE_COLOR_CONVERT_COMPLETE</b>

<dd>
<p>Color conversion has completed on the chunk.</p>
</dd>

### -field <a id="MIRACAST_CHUNK_TYPE_ENCODE_COMPLETE"></a><a id="miracast_chunk_type_encode_complete"></a><b>MIRACAST_CHUNK_TYPE_ENCODE_COMPLETE</b>

<dd>
<p>Encoding has completed on the chunk.</p>
</dd>

### -field <a id="MIRACAST_CHUNK_TYPE_FRAME_START"></a><a id="miracast_chunk_type_frame_start"></a><b>MIRACAST_CHUNK_TYPE_FRAME_START</b>

<dd>
<p>The chunk is at the start of the Wi-Fi frame.</p>
</dd>

### -field <a id="MIRACAST_CHUNK_TYPE_FRAME_DROPPED"></a><a id="miracast_chunk_type_frame_dropped"></a><b>MIRACAST_CHUNK_TYPE_FRAME_DROPPED</b>

<dd>
<p>The chunk is in a dropped Wi-Fi frame.</p>
</dd>

### -field <a id="MIRACAST_CHUNK_TYPE_ENCODE_DRIVER_DEFINED_1"></a><a id="miracast_chunk_type_encode_driver_defined_1"></a><b>MIRACAST_CHUNK_TYPE_ENCODE_DRIVER_DEFINED_1</b>

<dd>
<p>Encoding is driver-defined, of type 1.</p>
</dd>

### -field <a id="MIRACAST_CHUNK_TYPE_ENCODE_DRIVER_DEFINED_2"></a><a id="miracast_chunk_type_encode_driver_defined_2"></a><b>MIRACAST_CHUNK_TYPE_ENCODE_DRIVER_DEFINED_2</b>

<dd>
<p>Encoding is driver-defined, of type 2.</p>
</dd>

### -field <a id="MIRACAST_CHUNK_TYPE_ENCODE_FORCE_UINT32"></a><a id="miracast_chunk_type_encode_force_uint32"></a><b>MIRACAST_CHUNK_TYPE_ENCODE_FORCE_UINT32</b>

<dd>
<p>Forces this enumeration to compile to 32 bits in size. Without this value, some compilers would allow this enumeration to compile to a size other than 32 bits. You should not use this value.</p>
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
<dt>Netdispumdddi.h (include Netdispumdddi.h)</dt>
</dl>
</td>
</tr>
</table>