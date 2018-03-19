---
UID: NF:ntifs.MmCanFileBeTruncated
title: MmCanFileBeTruncated function
author: windows-driver-content
description: The MmCanFileBeTruncated routine checks whether a file can be truncated.
old-location: ifsk\mmcanfilebetruncated.htm
old-project: ifsk
ms.assetid: 219ecf09-54eb-4972-ae71-0eb3e7ea8ea9
ms.author: windowsdriverdev
ms.date: 2/16/2018
ms.keywords: MmCanFileBeTruncated, MmCanFileBeTruncated routine [Installable File System Drivers], ifsk.mmcanfilebetruncated, mmref_7d6c86f9-4a26-4d2c-bf55-9352044e9339.xml, ntifs/MmCanFileBeTruncated
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: ntifs.h
req.include-header: Ntifs.h
req.target-type: Universal
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: NtosKrnl.lib
req.dll: NtosKrnl.exe
req.irql: "< DISPATCH_LEVEL"
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	DllExport
api_location:
-	NtosKrnl.exe
api_name:
-	MmCanFileBeTruncated
product: Windows
targetos: Windows
req.typenames: TOKEN_TYPE
---


# MmCanFileBeTruncated function
The <b>MmCanFileBeTruncated</b> routine checks whether a file can be truncated.

## Syntax

````
BOOLEAN MmCanFileBeTruncated(
  _In_     PSECTION_OBJECT_POINTERS SectionPointer,
  _In_opt_ PLARGE_INTEGER           NewFileSize
);
````

## Parameters

`SectionPointer`

Pointer to a structure that contains the file object's section object pointers.

`NewFileSize`

Pointer to a variable that specifies the size to which the file is to be truncated.


## Return Value

<b>MmCanFileBeTruncated</b> returns <b>TRUE</b> if the file can be truncated, <b>FALSE</b> otherwise.

## Remarks

<b>MmCanFileBeTruncated</b> must always be called before a file is truncated.

A file cannot be truncated (and <b>MmCanFileBeTruncated</b> will return <b>FALSE</b>) if any of the following are true:

<ul>
<li>
An image section exists for the file.

</li>
<li>
There are one or more outstanding write probes on the file's data section.

</li>
<li>
There is a mapped view of file's data section within the truncation range determined by <i>NewFileSize</i>.

</li>
<li>
One or more users hold references to the data section for the file, and <i>NewFileSize</i> &lt;= the current file size.

</li>
</ul>

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Target Platform** | Universal |
| **Header** | ntifs.h (include Ntifs.h) |
| **Library** | NtosKrnl.lib |
| **DLL** | NtosKrnl.exe |
| **IRQL** | "< DISPATCH_LEVEL" |

## See Also

<a href="..\ntifs\nf-ntifs-mmflushimagesection.md">MmFlushImageSection</a>



<a href="..\ntifs\nf-ntifs-ccpurgecachesection.md">CcPurgeCacheSection</a>