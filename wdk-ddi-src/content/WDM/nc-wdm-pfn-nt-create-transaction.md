---
UID: NC.wdm.PFN_NT_CREATE_TRANSACTION
title: PFN_NT_CREATE_TRANSACTION
author: windows-driver-content
description: 
ms.assetid: 0512ff46-0122-4ebf-9469-799baaca0694
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

# PFN_NT_CREATE_TRANSACTION callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_NT_CREATE_TRANSACTION PfnNtCreateTransaction; 

// Definition

NTSTATUS PfnNtCreateTransaction 
(
	PHANDLE TransactionHandle
	ACCESS_MASK DesiredAccess
	POBJECT_ATTRIBUTES ObjectAttributes
	LPGUID Uow
	HANDLE TmHandle
	ULONG CreateOptions
	ULONG IsolationLevel
	ULONG IsolationFlags
	PLARGE_INTEGER Timeout
	PUNICODE_STRING Description
)
{...}

PFN_NT_CREATE_TRANSACTION 


```

## -parameters

### -param TransactionHandle: 
### -param DesiredAccess: 
### -param ObjectAttributes: 
### -param Uow: 
### -param TmHandle: 
### -param CreateOptions: 
### -param IsolationLevel: 
### -param IsolationFlags: 
### -param Timeout: 
### -param Description: 



## -returns

Returns NTSTATUS that ...
Return STATUS_SUCCESS if the operation succeeds. Otherwise, return an appropriate NTSTATUS Values error code. For more information, see [XREF-LINK:NTSTATUS Values].

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also