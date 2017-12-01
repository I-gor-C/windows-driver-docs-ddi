---
UID: NS.ntddndis._NDIS_NIC_SWITCH_VPORT_INFO
title: NDIS_NIC_SWITCH_VPORT_INFO
author: windows-driver-content
description: The NDIS_NIC_SWITCH_VPORT_INFO structure specifies the configuration for a virtual port (VPort) on a network adapter switch of the network adapter.
old-location: netvista\ndis_nic_switch_vport_info.htm
old-project: netvista
ms.assetid: 5effb179-18e8-4306-84c5-724cb5483449
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: NDIS_NIC_SWITCH_VPORT_INFO, NDIS_NIC_SWITCH_VPORT_INFO, *PNDIS_NIC_SWITCH_VPORT_INFO
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
req.alt-api: NDIS_NIC_SWITCH_VPORT_INFO
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

# NDIS_NIC_SWITCH_VPORT_INFO structure



## -description
<p>The <b>NDIS_NIC_SWITCH_VPORT_INFO</b> structure specifies the configuration for a virtual port (VPort) on a network adapter switch of the network adapter. </p>


## -syntax

````
typedef struct _NDIS_NIC_SWITCH_VPORT_INFO {
  NDIS_OBJECT_HEADER                         Header;
  NDIS_NIC_SWITCH_VPORT_ID                   VPortId;
  ULONG                                      Flags;
  NDIS_NIC_SWITCH_ID                         SwitchId;
  NDIS_VPORT_NAME                            VPortName;
  NDIS_SRIOV_FUNCTION_ID                     AttachedFunctionId;
  ULONG                                      NumQueuePairs;
  NDIS_NIC_SWITCH_VPORT_INTERRUPT_MODERATION InterruptModeration;
  NDIS_NIC_SWITCH_VPORT_STATE                VPortState;
  GROUP_AFFINITY                             ProcessorAffinity;
  ULONG                                      LookaheadSize;
  ULONG                                      NumFilters;
} NDIS_NIC_SWITCH_VPORT_INFO, *PNDIS_NIC_SWITCH_VPORT_INFO;
````


## -struct-fields
<dl>

### -field <b>Header</b>

<dd>
<p>The type, revision, and size of the <b>NDIS_NIC_SWITCH_VPORT_INFO</b> structure. This member is formatted as an <a href="..\ntddndis\ns-ntddndis--ndis-object-header.md">NDIS_OBJECT_HEADER</a> structure.</p>
<p>The miniport driver must set the <b>Type</b> member of <b>Header</b> to NDIS_OBJECT_TYPE_DEFAULT. To specify the version of the <b>NDIS_NIC_SWITCH_VPORT_INFO</b> structure, the driver must set the <b>Revision</b> member of <b>Header</b> to the following value: </p>
<p></p>
<dl>

### -field <a id="NDIS_NIC_SWITCH_VPORT_INFO_REVISION_1"></a><a id="ndis_nic_switch_vport_info_revision_1"></a>NDIS_NIC_SWITCH_VPORT_INFO_REVISION_1

<dd>
<p>Original version for NDIS 6.30 and later.</p>
<p>Set the <b>Size</b> member to NDIS_SIZEOF_NIC_SWITCH_VPORT_INFO_REVISION_1.</p>
</dd>
</dl>
</dd>

### -field <b>VPortId</b>

<dd>
<p>An NDIS_NIC_SWITCH_VPORT_ID value  that uniquely identifies the virtual port (VPort)  on the network adapter. </p>
<p>A value of NDIS_DEFAULT_VPORT_ID specifies the default VPort on the switch. The default

VPort is always attached to the PCI Express (PCIe) Physical Function (PF) of the network adapter.</p>
<div class="alert"><b>Note</b>  A nondefault VPort with the specified <b>VPortId</b> value must have previously been created through an OID method request of <a href="https://msdn.microsoft.com/library/windows/hardware/hh451816">OID_NIC_SWITCH_CREATE_VPORT</a>.</div>
<div> </div>
</dd>

### -field <b>Flags</b>

<dd>
<p>A ULONG value that contains a bitwise OR of flags. This member is reserved for NDIS.

</p>
</dd>

### -field <b>SwitchId</b>

<dd>
<p>An NDIS_NIC_SWITCH_ID value that uniquely identifies  a network adapter switch that was created on the network adapter. The VPort identified through the <b>VPortId</b> member is created on the switch specified by the <b>SwitchId</b> member.</p>
<p>The switch identifier is an integer between zero and the number of switches that the network adapter supports. A value of NDIS_DEFAULT_SWITCH_ID indicates the default network adapter switch.

</p>
<div class="alert"><b>Note</b>  Starting with Windows Server 2012, the single root I/O virtualization (SR-IOV) interface only supports the default network adapter switch on the network adapter. The value of this member must be set to NDIS_DEFAULT_SWITCH_ID. </div>
<div> </div>
</dd>

