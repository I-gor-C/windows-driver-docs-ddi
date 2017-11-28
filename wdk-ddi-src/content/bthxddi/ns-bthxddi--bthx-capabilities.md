---
UID: NS.bthxddi._BTHX_CAPABILITIES
title: BTHX_CAPABILITIES
author: windows-driver-content
description: The BTHX_CAPABILITIES structure describes the capabilities of the Bluetooth Extensible Transport Driver.
old-location: bltooth\bthx_capabilities.htm
old-project: bltooth
ms.assetid: BEC06C82-E103-4255-ACDD-9FB28E8E2DE5
ms.author: windowsdriverdev
ms.date: 10/23/2017
ms.keywords: BTHX_CAPABILITIES, BTHX_CAPABILITIES, *PBTHX_CAPABILITIES
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: bthxddi.h
req.include-header: BthXDDI.h
req.target-type: Windows
req.target-min-winverclnt: Versions: Supported starting with  Windows 8.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: BTHX_CAPABILITIES
req.alt-loc: BthXDDI.h
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
---

# BTHX_CAPABILITIES structure



## -description
<p>The BTHX_CAPABILITIES structure describes the capabilities of the Bluetooth Extensible Transport Driver.</p>


## -syntax

````
typedef struct _BTHX_CAPABILITIES {
  ULONG            MaxAclTransferInSize;
  BTHX_SCO_SUPPORT ScoSupport;
  ULONG            MaxScoChannels;
  BOOLEAN          IsDeviceIdleCapable;
  BOOLEAN          IsDeviceWakeCapable;
} BTHX_CAPABILITIES, *PBTHX_CAPABILITIES;
````


## -struct-fields
<dl>

### -field <b>MaxAclTransferInSize</b>

<dd>
<p>The maximum size, in bytes, of the ACL packets the transport layer can accept.</p>
</dd>

### -field <b>ScoSupport</b>

<dd>
<p>The type of SCO supported. This must be set to <b>ScoSupportHCIBypass</b>.</p>
</dd>

### -field <b>MaxScoChannels</b>

<dd>
<p>The maximum supported number of SCO channels. This must be set to 1.</p>
</dd>

### -field <b>IsDeviceIdleCapable</b>

<dd>
<p>Whether the device supports idle/sleep power state. TRUE if the device can support idle (in low duty cycle state), else FALSE.</p>
</dd>

### -field <b>IsDeviceWakeCapable</b>

<dd>
<p>Whether the device supports remote wake. TRUE if the device supports waking the system from sleep, else FALSE.</p>
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
<p>Versions: Supported starting with  Windows 8.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>BthXDDI.h (include BthXDDI.h)</dt>
</dl>
</td>
</tr>
</table>