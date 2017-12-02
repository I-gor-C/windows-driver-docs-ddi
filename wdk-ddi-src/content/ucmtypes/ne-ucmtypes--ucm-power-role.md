---
UID: NE.ucmtypes._UCM_POWER_ROLE
title: UCM_POWER_ROLE
author: windows-driver-content
description: Defines power roles of USB Type-C connected devices.
old-location: buses\ucm_power_role.htm
old-project: usbref
ms.assetid: 005B2A80-F6F8-42DA-86C3-277676B9168A
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
req.alt-api: UCM_POWER_ROLE
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

# UCM_POWER_ROLE enumeration



## -description
<p>Defines power roles of USB Type-C connected devices. </p>


## -syntax

````
typedef enum _UCM_POWER_ROLE { 
  UcmPowerRoleInvalid  = 0x0,
  UcmPowerRoleSink     = 0x1,
  UcmPowerRoleSource   = 0x2
} UCM_POWER_ROLE;
````


## -enum-fields
<dl>

### -field UcmPowerRoleInvalid

<dd>
<p>Indicates the power role state is invalid.</p>
</dd>

### -field UcmPowerRoleSink

<dd>
<p>Indicates the power role is set to sink power.</p>
</dd>

### -field UcmPowerRoleSource

<dd>
<p>Indicates the power role is set to source power. </p>
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
<a href="..\ucmmanager\ns-ucmmanager--ucm-connector-pd-config.md">UCM_CONNECTOR_PD_CONFIG</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/mt187914">UcmConnectorPowerDirectionChanged</a>
</dt>
<dt>
<a href="..\ucmmanager\nc-ucmmanager-evt-ucm-connector-set-power-role.md">EVT_UCM_CONNECTOR_SET_POWER_ROLE</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [usbref\buses]:%20UCM_POWER_ROLE enumeration%20 RELEASE:%20(11/20/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
