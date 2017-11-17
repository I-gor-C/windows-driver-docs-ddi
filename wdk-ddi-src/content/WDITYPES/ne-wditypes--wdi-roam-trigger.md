---
UID: NE.wditypes._WDI_ROAM_TRIGGER
title: WDI_ROAM_TRIGGER
author: windows-driver-content
description: The WDI_ROAM_TRIGGER enumeration defines roam triggers.
old-location: netvista\wdi_roam_trigger.htm
ms.assetid: 7AFA084B-5EFC-429B-B6D1-F4E484B16921
ms.author: windowsdriverdev
ms.date: 11/1/2017
ms.topic: enum
ms.prod: windows-hardware
ms.technology: netvista
req.header: wditypes.hpp
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: Windows 10
req.target-min-winversvr: Windows Server 2016
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: WDI_ROAM_TRIGGER
req.alt-loc: wditypes.hpp
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: <= DISPATCH_LEVEL
ms.keywords: WDF_WORKITEM_CONFIG, WDF_WORKITEM_CONFIG, *PWDF_WORKITEM_CONFIG
req.iface: 
req.product: Windows 10 or later.
---

# WDI_ROAM_TRIGGER enumeration



## -description
<p>The WDI_ROAM_TRIGGER enumeration defines roam triggers.</p>


## -syntax

````
typedef enum _WDI_ROAM_TRIGGER { 
  WDI_ROAM_TRIGGER_OTHER                            = 0x00000000,
  WDI_ROAM_TRIGGER_CRITICAL_BSS_TRANSITION_REQUEST  = 0x00000001
} WDI_ROAM_TRIGGER;
````


## -enum-fields
<dl>

### -field <a id="WDI_ROAM_TRIGGER_OTHER"></a><a id="wdi_roam_trigger_other"></a><b>WDI_ROAM_TRIGGER_OTHER</b>

<dd>
<p>None.</p>
</dd>

### -field <a id="WDI_ROAM_TRIGGER_CRITICAL_BSS_TRANSITION_REQUEST"></a><a id="wdi_roam_trigger_critical_bss_transition_request"></a><b>WDI_ROAM_TRIGGER_CRITICAL_BSS_TRANSITION_REQUEST</b>

<dd>
<p>This value is for roams due to a BSS Transition Request by the AP with the Disassociation Imminent bit set.</p>
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
<dt>Wditypes.hpp</dt>
</dl>
</td>
</tr>
</table>