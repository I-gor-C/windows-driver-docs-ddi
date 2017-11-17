---
UID: NC.wdm.PFN_NT_QUERY_INFORMATION_TRANSACTION
title: PFN_NT_QUERY_INFORMATION_TRANSACTION
author: windows-driver-content
description: 
ms.assetid: 6c2433c5-bd26-41d5-804a-2c6143c47476
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

# PFN_NT_QUERY_INFORMATION_TRANSACTION callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_NT_QUERY_INFORMATION_TRANSACTION PfnNtQueryInformationTransaction; 

// Definition

NTSTATUS PfnNtQueryInformationTransaction 
(
	HANDLE TransactionHandle
	TRANSACTION_INFORMATION_CLASS TransactionInformationClass
	PVOID TransactionInformation
	ULONG TransactionInformationLength
	PULONG ReturnLength
)
{...}

PFN_NT_QUERY_INFORMATION_TRANSACTION 


```

## -parameters

### -param TransactionHandle: 
### -param TransactionInformationClass: 
### -param TransactionInformation: 
### -param TransactionInformationLength: 
### -param ReturnLength: 



## -returns

Returns NTSTATUS that ...
Return STATUS_SUCCESS if the operation succeeds. Otherwise, return an appropriate NTSTATUS Values error code. For more information, see [XREF-LINK:NTSTATUS Values].

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also