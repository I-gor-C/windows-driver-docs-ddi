---
UID: NC.usbcamdi.PCAM_CONFIGURE_ROUTINE_EX
title: PCAM_CONFIGURE_ROUTINE_EX
author: windows-driver-content
description: 
ms.assetid: c4e302d3-4728-429c-afcf-6ca691c2fa3f
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

# PCAM_CONFIGURE_ROUTINE_EX callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PCAM_CONFIGURE_ROUTINE_EX PcamConfigureRoutineEx; 

// Definition

NTSTATUS PcamConfigureRoutineEx 
(
	PDEVICE_OBJECT BusDeviceObject
	PVOID DeviceContext
	PUSBD_INTERFACE_INFORMATION Interface
	PUSB_CONFIGURATION_DESCRIPTOR ConfigurationDescriptor
	ULONG PipeConfigListSize
	PUSBCAMD_Pipe_Config_Descriptor PipeConfig
	PUSB_DEVICE_DESCRIPTOR DeviceDescriptor
)
{...}

PCAM_CONFIGURE_ROUTINE_EX 


```

## -parameters

### -param BusDeviceObject: 
### -param DeviceContext: 
### -param Interface: 
### -param ConfigurationDescriptor: 
### -param PipeConfigListSize: 
### -param PipeConfig: 
### -param DeviceDescriptor: 



## -returns

Returns NTSTATUS that ...
Return STATUS_SUCCESS if the operation succeeds. Otherwise, return an appropriate NTSTATUS Values error code. For more information, see [XREF-LINK:NTSTATUS Values].

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also