### -field <b>VPortName</b>

<dd>
<p>An NDIS_VPORT_NAME value that  specifies the name of the VPort that was created on the network adapter switch. This member contains the user-friendly description of the VPort.</p>
</dd>

### -field <b>AttachedFunctionId</b>

<dd>
<p>An NDIS_SRIOV_FUNCTION_ID value that specifies the identifier of a VF or the PF to which the  VPort is attached. </p>
<div class="alert"><b>Note</b>  If this value is NDIS_PF_FUNCTION_ID, the VPort is attached to the PF.</div>
<div> </div>
</dd>

### -field <b>NumQueuePairs</b>

<dd>
<p>A ULONG value that specifies the number of queue pairs configured for this VPort.</p>
<p>A queue pair consists of a transmit queue and receive queue. Queue pairs associated with the default VPort are configured at the time of switch creation through an OID method request of <a href="https://msdn.microsoft.com/library/windows/hardware/hh451815">OID_NIC_SWITCH_CREATE_SWITCH</a>.
One or more queue pairs are configured on a nondefault VPort through an OID method request of <a href="https://msdn.microsoft.com/library/windows/hardware/hh451816">OID_NIC_SWITCH_CREATE_VPORT</a>.
</p>
</dd>

### -field <b>InterruptModeration</b>

<dd>
<p>An <a href="..\ntddndis\ne-ntddndis--ndis-nic-switch-vport-interrupt-moderation.md">NDIS_NIC_SWITCH_VPORT_INTERRUPT_MODERATION</a> value that specifies the interrupt moderation setting of the VPort.</p>
</dd>

### -field <b>VPortState</b>

<dd>
<p>An <a href="..\ntddndis\ne-ntddndis--ndis-nic-switch-vport-state.md">NDIS_NIC_SWITCH_VPORT_STATE</a> value that specifies the state of the VPort.  </p>
</dd>

### -field <b>ProcessorAffinity</b>

<dd>
<p>A <a href="..\miniport\ns-miniport--group-affinity.md">GROUP_AFFINITY</a> value that specifies the group number and a bitmap of the CPUs that this VPort can be associated with. </p>
<p>This member is valid only for the VPorts attached to the PF. This field is not valid for nondefault VPorts that are attached to a VF. </p>
</dd>

### -field <b>LookaheadSize</b>

<dd>
<p>This member is reserved for future use. This member must be set to zero.</p>
</dd>

### -field <b>NumFilters</b>

<dd>
<p>A ULONG value that specifies the number of receive filters that have been configured on the network adapter.</p>
<div class="alert"><b>Note</b>  Starting with NDIS 6.30, the miniport driver must maintain a counter for the current number of receive filters that are set on the network adapter. The driver must increment the counter each time a receive filter is set through an OID set request of <a href="https://msdn.microsoft.com/library/windows/hardware/ff569795">OID_RECEIVE_FILTER_SET_FILTER</a>.  The driver must also decrement the counter each time a receive filter is  cleared through an OID set request of <a href="https://msdn.microsoft.com/library/windows/hardware/ff569785">OID_RECEIVE_FILTER_CLEAR_FILTER</a>.</div>
<div> </div>
</dd>
</dl>

## -remarks
<p>An <b>NDIS_NIC_SWITCH_VPORT_INFO</b> structure contains information about one of the following:<ul>
<li>
<p>A nondefault VPort that was previously created through an OID method request of <a href="https://msdn.microsoft.com/library/windows/hardware/hh451816">OID_NIC_SWITCH_CREATE_VPORT</a>.</p>
</li>
<li>
<p>The default VPort that is attached to the PF. The default VPort always exists and cannot be deleted.</p>
</li>
</ul>
</p>

<p>A nondefault VPort that was previously created through an OID method request of <a href="https://msdn.microsoft.com/library/windows/hardware/hh451816">OID_NIC_SWITCH_CREATE_VPORT</a>.</p>

<p>The default VPort that is attached to the PF. The default VPort always exists and cannot be deleted.</p>

<p>One or more <b>NDIS_NIC_SWITCH_VPORT_INFO</b> structures are returned through the <a href="..\ntddndis\ns-ntddndis--ndis-nic-switch-vport-info-array.md">NDIS_NIC_SWITCH_VPORT_INFO_ARRAY</a> structure.</p>

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
<a href="..\ntddndis\ns-ntddndis--ndis-nic-switch-vport-info-array.md">NDIS_NIC_SWITCH_VPORT_INFO_ARRAY</a>
</dt>
<dt>
<a href="..\ntddndis\ns-ntddndis--ndis-object-header.md">NDIS_OBJECT_HEADER</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh451816">OID_NIC_SWITCH_CREATE_VPORT</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh451825">OID_NIC_SWITCH_VPORT_PARAMETERS</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NDIS_NIC_SWITCH_VPORT_INFO structure%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
