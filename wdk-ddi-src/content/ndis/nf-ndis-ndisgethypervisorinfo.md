---
UID: NF.ndis.NdisGetHypervisorInfo
title: NdisGetHypervisorInfo
author: windows-driver-content
description: Important  Starting with Windows 10 Version 1703, NdisGetHypervisorInfo is deprecated and should not be used.
old-location: netvista\ndisgethypervisorinfo.htm
old-project: netvista
ms.assetid: 5469c6aa-90df-4379-b670-23aaa6919055
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: NdisGetHypervisorInfo
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: ndis.h
req.include-header: Ndis.h
req.target-type: Universal
req.target-min-winverclnt: Supported in NDIS 6.0 and later.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: NdisGetHypervisorInfo
req.alt-loc: ndis.lib,ndis.dll
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Ndis.lib
req.dll: 
req.irql: <= DISPATCH_LEVEL
req.iface: 
---

# NdisGetHypervisorInfo function



## -description

## -syntax

````
NDIS_STATUS NdisGetHypervisorInfo(
  _Inout_ PNDIS_HYPERVISOR_INFO HypervisorInfo
);
````


## -parameters
<dl>

### -param <i>HypervisorInfo</i> [in, out]

<dd>
<p>A pointer to a caller-allocated <a href="https://msdn.microsoft.com/library/windows/hardware/ff565708">NDIS_HYPERVISOR_INFO</a> structure that
     contains information about the hypervisor that is present on the system.</p>
</dd>
</dl>

## -returns
<p><b>NdisGetHypervisorInfo</b> can return one of the following status values:</p><dl>
<dt><b>NDIS_STATUS_SUCCESS</b></dt>
</dl><p>The operation completed successfully.</p><dl>
<dt><b>NDIS_STATUS_BUFFER_TOO_SHORT</b></dt>
</dl><p>The size of the input parameter buffer was too small.</p>

<p> </p>

## -remarks
<p>NDIS miniport drivers call the 
    <b>NdisGetHypervisorInfo</b> function to determine whether a hypervisor is present on the system.</p>

<p>When the <b>NdisGetHypervisorInfo</b> function returns, the <i>HypervisorInfo</i> parameter contains a pointer to an <a href="https://msdn.microsoft.com/library/windows/hardware/ff565708">NDIS_HYPERVISOR_INFO</a> structure. This structure contains information about whether a hypervisor is present, along with the partition type from which this function was called. The <b>NDIS_HYPERVISOR_INFO</b> structure provides this information in the following way:</p>

<p>If a hypervisor is present, the <b>NDIS_HYPERVISOR_INFO_FLAG_HYPERVISOR_PRESENT</b> 
flag is set in the <b>Flags</b> member.</p>

<p>If the Microsoft hypervisor is present, the <b>PartitionType</b> member is set to one of the following values: </p>

<p>If the <b>NdisGetHypervisorInfo</b> function was called from the management operating system that runs in the Hyper-V parent partition, the <b>PartitionType</b> member is set to <b>NdisHypervisorPartitionTypeMsHvParent</b>.</p>

<p>If the <b>NdisGetHypervisorInfo</b> function was called from the guest operating system that runs in the Hyper-V child partition, the <b>PartitionType</b> member is set to <b>NdisHypervisorPartitionMsHvChild</b>.</p>

<p>If another vendor's hypervisor is present, the <b>PartitionType</b> member is set to  <b>NdisHypervisorPartitionTypeUnknown</b>.</p>

<p>NDIS miniport drivers call the 
    <b>NdisGetHypervisorInfo</b> function to determine whether a hypervisor is present on the system.</p>

<p>When the <b>NdisGetHypervisorInfo</b> function returns, the <i>HypervisorInfo</i> parameter contains a pointer to an <a href="https://msdn.microsoft.com/library/windows/hardware/ff565708">NDIS_HYPERVISOR_INFO</a> structure. This structure contains information about whether a hypervisor is present, along with the partition type from which this function was called. The <b>NDIS_HYPERVISOR_INFO</b> structure provides this information in the following way:</p>

<p>If a hypervisor is present, the <b>NDIS_HYPERVISOR_INFO_FLAG_HYPERVISOR_PRESENT</b> 
flag is set in the <b>Flags</b> member.</p>

<p>If the Microsoft hypervisor is present, the <b>PartitionType</b> member is set to one of the following values: </p>

<p>If the <b>NdisGetHypervisorInfo</b> function was called from the management operating system that runs in the Hyper-V parent partition, the <b>PartitionType</b> member is set to <b>NdisHypervisorPartitionTypeMsHvParent</b>.</p>

<p>If the <b>NdisGetHypervisorInfo</b> function was called from the guest operating system that runs in the Hyper-V child partition, the <b>PartitionType</b> member is set to <b>NdisHypervisorPartitionMsHvChild</b>.</p>

<p>If another vendor's hypervisor is present, the <b>PartitionType</b> member is set to  <b>NdisHypervisorPartitionTypeUnknown</b>.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Target platform</p>
</th>
<td width="70%">
<dl>
<dt><a href="http://go.microsoft.com/fwlink/p/?linkid=531356" target="_blank">Universal</a></dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Supported in NDIS 6.0 and later.</p>
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
<tr>
<th width="30%">
<p>Library</p>
</th>
<td width="70%">
<dl>
<dt>Ndis.lib</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>IRQL</p>
</th>
<td width="70%">
<p>&lt;= DISPATCH_LEVEL</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff565708">NDIS_HYPERVISOR_INFO</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NdisGetHypervisorInfo function%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
