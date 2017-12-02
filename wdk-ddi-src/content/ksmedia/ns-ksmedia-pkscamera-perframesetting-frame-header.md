---
UID: NS.ksmedia.PKSCAMERA_PERFRAMESETTING_FRAME_HEADER
title: PKSCAMERA_PERFRAMESETTING_FRAME_HEADER
author: windows-driver-content
description: This structure contains the header information for a frame in a per-frame settings payload.
old-location: stream\kscamera_perframesetting_frame_header.htm
old-project: stream
ms.assetid: 59A52F4B-D987-420D-BF83-1375354C6D6A
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: PKSCAMERA_PERFRAMESETTING_FRAME_HEADER, KSCAMERA_PERFRAMESETTING_FRAME_HEADER, *PKSCAMERA_PERFRAMESETTING_FRAME_HEADER
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: ksmedia.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: KSCAMERA_PERFRAMESETTING_FRAME_HEADER
req.alt-loc: Ksmedia.h
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

# PKSCAMERA_PERFRAMESETTING_FRAME_HEADER structure



## -description
<p>This structure contains the header information for a frame in a per-frame settings payload.</p>


## -syntax

````
typedef struct {
  ULONG Size;
  ULONG Id;
  ULONG ItemCount;
  ULONG Reserved;
} KSCAMERA_PERFRAMESETTING_FRAME_HEADER, *PKSCAMERA_PERFRAMESETTING_FRAME_HEADER;
````


## -struct-fields
<dl>

### -field Size

<dd>
<p>The size of this header, all the item headers, value payloads, custom items, and custom data for this frame.</p>
</dd>

### -field Id

<dd>
<p>The frame ID in the range of 0 and KSCAMERA_PERFRAMESETTING_HEADER.FrameCount - 1.</p>
</dd>

### -field ItemCount

<dd>
<p>The number of item settings for this frame. The value 0 indicates using global settings for this frame.</p>
</dd>

### -field Reserved

<dd>
<p>Reserved for future use.</p>
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
<dt>Ksmedia.h</dt>
</dl>
</td>
</tr>
</table>