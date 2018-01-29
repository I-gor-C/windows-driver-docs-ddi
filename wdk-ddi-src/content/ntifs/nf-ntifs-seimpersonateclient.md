---
UID : NF:ntifs.SeImpersonateClient
title : SeImpersonateClient function
author : windows-driver-content
description : Obsolete.
old-location : ifsk\seimpersonateclient.htm
old-project : ifsk
ms.assetid : b039609e-d259-44d7-bbde-20993576e18a
ms.author : windowsdriverdev
ms.date : 1/9/2018
ms.keywords : ntifs/SeImpersonateClient, seref_27996dfe-95b9-4d36-8182-9528fedef7d8.xml, SeImpersonateClient function [Installable File System Drivers], ifsk.seimpersonateclient, SeImpersonateClient
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : function
req.header : ntifs.h
req.include-header : Ntifs.h
req.target-type : Windows
req.target-min-winverclnt : 
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
req.lib : NtosKrnl.exe
req.dll : 
req.irql : 
topictype : 
apitype : 
apilocation : 
apiname : 
product : Windows
targetos : Windows
req.typenames : TOKEN_TYPE
---


# SeImpersonateClient function
The <b>SeImpersonateClient</b> routine is obsolete, but it is exported to support existing driver binaries. Use <a href="..\ntifs\nf-ntifs-seimpersonateclientex.md">SeImpersonateClientEx</a> instead.

## Syntax

````
  SeImpersonateClient(
    
);
````

## Parameters

`ClientContext`

TBD

`ServerThread`

TBD


## Return Value

None


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Target platform** | Windows |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | ntifs.h (include Ntifs.h) |
| **Library** |  |
| **IRQL** |  |
| **DDI compliance rules** |  |