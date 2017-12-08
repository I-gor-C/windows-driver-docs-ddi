---
UID: NE.wditypes._WDI_P2P_ACTION_FRAME_TYPE
title: WDI_P2P_ACTION_FRAME_TYPE
author: windows-driver-content
description: The WDI_P2P_ACTION_FRAME_TYPE enumeration defines the Wi-Fi Direct action frame types.
old-location: netvista\wdi_p2p_action_frame_type.htm
old-project: netvista
ms.assetid: 3E1C92D2-FFE0-402F-BE14-18AFB03F3FE4
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
req.alt-api: WDI_P2P_ACTION_FRAME_TYPE
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

# WDI_P2P_ACTION_FRAME_TYPE enumeration



## -description
<p>The WDI_P2P_ACTION_FRAME_TYPE enumeration defines the Wi-Fi Direct action frame types.</p>


## -syntax

````
typedef enum _WDI_P2P_ACTION_FRAME_TYPE { 
  WDI_P2P_ACTION_FRAME_GO_NEGOTIATION_REQUEST        = 1,
  WDI_P2P_ACTION_FRAME_GO_NEGOTIATION_RESPONSE       = 2,
  WDI_P2P_ACTION_FRAME_GO_NEGOTIATION_CONFIRM        = 3,
  WDI_P2P_ACTION_FRAME_INVITATION_REQUEST            = 4,
  WDI_P2P_ACTION_FRAME_INVITATION_RESPONSE           = 5,
  WDI_P2P_ACTION_FRAME_PROVISION_DISCOVERY_REQUEST   = 6,
  WDI_P2P_ACTION_FRAME_PROVISION_DISCOVERY_RESPONSE  = 7
} WDI_P2P_ACTION_FRAME_TYPE;
````


## -enum-fields
<dl>

### -field WDI_P2P_ACTION_FRAME_GO_NEGOTIATION_REQUEST

<dd>
<p>Wi-Fi Direct Group Owner Negotiation Request.</p>
</dd>

### -field WDI_P2P_ACTION_FRAME_GO_NEGOTIATION_RESPONSE

<dd>
<p>Wi-Fi Direct Group Owner Negotiation Response.</p>
</dd>

### -field WDI_P2P_ACTION_FRAME_GO_NEGOTIATION_CONFIRM

<dd>
<p>Wi-Fi Direct Group Owner Negotiation Confirmation.</p>
</dd>

### -field WDI_P2P_ACTION_FRAME_INVITATION_REQUEST

<dd>
<p>Wi-Fi Direct Invitation Request.</p>
</dd>

### -field WDI_P2P_ACTION_FRAME_INVITATION_RESPONSE

<dd>
<p>Wi-Fi Direct Invitation Response.</p>
</dd>

### -field WDI_P2P_ACTION_FRAME_PROVISION_DISCOVERY_REQUEST

<dd>
<p>Wi-Fi Direct Provision Discovery Request.</p>
</dd>

### -field WDI_P2P_ACTION_FRAME_PROVISION_DISCOVERY_RESPONSE

<dd>
<p>Wi-Fi Direct Provision Discovery Response.</p>
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