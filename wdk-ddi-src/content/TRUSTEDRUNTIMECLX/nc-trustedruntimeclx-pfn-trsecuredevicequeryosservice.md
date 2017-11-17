---
UID: NC.trustedruntimeclx.PFN_TRSECUREDEVICEQUERYOSSERVICE
title: *PFN_TRSECUREDEVICEQUERYOSSERVICE
author: windows-driver-content
description: 
ms.assetid: 55e9a640-c60d-40d6-a262-3bbf2006738e
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: trustedruntimeclx.h
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

# *PFN_TRSECUREDEVICEQUERYOSSERVICE callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

*PFN_TRSECUREDEVICEQUERYOSSERVICE *PfnTrsecuredevicequeryosservice; 

// Definition

NTSTATUS *PfnTrsecuredevicequeryosservice 
(
	WDFOBJECT BindContext
	WDFDEVICE Device
	LPCGUID OSServiceGuid
	PTR_SERVICE_INFORMATION Information
)
{...}

*PFN_TRSECUREDEVICEQUERYOSSERVICE 


```

## -parameters

### -param BindContext: 
### -param Device: 
### -param OSServiceGuid: 
### -param Information: 



## -returns

Returns NTSTATUS that ...
Return STATUS_SUCCESS if the operation succeeds. Otherwise, return an appropriate NTSTATUS Values error code. For more information, see [XREF-LINK:NTSTATUS Values].

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also