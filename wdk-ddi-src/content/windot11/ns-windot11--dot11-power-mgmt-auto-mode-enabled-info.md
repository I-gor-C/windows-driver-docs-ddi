---
UID: NS.windot11._DOT11_POWER_MGMT_AUTO_MODE_ENABLED_INFO
title: DOT11_POWER_MGMT_AUTO_MODE_ENABLED_INFO
author: windows-driver-content
description: The DOT11_POWER_MGMT_AUTO_MODE_ENABLED structure describes to a device whether to automatically manage its power saving mode.
old-location: netvista\dot11_power_mgmt_auto_mode_enabled_info.htm
old-project: netvista
ms.assetid: 9C75544F-A14C-4741-91FC-434AE1872A6E
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: DOT11_POWER_MGMT_AUTO_MODE_ENABLED_INFO, DOT11_POWER_MGMT_AUTO_MODE_ENABLED_INFO, *PDOT11_POWER_MGMT_AUTO_MODE_ENABLED_INFO
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
req.alt-api: DOT11_POWER_MGMT_AUTO_MODE_ENABLED_INFO
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

# DOT11_POWER_MGMT_AUTO_MODE_ENABLED_INFO structure



## -description

## -syntax

````
typedef struct _DOT11_POWER_MGMT_AUTO_MODE_ENABLED_INFO {
  NDIS_OBJECT_HEADER Header;
  BOOLEAN            bEnabled;
} DOT11_POWER_MGMT_AUTO_MODE_ENABLED_INFO, *PDOT11_POWER_MGMT_AUTO_MODE_ENABLED_INFO;
````


## -struct-fields
<dl>

### -field <b>Header</b>

<dd>
<p>The type, revision, and size of the DOT11_POWER_MGMT_AUTO_MODE_ENABLED_INFO structure. The required settings for the members of <b>Header</b> are the following.</p>
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
<td>DOT11_POWER_MGMT_AUTO_MODE_ENABLED_REVISION_1</td>
</tr>
<tr>
<td><b>Size</b></td>
<td>DOT11_SIZEOF_POWER_MGMT_AUTO_MODE_ENABLE_INFO_REVISION_1</td>
</tr>
</table>
<p> </p>
</dd>

### -field <b>bEnabled</b>

<dd>
<p>Windows sets this member to TRUE to indicate to the device to automatically manage its power saving mode. Windows set this to FALSE to indicate to the device to stop automatically managing its power save mode.</p>
</dd>
</dl>

## -remarks
<p>When Windows sets the device to auto power saving mode, devices must remain in this mode until Windows issues another request with <b>bEnabled</b> set to FALSE. In auto power saving mode, Windows may issue a <a href="https://msdn.microsoft.com/library/windows/hardware/ff569402">OID_DOT11_POWER_MGMT_REQUEST</a><i>set</i> request that hardware can use as a hint to adjust its power management.</p>

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