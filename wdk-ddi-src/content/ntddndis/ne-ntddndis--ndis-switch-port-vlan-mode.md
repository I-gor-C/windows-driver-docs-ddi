---
UID: NE.ntddndis._NDIS_SWITCH_PORT_VLAN_MODE
title: NDIS_SWITCH_PORT_VLAN_MODE
author: windows-driver-content
description: The NDIS_SWITCH_PORT_VLAN_MODE enumeration specifies the operation mode of the virtual local area network (VLAN) policy property of a Hyper-V extensible switch port.
old-location: netvista\ndis_switch_port_vlan_mode.htm
old-project: netvista
ms.assetid: 87828768-BE97-4549-AC5B-7CB27D0A9720
ms.author: windowsdriverdev
ms.date: 11/22/2017
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
req.alt-api: NDIS_SWITCH_PORT_VLAN_MODE
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

# NDIS_SWITCH_PORT_VLAN_MODE enumeration



## -description
<p>
<p>The <b>NDIS_SWITCH_PORT_VLAN_MODE</b> enumeration specifies the operation mode of the virtual local area network (VLAN) policy property of a Hyper-V extensible switch port.</p>
</p>
<p>The <b>NDIS_SWITCH_PORT_VLAN_MODE</b> enumeration specifies the operation mode of the virtual local area network (VLAN) policy property of a Hyper-V extensible switch port.</p>


## -syntax

````
typedef enum  { 
  NdisSwitchPortVlanModeUnknown  = 0,
  NdisSwitchPortVlanModeAccess   = 1,
  NdisSwitchPortVlanModeTrunk    = 2,
  NdisSwitchPortVlanModePrivate  = 3,
  NdisSwitchPortVlanModeMax      = 4
} NDIS_SWITCH_PORT_VLAN_MODE, *PNDIS_SWITCH_PORT_VLAN_MODE;
````


## -enum-fields
<dl>

### -field <a id="NdisSwitchPortVlanModeUnknown"></a><a id="ndisswitchportvlanmodeunknown"></a><a id="NDISSWITCHPORTVLANMODEUNKNOWN"></a><b>NdisSwitchPortVlanModeUnknown</b>

<dd>
<p>This value specifies an undefined VLAN operation mode.</p>
</dd>

### -field <a id="NdisSwitchPortVlanModeAccess"></a><a id="ndisswitchportvlanmodeaccess"></a><a id="NDISSWITCHPORTVLANMODEACCESS"></a><b>NdisSwitchPortVlanModeAccess</b>

<dd>
<p>This value specifies an operation mode in which packets from a single VLAN can be sent or received over the port. These packets can be forwarded from other ports on the extensible switch.</p>
</dd>

### -field <a id="NdisSwitchPortVlanModeTrunk"></a><a id="ndisswitchportvlanmodetrunk"></a><a id="NDISSWITCHPORTVLANMODETRUNK"></a><b>NdisSwitchPortVlanModeTrunk</b>

<dd>
<p>This value specifies an operation mode where the port acts as a VLAN trunk. In this mode, packets from multiple VLANs as well as non-VLAN packets can be sent or received over the port. These packets can be forwarded from other ports on the extensible switch.</p>
</dd>

### -field <a id="NdisSwitchPortVlanModePrivate"></a><a id="ndisswitchportvlanmodeprivate"></a><a id="NDISSWITCHPORTVLANMODEPRIVATE"></a><b>NdisSwitchPortVlanModePrivate</b>

<dd>
<p>This value specifies an operation mode where packets from a single VLAN can be sent or received over the port. These packets cannot be forwarded from other ports on the extensible switch.</p>
</dd>

### -field <a id="NdisSwitchPortVlanModeMax"></a><a id="ndisswitchportvlanmodemax"></a><a id="NDISSWITCHPORTVLANMODEMAX"></a><b>NdisSwitchPortVlanModeMax</b>

<dd>
<p>The maximum value for this enumeration. This value might change in future versions of the NDIS header files and binaries.

</p>
</dd>
</dl>

## -remarks
<p>The <b>OperationMode</b> member of the <a href="https://msdn.microsoft.com/library/windows/hardware/hh598243">NDIS_SWITCH_PORT_PROPERTY_VLAN</a> structure is an <b>NDIS_SWITCH_PORT_VLAN_MODE</b> enumeration data type. 

</p>

<p>For more information about extensible switch port policies, see <a href="NULL">Hyper-V Extensible Switch Policies</a>.

</p>

<p>The <b>OperationMode</b> member of the <a href="https://msdn.microsoft.com/library/windows/hardware/hh598243">NDIS_SWITCH_PORT_PROPERTY_VLAN</a> structure is an <b>NDIS_SWITCH_PORT_VLAN_MODE</b> enumeration data type. 

</p>

<p>For more information about extensible switch port policies, see <a href="NULL">Hyper-V Extensible Switch Policies</a>.

</p>

<p>The <b>OperationMode</b> member of the <a href="https://msdn.microsoft.com/library/windows/hardware/hh598243">NDIS_SWITCH_PORT_PROPERTY_VLAN</a> structure is an <b>NDIS_SWITCH_PORT_VLAN_MODE</b> enumeration data type. 

</p>

<p>For more information about extensible switch port policies, see <a href="NULL">Hyper-V Extensible Switch Policies</a>.

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
<a href="https://msdn.microsoft.com/library/windows/hardware/hh598210">NDIS_SWITCH_FORWARDING_DESTINATION_ARRAY</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh598243">NDIS_SWITCH_PORT_PROPERTY_VLAN</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NDIS_SWITCH_PORT_VLAN_MODE enumeration%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
