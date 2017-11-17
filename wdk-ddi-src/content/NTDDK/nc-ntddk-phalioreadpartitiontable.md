---
UID: NC.ntddk.pHalIoReadPartitionTable
title: pHalIoReadPartitionTable
author: windows-driver-content
description: 
ms.assetid: 55a73e30-b42b-498e-aadd-ec732c4b4e90
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: ntddk.h
req.include-header:
req.target-type:
req.target-min-winverclnt:
req.target-min-winversvr:
req.kmdf-ver:
req.umdf-ver:
req.lib:
req.dll:
req.irql: 
req.ddi-compliance:
req.alt-api:
req.alt-loc:
req.unicode-ansi:
req.idl:
req.max-support:
req.namespace:
req.assembly:
req.type-library:
---

# pHalIoReadPartitionTable callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

pHalIoReadPartitionTable Phalioreadpartitiontable; 

// Definition

NTSTATUS Phalioreadpartitiontable 
(
	PDEVICE_OBJECT DeviceObject
	ULONG SectorSize
	BOOLEAN ReturnRecognizedPartitions
	_DRIVE_LAYOUT_INFORMATION **PartitionBuffer
)
{...}

pHalIoReadPartitionTable 


```

## -parameters

### -param DeviceObject: 
### -param SectorSize: 
### -param ReturnRecognizedPartitions: 
### -param **PartitionBuffer: 



## -returns

Returns NTSTATUS that ...
Return STATUS_SUCCESS if the operation succeeds. Otherwise, return an appropriate NTSTATUS Values error code. For more information, see [XREF-LINK:NTSTATUS Values].

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also