---
UID: NC.portcls.PCPFNSTARTDEVICE
title: PCPFNSTARTDEVICE
author: windows-driver-content
description: 
ms.assetid: 29ac9943-8890-41c3-90fc-8d0a860d3147
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: portcls.h
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

# PCPFNSTARTDEVICE callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PCPFNSTARTDEVICE Pcpfnstartdevice; 

// Definition

NTSTATUS Pcpfnstartdevice 
(
	PVOID DeviceObject
	PVOID Irp
	PRESOURCELIST ResourceList
)
{...}

PCPFNSTARTDEVICE 


```

## -parameters

### -param DeviceObject: 
### -param Irp: 
### -param ResourceList: 



## -returns

Returns NTSTATUS that ...
Return STATUS_SUCCESS if the operation succeeds. Otherwise, return an appropriate NTSTATUS Values error code. For more information, see [XREF-LINK:NTSTATUS Values].

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also