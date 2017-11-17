---
UID: NE.wditypes._WDI_CAN_SUSTAIN_AP_REASON
title: WDI_CAN_SUSTAIN_AP_REASON
author: windows-driver-content
description: The WDI_CAN_SUSTAIN_AP_REASON enumeration defines the reasons the port is ready to receive a OID_WDI_TASK_START_AP request.
old-location: netvista\wdi_can_sustain_ap_reason.htm
ms.assetid: 9AAE4B3F-7C5C-457D-9388-63E6E6AB8A2E
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
req.alt-api: WDI_CAN_SUSTAIN_AP_REASON
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

# WDI_CAN_SUSTAIN_AP_REASON enumeration



## -description
<p>The WDI_CAN_SUSTAIN_AP_REASON enumeration defines the reasons the port is ready to receive a <a href="https://msdn.microsoft.com/library/windows/hardware/dn925964">OID_WDI_TASK_START_AP</a> request.</p>


## -syntax

````
typedef enum _WDI_CAN_SUSTAIN_AP_REASON { 
  WDI_CAN_SUSTAIN_AP_REASON_IHV_START  = 0xFF000000,
  WDI_CAN_SUSTAIN_AP_REASON_IHV_END    = 0xFFFFFFFF
} WDI_CAN_SUSTAIN_AP_REASON;
````


## -enum-fields
<dl>

### -field <a id="WDI_CAN_SUSTAIN_AP_REASON_IHV_START"></a><a id="wdi_can_sustain_ap_reason_ihv_start"></a><b>WDI_CAN_SUSTAIN_AP_REASON_IHV_START</b>

<dd>
<p>The start value of possible IHV-specified reasons.</p>
</dd>

### -field <a id="WDI_CAN_SUSTAIN_AP_REASON_IHV_END"></a><a id="wdi_can_sustain_ap_reason_ihv_end"></a><b>WDI_CAN_SUSTAIN_AP_REASON_IHV_END</b>

<dd>
<p>The end value of possible IHV-specified reasons.</p>
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