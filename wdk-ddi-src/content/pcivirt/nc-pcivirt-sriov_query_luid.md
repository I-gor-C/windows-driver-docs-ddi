---
UID: NC:pcivirt.SRIOV_QUERY_LUID
title: SRIOV_QUERY_LUID
author: windows-driver-content
description: Gets the local unique identifier of the SR-IOV device.
old-location: pci\sriov_query_luid.htm
old-project: PCI
ms.assetid: 9bb8e54f-b42a-4f61-a3f5-6972141c8f28
ms.author: windowsdriverdev
ms.date: 12/29/2017
ms.keywords: PCI.sriov_query_luid, SriovQueryLuid callback function [Buses], SriovQueryLuid, SRIOV_QUERY_LUID, SRIOV_QUERY_LUID, pcivirt/SriovQueryLuid, *PSRIOV_QUERY_LUID callback function pointer [Buses], *PSRIOV_QUERY_LUID
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
topictype:
-	APIRef
-	kbSyntax
apitype:
-	UserDefined
apilocation:
-	Pcivirt.h
apiname:
-	*PSRIOV_QUERY_LUID
product: Windows
targetos: Windows
req.typenames: PARCLASS_INFORMATION, *PPARCLASS_INFORMATION
---


# SRIOV_QUERY_LUID function
Gets the local unique identifier of the SR-IOV device.

## Syntax

```
SRIOV_QUERY_LUID SriovQueryLuid;

NTSTATUS SriovQueryLuid(
  PVOID Context,
  PLUID Luid
)
{...}
```

## Parameters

`Context`

A pointer to a driver-defined context.

`Luid`

A pointer to the local unique
identifier of the SR_IOV device implementing the interface.


## Return Value

Return STATUS_SUCCESS if the operation succeeds. Otherwise, return an appropriate <a href="https://msdn.microsoft.com/7792201b-63bb-4db5-803d-2af02893d505">NTSTATUS</a> error code.

## Remarks

This callback function is implemented by the physical function (PF) driver. It is invoked  when the system wants to get the identifier of a specific virtual function. 

The PF driver registers its implementation by setting the <b>QueryLuid</b> member of the <a href="https://msdn.microsoft.com/c71add7d-9920-4b2f-a46a-4a09a94f3900">SRIOV_DEVICE_INTERFACE_STANDARD</a>, configuring a <a href="..\wdfqueryinterface\ns-wdfqueryinterface-_wdf_query_interface_config.md">WDF_QUERY_INTERFACE_CONFIG</a> structure, and calling <a href="..\wdfqueryinterface\nf-wdfqueryinterface-wdfdeviceaddqueryinterface.md">WdfDeviceAddQueryInterface</a>.

Here is an example implementation of this callback function. The PF driver generates a unique identifier by calling <a href="..\ntddk\nf-ntddk-zwallocatelocallyuniqueid.md">ZwAllocateLocallyUniqueId</a>  and stores it in the device context. 
<div class="code"><span codelanguage=""><table>
<tr>
<th></th>
</tr>
<tr>
<td>
<pre>
NTSTATUS
Virtualization_QueryLuid (
    _In_        PVOID             Context,
    _Out_       PLUID             Luid
    )
{
    PDEVICE_CONTEXT deviceContext;

    PAGED_CODE();

    deviceContext = (PDEVICE_CONTEXT)Context;
    *Luid = deviceContext-&gt;Luid;

    return STATUS_SUCCESS;
}

</pre>
</td>
</tr>
</table></span></div>

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Windows 10 Windows 10 |
| **Target Platform** | Windows |
| **Header** | pcivirt.h |
| **IRQL** | PASSIVE_LEVEL |