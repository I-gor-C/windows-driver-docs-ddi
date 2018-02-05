---
UID : NF:ntddk.PsGetServerSiloActiveConsoleId
title : PsGetServerSiloActiveConsoleId function
author : windows-driver-content
description : Gets the active console for the current server silo context for the supplied thread.
old-location : kernel\psgetserversiloactiveconsoleid.htm
old-project : kernel
ms.assetid : 66b3c35d-681c-464a-86fa-972825bf3e97
ms.author : windowsdriverdev
ms.date : 1/4/2018
ms.keywords : PsGetServerSiloActiveConsoleId method [Kernel-Mode Driver Architecture], ntddk/PsGetServerSiloActiveConsoleId, PsGetServerSiloActiveConsoleId, kernel.psgetserversiloactiveconsoleid
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : function
req.header : ntddk.h
req.include-header : 
req.target-type : Windows
req.target-min-winverclnt : Windows 10, version 1709
req.target-min-winversvr : Windows Server 2016
req.kmdf-ver : 
req.umdf-ver : 
req.ddi-compliance : 
req.unicode-ansi : 
req.idl : 
req.max-support : 
req.namespace : 
req.assembly : 
req.type-library : 
req.lib : NtosKrnl.lib
req.dll : NtosKrnl.exe (kernel mode)
req.irql : PASSIVE_LEVEL
topictype : 
apitype : 
apilocation : 
apiname : 
product : Windows
targetos : Windows
req.typenames : WHEA_RAW_DATA_FORMAT, *PWHEA_RAW_DATA_FORMAT
---


# PsGetServerSiloActiveConsoleId function
Gets the active console for the current server silo context
    for the supplied thread.

## Syntax

````
ULONG  PsGetServerSiloActiveConsoleId(
   PESILO Silo
);
````

## Parameters

`Silo`

A pointer to the silo of the job.


## Return Value

Returns the session id for the active console session.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Windows 10, version 1709 Windows 10, version 1709 |
| **Target Platform** | Windows |
| **Header** | ntddk.h |
| **Library** | NtosKrnl.lib |
| **DLL** | NtosKrnl.exe (kernel mode) |
| **IRQL** | PASSIVE_LEVEL |