---
UID: NC.classpnp.PCLASS_EXECUTE_WMI_METHOD
title: PCLASS_EXECUTE_WMI_METHOD
author: windows-driver-content
description: 
ms.assetid: 6ace1264-1abd-4ef7-97b6-8dc93bae5918
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

# PCLASS_EXECUTE_WMI_METHOD callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PCLASS_EXECUTE_WMI_METHOD PclassExecuteWmiMethod; 

// Definition

NTSTATUS PclassExecuteWmiMethod 
(
	PDEVICE_OBJECT DeviceObject
	PIRP Irp
	ULONG GuidIndex
	ULONG MethodId
	ULONG InBufferSize
	ULONG OutBufferSize
	PUCHAR Buffer
)
{...}

PCLASS_EXECUTE_WMI_METHOD 


```

## -parameters

### -param DeviceObject: 
### -param Irp: 
### -param GuidIndex: 
### -param MethodId: 
### -param InBufferSize: 
### -param OutBufferSize: 
### -param Buffer: 



## -returns

Returns NTSTATUS that ...
Return STATUS_SUCCESS if the operation succeeds. Otherwise, return an appropriate NTSTATUS Values error code. For more information, see [XREF-LINK:NTSTATUS Values].

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also