---
UID : NF:ntifs.IoCheckDesiredAccess
title : IoCheckDesiredAccess function
author : windows-driver-content
description : Reserved for system use.
old-location : ifsk\iocheckdesiredaccess.htm
old-project : ifsk
ms.assetid : ab90ab40-7b45-4658-b11b-cf46f91f8699
ms.author : windowsdriverdev
ms.date : 1/9/2018
ms.keywords : ntifs/IoCheckDesiredAccess, ifsk.iocheckdesiredaccess, IoCheckDesiredAccess, ioref_f8879d66-0bad-4c92-b2a3-853b7eb65ac6.xml, IoCheckDesiredAccess function [Installable File System Drivers]
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


# IoCheckDesiredAccess function
The <b>IoCheckDesiredAccess</b> routine is reserved for system use. See <a href="..\wdm\nf-wdm-seaccesscheck.md">SeAccessCheck</a>.

## Syntax

````
  IoCheckDesiredAccess(
    
);
````

## Parameters

`DesiredAccess`

TBD

`GrantedAccess`

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