---
UID: NS.ntddndis._NDIS_NIC_SWITCH_INFO
title: NDIS_NIC_SWITCH_INFO
author: windows-driver-content
description: The NDIS_NIC_SWITCH_INFO structure specifies the information about a network adapter switch on a network adapter.
old-location: netvista\ndis_nic_switch_info.htm
old-project: netvista
ms.assetid: 0da6927f-c940-4e46-a63a-2127bd7fa63d
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: NDIS_NIC_SWITCH_INFO, NDIS_NIC_SWITCH_INFO, *PNDIS_NIC_SWITCH_INFO
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: ntddndis.h
req.include-header: Ndis.h
req.target-type: Windows
req.target-min-winverclnt: Supported in NDIS 6.30 and later.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: NDIS_NIC_SWITCH_INFO
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

# NDIS_NIC_SWITCH_INFO structure



## -description
<p>The <b>NDIS_NIC_SWITCH_INFO</b> structure specifies the information about a network adapter switch on a network adapter. </p>


## -syntax

````
typedef struct _NDIS_NIC_SWITCH_INFO {
  NDIS_OBJECT_HEADER            Header;
  ULONG                         Flags;
  NDIS_NIC_SWITCH_TYPE          SwitchType;
  NDIS_NIC_SWITCH_ID            SwitchId;
  NDIS_NIC_SWITCH_FRIENDLY_NAME SwitchFriendlyName;
  ULONG                         NumVFs;
  ULONG                         NumAllocatedVFs;
  ULONG                         NumVPorts;
  ULONG                         NumActiveVPorts;
  ULONG                         NumQueuePairsForDefaultVPort;
  ULONG                         NumQueuePairsForNonDefaultVPorts;
  ULONG                         NumActiveDefaultVPortMacAddresses;
  ULONG                         NumActiveNonDefaultVPortMacAddresses;
  ULONG                         NumActiveDefaultVPortVlanIds;
  ULONG                         NumActiveNonDefaultVPortVlanIds;
} NDIS_NIC_SWITCH_INFO, *PNDIS_NIC_SWITCH_INFO;
````


## -struct-fields
<dl>

### -field <b>Header</b>

<dd>
<p>The type, revision, and size of the <b>NDIS_NIC_SWITCH_INFO</b> structure. This member is formatted as an <a href="https://msdn.microsoft.com/library/windows/hardware/ff566588">NDIS_OBJECT_HEADER</a> structure.</p>
<p>The miniport driver must set the <b>Type</b> member of <b>Header</b> to NDIS_OBJECT_TYPE_DEFAULT. To specify the version of the <b>NDIS_NIC_SWITCH_INFO</b> structure, the driver must set the <b>Revision</b> member of <b>Header</b> to the following value: </p>
<p></p>
<dl>

### -field <a id="NDIS_NIC_SWITCH_INFO_REVISION_1"></a><a id="ndis_nic_switch_info_revision_1"></a>NDIS_NIC_SWITCH_INFO_REVISION_1

<dd>
<p>Original version for NDIS 6.30.</p>
<p>Set the <b>Size</b> member to NDIS_SIZEOF_NIC_SWITCH_INFO_REVISION_1.</p>
</dd>
</dl>
</dd>

### -field <b>Flags</b>

<dd>
<p>A ULONG value that contains a bitwise OR of configuration flags that are enabled on the switch.</p>
<div class="alert"><b>Note</b>  For NDIS 6.30, no configuration flags are defined for the switch. The <b>Flags</b> member must be set to zero.</div>
<div> </div>
</dd>

### -field <b>SwitchType</b>

<dd>
<p>An <a href="https://msdn.microsoft.com/library/windows/hardware/hh451589">NDIS_NIC_SWITCH_TYPE</a> value that specifies the type of the switch.</p>
</dd>

### -field <b>SwitchId</b>

<dd>
<p>An NDIS_NIC_SWITCH_ID value that specifies a switch identifier. The switch identifier is an integer between zero and the number of switches that the network adapter supports. An NDIS_DEFAULT_SWITCH_ID value indicates the default network adapter switch.

</p>
<div class="alert"><b>Note</b>  Starting with Windows Server 2012, the single root I/O virtualization (SR-IOV) interface only supports the default network adapter switch on the network adapter. The value of this member must be set to NDIS_DEFAULT_SWITCH_ID. </div>
<div> </div>
</dd>

### -field <b>SwitchFriendlyName</b>

<dd>
<p>An NDIS_NIC_SWITCH_FRIENDLY_NAME value that contains the user-friendly description of the switch.

</p>
</dd>

### -field <b>NumVFs</b>

<dd>
<p>A ULONG value that specifies the number of PCI Express (PCIe) Virtual Functions (VFs) that are enabled on the network adapter. Enabled VFs can be in either an allocated or unallocated state.</p>
</dd>

