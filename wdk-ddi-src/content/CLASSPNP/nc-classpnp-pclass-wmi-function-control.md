---
UID: NC.classpnp.PCLASS_WMI_FUNCTION_CONTROL
title: PCLASS_WMI_FUNCTION_CONTROL
author: windows-driver-content
description: 
ms.assetid: 15b776db-e3fe-4dd7-bd47-4a05ab4570d8
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: classpnp.h
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

# PCLASS_WMI_FUNCTION_CONTROL callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PCLASS_WMI_FUNCTION_CONTROL PclassWmiFunctionControl; 

// Definition

NTSTATUS PclassWmiFunctionControl 
(
	PDEVICE_OBJECT DeviceObject
	PIRP Irp
	ULONG GuidIndex
	CLASSENABLEDISABLEFUNCTION Function
	BOOLEAN Enable
)
{...}

PCLASS_WMI_FUNCTION_CONTROL 


```

## -parameters

### -param DeviceObject: 
### -param Irp: 
### -param GuidIndex: 
### -param Function: 
### -param Enable: 



## -returns

Returns NTSTATUS that ...
Return STATUS_SUCCESS if the operation succeeds. Otherwise, return an appropriate NTSTATUS Values error code. For more information, see [XREF-LINK:NTSTATUS Values].

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also