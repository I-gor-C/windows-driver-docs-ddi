---
UID: NS:d3dkmddi._DXGK_GPUMMUCAPS
title: "_DXGK_GPUMMUCAPS"
author: windows-driver-content
description: The DXGK_GPUMMUCAPS structure is used by the kernel mode driver to express virtual memory addressing capabilities.
old-location: display\dxgk_gpummucaps.htm
old-project: display
ms.assetid: 999820D0-FDEB-49FD-920A-75FD9886492A
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: DXGK_GPUMMUCAPS, DXGK_GPUMMUCAPS structure [Display Devices], _DXGK_GPUMMUCAPS, d3dkmddi/DXGK_GPUMMUCAPS, display.dxgk_gpummucaps
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: d3dkmddi.h
req.include-header: D3dkmddi.h
req.target-type: Windows
req.target-min-winverclnt: Windows 10
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
req.irql: PASSIVE_LEVEL
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	HeaderDef
api_location:
-	d3dkmddi.h
api_name:
-	DXGK_GPUMMUCAPS
product: Windows
targetos: Windows
req.typenames: DXGK_GPUMMUCAPS
---

# _DXGK_GPUMMUCAPS structure
The <b>DXGK_GPUMMUCAPS</b> structure is used by the kernel mode driver to express virtual memory addressing capabilities.

## Syntax
```
typedef struct _DXGK_GPUMMUCAPS {
  union {
    struct {
      UINT  : 1  ReadOnlyMemorySupported;
      UINT  : 1  NoExecuteMemorySupported;
      UINT  : 1  ZeroInPteSupported;
      UINT  : 1  ExplicitPageTableInvalidation;
      UINT  : 1  CacheCoherentMemorySupported;
      UINT  : 1  PageTableUpdateRequireAddressSpaceIdle;
      UINT  : 1  LargePageSupported;
      UINT  : 1  DualPteSupported;
      UINT  : 1  AllowNonAlignedLargePageAddress;
      UINT  : 1  SysMem64KBPageSupported;
      UINT  : 22 Reserved;
      UINT  : 24 Reserved;
    };
    UINT Value;
  };
  DXGK_PAGETABLEUPDATEMODE PageTableUpdateMode;
  UINT                     VirtualAddressBitCount;
  UINT                     LeafPageTableSizeFor64KPagesInBytes;
  UINT                     PageTableLevelCount;
  struct {
    UINT  : 31 Reserved;
    UINT  : 1  SourcePageTableVaInTransfer;
  } LegacyBehaviors;
} DXGK_GPUMMUCAPS;
```

## Members


`PageTableUpdateMode`

Defines the type of addresses which are used in <a href="https://msdn.microsoft.com/08328e82-d1cc-4c50-bc96-7382232676ab">DxgkDdiUpdatePageTable</a> operations. When <b>DXGK_PAGETABLEUPDATE_GPU_VIRTUAL</b> is set, all paging operation will occur in the virtual address space of the system context. When page directories are located in a local GPU memory segment, the update mode cannot be set to <b>DXGK_PAGETABLEUPDATE_CPU_VIRTUAL</b>.

`VirtualAddressBitCount`

The number of bits in the GPU virtual address.

`LeafPageTableSizeFor64KPagesInBytes`

The size of a leaf page table when 64KB pages are used. The size must be a multiple of CPU page size (4096).

`PageTableLevelCount`

The number of page table levels supported. The minimum value is 2 (defined as <b>DXGK_MIN_PAGE_TABLE_LEVEL_COUNT</b>). The maximum value is <b>DXGK_MAX_PAGE_TABLE_LEVEL_COUNT</b>. 

When <b>PageTableLevelCount</b> is 2, the root page table is dynamically resizable and the size of the page table is determined through <a href="https://msdn.microsoft.com/474F1772-0DF9-487B-AEB9-302392AE0B98">DxgkDdiGetRootPageTableSize</a>. When <b>PageTableLevelCount</b> is greater than 2, all page table levels have a fixed size, which is described through <a href="https://msdn.microsoft.com/library/windows/hardware/dn906832">DXGK_PAGE_TABLE_LEVEL_DESC</a><b>::PageTableSizeInBytes</b>.

`LegacyBehaviors`

#### SourcePageTableVaInTransfer

When set to 1, video memory manager sets <b>SourcePageTable</b> address in <b>TransferVirtual</b> during allocation eviction.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Windows 10 Windows 10 |
| **Header** | d3dkmddi.h (include D3dkmddi.h) |