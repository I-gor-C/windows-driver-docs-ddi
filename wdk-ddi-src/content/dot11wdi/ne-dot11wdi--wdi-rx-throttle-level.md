---
UID: NE.dot11wdi._WDI_RX_THROTTLE_LEVEL
title: WDI_RX_THROTTLE_LEVEL
author: windows-driver-content
description: The WDI_RX_THROTTLE_LEVEL enumeration defines the RX throttle level. The interpretation and implementation mechanisms of these throttle levels are defined by the independent hardware vendor (IHV).
old-location: netvista\wdi_rx_throttle_level.htm
old-project: netvista
ms.assetid: 637c0892-8d73-45b7-b679-ff3a0ba78a9c
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: SYNTHVOICEPRIORITY_INSTANCE, SYNTHVOICEPRIORITY_INSTANCE, *PSYNTHVOICEPRIORITY_INSTANCE
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: dot11wdi.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: Windows 10
req.target-min-winversvr: Windows Server 2016
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: WDI_RX_THROTTLE_LEVEL
req.alt-loc: dot11wdi.h
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
req.iface: ISynthSinkDMus
---

# WDI_RX_THROTTLE_LEVEL enumeration



## -description
<p>The WDI_RX_THROTTLE_LEVEL enumeration defines the RX throttle level. The interpretation and implementation mechanisms of these throttle levels are defined by the independent hardware vendor (IHV).</p>


## -syntax

````
typedef enum _WDI_RX_THROTTLE_LEVEL { 
  WDI_RxThrottleLevelNone        = 0x0,
  WDI_RxThrottleLevelMedium      = 0x1,
  WDI_RxThrottleLevelAggressive  = 0x2
} WDI_RX_THROTTLE_LEVEL;
````


## -enum-fields
<dl>

### -field WDI_RxThrottleLevelNone

<dd>
<p>No throttling.</p>
</dd>

### -field WDI_RxThrottleLevelMedium

<dd>
<p>Medium throttling.</p>
</dd>

### -field WDI_RxThrottleLevelAggressive

<dd>
<p>Aggressive throttling.</p>
</dd>
</dl>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Minimum supported client</p>
</th>
<td width="70%">
<p>Windows 10</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Minimum supported server</p>
</th>
<td width="70%">
<p>Windows Server 2016</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Dot11wdi.h</dt>
</dl>
</td>
</tr>
</table>