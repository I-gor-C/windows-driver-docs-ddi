---
UID : NF:ntifs.ExQueryPoolBlockSize
title : ExQueryPoolBlockSize function
author : windows-driver-content
description : Obsolete.
old-location : ifsk\exquerypoolblocksize.htm
old-project : ifsk
ms.assetid : 0be3f5da-3fe6-45a2-b44a-b1634d74ede3
ms.author : windowsdriverdev
ms.date : 1/9/2018
ms.keywords : ExQueryPoolBlockSize
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
req.alt-api : ExQueryPoolBlockSize
req.alt-loc : ntifs.h
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
req.typenames : TOKEN_TYPE
---


# ExQueryPoolBlockSize function
<b>ExQueryPoolBlockSize</b> is obsolete and has never been documented. This routine is exported only to support a small number of legacy drivers. Also, if you call it in Microsoft Windows 2000 and the block is in special pool, the system will crash. Do not use this routine in your driver.

## Syntax

````
  ExQueryPoolBlockSize(
    
);
````

## Parameters

`PoolBlock`



`QuotaCharged`




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