---
UID : NF:ks.KsCreateClock
title : KsCreateClock function
author : windows-driver-content
description : The KsCreateClock function creates a handle to a clock instance.
old-location : stream\kscreateclock.htm
old-project : stream
ms.assetid : a125161d-c086-45a4-9b66-4c13d9ed5f11
ms.author : windowsdriverdev
ms.date : 1/9/2018
ms.keywords : KsCreateClock
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : function
req.header : ks.h
req.include-header : Ks.h
req.target-type : Universal
req.target-min-winverclnt : 
req.target-min-winversvr : 
req.kmdf-ver : 
req.umdf-ver : 
req.alt-api : KsCreateClock
req.alt-loc : ks.lib,ks.dll
req.ddi-compliance : 
req.unicode-ansi : 
req.idl : 
req.max-support : 
req.namespace : 
req.assembly : 
req.type-library : 
req.lib : Ks.lib
req.dll : 
req.irql : PASSIVE_LEVEL
req.typenames : 
---


# KsCreateClock function
The <b>KsCreateClock</b> function creates a handle to a clock instance.

## Syntax

````
NTSTATUS KsCreateClock(
  _In_  HANDLE          ConnectionHandle,
  _In_  PKSCLOCK_CREATE ClockCreate,
  _Out_ PHANDLE         ClockHandle
);
````

## Parameters

`ConnectionHandle`

Specifies the handle to the connection on which to create the clock.

`ClockCreate`

Specifies clock create parameters. This currently consists of a flag that must be set to zero.

`ClockHandle`

Specifies the new clock handle.


## Return Value

The <b>KsCreateClock</b> function returns STATUS_SUCCESS if successful, or it returns an error on clock creation failure.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Target platform** | Universal |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | ks.h (include Ks.h) |
| **Library** |  |
| **IRQL** | PASSIVE_LEVEL |
| **DDI compliance rules** |  |