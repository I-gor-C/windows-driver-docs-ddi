---
UID : NF:ntddk.PsTerminateServerSilo
title : PsTerminateServerSilo function
author : windows-driver-content
description : This routine terminates the specified silo.
old-location : kernel\psterminateserversilo.htm
old-project : kernel
ms.assetid : C19190A3-57F9-4482-A550-045805734909
ms.author : windowsdriverdev
ms.date : 1/4/2018
ms.keywords : PsTerminateServerSilo
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : function
req.header : ntddk.h
req.include-header : 
req.target-type : Windows
req.target-min-winverclnt : Windows 10, version 1607
req.target-min-winversvr : Windows Server 2016
req.kmdf-ver : 
req.umdf-ver : 
req.alt-api : PsTerminateServerSilo
req.alt-loc : ntddk.h
req.ddi-compliance : 
req.unicode-ansi : 
req.idl : 
req.max-support : 
req.namespace : 
req.assembly : 
req.type-library : 
req.lib : 
req.dll : 
req.irql : 
req.typenames : WHEA_RAW_DATA_FORMAT, *PWHEA_RAW_DATA_FORMAT
---


# PsTerminateServerSilo function
This routine terminates the specified silo.

## Syntax

````
void PsTerminateServerSilo(
  _In_ PESILO   ServerSilo,
  _In_ NTSTATUS ExistStatus
);
````

## Parameters

`ServerSilo`

A pointer to the silo being terminated.

`ExitStatus`




## Return Value

This routine does not return a value.

## Remarks

This routine can be called within or from outside a silo context.
    Note that this is different from a BugCheck; this routine will return to
    the caller.</p>

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Target platform** | Windows |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | ntddk.h |
| **Library** |  |
| **IRQL** |  |
| **DDI compliance rules** |  |