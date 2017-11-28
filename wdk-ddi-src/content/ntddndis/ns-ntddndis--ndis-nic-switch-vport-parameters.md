---
UID: NS.ntddndis._NDIS_NIC_SWITCH_VPORT_PARAMETERS
title: NDIS_NIC_SWITCH_VPORT_PARAMETERS
author: windows-driver-content
description: The NDIS_NIC_SWITCH_VPORT_PARAMETERS structure specifies the configuration for a virtual port (VPort) on a network adapter switch of the network adapter.
old-location: netvista\ndis_nic_switch_vport_parameters.htm
old-project: netvista
ms.assetid: d75bec3d-b427-40d2-bec3-95b7409f31bb
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: NDIS_NIC_SWITCH_VPORT_PARAMETERS, NDIS_NIC_SWITCH_VPORT_PARAMETERS, *PNDIS_NIC_SWITCH_VPORT_PARAMETERS
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
req.alt-api: NDIS_NIC_SWITCH_VPORT_PARAMETERS
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

# NDIS_NIC_SWITCH_VPORT_PARAMETERS structure



## -description
<p>The <b>NDIS_NIC_SWITCH_VPORT_PARAMETERS</b> structure specifies the configuration for a virtual port (VPort) on a network adapter switch of the network adapter. </p>


## -syntax

````
typedef struct _NDIS_NIC_SWITCH_VPORT_PARAMETERS {
  NDIS_OBJECT_HEADER                         Header;
  ULONG                                      Flags;
  NDIS_NIC_SWITCH_ID                         SwitchId;
  NDIS_NIC_SWITCH_VPORT_ID                   VPortId;
  NDIS_VPORT_NAME                            VPortName;
  NDIS_SRIOV_FUNCTION_ID                     AttachedFunctionId;
  ULONG                                      NumQueuePairs;
  NDIS_NIC_SWITCH_VPORT_INTERRUPT_MODERATION InterruptModeration;
  NDIS_NIC_SWITCH_VPORT_STATE                VPortState;
  GROUP_AFFINITY                             ProcessorAffinity;
  ULONG                                      LookaheadSize;
} NDIS_NIC_SWITCH_VPORT_PARAMETERS, *PNDIS_NIC_SWITCH_VPORT_PARAMETERS;
````


## -struct-fields
<dl>

### -field <b>Header</b>

<dd>
<p>The type, revision, and size of the <b>NDIS_NIC_SWITCH_VPORT_PARAMETERS</b> structure. This member is formatted as an <a href="https://msdn.microsoft.com/library/windows/hardware/ff566588">NDIS_OBJECT_HEADER</a> structure.</p>
<p>The miniport driver must set the <b>Type</b> member of <b>Header</b> to NDIS_OBJECT_TYPE_DEFAULT. To specify the version of the <b>NDIS_NIC_SWITCH_VPORT_PARAMETERS</b> structure, the driver must set the <b>Revision</b> member of <b>Header</b> to the following value: </p>
<p></p>
<dl>

### -field <a id="NDIS_NIC_SWITCH_VPORT_PARAMETERS_REVISION_1"></a><a id="ndis_nic_switch_vport_parameters_revision_1"></a>NDIS_NIC_SWITCH_VPORT_PARAMETERS_REVISION_1

<dd>
<p>Original version for NDIS 6.30 and later.</p>
<p>Set the <b>Size</b> member to NDIS_SIZEOF_NIC_SWITCH_VPORT_PARAMETERS_REVISION_1.</p>
</dd>
</dl>
</dd>

### -field <b>Flags</b>

<dd>
<p> A ULONG value that contains a bitwise OR of flags. The following flags are defined for this member. 
</p>
<p></p>
<dl>

### -field <a id="NDIS_NIC_SWITCH_VPORT_PARAMS_LOOKAHEAD_SPLIT_ENABLED"></a><a id="ndis_nic_switch_vport_params_lookahead_split_enabled"></a>NDIS_NIC_SWITCH_VPORT_PARAMS_LOOKAHEAD_SPLIT_ENABLED

<dd>
<p>
	                                 
	This flag is reserved for future use. 
Miniport drivers must ignore this flag.</p>
</dd>

### -field <a id="NDIS_NIC_SWITCH_VPORT_PARAMS_FLAGS_CHANGED"></a><a id="ndis_nic_switch_vport_params_flags_changed"></a>NDIS_NIC_SWITCH_VPORT_PARAMS_FLAGS_CHANGED

