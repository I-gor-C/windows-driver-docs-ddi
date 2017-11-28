---
UID: NE.ucmtypes._UCM_TYPEC_CURRENT
title: UCM_TYPEC_CURRENT
author: windows-driver-content
description: Defines different Type-C current levels, as defined in the Type-C specification.
old-location: buses\ucm_type_c_current.htm
old-project: usbref
ms.assetid: 5A603C0E-BBB8-4909-B7B0-EAADF428CB5F
ms.author: windowsdriverdev
ms.date: 11/20/2017
ms.keywords: UCMTCPCI_PORT_CONTROLLER_SET_TRANSMIT_IN_PARAMS, UCMTCPCI_PORT_CONTROLLER_SET_TRANSMIT_IN_PARAMS, *PUCMTCPCI_PORT_CONTROLLER_SET_TRANSMIT_IN_PARAMS
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: ucmtypes.h
req.include-header: Ucmcx.h
req.target-type: Windows
req.target-min-winverclnt: Windows 10
req.target-min-winversvr: Windows Server 2016
req.kmdf-ver: 1.15
req.umdf-ver: 2.15
req.alt-api: UCM_TYPEC_CURRENT
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
req.iface: 
req.product: Windows 10 or later.
---

# UCM_TYPEC_CURRENT enumeration



## -description
<p>Defines different Type-C current levels, as defined in the Type-C specification.</p>


## -syntax

````
typedef enum _UCM_TYPE_C_CURRENT { 
  UcmTypeCCurrentInvalid     = 0x0,
  UcmTypeCCurrentDefaultUsb  = 0x1,
  UcmTypeCCurrent1500mA      = 0x2,
  UcmTypeCCurrent3000mA      = 0x4
} UCM_TYPEC_CURRENT;
````


## -enum-fields
<dl>

### -field <a id="UcmTypeCCurrentInvalid"></a><a id="ucmtypeccurrentinvalid"></a><a id="UCMTYPECCURRENTINVALID"></a><b>UcmTypeCCurrentInvalid</b>

<dd>
<p>Indicates the power sourcing current state is invalid.</p>
</dd>

### -field <a id="UcmTypeCCurrentDefaultUsb"></a><a id="ucmtypeccurrentdefaultusb"></a><a id="UCMTYPECCURRENTDEFAULTUSB"></a><b>UcmTypeCCurrentDefaultUsb</b>

<dd>
<p>Indicates the power sourcing current is the default USB current.</p>
</dd>

### -field <a id="UcmTypeCCurrent1500mA"></a><a id="ucmtypeccurrent1500ma"></a><a id="UCMTYPECCURRENT1500MA"></a><b>UcmTypeCCurrent1500mA</b>

<dd>
<p>Indicates the power sourcing current is 1500 mA.</p>
</dd>

### -field <a id="UcmTypeCCurrent3000mA"></a><a id="ucmtypeccurrent3000ma"></a><a id="UCMTYPECCURRENT3000MA"></a><b>UcmTypeCCurrent3000mA</b>

<dd>
<p>Indicates the power sourcing current is 3000 mA.</p>
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
<a href="https://msdn.microsoft.com/library/windows/hardware/mt187915">UcmConnectorTypeCAttach</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/mt187916">UcmConnectorTypeCCurrentAdChanged</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [usbref\buses]:%20UCM_TYPEC_CURRENT enumeration%20 RELEASE:%20(11/20/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
