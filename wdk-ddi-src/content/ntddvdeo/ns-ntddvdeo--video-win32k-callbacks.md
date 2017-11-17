---
UID: NS.ntddvdeo._VIDEO_WIN32K_CALLBACKS
title: VIDEO_WIN32K_CALLBACKS
author: windows-driver-content
description: The VIDEO_WIN32K_CALLBACKS structure is reserved for system use.
old-location: display\video_win32k_callbacks.htm
ms.assetid: dec6c610-811c-40cb-a099-1a35b91d2ee8
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: display
req.header: ntddvdeo.h
req.include-header: Ntddvdeo.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: VIDEO_WIN32K_CALLBACKS
req.alt-loc: ntddvdeo.h
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
ms.keywords: VIDEO_WIN32K_CALLBACKS, VIDEO_WIN32K_CALLBACKS, *PVIDEO_WIN32K_CALLBACKS
req.iface: 
---

# VIDEO_WIN32K_CALLBACKS structure



## -description
<p>The VIDEO_WIN32K_CALLBACKS structure is reserved for system use.</p>


## -syntax

````
typedef struct _VIDEO_WIN32K_CALLBACKS {
  PVOID                 PhysDisp;
  PVIDEO_WIN32K_CALLOUT Callout;
  ULONG                 bACPI;
  HANDLE                pPhysDeviceObject;
  ULONG                 DualviewFlags;
} VIDEO_WIN32K_CALLBACKS, *PVIDEO_WIN32K_CALLBACKS;
````


## -struct-fields
<dl>

### -field <b>PhysDisp</b>

<dd>
<p>Reserved for system use.</p>
</dd>

### -field <b>Callout</b>

<dd>
<p>Reserved for system use.</p>
</dd>

### -field <b>bACPI</b>

<dd>
<p>Reserved for system use.</p>
</dd>

### -field <b>pPhysDeviceObject</b>

<dd>
<p>Reserved for system use.</p>
</dd>

### -field <b>DualviewFlags</b>

<dd>
<p>Reserved for system use.</p>
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