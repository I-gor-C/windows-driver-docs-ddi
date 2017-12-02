---
UID: NS.ntddvdeo._VIDEO_POINTER_CAPABILITIES
title: VIDEO_POINTER_CAPABILITIES
author: windows-driver-content
description: Contains capabilities of the screen pointer.
old-location: display\video_pointer_capabilities.htm
old-project: display
ms.assetid: bc5f98da-1e2e-421b-9c76-97359e51b526
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: VIDEO_POINTER_CAPABILITIES, VIDEO_POINTER_CAPABILITIES, *PVIDEO_POINTER_CAPABILITIES
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: ntddvdeo.h
req.include-header: Ntddvdeo.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: VIDEO_POINTER_CAPABILITIES
req.alt-loc: Ntddvdeo.h
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

# VIDEO_POINTER_CAPABILITIES structure



## -description
<p>The <b>VIDEO_POINTER_CAPABILITIES</b> structure contains capabilities of the screen pointer.</p>


## -syntax

````
typedef struct _VIDEO_POINTER_CAPABILITIES {
  ULONG Flags;
  ULONG MaxWidth;
  ULONG MaxHeight;
  ULONG HWPtrBitmapStart;
  ULONG HWPtrBitmapEnd;
} VIDEO_POINTER_CAPABILITIES, *PVIDEO_POINTER_CAPABILITIES;
````


## -struct-fields
<dl>

### -field Flags

<dd>
<p>A set of flags that specify certain capabilities of the pointer. Flags can be a combination of the following values.</p>
<table>
<tr>
<th>Flag</th>
<th>Meaning</th>
</tr>
<tr>
<td>
<p>VIDEO_MODE_ASYNC_POINTER</p>
</td>
<td>
<p>The pointer can be updated asynchronously to drawing operations.</p>
</td>
</tr>
<tr>
<td>
<p>VIDEO_MODE_MONO_POINTER</p>
</td>
<td>
<p>A monochrome hardware pointer is supported.</p>
</td>
</tr>
<tr>
<td>
<p>VIDEO_MODE_COLOR_POINTER</p>
</td>
<td>
<p>A color hardware pointer is supported.</p>
</td>
</tr>
<tr>
<td>
<p>VIDEO_MODE_ANIMATE_START</p>
</td>
<td>
<p>The current pointer has the same hotspot as the previous pointer.</p>
</td>
</tr>
<tr>
<td>
<p>VIDEO_MODE_ANIMATE_UPDATE</p>
</td>
<td>
<p>The current pointer has the same hotspot as the previous pointer.</p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -field MaxWidth

<dd>
<p>Specifies the maximum width of the pointer, in pixels.</p>
</dd>

### -field MaxHeight

<dd>
<p>Specifies the maximum height of the pointer, in pixels.</p>
</dd>

### -field HWPtrBitmapStart

<dd>
<p>Specifies the first offset, in CPU-addressable units, in the memory bitmap that is used to store the hardware pointer bitmap. A value of –1 is not valid.</p>
</dd>

### -field HWPtrBitmapEnd

<dd>
<p>Specifies the last offset, in CPU-addressable units, in the memory bitmap that is used to store the hardware pointer bitmap. A value of –1 is not valid.</p>
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
<dt>Ntddvdeo.h (include Ntddvdeo.h)</dt>
</dl>
</td>
</tr>
</table>