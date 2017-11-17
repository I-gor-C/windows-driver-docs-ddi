---
UID: NS.msviddrv.tag_video_stream_init_parms
title: tag_video_stream_init_parms
author: windows-driver-content
description: TBD.
old-location: stream\video_stream_init_parms.htm
ms.assetid: 0FEC5054-8045-4CE5-AA59-AE3D23568308
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: stream
req.header: msviddrv.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: VIDEO_STREAM_INIT_PARMS
req.alt-loc: 
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: <= APC_LEVEL
ms.keywords: tag_video_stream_init_parms, VIDEO_STREAM_INIT_PARMS, *LPVIDEO_STREAM_INIT_PARMS
req.iface: 
---

# tag_video_stream_init_parms structure



## -description
<p>TBD</p>


## -syntax

````
typedef struct tag_video_stream_init_parms {
  DWORD  dwMicroSecPerFrame;
  DWORD  dwCallback;
  DWORD  dwCallbackInst;
  DWORD  dwFlags;
  HANDLE hVideo;
} VIDEO_STREAM_INIT_PARMS, *LPVIDEO_STREAM_INIT_PARMS;
````


## -struct-fields
<dl>

### -field <b>dwMicroSecPerFrame</b>

<dd>
<p>TBD</p>
</dd>

### -field <b>dwCallback</b>

<dd>
<p>TBD</p>
</dd>

### -field <b>dwCallbackInst</b>

<dd>
<p>TBD</p>
</dd>

### -field <b>dwFlags</b>

<dd>
<p>TBD</p>
</dd>

### -field <b>hVideo</b>

<dd>
<p>TBD</p>
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
<dt>Msviddrv.h</dt>
</dl>
</td>
</tr>
</table>