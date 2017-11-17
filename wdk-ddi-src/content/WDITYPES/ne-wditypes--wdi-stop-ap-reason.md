---
UID: NE.wditypes._WDI_STOP_AP_REASON
title: WDI_STOP_AP_REASON
author: windows-driver-content
description: The WDI_STOP_AP_REASON enumeration defines the reasons an adapter cannot sustain 802.11 Access Point (AP) functionality on any of the PHYs.
old-location: netvista\wdi_stop_ap_reason.htm
ms.assetid: F0CACC25-2F7B-431A-8AAB-CBE495178CC1
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
req.alt-api: WDI_STOP_AP_REASON
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

# WDI_STOP_AP_REASON enumeration



## -description
<p>The WDI_STOP_AP_REASON enumeration defines the reasons an adapter cannot sustain 802.11 Access Point (AP) functionality on any of the PHYs.</p>


## -syntax

````
typedef enum _WDI_STOP_AP_REASON { 
  WDI_STOP_AP_REASON_FREQUENCY_NOT_AVAILABLE  = 1,
  WDI_STOP_AP_REASON_CHANNEL_NOT_AVAILABLE    = 2,
  WDI_STOP_AP_REASON_AP_ACTIVE                = 3,
  WDI_STOP_AP_REASON_IHV_START                = 0xFF000000,
  WDI_STOP_AP_REASON_IHV_END                  = 0xFFFFFFFF
} WDI_STOP_AP_REASON;
````


## -enum-fields
<dl>

### -field <a id="WDI_STOP_AP_REASON_FREQUENCY_NOT_AVAILABLE"></a><a id="wdi_stop_ap_reason_frequency_not_available"></a><b>WDI_STOP_AP_REASON_FREQUENCY_NOT_AVAILABLE</b>

<dd>
<p>The adapter determined that no valid operating frequency is available.</p>
</dd>

### -field <a id="WDI_STOP_AP_REASON_CHANNEL_NOT_AVAILABLE"></a><a id="wdi_stop_ap_reason_channel_not_available"></a><b>WDI_STOP_AP_REASON_CHANNEL_NOT_AVAILABLE</b>

<dd>
<p>The adapter determined that no operating channel is available.</p>
</dd>

### -field <a id="WDI_STOP_AP_REASON_AP_ACTIVE"></a><a id="wdi_stop_ap_reason_ap_active"></a><b>WDI_STOP_AP_REASON_AP_ACTIVE</b>

<dd>
<p>The adapter determined that an AP is already active on another 802.11 MAC entity for this physical wireless LAN adapter.</p>
</dd>

### -field <a id="WDI_STOP_AP_REASON_IHV_START"></a><a id="wdi_stop_ap_reason_ihv_start"></a><b>WDI_STOP_AP_REASON_IHV_START</b>

<dd>
<p>The start value of possible IHV-specified reasons.</p>
</dd>

### -field <a id="WDI_STOP_AP_REASON_IHV_END"></a><a id="wdi_stop_ap_reason_ihv_end"></a><b>WDI_STOP_AP_REASON_IHV_END</b>

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