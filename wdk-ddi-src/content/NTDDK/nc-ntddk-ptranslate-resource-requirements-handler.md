---
UID: NC.ntddk.PTRANSLATE_RESOURCE_REQUIREMENTS_HANDLER
title: PTRANSLATE_RESOURCE_REQUIREMENTS_HANDLER
author: windows-driver-content
description: 
ms.assetid: 89b39776-c177-4f87-af17-dd6f51fbf1a0
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

# PTRANSLATE_RESOURCE_REQUIREMENTS_HANDLER callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PTRANSLATE_RESOURCE_REQUIREMENTS_HANDLER PtranslateResourceRequirementsHandler; 

// Definition

NTSTATUS PtranslateResourceRequirementsHandler 
(
	PVOID Context
	PIO_RESOURCE_DESCRIPTOR Source
	PDEVICE_OBJECT PhysicalDeviceObject
	PULONG TargetCount
	PIO_RESOURCE_DESCRIPTOR *Target
)
{...}

PTRANSLATE_RESOURCE_REQUIREMENTS_HANDLER 


```

## -parameters

### -param Context: 
### -param Source: 
### -param PhysicalDeviceObject: 
### -param TargetCount: 
### -param *Target: 



## -returns

Returns NTSTATUS that ...
Return STATUS_SUCCESS if the operation succeeds. Otherwise, return an appropriate NTSTATUS Values error code. For more information, see [XREF-LINK:NTSTATUS Values].

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also