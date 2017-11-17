---
UID: NC.usbcamdi.PCAM_CONFIGURE_ROUTINE
title: PCAM_CONFIGURE_ROUTINE
author: windows-driver-content
description: 
ms.assetid: b793585a-e935-4ae4-acce-5ca9fcee8a8e
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: usbcamdi.h
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

# PCAM_CONFIGURE_ROUTINE callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PCAM_CONFIGURE_ROUTINE PcamConfigureRoutine; 

// Definition

NTSTATUS PcamConfigureRoutine 
(
	PDEVICE_OBJECT BusDeviceObject
	PVOID DeviceContext
	PUSBD_INTERFACE_INFORMATION Interface
	PUSB_CONFIGURATION_DESCRIPTOR ConfigurationDescriptor
	PLONG DataPipeIndex
	PLONG SyncPipeIndex
)
{...}

PCAM_CONFIGURE_ROUTINE 


```

## -parameters

### -param BusDeviceObject: 
### -param DeviceContext: 
### -param Interface: 
### -param ConfigurationDescriptor: 
### -param DataPipeIndex: 
### -param SyncPipeIndex: 



## -returns

Returns NTSTATUS that ...
Return STATUS_SUCCESS if the operation succeeds. Otherwise, return an appropriate NTSTATUS Values error code. For more information, see [XREF-LINK:NTSTATUS Values].

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also