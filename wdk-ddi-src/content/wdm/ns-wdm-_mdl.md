---
UID: NS:wdm._MDL
title: "_MDL"
author: windows-driver-content
description: An MDL structure is a partially opaque structure that represents a memory descriptor list (MDL).
old-location: kernel\mdl.htm
old-project: kernel
ms.assetid: 71524333-dd5d-4f0b-8dd3-034ea926bc93
ms.author: windowsdriverdev
ms.date: 3/28/2018
ms.keywords: "*PMDLX, MDL, MDL structure [Kernel-Mode Driver Architecture], PMDL, _MDL, kernel.mdl, kstruct_c_2c589a9a-d775-4fa6-8a37-37212798a215.xml, wdm/MDL"
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: wdm.h
req.include-header: Wdm.h, Ntddk.h, Ntifs.h
req.target-type: Windows
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
req.irql: PASSIVE_LEVEL (see Remarks section)
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	HeaderDef
api_location:
-	Wdm.h
api_name:
-	MDL
product:
- Windows
targetos: Windows
req.typenames: MDL, PMDL
req.product: Windows 10 or later.
---

# _MDL structure
An <b>MDL</b> structure is a partially opaque structure that represents a memory descriptor list (MDL).

## Syntax
```
typedef struct _MDL {
  _MDL      *Next;
  struct    _MDL;
  CSHORT    Size;
  CSHORT    MdlFlags;
  _EPROCESS *Process;
  struct    _EPROCESS;
  PVOID     MappedSystemVa;
  PVOID     StartVa;
  ULONG     ByteCount;
  ULONG     ByteOffset;
} PMDL, MDL;
```

## Members


`Next`

Pointer to the next MDL in an MDL chain. For more information about MDL chains, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff565421">Using MDLs</a>.

`Size`



`MdlFlags`



`Process`



`MappedSystemVa`



`StartVa`



`ByteCount`



`ByteOffset`



## Remarks
An MDL describes the layout of a virtual memory buffer in physical memory. For more information, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff565421">Using MDLs</a>.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | wdm.h (include Wdm.h, Ntddk.h, Ntifs.h) |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff548263">IoAllocateMdl</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff554530">MmGetMdlByteCount</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff554533">MmGetMdlByteOffset</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff554537">MmGetMdlPfnArray</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff554539">MmGetMdlVirtualAddress</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff554568">MmInitializeMdl</a>