<dd>
<p>
	                                 
	This flag specifies that the <b>Flags</b> member has been updated after the VPort has been created. These flags can be enabled or disabled after the VPort has been created by using an OID set request of <a href="https://msdn.microsoft.com/library/windows/hardware/hh451825">OID_NIC_SWITCH_VPORT_PARAMETERS</a>. 
</p>
<div class="alert"><b>Note</b>  This flag is valid only when this structure is used in OID set requests of <a href="https://msdn.microsoft.com/library/windows/hardware/hh451825">OID_NIC_SWITCH_VPORT_PARAMETERS</a>. </div>
<div> </div>
</dd>

### -field <a id="NDIS_NIC_SWITCH_VPORT_PARAMS_NAME_CHANGED"></a><a id="ndis_nic_switch_vport_params_name_changed"></a>NDIS_NIC_SWITCH_VPORT_PARAMS_NAME_CHANGED

<dd>
<p>                                  
 This flag specifies that the <b>VPortName</b> member has been updated after the VPort has been created. This member can be updated by using an OID set request of <a href="https://msdn.microsoft.com/library/windows/hardware/hh451825">OID_NIC_SWITCH_VPORT_PARAMETERS</a>. 
</p>
<div class="alert"><b>Note</b>  This flag is valid only when this structure is used in OID set requests of <a href="https://msdn.microsoft.com/library/windows/hardware/hh451825">OID_NIC_SWITCH_VPORT_PARAMETERS</a>. </div>
<div> </div>
</dd>

### -field <a id="NDIS_NIC_SWITCH_VPORT_PARAMS_INT_MOD_CHANGED"></a><a id="ndis_nic_switch_vport_params_int_mod_changed"></a>NDIS_NIC_SWITCH_VPORT_PARAMS_INT_MOD_CHANGED

<dd>
<p>This flag specifies that the <b>InterruptModeration</b> member has been updated after the VPort has been created. This member can be updated by using an OID set request of <a href="https://msdn.microsoft.com/library/windows/hardware/hh451825">OID_NIC_SWITCH_VPORT_PARAMETERS</a>. 
 
</p>
<div class="alert"><b>Note</b>  This flag is valid only when this structure is used in OID set requests of <a href="https://msdn.microsoft.com/library/windows/hardware/hh451825">OID_NIC_SWITCH_VPORT_PARAMETERS</a>. </div>
<div> </div>
</dd>

### -field <a id="NDIS_NIC_SWITCH_VPORT_PARAMS_STATE_CHANGED"></a><a id="ndis_nic_switch_vport_params_state_changed"></a>NDIS_NIC_SWITCH_VPORT_PARAMS_STATE_CHANGED

<dd>
<p>This flag specifies that the <b>VPortState</b> member has been updated after the VPort has been created. This member can be updated by using an OID set request of <a href="https://msdn.microsoft.com/library/windows/hardware/hh451825">OID_NIC_SWITCH_VPORT_PARAMETERS</a>.</p>
<div class="alert"><b>Note</b>  This flag is valid only when this structure is used in OID set requests of <a href="https://msdn.microsoft.com/library/windows/hardware/hh451825">OID_NIC_SWITCH_VPORT_PARAMETERS</a>. </div>
<div> </div>
</dd>

### -field <a id="NDIS_NIC_SWITCH_VPORT_PARAMS_PROCESSOR_AFFINITY_CHANGED"></a><a id="ndis_nic_switch_vport_params_processor_affinity_changed"></a>NDIS_NIC_SWITCH_VPORT_PARAMS_PROCESSOR_AFFINITY_CHANGED

<dd>
<p>This flag specifies that the <b>ProcessoryAffinity</b> member has been updated after the VPort has been created. The processor affinity of a VPort can only be updated if the VPort is attached to the PF on the network adapter. The <b>ProcessoryAffinity</b> member can be updated by using an OID set request of <a href="https://msdn.microsoft.com/library/windows/hardware/hh451825">OID_NIC_SWITCH_VPORT_PARAMETERS</a>.</p>
<div class="alert"><b>Note</b>  This flag is valid only when this structure is used in OID set requests of <a href="https://msdn.microsoft.com/library/windows/hardware/hh451825">OID_NIC_SWITCH_VPORT_PARAMETERS</a>. </div>
<div> </div>
</dd>
</dl>
</dd>

### -field <b>SwitchId</b>

<dd>
<p>An NDIS_NIC_SWITCH_ID value that specifies the identifier of the switch on which the VPort is to be created.</p>
<p>The switch identifier is an integer between zero and the number of switches that the network adapter supports. An NDIS_DEFAULT_SWITCH_ID value indicates the default network adapter switch.

