---
UID: NE.wwan._WWAN_ACE_STATE
title: WWAN_ACE_STATE
author: windows-driver-content
description: The WWAN_ACE_STATE enumeration lists the different kinds of auto-connect states.
old-location: netvista\wwan_ace_state.htm
old-project: netvista
ms.assetid: 6BF63894-58D6-4C7C-B3D9-D4D9D19A686B
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: WUDF_WORKITEM_CONFIG, WUDF_WORKITEM_CONFIG, *PWUDF_WORKITEM_CONFIG
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: wwan.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: Versions: Supported in Windows 8 and later versions of Windows.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: WWAN_ACE_STATE
req.alt-loc: wwan.h
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
req.product: Windows 10 or later.
---

# WWAN_ACE_STATE enumeration



## -description
<p>The WWAN_ACE_STATE enumeration lists the different kinds of auto-connect states.</p>


## -syntax

````
typedef enum _WWAN_ACE_STATE { 
  WwanAutoOff    = 0,
  WwanAutoOn     = ,
  WwanManualOff  = ,
  WwanManualOn   = 
} WWAN_ACE_STATE;
````


## -enum-fields
<dl>

### -field WwanAutoOff

<dd>
<p>Auto-connect off.</p>
</dd>

### -field WwanAutoOn

<dd>
<p>Auto-connect on.</p>
</dd>

### -field WwanManualOff

<dd>
<p>Manual connect off.</p>
</dd>

### -field WwanManualOn

<dd>
<p>Manual connect on.</p>
</dd>
</dl>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Versions: Supported in Windows 8 and later versions of Windows.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Wwan.h</dt>
</dl>
</td>
</tr>
</table>