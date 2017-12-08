---
UID: NC.pcivirt.SRIOV_RESET_FUNCTION
title: SRIOV_RESET_FUNCTION
author: windows-driver-content
description: Resets the specified PCI Express SR-IOV Virtual Function (VF).
old-location: pci\sriov_reset_function.htm
old-project: PCI
ms.assetid: 30c01528-8254-431f-aaba-79c05f66fc00
ms.author: windowsdriverdev
ms.date: 12/6/2017
ms.keywords: _PARCLASS_INFORMATION, PARCLASS_INFORMATION, *PPARCLASS_INFORMATION
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
req.alt-api: *PSRIOV_RESET_FUNCTION
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
---

# SRIOV_RESET_FUNCTION callback



## -description
Resets the specified PCI Express SR-IOV Virtual Function (VF).


## -prototype

````
SRIOV_RESET_FUNCTION SriovResetFunction;

NTSTATUS SriovResetFunction(
  _In_ PVOID  Context,
  _In_ USHORT VfIndex
)
{ ... }

typedef SRIOV_RESET_FUNCTION *PSRIOV_RESET_FUNCTION;
````


## -parameters

### -param Context [in]

A pointer to a driver-defined context.
                    
                

### -param VfIndex [in]

A zero-based index of the VF that is to be reset.

## -returns

Return STATUS_SUCCESS if the operation succeeds. Otherwise, return an appropriate <a href="https://msdn.microsoft.com/7792201b-63bb-4db5-803d-2af02893d505">NTSTATUS</a> error code.

## -remarks
This callback function is implemented by the physical function (PF) driver. It is invoked  when the system wants to reset a specific virtual function. 

The PF driver registers its implementation by setting the <b>ResetVf </b> member of the <a href="buses._sriov_device_interface_standard">SRIOV_DEVICE_INTERFACE_STANDARD</a>, configuring a <a href="wdf.wdf_query_interface_config">WDF_QUERY_INTERFACE_CONFIG</a> structure, and calling <a href="wdf.wdfdeviceaddqueryinterface">WdfDeviceAddQueryInterface</a>.

## -requirements
<table>
<tr>
<th width="30%">
Minimum supported client
</th>
<td width="70%">
Windows 10
</td>
</tr>
<tr>
<th width="30%">
Minimum supported server
</th>
<td width="70%">
Windows Server 2016
</td>
</tr>
<tr>
<th width="30%">
Header
</th>
<td width="70%">
<dl>
<dt>Pcivirt.h</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
IRQL
</th>
<td width="70%">
PASSIVE_LEVEL
</td>
</tr>
</table>