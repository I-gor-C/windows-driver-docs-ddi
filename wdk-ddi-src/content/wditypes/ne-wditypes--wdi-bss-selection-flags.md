---
UID: NE.wditypes._WDI_BSS_SELECTION_FLAGS
title: WDI_BSS_SELECTION_FLAGS
author: windows-driver-content
description: The WDI_BSS_SELECTION_FLAGS enumeration defines flags for BSS selection.
old-location: netvista\wdi_bss_selection_flags.htm
old-project: netvista
ms.assetid: 9C2F862B-8BA8-4947-9C3D-538715C99F26
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: WDF_WORKITEM_CONFIG, WDF_WORKITEM_CONFIG, *PWDF_WORKITEM_CONFIG
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: wditypes.hpp
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: Windows 10
req.target-min-winversvr: Windows Server 2016
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: WDI_BSS_SELECTION_FLAGS
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
req.iface: 
req.product: Windows 10 or later.
---

# WDI_BSS_SELECTION_FLAGS enumeration



## -description
<p>The WDI_BSS_SELECTION_FLAGS enumeration defines flags for BSS selection.</p>


## -syntax

````
typedef enum _WDI_BSS_SELECTION_FLAGS { 
  WDI_BSS_SELECTION_HOST_PREFERRED                 = 0x00000001,
  WDI_BSS_SELECTION_RECENT_ASSOCIATION_ERROR       = 0x00000002,
  WDI_BSS_SELECTION_FLAGS_AP_REQUESTED_TRANSITION  = 0x00000004
} WDI_BSS_SELECTION_FLAGS;
````


## -enum-fields
<dl>

### -field <a id="WDI_BSS_SELECTION_HOST_PREFERRED"></a><a id="wdi_bss_selection_host_preferred"></a><b>WDI_BSS_SELECTION_HOST_PREFERRED</b>

<dd>
<p>Set for BSS entries that the host prefers to connect to. Non-preferred BSS entries would also be provided to the port, but should only be used  for connection if port performs its own BSS ranking.</p>
</dd>

### -field <a id="WDI_BSS_SELECTION_RECENT_ASSOCIATION_ERROR"></a><a id="wdi_bss_selection_recent_association_error"></a><b>WDI_BSS_SELECTION_RECENT_ASSOCIATION_ERROR</b>

<dd>
<p>Set for BSS entries that had recent association failures or were recently disassociated from. This flag is already accounted for by the host when setting WDI_BSS_SELECTION_HOST_PREFERRED.</p>
</dd>

### -field <a id="WDI_BSS_SELECTION_FLAGS_AP_REQUESTED_TRANSITION"></a><a id="wdi_bss_selection_flags_ap_requested_transition"></a><b>WDI_BSS_SELECTION_FLAGS_AP_REQUESTED_TRANSITION</b>

<dd>
<p>Specifies whether this roam was requested by the AP or not (11v BSS Transition management request).</p>
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