---
UID: NS.netdispumdddi.MIRACAST_CHUNK_ID
title: MIRACAST_CHUNK_ID
author: windows-driver-content
description: Stores info that identifies a wireless display (Miracast) encode chunk.
old-location: display\miracast_chunk_id.htm
ms.assetid: 30140530-63B6-4FE4-98A4-C6950D7D4D9A
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: display
req.header: netdispumdddi.h
req.include-header: Netdispumdddi.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: MIRACAST_CHUNK_ID
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
ms.keywords: MIRACAST_CHUNK_ID, MIRACAST_CHUNK_ID
req.iface: 
---

# MIRACAST_CHUNK_ID structure



## -description
<p>Stores info that identifies a wireless display (Miracast) encode chunk.</p>


## -syntax

````
typedef union {
  struct {
    UINT64 FrameNumber  :40;
    UINT64 PartNumber  :24;
  };
  UINT64 Value;
} MIRACAST_CHUNK_ID;
````


## -struct-fields
<dl>

### -field <b>FrameNumber</b>

<dd>
<p>The number of the encoded Wi-Fi frame.</p>
</dd>

### -field <b>PartNumber</b>

<dd>
<p>The frame part number.</p>
</dd>

### -field <b>Value</b>

<dd>
<p>Holds a 64-bit value that identifies the encode chunk.</p>
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
<dt>Netdispumdddi.h (include Netdispumdddi.h)</dt>
</dl>
</td>
</tr>
</table>