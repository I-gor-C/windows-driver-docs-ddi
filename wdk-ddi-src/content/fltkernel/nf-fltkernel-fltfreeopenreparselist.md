---
UID: NF:fltkernel.FltFreeOpenReparseList
title: FltFreeOpenReparseList function
author: windows-driver-content
description: This routine deallocates any information copied into a create operation by a previous call to FltCopyOpenReparseList.
old-location: ifsk\fltfreeopenreparselist.htm
old-project: ifsk
ms.assetid: 78FA1585-F834-48E4-BB15-78BA5563F9D0
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: FltAddOpenReparseEntry, FltAddOpenReparseEntry routine [Installable File System Drivers], FltFreeOpenReparseList, fltkernel/FltAddOpenReparseEntry, ifsk.fltfreeopenreparselist
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: fltkernel.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: Windows 10, version 1607
req.target-min-winversvr: Windows Server 2016
req.kmdf-ver: 
req.umdf-ver: 
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: "_IRQL_requires_max_(APC_LEVEL)"
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	HeaderDef
api_location:
-	fltKernel.h
api_name:
-	FltAddOpenReparseEntry
product:
- Windows
targetos: Windows
req.typenames: EXpsFontRestriction
---


# FltFreeOpenReparseList function
This routine deallocates any information copied into a create operation by
    a previous call to <a href="https://msdn.microsoft.com/library/windows/hardware/mt734258">FltCopyOpenReparseList</a>.

## Syntax

```
VOID FLTAPI FltFreeOpenReparseList(
  PFLT_FILTER Filter,
  PECP_LIST   EcpList
);
```

## Parameters

`Filter`

The filter to dereference.

`EcpList`

The ECP list whose open reparse information should
                       be deallocated.


## Return Value

This routine does not return a value.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Windows 10, version 1607 Windows Server 2016 |
| **Target Platform** | Windows |
| **Header** | fltkernel.h |
| **IRQL** | "_IRQL_requires_max_(APC_LEVEL)" |