---
UID: NC.wdm.PDEVICE_RESET_HANDLER
title: PDEVICE_RESET_HANDLER
author: windows-driver-content
description: 
ms.assetid: 421f6822-0e04-41a0-b616-ef2a4fa1141f
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: wdm.h
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

# PDEVICE_RESET_HANDLER callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PDEVICE_RESET_HANDLER PdeviceResetHandler; 

// Definition

NTSTATUS PdeviceResetHandler 
(
	PVOID InterfaceContext
	DEVICE_RESET_TYPE ResetType
	ULONG Flags
	PVOID ResetParameters
)
{...}

PDEVICE_RESET_HANDLER 


```

## -parameters

### -param InterfaceContext: 
### -param ResetType: 
### -param Flags: 
### -param ResetParameters: 



## -returns

Returns NTSTATUS that ...
Return STATUS_SUCCESS if the operation succeeds. Otherwise, return an appropriate NTSTATUS Values error code. For more information, see [XREF-LINK:NTSTATUS Values].

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also