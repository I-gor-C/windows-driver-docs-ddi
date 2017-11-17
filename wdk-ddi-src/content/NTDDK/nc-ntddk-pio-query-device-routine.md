---
UID: NC.ntddk.PIO_QUERY_DEVICE_ROUTINE
title: PIO_QUERY_DEVICE_ROUTINE
author: windows-driver-content
description: 
ms.assetid: 6f6714ae-fbe9-4df0-8d36-e051cf5be2a4
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

# PIO_QUERY_DEVICE_ROUTINE callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PIO_QUERY_DEVICE_ROUTINE PioQueryDeviceRoutine; 

// Definition

NTSTATUS PioQueryDeviceRoutine 
(
	PVOID Context
	PUNICODE_STRING PathName
	INTERFACE_TYPE BusType
	ULONG BusNumber
	PKEY_VALUE_FULL_INFORMATION *BusInformation
	CONFIGURATION_TYPE ControllerType
	ULONG ControllerNumber
	PKEY_VALUE_FULL_INFORMATION *ControllerInformation
	CONFIGURATION_TYPE PeripheralType
	ULONG PeripheralNumber
	PKEY_VALUE_FULL_INFORMATION *PeripheralInformation
)
{...}

PIO_QUERY_DEVICE_ROUTINE 


```

## -parameters

### -param Context: 
### -param PathName: 
### -param BusType: 
### -param BusNumber: 
### -param *BusInformation: 
### -param ControllerType: 
### -param ControllerNumber: 
### -param *ControllerInformation: 
### -param PeripheralType: 
### -param PeripheralNumber: 
### -param *PeripheralInformation: 



## -returns

Returns NTSTATUS that ...
Return STATUS_SUCCESS if the operation succeeds. Otherwise, return an appropriate NTSTATUS Values error code. For more information, see [XREF-LINK:NTSTATUS Values].

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also