</p>
<div class="alert"><b>Note</b>  Starting with Windows Server 2012, the single root I/O virtualization (SR-IOV) interface only supports the default network adapter switch on the network adapter. The value of this member must be set to NDIS_DEFAULT_SWITCH_ID. </div>
<div> </div>
</dd>

### -field <b>VPortId</b>

<dd>
<p>An NDIS_NIC_SWITCH_VPORT_ID value that specifies the identifier of a VPort  on the network adapter. The value is allocated by NDIS,  and is unique across the network adapter. </p>
<p>The <b>VPortId</b> value is within the range from zero to (<b>NumVPorts</b> - 1), where <b>NumVPorts</b> is the number of VPorts that the miniport driver has configured on the network adapter. The driver specifies this number in the <b>NumVPorts</b> member of the <a href="https://msdn.microsoft.com/library/windows/hardware/hh451582">NDIS_NIC_SWITCH_INFO</a> structure. The driver returns this structure through an OID query request of <a href="https://msdn.microsoft.com/library/windows/hardware/hh451819">OID_NIC_SWITCH_ENUM_SWITCHES</a>. 
</p>
<div class="alert"><b>Note</b>  A VPort identifier of NDIS_DEFAULT_VPORT_ID is reserved for the default VPort that is attached to the PF on the default NIC switch.</div>
<div> </div>
</dd>

### -field <b>VPortName</b>

<dd>
<p>An NDIS_VPORT_NAME value that specifies the name of the VPort. This member contains a user-friendly description of the VPort.

</p>
</dd>

### -field <b>AttachedFunctionId</b>

<dd>
<p>An NDIS_SRIOV_FUNCTION_ID value that specifies the ID of the Physical Function (PF) or Virtual Function (VF) that the VPort is attached to. A value of NDIS_PF_FUNCTION_ID specifies that the VPort is attached to the PF. If the value is a valid VF identifier, the VPort is attached to the VF. </p>
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
<p>An <a href="https://msdn.microsoft.com/library/windows/hardware/hh451596">NDIS_NIC_SWITCH_VPORT_INTERRUPT_MODERATION</a> value that specifies the interrupt moderation setting of the VPort.

</p>
</dd>

### -field <b>VPortState</b>

<dd>
<p>An <a href="https://msdn.microsoft.com/library/windows/hardware/hh451598">NDIS_NIC_SWITCH_VPORT_STATE</a> value that specifies the current state of the VPort.</p>
</dd>

### -field <b>ProcessorAffinity</b>

<dd>
<p>A GROUP_AFFINITY value that specifies the group number and a bitmap of the CPUs that this VPort is associated with. This field is valid only for VPorts that are attached to the PF. </p>
<div class="alert"><b>Note</b>  For nondefault PF VPorts, a GROUP_AFFINITY value that specifies only one processor must be specified when the VPort is created. VPorts are created through an OID method request of  <a href="https://msdn.microsoft.com/library/windows/hardware/hh451816">OID_NIC_SWITCH_CREATE_VPORT</a>.</div>
<div> </div>
<p>The processor affinity associated with the nondefault VPort attached to the PF can be changed after VPort creation. The processor affinity associated with the default VPort can also be changed by using an OID set request of <a href="https://msdn.microsoft.com/library/windows/hardware/hh451825">OID_NIC_SWITCH_VPORT_PARAMETERS</a>.

</p>
</dd>

### -field <b>LookaheadSize</b>

<dd>
<p>This member is reserved for future use. This member must be set to zero.</p>
</dd>
</dl>

## -remarks
<p>This structure is used in OID requests of <a href="https://msdn.microsoft.com/library/windows/hardware/hh451816">OID_NIC_SWITCH_CREATE_VPORT</a> and <a href="https://msdn.microsoft.com/library/windows/hardware/hh451825">OID_NIC_SWITCH_VPORT_PARAMETERS</a>.</p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/hh451582">NDIS_NIC_SWITCH_INFO</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh451591">NDIS_NIC_SWITCH_VF_INFO</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff566588">NDIS_OBJECT_HEADER</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh451816">OID_NIC_SWITCH_CREATE_VPORT</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh451819">OID_NIC_SWITCH_ENUM_SWITCHES</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh451825">OID_NIC_SWITCH_VPORT_PARAMETERS</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NDIS_NIC_SWITCH_VPORT_PARAMETERS structure%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
