---
UID: NF:wdm.ExIsResourceAcquiredSharedLite
title: ExIsResourceAcquiredSharedLite function
author: windows-driver-content
description: The ExIsResourceAcquiredSharedLite routine returns whether the current thread has access (either shared or exclusive) to a given resource.
old-location: kernel\exisresourceacquiredsharedlite.htm
old-project: kernel
ms.assetid: e87a4078-dbd4-4df2-bbfb-efbf76fc6279
ms.author: windowsdriverdev
ms.date: 3/1/2018
ms.keywords: ExIsResourceAcquiredLite, ExIsResourceAcquiredSharedLite, ExIsResourceAcquiredSharedLite routine [Kernel-Mode Driver Architecture], k102_e1ae158d-fd02-4962-813f-7bd87943f033.xml, kernel.exisresourceacquiredsharedlite, wdm/ExIsResourceAcquiredSharedLite
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: wdm.h
req.include-header: Wdm.h, Ntddk.h, Ntifs.h
req.target-type: Universal
req.target-min-winverclnt: Available starting with Windows 2000.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.ddi-compliance: HwStorPortProhibitedDDIs
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: NtosKrnl.lib
req.dll: NtosKrnl.exe
req.irql: "<= DISPATCH_LEVEL"
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	DllExport
api_location:
-	NtosKrnl.exe
api_name:
-	ExIsResourceAcquiredSharedLite
product: Windows
targetos: Windows
req.typenames: WORK_QUEUE_TYPE
req.product: Windows 10 or later.
---


# ExIsResourceAcquiredSharedLite function
The <b>ExIsResourceAcquiredSharedLite</b> routine returns whether the current thread has access (either shared or exclusive) to a given resource.

## Syntax

````
ULONG ExIsResourceAcquiredSharedLite(
  _In_ PERESOURCE Resource
);
````

## Parameters

`Resource`

A pointer to the resource to be queried.


## Return Value

<b>ExIsResourceAcquiredSharedLite</b> returns the number of times the caller has acquired the given resource for shared or exclusive access.

## Remarks

The system considers exclusive access to be a subset of shared access. Therefore, a thread that has exclusive access to a resource also has shared access to the resource.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Available starting with Windows 2000.  |
| **Target Platform** | Universal |
| **Header** | wdm.h (include Wdm.h, Ntddk.h, Ntifs.h) |
| **Library** | NtosKrnl.lib |
| **DLL** | NtosKrnl.exe |
| **IRQL** | "<= DISPATCH_LEVEL" |
| **DDI compliance rules** | HwStorPortProhibitedDDIs |

## See Also

<a href="..\wdm\nf-wdm-exacquiresharedstarveexclusive.md">ExAcquireSharedStarveExclusive</a>



<a href="..\wdm\nf-wdm-exacquiresharedwaitforexclusive.md">ExAcquireSharedWaitForExclusive</a>



<a href="..\wdm\nf-wdm-exisresourceacquiredexclusivelite.md">ExIsResourceAcquiredExclusiveLite</a>



<a href="..\wdm\nf-wdm-exacquireresourcesharedlite.md">ExAcquireResourceSharedLite</a>