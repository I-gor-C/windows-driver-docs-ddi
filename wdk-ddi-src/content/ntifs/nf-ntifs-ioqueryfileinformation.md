---
UID : NF:ntifs.IoQueryFileInformation
title : IoQueryFileInformation function
author : windows-driver-content
description : Reserved for system use.
old-location : ifsk\ioqueryfileinformation.htm
old-project : ifsk
ms.assetid : cfaa6068-979c-49c3-b671-c51ede023776
ms.author : windowsdriverdev
ms.date : 1/9/2018
ms.keywords : ntifs/IoQueryFileInformation, IoQueryFileInformation function [Installable File System Drivers], ioref_7dc69c37-bd12-4857-ae49-69d0d29d8e72.xml, ifsk.ioqueryfileinformation, IoQueryFileInformation
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


# IoQueryFileInformation function
The <b>IoQueryFileInformation</b> routine is reserved for system use. See <a href="..\wdm\nf-wdm-zwqueryinformationfile.md">ZwQueryInformationFile</a>.

## Syntax

````
  IoQueryFileInformation(
    
);
````

## Parameters

`FileObject`

TBD

`FileInformationClass`

TBD

`Length`

TBD

`FileInformation`

TBD

`ReturnedLength`

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