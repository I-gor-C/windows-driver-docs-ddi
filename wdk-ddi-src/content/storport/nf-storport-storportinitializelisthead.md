---
UID: NF:storport.StorPortInitializeListHead
title: StorPortInitializeListHead function
author: windows-driver-content
description: The StorPortInitializeListHead routine initializes a STOR_LIST_ENTRY structure that represents the head of a doubly linked list.
old-location: storage\storportinitializelisthead.htm
old-project: storage
ms.assetid: E37C54C1-209F-4944-940B-2247E86C8130
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: StorPortInitializeListHead, StorPortInitializeListHead routine [Storage Devices], storage.storportinitializelisthead, storport/StorPortInitializeListHead
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: storport.h
req.include-header: Storport.h
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
req.lib: 
req.dll: 
req.irql: 
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	HeaderDef
api_location:
-	storport.h
api_name:
-	StorPortInitializeListHead
product: Windows
targetos: Windows
req.typenames: STOR_SPINLOCK
req.product: Windows 10 or later.
---


# StorPortInitializeListHead function
<p class="CCE_Message">[Some information relates to pre-released product which may be substantially modified before it's commercially released. Microsoft makes no warranties, express or implied, with respect to the information provided here.]

The <b>StorPortInitializeListHead</b> routine initializes a <a href="https://msdn.microsoft.com/library/windows/hardware/mt790432">STOR_LIST_ENTRY</a> structure that represents the head of a doubly linked list.

## Syntax

```
void StorPortInitializeListHead(
  PVOID            HwDeviceExtension,
  PSTOR_LIST_ENTRY ListHead
);
```

## Parameters

`HwDeviceExtension`

A pointer to the hardware device extension for the host bus adapter (HBA).

`ListHead`

Pointer to the <a href="https://msdn.microsoft.com/library/windows/hardware/mt790432">STOR_LIST_ENTRY</a> structure that represents the head of the list.


## Return Value

This routine does not return a value.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Target Platform** | Universal |
| **Header** | storport.h (include Storport.h) |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff547799">InitializeListHead</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/mt790428">StorPortInterlockedInsertHeadList</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/mt790429">StorPortInterlockedInsertTailList</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/mt790430">StorPortInterlockedRemoveHeadList</a>