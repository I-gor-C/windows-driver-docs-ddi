---
UID: NE.wditypes._WDI_WNM_ACTION
title: WDI_WNM_ACTION
author: windows-driver-content
description: The WDI_WNM_ACTION enumeration defines the message type for 802.11v BSS Transition Management action frames.
old-location: netvista\wdi_wnm_action.htm
old-project: netvista
ms.assetid: 350D3182-3BEE-4AB7-A9F0-5C5D7D60A617
ms.author: windowsdriverdev
ms.date: 11/30/2017
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
req.alt-api: WDI_WNM_ACTION
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

# WDI_WNM_ACTION enumeration



## -description
<p>The WDI_WNM_ACTION enumeration defines the message type for 802.11v BSS Transition Management action frames.</p>


## -syntax

````
typedef enum _WDI_WNM_ACTION { 
  WDI_WNM_ACTION_BSS_TRANSITION_MANAGEMENT_QUERY     = 6,
  WDI_WNM_ACTION_BSS_TRANSITION_MANAGEMENT_REQUEST   = 7,
  WDI_WNM_ACTION_BSS_TRANSITION_MANAGEMENT_RESPONSE  = 8
} WDI_WNM_ACTION;
````


## -enum-fields
<dl>

### -field WDI_WNM_ACTION_BSS_TRANSITION_MANAGEMENT_QUERY

<dd>
<p>The message is a BSS Transition Management query frame.</p>
</dd>

### -field WDI_WNM_ACTION_BSS_TRANSITION_MANAGEMENT_REQUEST

<dd>
<p>The message is a BSS Transition Management request frame. This is sent by the AP to the client.</p>
</dd>

### -field WDI_WNM_ACTION_BSS_TRANSITION_MANAGEMENT_RESPONSE

<dd>
<p>The message is a BSS Transition Management response frame. This is a response to the above request frame from the AP.</p>
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