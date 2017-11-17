---
UID: NS.ksmedia.PKSCAMERA_PERFRAMESETTING_HEADER
title: PKSCAMERA_PERFRAMESETTING_HEADER
author: windows-driver-content
description: This structure contains header information for the per-frame settings payload.
old-location: stream\kscamera_perframesetting_header.htm
ms.assetid: 2D8A9E54-5551-4DDF-A123-077BA73AE06D
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: stream
req.header: ksmedia.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: KSCAMERA_PERFRAMESETTING_HEADER
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
ms.keywords: PKSCAMERA_PERFRAMESETTING_HEADER, KSCAMERA_PERFRAMESETTING_HEADER, *PKSCAMERA_PERFRAMESETTING_HEADER
req.iface: 
---

# PKSCAMERA_PERFRAMESETTING_HEADER structure



## -description
<p>This structure contains header information for the per-frame settings payload.</p>


## -syntax

````
typedef struct {
  ULONG     Size;
  ULONG     FrameCount;
  GUID      Id;
  ULONGLONG Flags;
  ULONG     LoopCount;
  ULONG     Reserved;
} KSCAMERA_PERFRAMESETTING_HEADER, *PKSCAMERA_PERFRAMESETTING_HEADER;
````


## -struct-fields
<dl>

### -field <b>Size</b>

<dd>
<p>The size of this header, frame headers, item headers, value payloads, custom items, and custom data for all frames.</p>
</dd>

### -field <b>FrameCount</b>

<dd>
<p>The number of frame settings in this per-frame settings payload.</p>
</dd>

### -field <b>Id</b>

<dd>
<p>Not used.</p>
</dd>

### -field <b>Flags</b>

<dd>
<p>Not used.</p>
</dd>

### -field <b>LoopCount</b>

<dd>
<p>The number of repeats for this per-frame setting. This is always 1.</p>
</dd>

### -field <b>Reserved</b>

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