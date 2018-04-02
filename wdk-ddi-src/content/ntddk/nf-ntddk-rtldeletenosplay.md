---
UID: NF:ntddk.RtlDeleteNoSplay
title: RtlDeleteNoSplay function
author: windows-driver-content
description: The RtlDeleteNoSplay routine deletes the specified node from the splay link tree.
old-location: ifsk\rtldeletenosplay.htm
old-project: ifsk
ms.assetid: 09d8096a-71f9-4e9d-a66b-282424394b76
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: RtlDeleteNoSplay, RtlDeleteNoSplay routine [Installable File System Drivers], ifsk.rtldeletenosplay, ntddk/RtlDeleteNoSplay, rtlref_def5bfa8-367a-410e-8e3c-fdbf11cce05e.xml
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: ntddk.h
req.include-header: Ntddk.h, Ntifs.h
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
req.irql: See Remarks section.
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	DllExport
api_location:
-	NtosKrnl.exe
api_name:
-	RtlDeleteNoSplay
product:
- Windows
targetos: Windows
req.typenames: WHEA_RAW_DATA_FORMAT, *PWHEA_RAW_DATA_FORMAT
---


# RtlDeleteNoSplay function
The <b>RtlDeleteNoSplay</b> routine deletes the specified node from the splay link tree.

## Syntax

```
NTSYSAPI VOID RtlDeleteNoSplay(
  PRTL_SPLAY_LINKS Links,
  PRTL_SPLAY_LINKS *Root
);
```

## Parameters

`Links`

A pointer to the node to be deleted. The node must have been initialized by calling <b>RtlInitializeSplayLinks</b>.

`Root`

A pointer to the caller's pointer to the root node of the splay link tree. The caller's pointer is updated after the node is deleted.


## Return Value

None

## Remarks

Unlike <b>RtlDelete</b>, <b>RtlDeleteNoSplay</b> does not rebalance the splay link tree after the node is deleted. 

Callers of the <b>Rtl</b> splay link routines are responsible for synchronizing access to the splay link tree. A fast mutex is the most efficient synchronization mechanism to use for this purpose. 

Callers of <b>RtlDeleteNoSplay</b> must be running at IRQL &lt;= DISPATCH_LEVEL if the splay link tree is nonpaged. Usually, callers are running at IRQL PASSIVE_LEVEL.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Target Platform** | Universal |
| **Header** | ntddk.h (include Ntddk.h, Ntifs.h) |
| **Library** | NtosKrnl.lib |
| **DLL** | NtosKrnl.exe |
| **IRQL** | See Remarks section. |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff552201">RtlDelete</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff553010">RtlInitializeSplayLinks</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff553017">RtlInsertAsLeftChild</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff553022">RtlInsertAsRightChild</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff553226">RtlSplay</a>