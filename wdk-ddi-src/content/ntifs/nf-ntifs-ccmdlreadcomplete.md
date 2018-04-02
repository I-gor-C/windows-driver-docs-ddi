---
UID: NF:ntifs.CcMdlReadComplete
title: CcMdlReadComplete function
author: windows-driver-content
description: The CcMdlReadComplete routine frees the memory descriptor lists (MDL) created by CcMdlRead for a cached file.
old-location: ifsk\ccmdlreadcomplete.htm
old-project: ifsk
ms.assetid: c1525604-3aee-464d-a7f5-a6a4739a2aa4
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: CcMdlReadComplete, CcMdlReadComplete routine [Installable File System Drivers], ccref_9739ef62-748c-43c6-ae79-ae54f2358368.xml, ifsk.ccmdlreadcomplete, ntifs/CcMdlReadComplete
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
req.irql: PASSIVE_LEVEL
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	DllExport
api_location:
-	NtosKrnl.exe
api_name:
-	CcMdlReadComplete
product:
- Windows
targetos: Windows
req.typenames: TOKEN_TYPE
---


# CcMdlReadComplete function
The <b>CcMdlReadComplete</b> routine frees the memory descriptor lists (MDL) created by <a href="https://msdn.microsoft.com/library/windows/hardware/ff539159">CcMdlRead</a> for a cached file.

## Syntax

```
NTKERNELAPI VOID CcMdlReadComplete(
  PFILE_OBJECT FileObject,
  PMDL         MdlChain
);
```

## Parameters

`FileObject`

File object pointer that was passed to <a href="https://msdn.microsoft.com/library/windows/hardware/ff539159">CcMdlRead</a>.

`MdlChain`

Address of the MDL chain returned by <a href="https://msdn.microsoft.com/library/windows/hardware/ff539159">CcMdlRead</a>.


## Return Value

None

## Remarks

<b>CcMdlReadComplete</b> frees the memory descriptor lists (MDL) created by <a href="https://msdn.microsoft.com/library/windows/hardware/ff539159">CcMdlRead</a> for a cached file. All physical pages that were locked down are unlocked. Any pages that were mapped are unmapped.

Each call to <a href="https://msdn.microsoft.com/library/windows/hardware/ff539159">CcMdlRead</a> must be followed by a call to <b>CcMdlReadComplete</b>.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Target Platform** | Universal |
| **Header** | ntifs.h (include Ntifs.h) |
| **Library** | NtosKrnl.lib |
| **DLL** | NtosKrnl.exe |
| **IRQL** | PASSIVE_LEVEL |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff539159">CcMdlRead</a>