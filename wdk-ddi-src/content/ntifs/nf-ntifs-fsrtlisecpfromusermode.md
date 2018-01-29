---
UID : NF:ntifs.FsRtlIsEcpFromUserMode
title : FsRtlIsEcpFromUserMode function
author : windows-driver-content
description : The FsRtlIsEcpFromUserMode routine determines whether an extra create parameter (ECP) context structure originated from user mode.
old-location : ifsk\fsrtlisecpfromusermode.htm
old-project : ifsk
ms.assetid : cdc5d6a3-637e-4f0e-bc94-25bfe5763695
ms.author : windowsdriverdev
ms.date : 1/9/2018
ms.keywords : ntifs/FsRtlIsEcpFromUserMode, ifsk.fsrtlisecpfromusermode, FsRtlIsEcpFromUserMode routine [Installable File System Drivers], FsRtlIsEcpFromUserMode, fsrtlref_14f09529-adf9-4113-bff4-5183ade20059.xml
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : function
req.header : ntifs.h
req.include-header : Ntifs.h
req.target-type : Universal
req.target-min-winverclnt : FsRtlIsEcpFromUserMode is available starting with Windows Vista.
req.target-min-winversvr : 
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
req.dll : NtosKrnl.exe
req.irql : "<= APC_LEVEL"
topictype : 
apitype : 
apilocation : 
apiname : 
product : Windows
targetos : Windows
req.typenames : TOKEN_TYPE
---


# FsRtlIsEcpFromUserMode function
The <b>FsRtlIsEcpFromUserMode</b> routine determines whether an extra create parameter (ECP) context structure originated from user mode.

## Syntax

````
BOOLEAN FsRtlIsEcpFromUserMode(
  _In_ PVOID EcpContext
);
````

## Parameters

`EcpContext`

Pointer to the ECP context structure to test.


## Return Value

<b>FsRtlIsEcpFromUserMode</b> returns <b>TRUE</b> if the ECP context structure originated in user mode and <b>FALSE</b> if the ECP context structure originated in kernel mode.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Target platform** | Universal |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | ntifs.h (include Ntifs.h) |
| **Library** |  |
| **IRQL** | <= APC_LEVEL |
| **DDI compliance rules** |  |