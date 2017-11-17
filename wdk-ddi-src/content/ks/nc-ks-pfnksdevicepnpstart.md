---
UID: NC.ks.PFNKSDEVICEPNPSTART
title: PFNKSDEVICEPNPSTART
author: windows-driver-content
description: 
ms.assetid: 8932c5ec-5f6b-4d51-97c9-6bb11797051c
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: ks.h
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

# PFNKSDEVICEPNPSTART callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFNKSDEVICEPNPSTART Pfnksdevicepnpstart; 

// Definition

NTSTATUS Pfnksdevicepnpstart 
(
	PKSDEVICE Device
	PIRP Irp
	PCM_RESOURCE_LIST TranslatedResourceList
	PCM_RESOURCE_LIST UntranslatedResourceList
)
{...}

PFNKSDEVICEPNPSTART 


```

## -parameters

### -param Device: 
### -param Irp: 
### -param TranslatedResourceList: 
### -param UntranslatedResourceList: 



## -returns

Returns NTSTATUS that ...
Return STATUS_SUCCESS if the operation succeeds. Otherwise, return an appropriate NTSTATUS Values error code. For more information, see [XREF-LINK:NTSTATUS Values].

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also