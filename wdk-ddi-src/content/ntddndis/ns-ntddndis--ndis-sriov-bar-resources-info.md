---
UID: NS.ntddndis._NDIS_SRIOV_BAR_RESOURCES_INFO
title: NDIS_SRIOV_BAR_RESOURCES_INFO
author: windows-driver-content
description: The NDIS_SRIOV_BAR_RESOURCES_INFO structure specifies the PCI Express (PCIe) Base Address Register (BAR) of a network adapter's PCIe Virtual Function (VF).
old-location: netvista\ndis_sriov_bar_resources_info.htm
old-project: netvista
ms.assetid: e5a5ac98-171d-4a31-8bc6-400f613b7dc9
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: NDIS_SRIOV_BAR_RESOURCES_INFO, NDIS_SRIOV_BAR_RESOURCES_INFO, *PNDIS_SRIOV_BAR_RESOURCES_INFO
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
req.alt-api: NDIS_SRIOV_BAR_RESOURCES_INFO
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

# NDIS_SRIOV_BAR_RESOURCES_INFO structure



## -description
<p>The <b>NDIS_SRIOV_BAR_RESOURCES_INFO</b> structure specifies the PCI Express (PCIe) Base Address Register (BAR) of a network adapter's PCIe Virtual Function (VF). </p>


## -syntax

````
typedef struct _NDIS_SRIOV_BAR_RESOURCES_INFO {
  NDIS_OBJECT_HEADER     Header;
  NDIS_SRIOV_FUNCTION_ID VFId;
  USHORT                 BarIndex;
  ULONG                  BarResourcesOffset;
} NDIS_SRIOV_BAR_RESOURCES_INFO, *PNDIS_SRIOV_BAR_RESOURCES_INFO;
````


## -struct-fields
<dl>

### -field <b>Header</b>

<dd>
<p>The type, revision, and size of the <b>NDIS_SRIOV_BAR_RESOURCES_INFO</b> structure. This member is formatted as an <a href="..\ntddndis\ns-ntddndis--ndis-object-header.md">NDIS_OBJECT_HEADER</a> structure.</p>
<p>The miniport driver must set the <b>Type</b> member of <b>Header</b> to NDIS_OBJECT_TYPE_DEFAULT. To specify the version of the <b>NDIS_SRIOV_BAR_RESOURCES_INFO</b> structure, the driver must set the <b>Revision</b> member of <b>Header</b> to the following value: </p>
<p></p>
<dl>

### -field <a id="NDIS_SRIOV_BAR_RESOURCES_INFO_REVISION_1"></a><a id="ndis_sriov_bar_resources_info_revision_1"></a>NDIS_SRIOV_BAR_RESOURCES_INFO_REVISION_1

<dd>
<p>Original version for NDIS 6.30 and later.</p>
<p>Set the <b>Size</b> member to NDIS_SIZEOF_SRIOV_BAR_RESOURCES_INFO_REVISION_1.</p>
</dd>
</dl>
</dd>

### -field <b>VFId</b>

<dd>
<p>An NDIS_SRIOV_FUNCTION_ID value that specifies the unique identifier of the VF on the network adapter.</p>
<div class="alert"><b>Note</b>  The VF with the specified NDIS_SRIOV_FUNCTION_ID value must have resources that were previously allocated through an OID set request of <a href="https://msdn.microsoft.com/library/windows/hardware/hh451814">OID_NIC_SWITCH_ALLOCATE_VF</a>.

</div>
<div> </div>
</dd>

### -field <b>BarIndex</b>

<dd>
<p>A USHORT value that specifies the BAR index on the VF. This value is the offset of the register within the table of BARs in the PCI configuration space.</p>
</dd>

### -field <b>BarResourcesOffset</b>

<dd>
<p>A ULONG value that specifies the offset, in units of bytes, from the beginning of this structure to a <a href="..\wdm\ns-wdm--cm-partial-resource-descriptor.md">CM_PARTIAL_RESOURCE_DESCRIPTOR</a> structure.</p>
</dd>
</dl>

## -remarks
<p>The <b>NDIS_SRIOV_BAR_RESOURCES_INFO</b> structure is used in OID method requests of <a href="https://msdn.microsoft.com/library/windows/hardware/hh451852">OID_SRIOV_BAR_RESOURCES</a>.  </p>

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
<a href="..\wdm\ns-wdm--cm-partial-resource-descriptor.md">CM_PARTIAL_RESOURCE_DESCRIPTOR</a>
</dt>
<dt>
<a href="..\ntddndis\ns-ntddndis--ndis-object-header.md">NDIS_OBJECT_HEADER</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh451852">OID_SRIOV_BAR_RESOURCES</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NDIS_SRIOV_BAR_RESOURCES_INFO structure%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
