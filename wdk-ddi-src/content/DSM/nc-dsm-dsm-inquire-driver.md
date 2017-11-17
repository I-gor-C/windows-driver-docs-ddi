---
UID: NC.dsm.DSM_INQUIRE_DRIVER
title: DSM_INQUIRE_DRIVER
author: windows-driver-content
description: 
ms.assetid: 92f02f24-74a9-46eb-8f67-7ea30f86fb51
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: dsm.h
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

# DSM_INQUIRE_DRIVER callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

DSM_INQUIRE_DRIVER DsmInquireDriver; 

// Definition

NTSTATUS DsmInquireDriver 
(
	IN PVOID DsmContext
	IN PDEVICE_OBJECT TargetDevice
	IN PDEVICE_OBJECT PortFdo
	IN PSTORAGE_DEVICE_DESCRIPTOR Descriptor
	IN PSTORAGE_DEVICE_ID_DESCRIPTOR DeviceIdList
	OUT PVOID *DsmIdentifier
)
{...}

DSM_INQUIRE_DRIVER 


```

## -parameters

### -param DsmContext: 
### -param TargetDevice: 
### -param PortFdo: 
### -param Descriptor: 
### -param DeviceIdList: 
### -param *DsmIdentifier: 



## -returns

Returns NTSTATUS that ...
Return STATUS_SUCCESS if the operation succeeds. Otherwise, return an appropriate NTSTATUS Values error code. For more information, see [XREF-LINK:NTSTATUS Values].

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also