---
UID: NS.d3dkmddi._DXGKARG_CREATEPERIODICFRAMENOTIFICATION
title: DXGKARG_CREATEPERIODICFRAMENOTIFICATION
author: windows-driver-content
description: The arguments needed to create a periodic frame notification.
old-location: display\dxgkarg_createperiodicframenotification.htm
old-project: display
ms.assetid: 455C3FBD-2E0D-4CD7-B753-E53ED58A7F6F
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: DXGKARG_CREATEPERIODICFRAMENOTIFICATION, DXGKARG_CREATEPERIODICFRAMENOTIFICATION
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: d3dkmddi.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: DXGKARG_CREATEPERIODICFRAMENOTIFICATION
req.alt-loc: d3dkmddi.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: PASSIVE_LEVEL
req.iface: 
---

# DXGKARG_CREATEPERIODICFRAMENOTIFICATION structure



## -description
<p>The arguments needed to create a periodic frame notification.</p>


## -syntax

````
typedef struct _DXGKARG_CREATEPERIODICFRAMENOTIFICATION {
  HANDLE                         hAdapter;
  D3DDDI_VIDEO_PRESENT_TARGET_ID VidPnTargetID;
  UINT64                         Time;
  UINT                           NotificationID;
  HANDLE                         hNotification;
} DXGKARG_CREATEPERIODICFRAMENOTIFICATION;
````


## -struct-fields
<dl>

### -field hAdapter

<dd>
<p>A handle to the adapter associated with VidPnSourceID.</p>
</dd>

### -field VidPnTargetID

<dd>
<p>The output that the compositor wishes to receive notifications for.</p>
</dd>

### -field Time

<dd>
<p>Represents an offset before the VSync. The Time value may not be longer than a VSync interval while in VSync mode. In units of 100ns.</p>
</dd>

### -field NotificationID

<dd>
<p>Represents an ID for the notification that will be used to track which interrupt has fired from the GPU.</p>
</dd>

### -field hNotification

<dd>
<p>A Handle to the notification object, later used to destroy the object.</p>
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
<dt>D3dkmddi.h</dt>
</dl>
</td>
</tr>
</table>