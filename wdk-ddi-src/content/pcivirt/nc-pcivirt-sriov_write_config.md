---
UID : NC:pcivirt.SRIOV_WRITE_CONFIG
title : SRIOV_WRITE_CONFIG
author : windows-driver-content
description : Writes configuration data to a PCI Express SR-IOV Virtual Function (VF).
old-location : pci\sriov_write_config.htm
old-project : PCI
ms.assetid : 323c8150-ef58-42a4-8c8b-77081ecb64b3
ms.author : windowsdriverdev
ms.date : 12/29/2017
ms.keywords : PCI.sriov_write_config, SriovWriteConfig callback function [Buses], SriovWriteConfig, SRIOV_WRITE_CONFIG, SRIOV_WRITE_CONFIG, pcivirt/SriovWriteConfig, *PSRIOV_WRITE_CONFIG callback function pointer [Buses], *PSRIOV_WRITE_CONFIG
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
topictype : 
apitype : 
apilocation : 
apiname : 
product : Windows
targetos : Windows
req.typenames : PARCLASS_INFORMATION, *PPARCLASS_INFORMATION
---


# SRIOV_WRITE_CONFIG function
Writes configuration data to a PCI Express SR-IOV Virtual Function (VF).

## Syntax

```
SRIOV_WRITE_CONFIG SriovWriteConfig;

NTSTATUS SriovWriteConfig(
  PVOID Context,
  const VOID * Data,
  USHORT VfIndex,
  ULONG Offset,
  ULONG Length
)
{...}
```

## Parameters

`Context`

A pointer to a driver-defined context.

`Data`

A pointer to buffer that contains the data to be written to the configuration space.

`VfIndex`

A zero-based index of the VF to which this write operation applies.

`Offset`

An offset in bytes to the start of the VF’s configuration space where the write begins.

`Length`

The length, in bytes, of the data to write to the configuration space.


## Return Value

Return STATUS_SUCCESS if the operation succeeds. Otherwise, return an appropriate <a href="https://msdn.microsoft.com/7792201b-63bb-4db5-803d-2af02893d505">NTSTATUS</a> error code.

## Remarks

This callback function is implemented by the physical function (PF) driver. It is invoked  when the system wants to write to the configuration space of a specific virtual function. 

The PF driver registers its implementation by setting the <b>WriteVfConfig</b> member of the <a href="https://msdn.microsoft.com/c71add7d-9920-4b2f-a46a-4a09a94f3900">SRIOV_DEVICE_INTERFACE_STANDARD</a>, configuring a <a href="..\wdfqueryinterface\ns-wdfqueryinterface-_wdf_query_interface_config.md">WDF_QUERY_INTERFACE_CONFIG</a> structure, and calling <a href="..\wdfqueryinterface\nf-wdfqueryinterface-wdfdeviceaddqueryinterface.md">WdfDeviceAddQueryInterface</a>.

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