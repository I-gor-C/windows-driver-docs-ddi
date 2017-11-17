---
UID: NC.classpnp.PCLASS_QUERY_PNP_CAPABILITIES
title: PCLASS_QUERY_PNP_CAPABILITIES
author: windows-driver-content
description: 
ms.assetid: 2887cb56-60ee-496d-8f6c-bb840ab775b2
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

# PCLASS_QUERY_PNP_CAPABILITIES callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PCLASS_QUERY_PNP_CAPABILITIES PclassQueryPnpCapabilities; 

// Definition

NTSTATUS PclassQueryPnpCapabilities 
(
	PDEVICE_OBJECT PhysicalDeviceObject
	PDEVICE_CAPABILITIES Capabilities
)
{...}

PCLASS_QUERY_PNP_CAPABILITIES 


```

## -parameters

### -param PhysicalDeviceObject: 
### -param Capabilities: 



## -returns

Returns NTSTATUS that ...
Return STATUS_SUCCESS if the operation succeeds. Otherwise, return an appropriate NTSTATUS Values error code. For more information, see [XREF-LINK:NTSTATUS Values].

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also