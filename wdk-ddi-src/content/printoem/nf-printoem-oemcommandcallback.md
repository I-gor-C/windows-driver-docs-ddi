---
UID : NF:printoem.OEMCommandCallback
title : OEMCommandCallback function
author : windows-driver-content
description : OEMCommandCallback function
old-location : print\oemcommandcallback.htm
old-project : print
ms.assetid : 0ac9c56d-f03d-4082-a7df-c21db12c0d74
ms.author : windowsdriverdev
ms.date : 1/18/2018
ms.keywords : OEMCommandCallback function [Print Devices], printoem/OEMCommandCallback, OEMCommandCallback, print.oemcommandcallback, print_obsoletefunctions_e59bdbd7-9100-40b3-9e89-6d41cbc85f44.xml
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


# OEMCommandCallback function


## Syntax

````
INT APIENTRY OEMCommandCallback(
       PDEVOBJ                     pdevobj,
       DWORD                       dwCallbackID,
       DWORD                       dwCount,
  _In_ _reads_opt_(dwCount) PDWORD pdwParams
);
````

## Parameters

`pdevobj`



`dwCallbackID`



`dwCount`



`pdwParams`




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