---
UID: NS.ks.PKSSTREAM_UVC_METADATA
title: PKSSTREAM_UVC_METADATA
author: windows-driver-content
description: The KSSTREAM_UVC_METADATA structure contains start and end of frame timestamp information.
old-location: stream\ksstream_uvc_metadata.htm
old-project: stream
ms.assetid: 99ED5E06-23C7-4B24-BD9B-E6713B1D58D2
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: PKSSTREAM_UVC_METADATA, KSSTREAM_UVC_METADATA, *PKSSTREAM_UVC_METADATA
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: ks.h
req.include-header: Ks.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: KSSTREAM_UVC_METADATA
req.alt-loc: ks.h
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

# PKSSTREAM_UVC_METADATA structure



## -description
<p>The <b>KSSTREAM_UVC_METADATA</b> structure contains start and end of frame timestamp information.</p>


## -syntax

````
typedef struct {
  KSSTREAM_UVC_METADATATYPE_TIMESTAMP StartOfFrameTimestamp;
  KSSTREAM_UVC_METADATATYPE_TIMESTAMP EndOfFrameTimestamp;
} KSSTREAM_UVC_METADATA, *PKSSTREAM_UVC_METADATA;
````


## -struct-fields
<dl>

### -field StartOfFrameTimestamp

<dd>
<p>Contains  start of frame timestamp information.</p>
</dd>

### -field EndOfFrameTimestamp

<dd>
<p>Contains end of frame timestamp information.</p>
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
<dt>Ks.h (include Ks.h)</dt>
</dl>
</td>
</tr>
</table>