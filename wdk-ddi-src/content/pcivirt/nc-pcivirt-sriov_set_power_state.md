---
UID : NC:pcivirt.SRIOV_SET_POWER_STATE
title : SRIOV_SET_POWER_STATE
author : windows-driver-content
description : Sets the power state of the specified PCI Express SR-IOV Virtual Function (VF).
old-location : pci\sriov_set_power_state.htm
old-project : PCI
ms.assetid : d43a21cb-5cee-4e72-8f0c-7aa8b2453507
ms.author : windowsdriverdev
ms.date : 12/29/2017
ms.keywords : _PARCLASS_INFORMATION, PARCLASS_INFORMATION, *PPARCLASS_INFORMATION
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : callback
req.header : pcivirt.h
req.include-header : 
req.target-type : Windows
req.target-min-winverclnt : Windows 10
req.target-min-winversvr : Windows Server 2016
req.kmdf-ver : 
req.umdf-ver : 
req.alt-api : SRIOV_SET_POWER_STATE
req.alt-loc : Pcivirt.h
req.ddi-compliance : 
req.unicode-ansi : 
req.idl : 
req.max-support : 
req.namespace : 
req.assembly : 
req.type-library : 
req.lib : 
req.dll : 
req.irql : PASSIVE_LEVEL
req.typenames : PARCLASS_INFORMATION, *PPARCLASS_INFORMATION
---


# SRIOV_SET_POWER_STATE function
Sets the power state of the specified PCI Express SR-IOV Virtual Function (VF).

## Syntax

```
SRIOV_SET_POWER_STATE SriovSetPowerState;

NTSTATUS SriovSetPowerState(
  PVOID Context,
  USHORT VfIndex,
  DEVICE_POWER_STATE PowerState,
  BOOLEAN Wake
)
{...}
```

## Parameters

`Context`

A pointer to a driver-defined context.

`VfIndex`

A zero-based index of the VF to which this power state set operation applies.

`PowerState`

A <a href="..\wudfddi\ne-wudfddi-_device_power_state.md">DEVICE_POWER_STATE</a>-type value that indicates the <b>Dx</b> power state to set.

`Wake`

A boolean value that indicates whether to arm the device for a wake signal (PME for PCI Express devices), as it goes into the low power state. TRUE  indicates the device is armed; FALSE otherwise. This value must be FALSE if <i>PowerState</i> is <b>PowerDeviceD0</b>.


## Return Value

Set to STATUS_SUCCESS if the request is successful. Otherwise, return appropriate a <a href="https://msdn.microsoft.com/7792201b-63bb-4db5-803d-2af02893d505">NTSTATUS</a> code to indicate the error condition.

## Remarks

This callback function is implemented by the physical function (PF) driver. The callback is invoked when the system wants to change the power state of a virtual function. 

The PF driver registers its implementation by setting the <b>SetVfPowerState</b> member of the SRIOV_DEVICE_INTERFACE_STANDARD, configuring a <a href="..\wdfqueryinterface\ns-wdfqueryinterface-_wdf_query_interface_config.md">WDF_QUERY_INTERFACE_CONFIG</a> structure, and calling <a href="..\wdfqueryinterface\nf-wdfqueryinterface-wdfdeviceaddqueryinterface.md">WdfDeviceAddQueryInterface</a>.

Here is an example implementation of this callback function.</p>

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Target platform** | Windows |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | pcivirt.h |
| **Library** |  |
| **IRQL** | PASSIVE_LEVEL |
| **DDI compliance rules** |  |