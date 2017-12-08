---
UID: NS.D3DKMTHK.D3DKMT_PRESENT_MULTIPLANE_OVERLAY
title: D3DKMT_PRESENT_MULTIPLANE_OVERLAY
author: windows-driver-content
description: Reserved for system use. Do not use in your driver.
old-location: display\d3dkmt_present_multiplane_overlay.htm
old-project: display
ms.assetid: 2526ccce-826a-4e8f-ab15-639510b1d5cf
ms.author: windowsdriverdev
ms.date: 12/6/2017
ms.keywords: D3DKMT_PRESENT_MULTIPLANE_OVERLAY, D3DKMT_PRESENT_MULTIPLANE_OVERLAY
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
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
---

# D3DKMT_PRESENT_MULTIPLANE_OVERLAY structure



## -description
Reserved for system use. Do not use in your driver.


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

### -field hDevice


### -field hContext


### -field BroadcastContextCount


### -field BroadcastContext


### -field VidPnSourceId


### -field PresentCount


### -field FlipInterval


### -field Flags


### -field PresentPlaneCount


### -field pPresentPlanes


### -field Duration


## -remarks


## -requirements
<table>
<tr>
<th width="30%">
Minimum supported client
</th>
<td width="70%">
Windows 8
</td>
</tr>
<tr>
<th width="30%">
Minimum supported server
</th>
<td width="70%">
Windows Server 2012
</td>
</tr>
<tr>
<th width="30%">
Header
</th>
<td width="70%">
<dl>
<dt>D3dkmthk.h</dt>
</dl>
</td>
</tr>
</table>