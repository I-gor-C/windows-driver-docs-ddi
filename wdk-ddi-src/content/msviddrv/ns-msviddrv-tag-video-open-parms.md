---
UID: NS.msviddrv.tag_video_open_parms
title: tag_video_open_parms
author: windows-driver-content
description: .
old-location: stream\video_open_parms.htm
old-project: stream
ms.assetid: BD11B67F-9229-4584-A20D-7D7C70B42977
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: tag_video_open_parms, VIDEO_OPEN_PARMS, *LPVIDEO_OPEN_PARMS
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: msviddrv.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: VIDEO_OPEN_PARMS
req.alt-loc: Msviddrv.h
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
req.iface: 
---

# tag_video_open_parms structure



## -description
<p></p>


## -syntax

````
typedef struct tag_video_open_parms {
  DWORD  dwSize;
  FOURCC fccType;
  FOURCC fccComp;
  DWORD  dwVersion;
  DWORD  dwFlags;
  DWORD  dwError;
  LPVOID pV1Reserved;
  LPVOID pV2Reserved;
  DWORD  dnDevNode;
} VIDEO_OPEN_PARMS, *LPVIDEO_OPEN_PARMS;
````


## -struct-fields
<dl>

### -field <b>dwSize</b>

<dd>
<p>Set to the size of the <b>VIDEO_OPEN_PARMS</b> structure.</p>
</dd>

### -field <b>fccType</b>

<dd>
<p>'vcap'</p>
</dd>

### -field <b>fccComp</b>

<dd>
<p>This member is not used.</p>
</dd>

### -field <b>dwVersion</b>

<dd>
<p>Specifies the version of msvideo.</p>
</dd>

### -field <b>dwFlags</b>

<dd>
<p>Specifies the type of channel.</p>
</dd>

### -field <b>dwError</b>

<dd>
<p>If open fails, specifies why it failed.</p>
</dd>

### -field <b>pV1Reserved</b>

<dd>
<p>Reserved.</p>
</dd>

### -field <b>pV2Reserved</b>

<dd>
<p>Reserved.</p>
</dd>

### -field <b>dnDevNode</b>

<dd>
<p>Specifies the devnode for PnP devices.</p>
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