---
UID: NC.pcivirt.SRIOV_QUERY_LUID
title: SRIOV_QUERY_LUID
author: windows-driver-content
description: Gets the local unique identifier of the SR-IOV device.
old-location: pci\sriov_query_luid.htm
old-project: PCI
ms.assetid: 9bb8e54f-b42a-4f61-a3f5-6972141c8f28
ms.author: windowsdriverdev
ms.date: 11/15/2017
ms.keywords: PARCLASS_INFORMATION, PARCLASS_INFORMATION, *PPARCLASS_INFORMATION
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: callback
req.header: pcivirt.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: Windows 10
req.target-min-winversvr: Windows Server 2016
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: *PSRIOV_QUERY_LUID
req.alt-loc: Pcivirt.h
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

# SRIOV_QUERY_LUID callback



## -description
<p>Gets the local unique identifier of the SR-IOV device.</p>


## -prototype

````
SRIOV_QUERY_LUID SriovQueryLuid;

NTSTATUS SriovQueryLuid(
  _In_  PVOID Context,
  _Out_ PLUID Luid
)
{ ... }

typedef SRIOV_QUERY_LUID *PSRIOV_QUERY_LUID;
````


## -parameters
<dl>

### -param Context [in]

<dd>
<p>A pointer to a driver-defined context.
                    
                </p>
</dd>

### -param Luid [out]

<dd>
<p>A pointer to the local unique
identifier of the SR_IOV device implementing the interface.</p>
</dd>
</dl>

## -returns
<p>
Return STATUS_SUCCESS if the operation succeeds. Otherwise, return an appropriate <a href="https://msdn.microsoft.com/7792201b-63bb-4db5-803d-2af02893d505">NTSTATUS</a> error code.</p>

## -remarks
<p>This callback function is implemented by the physical function (PF) driver. It is invoked  when the system wants to get the identifier of a specific virtual function. </p>

<p>The PF driver registers its implementation by setting the <b>QueryLuid</b> member of the <a href="buses._sriov_device_interface_standard">SRIOV_DEVICE_INTERFACE_STANDARD</a>, configuring a <a href="..\wdfqueryinterface\ns-wdfqueryinterface--wdf-query-interface-config.md">WDF_QUERY_INTERFACE_CONFIG</a> structure, and calling <a href="..\wdfqueryinterface\nf-wdfqueryinterface-wdfdeviceaddqueryinterface.md">WdfDeviceAddQueryInterface</a>.</p>

<p>Here is an example implementation of this callback function. The PF driver generates a unique identifier by calling <a href="..\ntddk\nf-ntddk-zwallocatelocallyuniqueid.md">ZwAllocateLocallyUniqueId</a>  and stores it in the device context. </p>

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
<p>PASSIVE_LEVEL</p>
</td>
</tr>
</table>