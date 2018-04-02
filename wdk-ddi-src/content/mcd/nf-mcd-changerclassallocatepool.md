---
UID: NF:mcd.ChangerClassAllocatePool
title: ChangerClassAllocatePool function
author: windows-driver-content
description: The ChangerClassAllocatePool function allocates pool memory.
old-location: storage\changerclassallocatepool.htm
old-project: storage
ms.assetid: d211bab9-4932-41c5-9b6f-528a75bb2ae4
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: ChangerClassAllocatePool, ChangerClassAllocatePool function [Storage Devices], chgrclas_e1b15ece-f3e4-446f-adc4-39301fc0346f.xml, mcd/ChangerClassAllocatePool, storage.changerclassallocatepool
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: mcd.h
req.include-header: Mcd.h, Ntddchgr.h
req.target-type: Desktop
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
req.lib: Mcd.lib
req.dll: 
req.irql: 
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	LibDef
api_location:
-	Mcd.lib
-	Mcd.dll
api_name:
-	ChangerClassAllocatePool
product: Windows
targetos: Windows
req.typenames: LAMP_INTENSITY_WHITE
---


# ChangerClassAllocatePool function
The <b>ChangerClassAllocatePool</b> function allocates pool memory.

## Syntax

```
PVOID ChangerClassAllocatePool(
  POOL_TYPE PoolType,
  ULONG     NumberOfBytes
);
```

## Parameters

`PoolType`

Indicates the type of pool memory to allocate. See <a href="https://msdn.microsoft.com/library/windows/hardware/ff559707">POOL_TYPE</a> for a list of types.

`NumberOfBytes`

Indicates number of bytes to allocate.


## Return Value

None


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Target Platform** | Desktop |
| **Header** | mcd.h (include Mcd.h, Ntddchgr.h) |
| **Library** | Mcd.lib |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff559707">POOL_TYPE</a>