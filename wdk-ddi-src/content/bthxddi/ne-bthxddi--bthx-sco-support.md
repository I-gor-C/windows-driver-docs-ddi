---
UID: NE.bthxddi._BTHX_SCO_SUPPORT
title: BTHX_SCO_SUPPORT
author: windows-driver-content
description: The BTHX_SCO_SUPPORT enumeration lists the different types of SCO supported by the transport driver.
old-location: bltooth\bthx_sco_support.htm
old-project: bltooth
ms.assetid: A9B303C7-868D-47EB-8279-9F655F58630C
ms.author: windowsdriverdev
ms.date: 11/27/2017
ms.keywords: BTHDDI_SDP_PARSE_INTERFACE, BTHDDI_SDP_PARSE_INTERFACE, *PBTHDDI_SDP_PARSE_INTERFACE
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: bthxddi.h
req.include-header: BthXDDI.h
req.target-type: Windows
req.target-min-winverclnt: Versions: Supported starting with  Windows 8.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: BTHX_SCO_SUPPORT
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
req.irql: 
req.iface: 
---

# BTHX_SCO_SUPPORT enumeration



## -description
<p>The BTHX_SCO_SUPPORT enumeration lists the different types of SCO supported by the transport driver.</p>


## -syntax

````
typedef enum _BTHX_SCO_SUPPORT { 
  ScoSupportNone       = 0,
  ScoSupportHCI        = 1,
  ScoSupportHCIBypass  = 2
} BTHX_SCO_SUPPORT;
````


## -enum-fields
<dl>

### -field <a id="ScoSupportNone"></a><a id="scosupportnone"></a><a id="SCOSUPPORTNONE"></a><b>ScoSupportNone</b>

<dd>
<p>SCO is not supported.</p>
</dd>

### -field <a id="ScoSupportHCI"></a><a id="scosupporthci"></a><a id="SCOSUPPORTHCI"></a><b>ScoSupportHCI</b>

<dd>
<p>SCO data passes through the HCI layer (stack).</p>
</dd>

### -field <a id="ScoSupportHCIBypass"></a><a id="scosupporthcibypass"></a><a id="SCOSUPPORTHCIBYPASS"></a><b>ScoSupportHCIBypass</b>

<dd>
<p>SCO data does not pass through the HCI layer but through a sideband mechanism like an I2S channel.</p>
</dd>
</dl>

## -remarks
<p>Upon starting, the Bluetooth stack will query the transport driver for its capabilities by sending the <a href="..\bthxddi\ni-bthxddi-ioctl-bthx-query-capabilities.md">IOCTL_BTHX_QUERY_CAPABILITIES</a> IOCTL.

The output buffer of this IOCTL is defined by the <a href="..\bthxddi\ns-bthxddi--bthx-capabilities.md">BTHX_CAPABILITIES</a> structure which contains the 
BTHX_SCO_SUPPORT structure.

The transport driver must specify <b>ScoSupportHCIBypass</b>.</p>

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