### -field <b>NumAllocatedVFs</b>

<dd>
<p>A ULONG value that specifies the number of VFs that have been allocated on the network adapter switch specified by <b>SwitchId</b>. VFs are allocated  through OID set requests of <a href="https://msdn.microsoft.com/library/windows/hardware/hh451814">OID_NIC_SWITCH_ALLOCATE_VF</a>. 
</p>
</dd>

### -field <b>NumVPorts</b>

<dd>
<p>A ULONG value that specifies the  number of virtual ports (VPorts) that are configured on the network adapter switch specified by <b>SwitchId</b>.</p>
<p>This ULONG value is the sum of the following:</p>
<ul>
<li>The maximum number of VPorts that can be created through OID set requests of <a href="https://msdn.microsoft.com/library/windows/hardware/hh451816">OID_NIC_SWITCH_CREATE_VPORT</a>.</li>
<li>The default VPort attached to the Physical Function (PF).</li>
</ul>
</dd>

### -field <b>NumActiveVPorts</b>

<dd>
<p>A ULONG value that specifies the number of VPorts that have been created on the network adapter switch specified by <b>SwitchId</b>. </p>
<div class="alert"><b>Note</b>  This ULONG value includes the default VPort, in addition to the nondefault VPorts created through OID set requests of <a href="https://msdn.microsoft.com/library/windows/hardware/hh451816">OID_NIC_SWITCH_CREATE_VPORT</a>.</div>
<div> </div>
</dd>

### -field <b>NumQueuePairsForDefaultVPort</b>

<dd>
<p>A ULONG value that specifies the number of queue pairs allocated for the default VPort.  The  default VPort is always attached to the PF.</p>
<p>A queue pair consists of a transmit queue and receive queue. The miniport driver associates one or more queue pairs with the default VPort at the time of switch creation through an OID method request of <a href="https://msdn.microsoft.com/library/windows/hardware/hh451815">OID_NIC_SWITCH_CREATE_SWITCH</a>. </p>
<div class="alert"><b>Note</b>  Starting with NDIS 6.30, there can only be one queue pair that can be configured for the default VPort.</div>
<div> </div>
</dd>

### -field <b>NumQueuePairsForNonDefaultVPorts</b>

<dd>
<p>A ULONG value that specifies the number of queue pairs allocated for the nondefault VPorts. A nondefault VPort can be attached to either the PF or any VF of the network adapter.</p>
<p>The miniport driver associates one or more queue pairs with a nondefault VPort through an OID method request of <a href="https://msdn.microsoft.com/library/windows/hardware/hh451816">OID_NIC_SWITCH_CREATE_VPORT</a>.</p>
</dd>

### -field <b>NumActiveDefaultVPortMacAddresses</b>

<dd>
<p>A ULONG value that specifies the number of unicast MAC address filters that are currently set on the default VPort that is attached to the PF of the network adapter.</p>
</dd>

### -field <b>NumActiveNonDefaultVPortMacAddresses</b>

<dd>
<p>A ULONG value that specifies the number of unicast MAC address filters that are currently set on nondefault VPorts.</p>
</dd>

### -field <b>NumActiveDefaultVPortVlanIds</b>

<dd>
<p>A ULONG value that specifies the number of virtual local area network (VLAN) identifier filters that are currently set on the default VPort.</p>
</dd>

### -field <b>NumActiveNonDefaultVPortVlanIds</b>

<dd>
<p>A ULONG value that specifies the number of VLAN identifier filters that are currently set on the nondefault VPorts.</p>
</dd>
</dl>

## -remarks
<p>The <b>NDIS_NIC_SWITCH_INFO</b> structure is used in OID query requests of <a href="https://msdn.microsoft.com/library/windows/hardware/hh451819">OID_NIC_SWITCH_ENUM_SWITCHES</a>. This OID request is used to enumerate the network adapter switches on a network adapter. When this OID request is issued, one or more <b>NDIS_NIC_SWITCH_INFO</b> structures are returned within an <a href="https://msdn.microsoft.com/library/windows/hardware/hh451584">NDIS_NIC_SWITCH_INFO_ARRAY</a> structure.</p>

<p>An <b>NDIS_NIC_SWITCH_INFO</b> structure contains information about a network adapter switch that was previously created through an OID method request of OID_NIC_SWITCH_CREATE_SWITCH. </p>

<p>For more information about the SR-IOV interface, see 	<a href="NULL">Overview of Single Root I/O Virtualization (SR-IOV)</a>.</p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/hh451584">NDIS_NIC_SWITCH_INFO_ARRAY</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff566588">NDIS_OBJECT_HEADER</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh451815">OID_NIC_SWITCH_CREATE_SWITCH</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh451816">OID_NIC_SWITCH_CREATE_VPORT</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NDIS_NIC_SWITCH_INFO structure%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
