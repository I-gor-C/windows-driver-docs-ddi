---
UID: NF:fltkernel.FltAddOpenReparseEntry
title: FltAddOpenReparseEntry function
author: windows-driver-content
description: This routine adds a caller allocated open reparse structure, OPEN_REPARSE_LIST_ENTRY, into a create operation.
old-location: ifsk\fltaddopenreparseentry.htm
old-project: ifsk
ms.assetid: D58AB46A-0D87-45B5-8C58-E99ED0F906D2
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: FltAddOpenReparseEntry, FltAddOpenReparseEntry routine [Installable File System Drivers], fltkernel/FltAddOpenReparseEntry, ifsk.fltaddopenreparseentry
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
product: Windows
targetos: Windows
req.typenames: EXpsFontRestriction
---


# FltAddOpenReparseEntry function
This routine adds a caller allocated open reparse structure, <a href="https://msdn.microsoft.com/A6D28F60-FA38-45EA-9E3C-D2E6F899333E">OPEN_REPARSE_LIST_ENTRY</a>,  into a create operation.

## Syntax

```
NTSTATUS FLTAPI FltAddOpenReparseEntry(
  PFLT_FILTER              Filter,
  PFLT_CALLBACK_DATA       Data,
  POPEN_REPARSE_LIST_ENTRY OpenReparseEntry
);
```

## Parameters

`Filter`

The filter to reference.

`Data`

The create operation to attach open reparse information to.

`OpenReparseEntry`

The open reparse information to add, of type <a href="https://msdn.microsoft.com/A6D28F60-FA38-45EA-9E3C-D2E6F899333E">OPEN_REPARSE_LIST_ENTRY</a>.


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

## Remarks

This routine adds an ECP list and/or ECP as needed.  <i>Filter</i> is referenced
    for the lifetime of the open reparse entry structure, not the ECP itself,
    which is conceptually independent of any specific filter.

Use <a href="https://msdn.microsoft.com/library/windows/hardware/mt734261">FltRemoveOpenReparseEntry</a> to remove the open reparse structure from the create operation.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Windows 10, version 1607 Windows Server 2016 |
| **Target Platform** | Windows |
| **Header** | fltkernel.h |
| **IRQL** | "_IRQL_requires_max_(APC_LEVEL)" |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/mt734261">FltRemoveOpenReparseEntry</a>