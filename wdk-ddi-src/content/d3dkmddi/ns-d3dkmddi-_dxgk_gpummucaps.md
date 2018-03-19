---
UID: NS:d3dkmddi._DXGK_GPUMMUCAPS
title: "_DXGK_GPUMMUCAPS"
author: windows-driver-content
description: The DXGK_GPUMMUCAPS structure is used by the kernel mode driver to express virtual memory addressing capabilities.
old-location: display\dxgk_gpummucaps.htm
old-project: display
ms.assetid: 999820D0-FDEB-49FD-920A-75FD9886492A
ms.author: windowsdriverdev
ms.date: 2/26/2018
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
````
typedef struct _DXGK_GPUMMUCAPS {
  union {
    struct {
      UINT ReadOnlyMemorySupported  :1;
      UINT NoExecuteMemorySupported  :1;
      UINT ZeroInPteSupported  :1;
      UINT ExplicitPageTableInvalidation  :1;
      UINT CacheCoherentMemorySupported  :1;
      UINT PageTableUpdateRequireAddressSpaceIdle  :1;
      UINT LargePageSupported  :1;
      UINT DualPteSupported  :1;
#if (DXGKDDI_INTERFACE_VERSION >= DXGKDDI_INTERFACE_VERSION_WDDM2_1)
      UINT AllowNonAlignedLargePageAddress  :1;
      UINT Reserved  :23;
    };
    UINT   Value;
  };
  DXGK_PAGETABLEUPDATEMODE PageTableUpdateMode;
  UINT                     VirtualAddressBitCount;
  UINT                     LeafPageTableSizeFor64KPagesInBytes;
  UINT                     PageTableLevelCount;
  struct {
    UINT SourcePageTableVaInTransfer  :1;
    UINT Reserved  :31;
  } LegacyBehaviors;
} DXGK_GPUMMUCAPS;
````

## Members


`PageTableUpdateMode`

Defines the type of addresses which are used in <a href="https://msdn.microsoft.com/08328e82-d1cc-4c50-bc96-7382232676ab">DxgkDdiUpdatePageTable</a> operations. When <b>DXGK_PAGETABLEUPDATE_GPU_VIRTUAL</b> is set, all paging operation will occur in the virtual address space of the system context. When page directories are located in a local GPU memory segment, the update mode cannot be set to <b>DXGK_PAGETABLEUPDATE_CPU_VIRTUAL</b>.

`VirtualAddressBitCount`

The number of bits in the GPU virtual address.

`LeafPageTableSizeFor64KPagesInBytes`

The size of a leaf page table when 64KB pages are used. The size must be a multiple of CPU page size (4096).

`PageTableLevelCount`

The number of page table levels supported. The minimum value is 2 (defined as <b>DXGK_MIN_PAGE_TABLE_LEVEL_COUNT</b>). The maximum value is <b>DXGK_MAX_PAGE_TABLE_LEVEL_COUNT</b>. 

When <b>PageTableLevelCount</b> is 2, the root page table is dynamically resizable and the size of the page table is determined through <a href="..\d3dkmddi\nc-d3dkmddi-dxgkddi_getrootpagetablesize.md">DxgkDdiGetRootPageTableSize</a>. When <b>PageTableLevelCount</b> is greater than 2, all page table levels have a fixed size, which is described through <a href="..\d3dkmddi\ns-d3dkmddi-_dxgk_page_table_level_desc.md">DXGK_PAGE_TABLE_LEVEL_DESC</a><b>::PageTableSizeInBytes</b>.

`LegacyBehaviors`

#### SourcePageTableVaInTransfer

When set to 1, video memory manager sets <b>SourcePageTable</b> address in <b>TransferVirtual</b> during allocation eviction.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Windows 10 Windows 10 |
| **Header** | d3dkmddi.h (include D3dkmddi.h) |