---
UID : NF:printoem.OEMPDriverEvent
title : OEMPDriverEvent function
author : windows-driver-content
description : OEMPDriverEvent function
old-location : print\oempdriverevent.htm
old-project : print
ms.assetid : 761967c9-c31f-4b7b-837a-bd48285c54fc
ms.author : windowsdriverdev
ms.date : 1/18/2018
ms.keywords : printoem/OEMPDriverEvent, OEMPDriverEvent, print_obsoletefunctions_c7348f27-998e-466b-97ad-b3175cfea28a.xml, OEMPDriverEvent function [Print Devices], print.oempdriverevent
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


# OEMPDriverEvent function


## Syntax

````
BOOL APIENTRY OEMPDriverEvent(
   DWORD  dwDriverEvent,
   DWORD  dwLevel,
   LPBYTE pDriverInfo,
   LPARAM lParam
);
````

## Parameters

`dwDriverEvent`



`dwLevel`



`pDriverInfo`



`lParam`




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