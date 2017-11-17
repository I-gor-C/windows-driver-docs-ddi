---
UID: NC.pcivirt.SRIOV_QUERY_LUID_VF
title: SRIOV_QUERY_LUID_VF
author: windows-driver-content
description: Gets the PCI Express SR-IOV Virtual Function (VF) given a unique identifier.
old-location: pci\sriov_query_luid_vf.htm
ms.assetid: 00dddc92-08d1-4eaa-b3de-5e96c7a6d3e0
ms.author: windowsdriverdev
ms.date: 10/23/2017
ms.topic: callback
ms.prod: windows-hardware
ms.technology: PCI
req.header: pcivirt.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: Windows 10
req.target-min-winversvr: Windows Server 2016
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: *PSRIOV_QUERY_LUID_VF
req.alt-loc: pcivirt.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: 
ms.keywords: PARCLASS_INFORMATION, PARCLASS_INFORMATION, *PPARCLASS_INFORMATION
req.iface: 
---

# SRIOV_QUERY_LUID_VF callback



## -description
<p>Gets the PCI Express SR-IOV Virtual Function (VF) given a unique identifier.</p>


## -prototype

````
SRIOV_QUERY_LUID_VF SriovQueryLuidVf;

NTSTATUS SriovQueryLuidVf(
  _In_  PVOID  Context,
  _In_  LUID   Luid,
  _Out_ USHORT VfIndex
)
{ ... }

typedef SRIOV_QUERY_LUID_VF *PSRIOV_QUERY_LUID_VF;
````


## -parameters
<dl>

### -param <i>Context</i> [in]

<dd>
<p>A pointer to a driver-defined context.
                    
                </p>
</dd>

### -param <i>Luid</i> [in]

<dd>
<p>The local unique
identifier of the VF whose index is being retrieved.</p>
</dd>

### -param <i>VfIndex</i> [out]

<dd>
<p>A zero-based index of the VF that is being queried.</p>
</dd>
</dl>

## -returns
<p>
Return STATUS_SUCCESS if the operation succeeds. Otherwise, return an appropriate <a href="https://msdn.microsoft.com/7792201b-63bb-4db5-803d-2af02893d505">NTSTATUS</a> error code.</p>

## -remarks
<p>This callback function is implemented by the physical function (PF) driver. It is invoked  when the system wants to get the identifier of a specific virtual function. </p>

<p>The PF driver registers its implementation by setting the <b>QueryLuidVf</b> member of the <a href="buses._sriov_device_interface_standard_2">SRIOV_DEVICE_INTERFACE_STANDARD_2</a>, configuring a <a href="https://msdn.microsoft.com/library/windows/hardware/ff552439">WDF_QUERY_INTERFACE_CONFIG</a> structure, and calling <a href="https://msdn.microsoft.com/library/windows/hardware/ff545870">WdfDeviceAddQueryInterface</a>.</p>

<p>This callback function is implemented by the physical function (PF) driver. It is invoked  when the system wants to get the identifier of a specific virtual function. </p>

<p>The PF driver registers its implementation by setting the <b>QueryLuidVf</b> member of the <a href="buses._sriov_device_interface_standard_2">SRIOV_DEVICE_INTERFACE_STANDARD_2</a>, configuring a <a href="https://msdn.microsoft.com/library/windows/hardware/ff552439">WDF_QUERY_INTERFACE_CONFIG</a> structure, and calling <a href="https://msdn.microsoft.com/library/windows/hardware/ff545870">WdfDeviceAddQueryInterface</a>.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Minimum supported client</p>
</th>
<td width="70%">
<p>Windows 10</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Minimum supported server</p>
</th>
<td width="70%">
<p>Windows Server 2016</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Pcivirt.h</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>IRQL</p>
</th>
<td width="70%">
<p></p>
</td>
</tr>
</table>