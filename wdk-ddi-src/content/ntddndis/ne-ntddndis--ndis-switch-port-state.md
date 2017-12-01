---
UID: NE.ntddndis._NDIS_SWITCH_PORT_STATE
title: NDIS_SWITCH_PORT_STATE
author: windows-driver-content
description: The NDIS_SWITCH_PORT_STATE enumeration specifies the current state of the Hyper-V extensible switch port.
old-location: netvista\ndis_switch_port_state.htm
old-project: netvista
ms.assetid: BEF37F32-036D-4381-93B3-C159ABCFC3F9
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: GET_CONFIGURATION_IOCTL_INPUT, GET_CONFIGURATION_IOCTL_INPUT, *PGET_CONFIGURATION_IOCTL_INPUT
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: ntddndis.h
req.include-header: Ndis.h
req.target-type: Windows
req.target-min-winverclnt: Supported in NDIS 6.30 and later.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: NDIS_SWITCH_PORT_STATE
req.alt-loc: Ntddndis.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: PASSIVE_LEVEL
req.iface: 
---

# NDIS_SWITCH_PORT_STATE enumeration



## -description
<p>The <b>NDIS_SWITCH_PORT_STATE</b> enumeration specifies the current state of the Hyper-V extensible switch port. </p>


## -syntax

````
typedef enum _NDIS_SWITCH_PORT_STATE { 
  NdisSwitchPortStateUnknown   = 0,
  NdisSwitchPortStateCreated   = 1,
  NdisSwitchPortStateTeardown  = 2,
  NdisSwitchPortStateDeleted   = 3
} NDIS_SWITCH_PORT_STATE;
````


## -enum-fields
<dl>

### -field <a id="NdisSwitchPortStateUnknown"></a><a id="ndisswitchportstateunknown"></a><a id="NDISSWITCHPORTSTATEUNKNOWN"></a><b>NdisSwitchPortStateUnknown</b>

<dd>
<p>This value specifies an undefined port state. This value is unused.</p>
</dd>

### -field <a id="NdisSwitchPortStateCreated"></a><a id="ndisswitchportstatecreated"></a><a id="NDISSWITCHPORTSTATECREATED"></a><b>NdisSwitchPortStateCreated</b>

<dd>
<p>This value specifies that the port is in the created state. </p>
</dd>

### -field <a id="NdisSwitchPortStateTeardown"></a><a id="ndisswitchportstateteardown"></a><a id="NDISSWITCHPORTSTATETEARDOWN"></a><b>NdisSwitchPortStateTeardown</b>

<dd>
<p>This value specifies that the port is being torn down.</p>
</dd>

### -field <a id="NdisSwitchPortStateDeleted"></a><a id="ndisswitchportstatedeleted"></a><a id="NDISSWITCHPORTSTATEDELETED"></a><b>NdisSwitchPortStateDeleted</b>

<dd>
<p>This value specifies that the port has been deleted. </p>
</dd>
</dl>

## -remarks
<p>The <b>PortState</b>  member of the <a href="..\fwpsk\ns-fwpsk--ndis-switch-port-parameters.md">NDIS_SWITCH_PORT_PARAMETER</a> structure is an <b>NDIS_SWITCH_PORT_STATE</b> enumeration data type. 
</p>

<p>For more information about extensible switch port states, see <a href="NULL">Overview of Hyper-V Extensible Switch Ports</a>. 
</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Supported in NDIS 6.30 and later.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ntddndis.h (include Ndis.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt><b></b></dt>
<dt>
<a href="..\fwpsk\ns-fwpsk--ndis-switch-port-parameters.md">NDIS_SWITCH_PORT_PARAMETER</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NDIS_SWITCH_PORT_STATE enumeration%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
