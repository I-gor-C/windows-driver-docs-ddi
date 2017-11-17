---
UID: NC.udecxusbdevice.PFN_UDECXUSBDEVICEINITADDSTRINGDESCRIPTORRAW
title: *PFN_UDECXUSBDEVICEINITADDSTRINGDESCRIPTORRAW
author: windows-driver-content
description: 
ms.assetid: ef4269b5-0c31-44e5-98f6-6063e7963982
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

# *PFN_UDECXUSBDEVICEINITADDSTRINGDESCRIPTORRAW callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

*PFN_UDECXUSBDEVICEINITADDSTRINGDESCRIPTORRAW *PfnUdecxusbdeviceinitaddstringdescriptorraw; 

// Definition

NTSTATUS *PfnUdecxusbdeviceinitaddstringdescriptorraw 
(
	PUDECX_DRIVER_GLOBALS DriverGlobals
	PUDECXUSBDEVICE_INIT UdecxUsbDeviceInit
	PUCHAR Descriptor
	USHORT DescriptorLength
	UCHAR DescriptorIndex
	USHORT LanguageId
)
{...}

*PFN_UDECXUSBDEVICEINITADDSTRINGDESCRIPTORRAW 


```

## -parameters

### -param DriverGlobals: 
### -param UdecxUsbDeviceInit: 
### -param Descriptor: 
### -param DescriptorLength: 
### -param DescriptorIndex: 
### -param LanguageId: 



## -returns

Returns NTSTATUS that ...
Return STATUS_SUCCESS if the operation succeeds. Otherwise, return an appropriate NTSTATUS Values error code. For more information, see [XREF-LINK:NTSTATUS Values].

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also