---
UID: NE.ntddndis._NDIS_SWITCH_PORT_TYPE
title: NDIS_SWITCH_PORT_TYPE
author: windows-driver-content
description: The NDIS_SWITCH_PORT_TYPE enumeration specifies the type of a Hyper-V extensible switch port.
old-location: netvista\ndis_switch_port_type.htm
old-project: netvista
ms.assetid: 4FCE88BC-6FA1-44D0-9BC1-3065A5EEE1A0
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
req.alt-api: NDIS_SWITCH_PORT_TYPE
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

# NDIS_SWITCH_PORT_TYPE enumeration



## -description
<p>
<p>The <b>NDIS_SWITCH_PORT_TYPE</b> enumeration specifies the type of  a Hyper-V extensible switch port.  </p>
</p>
<p>The <b>NDIS_SWITCH_PORT_TYPE</b> enumeration specifies the type of  a Hyper-V extensible switch port.  </p>


## -syntax

````
typedef enum _NDIS_SWITCH_PORT_TYPE { 
  NdisSwitchPortTypeGeneric    = 0,
  NdisSwitchPortTypeExternal   = 1,
  NdisSwitchPortTypeSynthetic  = 2,
  NdisSwitchPortTypeEmulated   = 3,
  NdisSwitchPortTypeInternal   = 4
} NDIS_SWITCH_PORT_TYPE, *PNDIS_SWITCH_PORT_TYPE;
````


## -enum-fields
<dl>

### -field <a id="NdisSwitchPortTypeGeneric"></a><a id="ndisswitchporttypegeneric"></a><a id="NDISSWITCHPORTTYPEGENERIC"></a><b>NdisSwitchPortTypeGeneric</b>

<dd>
<p>This value specifies a generic port type that was created with an earlier version of the extensible switch WMI management platform.</p>
</dd>

### -field <a id="NdisSwitchPortTypeExternal"></a><a id="ndisswitchporttypeexternal"></a><a id="NDISSWITCHPORTTYPEEXTERNAL"></a><b>NdisSwitchPortTypeExternal</b>

<dd>
<p>This value specifies a port that is connected to an external network adapter. This  adapter is exposed in the management operating system that runs in the Hyper-V parent partition. </p>
<p>The external network adapter provides the connection to the  physical network interface that is available on the host. This allows processes that run in either the management or guest operating systems to send or receive packets over the extensible switch.</p>
<div class="alert"><b>Note</b>  An extensible switch supports no more than one external network adapter. The external network adapter can be bound to one or more underlying physical network adapters. For more information, see <a href="NULL">External Network Adapters</a>.</div>
<div> </div>
</dd>

### -field <a id="NdisSwitchPortTypeSynthetic"></a><a id="ndisswitchporttypesynthetic"></a><a id="NDISSWITCHPORTTYPESYNTHETIC"></a><b>NdisSwitchPortTypeSynthetic</b>

<dd>
<p>This value specifies a port that is connected to a synthetic network adapter. This adapter is exposed in a guest operating system that runs in a Hyper-V child partition.</p>
<div class="alert"><b>Note</b>  A synthetic network adapter is a type of virtual machine (VM) network adapter. This adapter is exposed in a guest operating system that is running Windows Vista or a later version of Windows.</div>
<div> </div>
</dd>

### -field <a id="NdisSwitchPortTypeEmulated"></a><a id="ndisswitchporttypeemulated"></a><a id="NDISSWITCHPORTTYPEEMULATED"></a><b>NdisSwitchPortTypeEmulated</b>

<dd>
<p>This value specifies a port that is connected to an emulated network adapter. This adapter is exposed in a guest operating system.</p>
<div class="alert"><b>Note</b>  An emulated network adapter is a type of VM network adapter. This adapter can be exposed in a guest operating system that is running Windows XP or a non-Windows operating system.</div>
<div> </div>
</dd>

### -field <a id="NdisSwitchPortTypeInternal"></a><a id="ndisswitchporttypeinternal"></a><a id="NDISSWITCHPORTTYPEINTERNAL"></a><b>NdisSwitchPortTypeInternal</b>

<dd>
<p>This value specifies a port that is connected to an internal network adapter. This adapter is exposed in the management operating system that runs in the Hyper-V parent partition. </p>
<p>The internal network adapter provides access to an extensible switch for processes that run in the management operating system. This allows these processes to send or receive packets over the extensible switch.</p>
<div class="alert"><b>Note</b>  An extensible switch supports no more than one internal network adapter. For more information, see <a href="NULL">Internal Network Adapters</a>.</div>
<div> </div>
</dd>
</dl>

## -remarks
<p>The <b>PortType</b> member of the <a href="..\fwpsk\ns-fwpsk--ndis-switch-port-parameters.md">NDIS_SWITCH_PORT_PARAMETERS</a> structure is an <b>NDIS_SWITCH_PORT_TYPE</b> enumeration data type. 

</p>

<p>For more information on the extensible switch ports, see <a href="NULL">Hyper-V Extensible Switch Ports</a>.

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
<a href="..\fwpsk\ns-fwpsk--ndis-switch-port-parameters.md">NDIS_SWITCH_PORT_PARAMETERS</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NDIS_SWITCH_PORT_TYPE enumeration%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
