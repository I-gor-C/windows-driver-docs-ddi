---
UID: NE.ucmtypes._UCM_TYPEC_OPERATING_MODE
title: UCM_TYPEC_OPERATING_MODE
author: windows-driver-content
description: Defines operating modes of a USB Type-C connector.
old-location: buses\ucm_type_c_operating_mode.htm
ms.assetid: B64849A6-DDB1-4BD1-B4B6-1E38DE9237E5
ms.author: windowsdriverdev
ms.date: 11/3/2017
ms.topic: enum
ms.prod: windows-hardware
ms.technology: usbref
req.header: ucmtypes.h
req.include-header: Ucmcx.h
req.target-type: Windows
req.target-min-winverclnt: Windows 10
req.target-min-winversvr: Windows Server 2016
req.kmdf-ver: 1.15
req.umdf-ver: 2.15
req.alt-api: UCM_TYPEC_OPERATING_MODE
req.alt-loc: Ucmtypes.h
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
ms.keywords: UCMTCPCI_PORT_CONTROLLER_SET_TRANSMIT_IN_PARAMS, UCMTCPCI_PORT_CONTROLLER_SET_TRANSMIT_IN_PARAMS, *PUCMTCPCI_PORT_CONTROLLER_SET_TRANSMIT_IN_PARAMS
req.iface: 
req.product: Windows 10 or later.
---

# UCM_TYPEC_OPERATING_MODE enumeration



## -description
<p>Defines operating modes of a USB Type-C connector.</p>


## -syntax

````
typedef enum _UCM_TYPEC_OPERATING_MODE { 
  UcmTypeCOperatingModeInvalid  = 0x0,
  UcmTypeCOperatingModeDfp      = 0x1,
  UcmTypeCOperatingModeUfp      = 0x2,
  UcmTypeCOperatingModeDrp      = 0x4
} UCM_TYPEC_OPERATING_MODE;
````


## -enum-fields
<dl>

### -field <a id="UcmTypeCOperatingModeInvalid"></a><a id="ucmtypecoperatingmodeinvalid"></a><a id="UCMTYPECOPERATINGMODEINVALID"></a><b>UcmTypeCOperatingModeInvalid</b>

<dd>
<p>Indicates the operating mode is invalid.</p>
</dd>

### -field <a id="UcmTypeCOperatingModeDfp"></a><a id="ucmtypecoperatingmodedfp"></a><a id="UCMTYPECOPERATINGMODEDFP"></a><b>UcmTypeCOperatingModeDfp</b>

<dd>
<p>Indicates the operating mode is set to downstream-facing port.</p>
</dd>

### -field <a id="UcmTypeCOperatingModeUfp"></a><a id="ucmtypecoperatingmodeufp"></a><a id="UCMTYPECOPERATINGMODEUFP"></a><b>UcmTypeCOperatingModeUfp</b>

<dd>
<p>Indicates the operating mode is set to upstream-facing port.</p>
</dd>

### -field <a id="UcmTypeCOperatingModeDrp"></a><a id="ucmtypecoperatingmodedrp"></a><a id="UCMTYPECOPERATINGMODEDRP"></a><b>UcmTypeCOperatingModeDrp</b>

<dd>
<p>Indicates the operating mode is set to dual-role port. </p>
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
<p>Minimum KMDF version</p>
</th>
<td width="70%">
<p>1.15</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Minimum UMDF version</p>
</th>
<td width="70%">
<p>2.15</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ucmtypes.h (include Ucmcx.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/mt187931">UCM_CONNECTOR_TYPEC_CONFIG_INIT</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [usbref\buses]:%20UCM_TYPEC_OPERATING_MODE enumeration%20 RELEASE:%20(11/3/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
