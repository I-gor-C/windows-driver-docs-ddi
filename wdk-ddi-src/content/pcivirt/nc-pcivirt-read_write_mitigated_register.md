---
UID : NC:pcivirt.READ_WRITE_MITIGATED_REGISTER
title : READ_WRITE_MITIGATED_REGISTER
author : windows-driver-content
description : Reads or writes to mitigated address spaces.
old-location : pci\read_write_mitigated_registers.htm
old-project : PCI
ms.assetid : 7cd45484-0fee-4b8e-aa35-4142883c146e
ms.author : windowsdriverdev
ms.date : 12/29/2017
ms.keywords : PCI.read_write_mitigated_registers, ReadWriteMitigatedRegister callback function [Buses], ReadWriteMitigatedRegister, READ_WRITE_MITIGATED_REGISTER, READ_WRITE_MITIGATED_REGISTER, pcivirt/ReadWriteMitigatedRegister, *PREAD_WRITE_MITIGATED_REGISTER callback function pointer [Buses], *PREAD_WRITE_MITIGATED_REGISTER
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


# READ_WRITE_MITIGATED_REGISTER function
Reads or writes to mitigated address spaces.

## Syntax

```
READ_WRITE_MITIGATED_REGISTER ReadWriteMitigatedRegister;

NTSTATUS ReadWriteMitigatedRegister(
  PVOID Context,
  USHORT VfIndex,
  BOOLEAN Read,
  USHORT BarIndex,
  ULONGLONG Offset,
  ULONG Length,
  PUCHAR Data
)
{...}
```

## Parameters

`Context`

A pointer to a driver-defined context.

`VfIndex`

A zero-based index of the VF to which this read/write operation applies.

`Read`

A boolean that indicates whether to perform a read or a write operation. TRUE indicates read, FALSE otherwise.

`BarIndex`

The BAR that maps the address space being mitigated.

`Offset`

The offset in number of bytes into the BAR at which this access begins.

`Length`

The length in bytes of this read or write operation.

`Data`

A pointer to a buffer that contains the data to read or write.


## Return Value

Return STATUS_SUCCESS if the operation succeeds. Otherwise, return an appropriate <a href="https://msdn.microsoft.com/7792201b-63bb-4db5-803d-2af02893d505">NTSTATUS</a> error code.

## Remarks

This callback function is implemented by the physical function (PF) driver. It is invoked  when the system wants to read or write from a mitigable register. 

The PF driver registers its implementation by setting the <b>ReadWriteMitigatedRegister</b> member of the <a href="https://msdn.microsoft.com/1fac7c03-2a48-4b29-951d-c777fbec7dd3">MITIGABLE_DEVICE_INTERFACE</a>, configuring a <a href="..\wdfqueryinterface\ns-wdfqueryinterface-_wdf_query_interface_config.md">WDF_QUERY_INTERFACE_CONFIG</a> structure, and calling <a href="..\wdfqueryinterface\nf-wdfqueryinterface-wdfdeviceaddqueryinterface.md">WdfDeviceAddQueryInterface</a>.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Windows 10 Windows 10 |
| **Target Platform** | Windows |
| **Header** | pcivirt.h |
| **IRQL** | PASSIVE_LEVEL |