---
UID: NE.windot11._DOT11_POWER_MODE_REASON
title: DOT11_POWER_MODE_REASON
author: windows-driver-content
description: The DOT11_POWER_MODE_REASON lists the different reasons for changes to auto power save mode state.
old-location: netvista\dot11_power_mode_reason.htm
old-project: netvista
ms.assetid: 0B8402B5-CFDA-402F-BA7A-A44478333C04
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: PRINTER_EVENT_ATTRIBUTES_INFO, PRINTER_EVENT_ATTRIBUTES_INFO, *PPRINTER_EVENT_ATTRIBUTES_INFO
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: windot11.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: Supported starting with  Windows 8.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: DOT11_POWER_MODE_REASON
req.alt-loc: Windot11.h
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

# DOT11_POWER_MODE_REASON enumeration



## -description

## -syntax

````
typedef enum _DOT11_POWER_MODE_REASON { 
  dot11_power_mode_reason_no_change             = 0,
  dot11_power_mode_reason_noncompliant_AP       = 1,
  dot11_power_mode_reason_legacy_WFD_device     = 2,
  dot11_power_mode_reason_compliant_AP          = 3,
  dot11_power_mode_reason_compliant_WFD_device  = 4,
  dot11_power_mode_reason_others                = 5
} DOT11_POWER_MODE_REASON;
````


## -enum-fields
<dl>

### -field <a id="dot11_power_mode_reason_no_change"></a><a id="DOT11_POWER_MODE_REASON_NO_CHANGE"></a><b>dot11_power_mode_reason_no_change</b>

<dd>
<p>Device is initially in this state and has not changed since.</p>
</dd>

### -field <a id="dot11_power_mode_reason_noncompliant_AP"></a><a id="dot11_power_mode_reason_noncompliant_ap"></a><a id="DOT11_POWER_MODE_REASON_NONCOMPLIANT_AP"></a><b>dot11_power_mode_reason_noncompliant_AP</b>

<dd>
<p>AP is not compliant. As to be in CAM.</p>
</dd>

### -field <a id="dot11_power_mode_reason_legacy_WFD_device"></a><a id="dot11_power_mode_reason_legacy_wfd_device"></a><a id="DOT11_POWER_MODE_REASON_LEGACY_WFD_DEVICE"></a><b>dot11_power_mode_reason_legacy_WFD_device</b>

<dd>
<p>WFD device is legacy.</p>
</dd>

### -field <a id="dot11_power_mode_reason_compliant_AP"></a><a id="dot11_power_mode_reason_compliant_ap"></a><a id="DOT11_POWER_MODE_REASON_COMPLIANT_AP"></a><b>dot11_power_mode_reason_compliant_AP</b>

<dd>
<p>AP is compliant.</p>
</dd>

### -field <a id="dot11_power_mode_reason_compliant_WFD_device"></a><a id="dot11_power_mode_reason_compliant_wfd_device"></a><a id="DOT11_POWER_MODE_REASON_COMPLIANT_WFD_DEVICE"></a><b>dot11_power_mode_reason_compliant_WFD_device</b>

<dd>
<p>All connected WFD device can do PSM.</p>
</dd>

### -field <a id="dot11_power_mode_reason_others"></a><a id="DOT11_POWER_MODE_REASON_OTHERS"></a><b>dot11_power_mode_reason_others</b>

<dd>
<p>Other reason.</p>
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
<p>Supported starting with  Windows 8.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Windot11.h</dt>
</dl>
</td>
</tr>
</table>