---
UID: NF:wdm.ClfsLsnEqual
title: ClfsLsnEqual function
author: windows-driver-content
description: The ClfsLsnEqual routine determines whether two LSNs from the same stream are equal.
old-location: kernel\clfslsnequal.htm
old-project: kernel
ms.assetid: e154c9d5-a131-47db-b0fa-d51154637c56
ms.author: windowsdriverdev
ms.date: 3/28/2018
ms.keywords: ClfsLsnEqual, ClfsLsnEqual routine [Kernel-Mode Driver Architecture], Clfs_09dba2f1-3508-488d-b663-8ba0806b9d31.xml, kernel.clfslsnequal, wdm/ClfsLsnEqual
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: wdm.h
req.include-header: Wdm.h
req.target-type: Desktop
req.target-min-winverclnt: Available in Windows Server 2003 R2, Windows Vista, and later versions of Windows.
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
req.lib: Clfs.lib
req.dll: Clfs.sys
req.irql: Any level
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	DllExport
api_location:
-	Clfs.sys
-	Ext-MS-Win-fs-clfs-l1-1-0.dll
api_name:
-	ClfsLsnEqual
product:
- Windows
targetos: Windows
req.typenames: WORK_QUEUE_TYPE
req.product: Windows 10 or later.
---


# ClfsLsnEqual function
The <b>ClfsLsnEqual</b> routine determines whether two LSNs from the same stream are equal.

## Syntax

```
CLFSUSER_API BOOLEAN ClfsLsnEqual(
  const CLFS_LSN *plsn1,
  const CLFS_LSN *plsn2
);
```

## Parameters

`plsn1`

A pointer to a <a href="https://msdn.microsoft.com/library/windows/hardware/ff541824">CLFS_LSN</a> structure that supplies one of the LSNs to be compared.

`plsn2`

A pointer to a <a href="https://msdn.microsoft.com/library/windows/hardware/ff541824">CLFS_LSN</a> structure that supplies the other LSN to be compared.


## Return Value

<b>ClfsLsnEqual</b> returns <b>TRUE</b> if the two LSNs are equal; otherwise, it returns <b>FALSE</b>.

## Remarks

CLFS_LSN_NULL (the smallest LSN) and CLFS_LSN_INVALID (larger than any valid LSN) are valid arguments to <b>ClfsLsnEqual</b>.

LSNs from different streams are not comparable. Do not use <b>ClfsLsnEqual</b>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff541595">ClfsLsnGreater</a>, and the like to compare LSNs from different streams.

For an explanation of CLFS concepts and terminology, see <a href="https://msdn.microsoft.com/a9685648-b08c-48ca-b020-e683068f2ea2">Common Log File System</a>.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Available in Windows Server 2003 R2, Windows Vista, and later versions of Windows.  |
| **Target Platform** | Desktop |
| **Header** | wdm.h (include Wdm.h) |
| **Library** | Clfs.lib |
| **DLL** | Clfs.sys |
| **IRQL** | Any level |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff541595">ClfsLsnGreater</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff541608">ClfsLsnLess</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff541609">ClfsLsnNull</a>