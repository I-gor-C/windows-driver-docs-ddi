---
UID: NS.ntddndis._NDIS_NIC_SWITCH_FREE_VF_PARAMETERS
title: NDIS_NIC_SWITCH_FREE_VF_PARAMETERS
author: windows-driver-content
description: The NDIS_NIC_SWITCH_FREE_VF_PARAMETERS specifies a PCI Express (PCIe) Virtual Function (VF) whose resources will be freed.
old-location: netvista\ndis_nic_switch_free_vf_parameters.htm
old-project: netvista
ms.assetid: 61f3839a-f428-4585-a046-edce85d829dd
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: NDIS_NIC_SWITCH_FREE_VF_PARAMETERS, NDIS_NIC_SWITCH_FREE_VF_PARAMETERS, *PNDIS_NIC_SWITCH_FREE_VF_PARAMETERS
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
req.alt-api: NDIS_NIC_SWITCH_FREE_VF_PARAMETERS
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

# NDIS_NIC_SWITCH_FREE_VF_PARAMETERS structure



## -description
<p>The <b>NDIS_NIC_SWITCH_FREE_VF_PARAMETERS</b> specifies a PCI Express (PCIe) Virtual Function (VF) whose resources will be freed.</p>


## -syntax

````
typedef struct _NDIS_NIC_SWITCH_FREE_VF_PARAMETERS {
  NDIS_OBJECT_HEADER     Header;
  ULONG                  Flags;
  NDIS_SRIOV_FUNCTION_ID VFId;
} NDIS_NIC_SWITCH_FREE_VF_PARAMETERS, *PNDIS_NIC_SWITCH_FREE_VF_PARAMETERS;
````


## -struct-fields
<dl>

### -field <b>Header</b>

<dd>
<p>The type, revision, and size of the <b>NDIS_NIC_SWITCH_FREE_VF_PARAMETERS</b> structure. This member is formatted as an <a href="https://msdn.microsoft.com/library/windows/hardware/ff566588">NDIS_OBJECT_HEADER</a> structure.</p>
<p>The miniport driver must set the <b>Type</b> member of <b>Header</b> to NDIS_OBJECT_TYPE_DEFAULT. To specify the version of the <b>NDIS_NIC_SWITCH_FREE_VF_PARAMETERS</b> structure, the driver must set the <b>Revision</b> member of <b>Header</b> to the following value: </p>
<p></p>
<dl>

### -field <a id="NDIS_NIC_SWITCH_FREE_VF_PARAMETERS_REVISION_1"></a><a id="ndis_nic_switch_free_vf_parameters_revision_1"></a>NDIS_NIC_SWITCH_FREE_VF_PARAMETERS_REVISION_1

<dd>
<p>Original version for NDIS 6.30.</p>
<p>Set the <b>Size</b> member to NDIS_SIZEOF_NIC_SWITCH_FREE_VF_PARAMETERS_REVISION_1.</p>
</dd>
</dl>
</dd>

### -field <b>Flags</b>

<dd>
<p>A ULONG value that contains a bitwise OR of flags. This member is reserved for NDIS.</p>
</dd>

### -field <b>VFId</b>

<dd>
<p>An NDIS_SRIOV_FUNCTION_ID value that specifies the unique identifier of the VF on the network adapter.</p>
<div class="alert"><b>Note</b>  Resources for the VF with the specified NDIS_SRIOV_FUNCTION_ID value must have previously been allocated through an OID method request of <a href="https://msdn.microsoft.com/library/windows/hardware/hh451814">OID_NIC_SWITCH_ALLOCATE_VF</a>.

</div>
<div> </div>
</dd>
</dl>

## -remarks
<p> The <b>NDIS_NIC_SWITCH_FREE_VF_PARAMETERS</b> structure is used in OID set requests of <a href="https://msdn.microsoft.com/library/windows/hardware/hh451822">OID_NIC_SWITCH_FREE_VF</a>.</p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff566588">NDIS_OBJECT_HEADER</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh451814">OID_NIC_SWITCH_ALLOCATE_VF</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh451822">OID_NIC_SWITCH_FREE_VF</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NDIS_NIC_SWITCH_FREE_VF_PARAMETERS structure%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
