---
UID : NF:printoem.OEMCommand
title : OEMCommand function
author : windows-driver-content
description : OEMCommand function
old-location : print\oemcommand.htm
old-project : print
ms.assetid : 67f75696-dee4-43ec-90fd-96fd1a91ec16
ms.author : windowsdriverdev
ms.date : 1/18/2018
ms.keywords : print.oemcommand, print_obsoletefunctions_f6d1a0f9-6560-4e4c-9826-c2714b7c1ad3.xml, OEMCommand, printoem/OEMCommand, OEMCommand function [Print Devices]
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : function
req.header : printoem.h
req.include-header : Printoem.h
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
req.typenames : STDVARIABLEINDEX
req.product : Windows 10 or later.
---


# OEMCommand function


## Syntax

````
DWORD APIENTRY OEMCommand(
       PDEVOBJ                         pdevobj,
       DWORD                           dwIndex,
  _In_ _reads_bytes_opt_(cbSize) PVOID pData,
       DWORD                           cbSize
);
````

## Parameters

`pdevobj`



`dwIndex`



`pData`



`cbSize`




## Return Value

None


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Target platform** | Windows |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | printoem.h (include Printoem.h) |
| **Library** |  |
| **IRQL** |  |
| **DDI compliance rules** |  |