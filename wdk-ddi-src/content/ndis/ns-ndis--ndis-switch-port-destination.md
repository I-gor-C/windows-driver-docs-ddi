---
UID: NS.ndis._NDIS_SWITCH_PORT_DESTINATION
title: NDIS_SWITCH_PORT_DESTINATION
author: windows-driver-content
description: The NDIS_SWITCH_PORT_DESTINATION structure specifies the Hyper-V extensible switch destination port to which a packet will be delivered.
old-location: netvista\ndis_switch_port_destination.htm
old-project: netvista
ms.assetid: EC7FFB5E-F50B-40C4-B4B7-0A11A374EBD0
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: NDIS_SWITCH_PORT_DESTINATION, NDIS_SWITCH_PORT_DESTINATION, *PNDIS_SWITCH_PORT_DESTINATION
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: ndis.h
req.include-header: Ndis.h
req.target-type: Windows
req.target-min-winverclnt: Supported in NDIS 6.30 and later.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: NDIS_SWITCH_PORT_DESTINATION
req.alt-loc: Ndis.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: See Remarks section
req.iface: 
---

# NDIS_SWITCH_PORT_DESTINATION structure



## -description
<p>The <b>NDIS_SWITCH_PORT_DESTINATION</b> structure specifies the Hyper-V extensible switch destination port to which a packet will be delivered.</p>


## -syntax

````
typedef struct _NDIS_SWITCH_PORT_DESTINATION {
  NDIS_SWITCH_PORT_ID   PortId;
  NDIS_SWITCH_NIC_INDEX NicIndex;
  USHORT                IsExcluded  :1;
  UINT32                PreserveVLAN  :1;
  UINT32                PreservePriority  :1;
  USHORT                Reserved  :13;
} NDIS_SWITCH_PORT_DESTINATION, *PNDIS_SWITCH_PORT_DESTINATION;
````


## -struct-fields
<dl>

### -field <b>PortId</b>

<dd>
<p>An NDIS_SWITCH_PORT_ID value that specifies the unique identifier of the destination port on the extensible switch.</p>
</dd>

### -field <b>NicIndex</b>

<dd>
<p>An NDIS_SWITCH_NIC_INDEX value that specifies the index of the network adapter that is connected to the  extensible switch port specified by the <b>PortId</b> member.</p>
<p>For more information on NDIS_SWITCH_NIC_INDEX values, see <a href="NULL">Network Adapter Index Values</a>.</p>
<div class="alert"><b>Note</b>  This member must specify the index value of a network adapter that is in a connected state. Index values for network adapters that are in a created or disconnected state cannot be specified. For more information about network connection states, see <a href="NULL">Hyper-V Extensible Switch Port and Network Adapter States</a>.</div>
<div> </div>
</dd>

### -field <b>IsExcluded</b>

<dd>
<p>If this member is set to TRUE, the packet will not be delivered to the
    destination port.
</p>
</dd>

### -field <b>PreserveVLAN</b>

<dd>
<p>If this member is set to TRUE, the 802.1Q virtual local area network (VLAN) information will be preserved when the packet is delivered to the destination port.  
</p>
</dd>

### -field <b>PreservePriority</b>

<dd>
<p>If this member is set to TRUE, the 802.1Q priority information will be preserved when the packet is delivered to the destination port.  
</p>
</dd>

### -field <b>Reserved</b>

<dd>
<p>This member is reserved for future use by NDIS.</p>
</dd>
</dl>

## -remarks
<p>The <a href="https://msdn.microsoft.com/library/windows/hardware/hh598210">NDIS_SWITCH_FORWARDING_DESTINATION_ARRAY</a> contains one or more elements. Each element is formatted as an <b>NDIS_SWITCH_PORT_DESTINATION</b> structure.</p>

<p>For more information on destination ports, see <a href="NULL">Managing Hyper-V Extensible Switch Destination Port Data</a>.</p>

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
<dt>Ndis.h (include Ndis.h)</dt>
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
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NDIS_SWITCH_PORT_DESTINATION structure%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
