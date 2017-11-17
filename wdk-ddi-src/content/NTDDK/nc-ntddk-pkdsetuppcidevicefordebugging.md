---
UID: NC.ntddk.pKdSetupPciDeviceForDebugging
title: pKdSetupPciDeviceForDebugging
author: windows-driver-content
description: 
ms.assetid: 01110763-4906-4b64-9645-2c8103f7d4ed
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

# pKdSetupPciDeviceForDebugging callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

pKdSetupPciDeviceForDebugging Pkdsetuppcidevicefordebugging; 

// Definition

NTSTATUS Pkdsetuppcidevicefordebugging 
(
	PVOID LoaderBlock
	OPTIONAL PDEBUG_DEVICE_DESCRIPTOR PciDevice
)
{...}

pKdSetupPciDeviceForDebugging 


```

## -parameters

### -param LoaderBlock: 
### -param PciDevice: 



## -returns

Returns NTSTATUS that ...
Return STATUS_SUCCESS if the operation succeeds. Otherwise, return an appropriate NTSTATUS Values error code. For more information, see [XREF-LINK:NTSTATUS Values].

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also