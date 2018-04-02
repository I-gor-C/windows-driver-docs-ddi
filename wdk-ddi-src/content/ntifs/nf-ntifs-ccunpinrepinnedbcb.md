---
UID: NF:ntifs.CcUnpinRepinnedBcb
title: CcUnpinRepinnedBcb function
author: windows-driver-content
description: The CcUnpinRepinnedBcb routine unpins a repinned buffer control block (BCB).
old-location: ifsk\ccunpinrepinnedbcb.htm
old-project: ifsk
ms.assetid: 96a35574-87dc-4a2f-aaef-616096839f3f
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: CcUnpinRepinnedBcb, CcUnpinRepinnedBcb routine [Installable File System Drivers], ccref_72300deb-bf8a-4f2a-b594-69ccb01cff56.xml, ifsk.ccunpinrepinnedbcb, ntifs/CcUnpinRepinnedBcb
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
req.irql: 
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	DllExport
api_location:
-	NtosKrnl.exe
api_name:
-	CcUnpinRepinnedBcb
product:
- Windows
targetos: Windows
req.typenames: TOKEN_TYPE
---


# CcUnpinRepinnedBcb function
The <b>CcUnpinRepinnedBcb</b> routine unpins a repinned buffer control block (BCB).

## Syntax

```
NTKERNELAPI VOID CcUnpinRepinnedBcb(
  PVOID            Bcb,
  BOOLEAN          WriteThrough,
  PIO_STATUS_BLOCK IoStatus
);
```

## Parameters

`Bcb`

Pointer to the repinned BCB.

`WriteThrough`

Set to <b>TRUE</b> if the BCB should be written through.

`IoStatus`

Pointer to an IO_STATUS_BLOCK structure. If the call to <b>CcUnpinRepinnedBcb</b> succeeds, <i>IoStatus.Status</i> is set to STATUS_SUCCESS. Otherwise, it is set to an appropriate NTSTATUS error code. <i>IoStatus.Information</i> is set to the actual number of bytes that were successfully flushed to disk.


## Return Value

None

## Remarks

File systems call <b>CcUnpinRepinnedBcb</b> to write a previously pinned buffer through to disk.

Every call to <a href="https://msdn.microsoft.com/library/windows/hardware/ff539196">CcRepinBcb</a> must be matched by a subsequent call to <b>CcUnpinRepinnedBcb</b>.

Because <b>CcUnpinRepinnedBcb</b> acquires the BCB resource exclusively, the caller must be extremely careful to avoid deadlocks. If possible, the caller should own no resources. Otherwise the caller must guarantee that it has nothing else pinned in the same cached file. Normally <b>CcUnpinRepinnedBcb</b> is called during request completion, after all other resources have been released.

<b>CcUnpinRepinnedBcb</b> synchronously writes the buffer (for write-through requests) and unpins the BCB repinned by the earlier call to <a href="https://msdn.microsoft.com/library/windows/hardware/ff539196">CcRepinBcb</a>.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Target Platform** | Universal |
| **Header** | ntifs.h (include Ntifs.h) |
| **Library** | NtosKrnl.lib |
| **DLL** | NtosKrnl.exe |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff539196">CcRepinBcb</a>