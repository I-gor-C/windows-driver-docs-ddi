---
UID: NS.ks.PKSSTREAM_UVC_METADATATYPE_TIMESTAMP
title: PKSSTREAM_UVC_METADATATYPE_TIMESTAMP
author: windows-driver-content
description: The KSSTREAM_UVC_METADATATYPE_TIMESTAMP structure contains USB video class (UVC) clock and timestamp information.
old-location: stream\ksstream_uvc_metadatatype_timestamp.htm
old-project: stream
ms.assetid: FDA0CD47-36D9-4E64-9377-F419A7D788A3
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: PKSSTREAM_UVC_METADATATYPE_TIMESTAMP, KSSTREAM_UVC_METADATATYPE_TIMESTAMP, *PKSSTREAM_UVC_METADATATYPE_TIMESTAMP
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
req.alt-api: KSSTREAM_UVC_METADATATYPE_TIMESTAMP
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

# PKSSTREAM_UVC_METADATATYPE_TIMESTAMP structure



## -description
<p>The <b>KSSTREAM_UVC_METADATATYPE_TIMESTAMP</b> structure contains USB video class (UVC) clock and timestamp information.</p>


## -syntax

````
typedef struct {
  ULONG  PresentationTimeStamp;
  ULONG  SourceClockReference;
  union {
    struct {
      USHORT Counter  :11;
      USHORT Reserved  :5;
    };
    USHORT SCRToken;
  };
  USHORT Reserved0;
  ULONG  Reserved1;
} KSSTREAM_UVC_METADATATYPE_TIMESTAMP, *PKSSTREAM_UVC_METADATATYPE_TIMESTAMP;
````


## -struct-fields
<dl>

### -field PresentationTimeStamp

<dd>
<p>Specifies the presentation timestamp.</p>
</dd>

### -field SourceClockReference

<dd>
<p>Specifies the source clock reference.</p>
</dd>

### -field Counter

<dd>
<p>Specifies the source clock reference counter.</p>
</dd>

### -field Reserved

<dd>
<p>Reserved.</p>
</dd>

### -field SCRToken

<dd>
<p>Specifies the source clock reference token.</p>
</dd>

### -field Reserved0

<dd>
<p>Reserved.</p>
</dd>

### -field Reserved1

<dd>
<p>Reserved.</p>
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