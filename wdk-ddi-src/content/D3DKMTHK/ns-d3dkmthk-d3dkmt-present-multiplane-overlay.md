---
UID: NS.d3dkmthk.D3DKMT_PRESENT_MULTIPLANE_OVERLAY
title: D3DKMT_PRESENT_MULTIPLANE_OVERLAY
author: windows-driver-content
description: Reserved for system use. Do not use in your driver.
old-location: display\d3dkmt_present_multiplane_overlay.htm
ms.assetid: 2526ccce-826a-4e8f-ab15-639510b1d5cf
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: display
req.header: d3dkmthk.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: Windows 8
req.target-min-winversvr: Windows Server 2012
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: D3DKMT_PRESENT_MULTIPLANE_OVERLAY
req.alt-loc: D3dkmthk.h
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
ms.keywords: D3DKMT_PRESENT_MULTIPLANE_OVERLAY, D3DKMT_PRESENT_MULTIPLANE_OVERLAY
req.iface: 
---

# D3DKMT_PRESENT_MULTIPLANE_OVERLAY structure



## -description
<p>Reserved for system use. Do not use in your driver.</p>


## -syntax

````
typedef struct D3DKMT_PRESENT_MULTIPLANE_OVERLAY {
  union {
    D3DKMT_HANDLE hDevice;
    D3DKMT_HANDLE hContext;
  };
  ULONG                          BroadcastContextCount;
  D3DKMT_HANDLE                  BroadcastContext[D3DDDI_MAX_BROADCAST_CONTEXT];
  D3DDDI_VIDEO_PRESENT_SOURCE_ID VidPnSourceId;
  UINT                           PresentCount;
  D3DDDI_FLIPINTERVAL_TYPE       FlipInterval;
  D3DKMT_PRESENTFLAGS            Flags;
  UINT                           PresentPlaneCount;
  D3DKMT_MULTIPLANE_OVERLAY      *pPresentPlanes;
  UINT                           Duration;
} D3DKMT_PRESENT_MULTIPLANE_OVERLAY;
````


## -struct-fields
<dl>

### -field <b>hDevice</b>

<dd></dd>

### -field <b>hContext</b>

<dd></dd>

### -field <b>BroadcastContextCount</b>

<dd></dd>

### -field <b>BroadcastContext</b>

<dd></dd>

### -field <b>VidPnSourceId</b>

<dd></dd>

### -field <b>PresentCount</b>

<dd></dd>

### -field <b>FlipInterval</b>

<dd></dd>

### -field <b>Flags</b>

<dd></dd>

### -field <b>PresentPlaneCount</b>

<dd></dd>

### -field <b>pPresentPlanes</b>

<dd></dd>

### -field <b>Duration</b>

<dd></dd>
</dl>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Minimum supported client</p>
</th>
<td width="70%">
<p>Windows 8</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Minimum supported server</p>
</th>
<td width="70%">
<p>Windows Server 2012</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>D3dkmthk.h</dt>
</dl>
</td>
</tr>
</table>