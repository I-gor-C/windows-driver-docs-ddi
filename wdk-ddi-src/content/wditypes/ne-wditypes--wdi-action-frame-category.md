---
UID: NE.wditypes._WDI_ACTION_FRAME_CATEGORY
title: WDI_ACTION_FRAME_CATEGORY
author: windows-driver-content
description: The WDI_ACTION_FRAME_CATEGORY enumeration defines the action frame categories.
old-location: netvista\wdi_action_frame_category.htm
old-project: netvista
ms.assetid: F2A3D1F0-E6E7-46DC-875A-7F36E6ACBC6D
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
req.alt-api: WDI_ACTION_FRAME_CATEGORY
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

# WDI_ACTION_FRAME_CATEGORY enumeration



## -description
<p>The WDI_ACTION_FRAME_CATEGORY enumeration defines the action frame categories.</p>


## -syntax

````
typedef enum _WDI_ACTION_FRAME_CATEGORY { 
  WDI_ACTION_FRAME_CATEGORY_PUBLIC               = 4,
  WDI_ACTION_FRAME_CATEGORY_RADIO_MEASUREMENT    = 5,
  WDI_ACTION_FRAME_CATEGORY_FAST_BSS_TRANSITION  = 6,
  WDI_ACTION_FRAME_CATEGORY_WNM                  = 10
} WDI_ACTION_FRAME_CATEGORY;
````


## -enum-fields
<dl>

### -field <a id="WDI_ACTION_FRAME_CATEGORY_PUBLIC"></a><a id="wdi_action_frame_category_public"></a><b>WDI_ACTION_FRAME_CATEGORY_PUBLIC</b>

<dd>
<p>Specifies a Public Action frame.  It is used in:</p>
<ul>
<li>Inter-BSS and AP to unassociated-STA communications</li>
<li>Intra-BSS communication</li>
<li>GAS frames</li>
</ul>
</dd>

### -field <a id="WDI_ACTION_FRAME_CATEGORY_RADIO_MEASUREMENT"></a><a id="wdi_action_frame_category_radio_measurement"></a><b>WDI_ACTION_FRAME_CATEGORY_RADIO_MEASUREMENT</b>

<dd>
<p>Specifies a Radio Measurement Report frame. It is transmitted by a STA requesting another STA to make one or more measurements on one or more channels.</p>
</dd>

### -field <a id="WDI_ACTION_FRAME_CATEGORY_FAST_BSS_TRANSITION"></a><a id="wdi_action_frame_category_fast_bss_transition"></a><b>WDI_ACTION_FRAME_CATEGORY_FAST_BSS_TRANSITION</b>

<dd>
<p>Specifies a Fast BSS Transition Action frame.  It is used by a currently-associated AP to enable fast BSS transitions over the DS.  Over the DS transitions are not supported in Windows 10.</p>
</dd>

### -field <a id="WDI_ACTION_FRAME_CATEGORY_WNM"></a><a id="wdi_action_frame_category_wnm"></a><b>WDI_ACTION_FRAME_CATEGORY_WNM</b>

<dd>
<p>Specifies a Wireless Network Management Action frame.  In Windows 10, it is only used for handling BSS Transition Management requests/responses.</p>
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