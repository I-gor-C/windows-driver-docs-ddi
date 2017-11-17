---
UID: NC.trustedruntimeclx.PFN_TRSECUREDEVICECOMPLETEASYNCREQUEST
title: *PFN_TRSECUREDEVICECOMPLETEASYNCREQUEST
author: windows-driver-content
description: 
ms.assetid: adfe3e88-1cc9-4e12-81b2-49c139905034
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

# *PFN_TRSECUREDEVICECOMPLETEASYNCREQUEST callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

*PFN_TRSECUREDEVICECOMPLETEASYNCREQUEST *PfnTrsecuredevicecompleteasyncrequest; 

// Definition

NTSTATUS *PfnTrsecuredevicecompleteasyncrequest 
(
	WDFOBJECT BindContext
	PVOID RequestHandle
	NTSTATUS Result
	ULONG_PTR BytesWritten
)
{...}

*PFN_TRSECUREDEVICECOMPLETEASYNCREQUEST 


```

## -parameters

### -param BindContext: 
### -param RequestHandle: 
### -param Result: 
### -param BytesWritten: 



## -returns

Returns NTSTATUS that ...
Return STATUS_SUCCESS if the operation succeeds. Otherwise, return an appropriate NTSTATUS Values error code. For more information, see [XREF-LINK:NTSTATUS Values].

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also