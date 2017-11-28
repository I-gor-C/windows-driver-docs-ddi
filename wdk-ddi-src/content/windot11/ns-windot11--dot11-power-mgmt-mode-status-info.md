---
UID: NS.windot11._DOT11_POWER_MGMT_MODE_STATUS_INFO
title: DOT11_POWER_MGMT_MODE_STATUS_INFO
author: windows-driver-content
description: The DOT11_POWER_MGMT_MODE_STATUS_INFO structure describes the power mode of the hardware.
old-location: netvista\dot11_power_mgmt_mode_status_info.htm
old-project: netvista
ms.assetid: A373EA34-A7CF-47B3-8194-438BE7F4FC9C
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: DOT11_POWER_MGMT_MODE_STATUS_INFO, DOT11_POWER_MGMT_MODE_STATUS_INFO, *PDOT11_POWER_MGMT_MODE_STATUSINFO
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: windot11.h
req.include-header: Windot11.h
req.target-type: Windows
req.target-min-winverclnt: Versions: Supported in Windows 8
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: DOT11_POWER_MGMT_MODE_STATUS_INFO
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

# DOT11_POWER_MGMT_MODE_STATUS_INFO structure



## -description

## -syntax

````
typedef struct _DOT11_POWER_MGMT_MODE_STATUS_INFO {
  NDIS_OBJECT_HEADER      Header;
  DOT11_POWER_MODE        PowerSaveMode;
  ULONG                   uPowerSaveLevel;
  DOT11_POWER_MODE_REASON Reason;
} DOT11_POWER_MGMT_MODE_STATUS_INFO, *PDOT11_POWER_MGMT_MODE_STATUS_INFO;
````


## -struct-fields
<dl>

### -field <b>Header</b>

<dd>
<p>The type, revision, and size of the DOT11_POWER_MGMT_MODE_STATUS_INFO structure. The required settings for the members of <b>Header</b> are the following.</p>
<table>
<tr>
<th>Member</th>
<th>Setting</th>
</tr>
<tr>
<td><b>Type</b></td>
<td>NDIS_OBJECT_TYPE_DEFAULT</td>
</tr>
<tr>
<td><b>Revision</b></td>
<td>DOT11_POWER_MGMT_MODE_STATUS_INFO_REVISION_1</td>
</tr>
<tr>
<td><b>Size</b></td>
<td>DOT11_SIZEOF_POWER_MGMT_MODE_STATUS_INFO_REVISION_1</td>
</tr>
</table>
<p> </p>
</dd>

### -field <b>PowerSaveMode</b>

<dd>
<p>The current power mode of the hardware. The mode may be <b>dot11_power_mode_active</b> or <b>dot11_power_mode_powersave</b>, but should not be <b>dot11_power_mode_unknown</b>.</p>
</dd>

### -field <b>uPowerSaveLevel</b>

<dd>
<p>One of the following values describing power saving levels:</p>
<table>
<tr>
<th>Value</th>
<th>Meaning</th>
</tr>
<tr>
<td>DOT11_POWER_SAVING_NO_POWER_SAVING</td>
<td>No power saving</td>
</tr>
<tr>
<td>DOT11_POWER_SAVING_FAST_PSP</td>
<td>Fast PSP</td>
</tr>
<tr>
<td>DOT11_POWER_SAVING_MAX_PSP</td>
<td>Maximum PSP</td>
</tr>
<tr>
<td>DOT11_POWER_SAVING_MAXIMUM_LEVEL</td>
<td>Maximum power saving level</td>
</tr>
</table>
<p> </p>
</dd>

### -field <b>Reason</b>

<dd>
<p>Reason that the device changed into the current power mode.</p>
</dd>
</dl>

## -remarks
<p>At each transition of the mode change, a device should remember the reason it made the last change.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Versions: Supported in Windows 8</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Windot11.h (include Windot11.h)</dt>
</dl>
</td>
</tr>
</table>