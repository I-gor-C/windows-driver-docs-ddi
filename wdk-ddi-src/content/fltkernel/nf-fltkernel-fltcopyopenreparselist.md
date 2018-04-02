---
UID: NF:fltkernel.FltCopyOpenReparseList
title: FltCopyOpenReparseList function
author: windows-driver-content
description: This routine copies any open reparse information from a previous create into a new ECP list that can be used to issue a second create.
old-location: ifsk\fltcopyopenreparselist.htm
old-project: ifsk
ms.assetid: 07C39363-559A-4B55-850E-052BA78E869D
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: FltAddOpenReparseEntry, FltAddOpenReparseEntry routine [Installable File System Drivers], FltCopyOpenReparseList, fltkernel/FltAddOpenReparseEntry, ifsk.fltcopyopenreparselist
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


# FltCopyOpenReparseList function
This routine copies any open reparse information from a previous create into
    a new ECP list that can be used to issue a second create.

## Syntax

```
NTSTATUS FLTAPI FltCopyOpenReparseList(
  PFLT_FILTER        Filter,
  PFLT_CALLBACK_DATA Data,
  PECP_LIST          EcpList
);
```

## Parameters

`Filter`

The filter to reference.

`Data`

The create operation from which open reparse
                       information should be copied.

`EcpList`

A new ECP list to copy open reparse information
                       to.


## Return Value

The following NT status codes are returned.

<table>
<tr>
<th>Return code</th>
<th>Description</th>
</tr>
<tr>
<td width="40%">
<dl>
<dt><b>STATUS_INVALID_PARAMETER_2</b></dt>
</dl>
</td>
<td width="60%">
Status code if <i>Data</i> is not a create operation. This is an error code.

</td>
</tr>
<tr>
<td width="40%">
<dl>
<dt><b>STATUS_SUCCESS</b></dt>
</dl>
</td>
<td width="60%">
The operation completed successfully.

</td>
</tr>
</table>


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Windows 10, version 1607 Windows Server 2016 |
| **Target Platform** | Windows |
| **Header** | fltkernel.h |
| **IRQL** | "_IRQL_requires_max_(APC_LEVEL)" |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/mt734259">FltFreeOpenReparseList</a>