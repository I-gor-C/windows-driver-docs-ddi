---
UID: NE.wditypes._WDI_RADIO_MEASUREMENT_ACTION
title: WDI_RADIO_MEASUREMENT_ACTION
author: windows-driver-content
description: The WDI_RADIO_MEASUREMENT_ACTION enumeration defines the radio measurement actions.
old-location: netvista\wdi_radio_measurement_action.htm
old-project: netvista
ms.assetid: AA17E666-5934-453D-B55D-98F8616F6369
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
req.alt-api: WDI_RADIO_MEASUREMENT_ACTION
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

# WDI_RADIO_MEASUREMENT_ACTION enumeration



## -description
<p>The WDI_RADIO_MEASUREMENT_ACTION enumeration defines the radio measurement actions.</p>


## -syntax

````
typedef enum _WDI_RADIO_MEASUREMENT_ACTION { 
  WDI_RADIO_MEASUREMENT_ACTION_NEIGHBOR_REPORT_REQUEST   = 4,
  WDI_RADIO_MEASUREMENT_ACTION_NEIGHBOR_REPORT_RESPONSE  = 5
} WDI_RADIO_MEASUREMENT_ACTION;
````


## -enum-fields
<dl>

### -field <a id="WDI_RADIO_MEASUREMENT_ACTION_NEIGHBOR_REPORT_REQUEST"></a><a id="wdi_radio_measurement_action_neighbor_report_request"></a><b>WDI_RADIO_MEASUREMENT_ACTION_NEIGHBOR_REPORT_REQUEST</b>

<dd>
<p>This refers to the neighbor report request action frame sent by the client to the AP.</p>
</dd>

### -field <a id="WDI_RADIO_MEASUREMENT_ACTION_NEIGHBOR_REPORT_RESPONSE"></a><a id="wdi_radio_measurement_action_neighbor_report_response"></a><b>WDI_RADIO_MEASUREMENT_ACTION_NEIGHBOR_REPORT_RESPONSE</b>

<dd>
<p>This refers to the neighbor report response action frame from the AP.</p>
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