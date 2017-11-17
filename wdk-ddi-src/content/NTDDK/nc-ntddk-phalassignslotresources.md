---
UID: NC.ntddk.pHalAssignSlotResources
title: pHalAssignSlotResources
author: windows-driver-content
description: 
ms.assetid: 02b6f0c5-3b03-47a6-bd19-f22004f076fc
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

# pHalAssignSlotResources callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

pHalAssignSlotResources Phalassignslotresources; 

// Definition

NTSTATUS Phalassignslotresources 
(
	PUNICODE_STRING RegistryPath
	PUNICODE_STRING DriverClassName OPTIONAL
	PDRIVER_OBJECT DriverObject
	PDEVICE_OBJECT DeviceObject
	INTERFACE_TYPE BusType
	ULONG BusNumber
	ULONG SlotNumber
	PCM_RESOURCE_LIST *AllocatedResources
)
{...}

pHalAssignSlotResources 


```

## -parameters

### -param RegistryPath: 
### -param OPTIONAL: 
### -param DriverObject: 
### -param DeviceObject: 
### -param BusType: 
### -param BusNumber: 
### -param SlotNumber: 
### -param *AllocatedResources: 



## -returns

Returns NTSTATUS that ...
Return STATUS_SUCCESS if the operation succeeds. Otherwise, return an appropriate NTSTATUS Values error code. For more information, see [XREF-LINK:NTSTATUS Values].

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also