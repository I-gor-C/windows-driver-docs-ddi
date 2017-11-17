---
UID: NC.udecxusbdevice.PFN_UDECXUSBDEVICEINITADDDESCRIPTORWITHINDEX
title: *PFN_UDECXUSBDEVICEINITADDDESCRIPTORWITHINDEX
author: windows-driver-content
description: 
ms.assetid: 3d0679d5-2e1f-4e86-a9cd-4c80e1fdcebb
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: udecxusbdevice.h
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

# *PFN_UDECXUSBDEVICEINITADDDESCRIPTORWITHINDEX callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

*PFN_UDECXUSBDEVICEINITADDDESCRIPTORWITHINDEX *PfnUdecxusbdeviceinitadddescriptorwithindex; 

// Definition

NTSTATUS *PfnUdecxusbdeviceinitadddescriptorwithindex 
(
	PUDECX_DRIVER_GLOBALS DriverGlobals
	PUDECXUSBDEVICE_INIT UdecxUsbDeviceInit
	PUCHAR Descriptor
	USHORT DescriptorLength
	UCHAR DescriptorIndex
)
{...}

*PFN_UDECXUSBDEVICEINITADDDESCRIPTORWITHINDEX 


```

## -parameters

### -param DriverGlobals: 
### -param UdecxUsbDeviceInit: 
### -param Descriptor: 
### -param DescriptorLength: 
### -param DescriptorIndex: 



## -returns

Returns NTSTATUS that ...
Return STATUS_SUCCESS if the operation succeeds. Otherwise, return an appropriate NTSTATUS Values error code. For more information, see [XREF-LINK:NTSTATUS Values].

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also