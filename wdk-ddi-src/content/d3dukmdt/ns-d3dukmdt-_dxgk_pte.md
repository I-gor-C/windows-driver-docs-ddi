---
UID : NS:d3dukmdt._DXGK_PTE
title : "_DXGK_PTE"
author : windows-driver-content
description : A page table entry (PTE) provides a physical address of a page and other attributes. The exact format of PTE depends on hardware implementation.
old-location : display\dxgk_pte.htm
old-project : display
ms.assetid : 2d5c1f3e-69a6-4f7f-9c99-bbaf94e6401b
ms.author : windowsdriverdev
ms.date : 12/29/2017
ms.keywords : DmStructs_701e980c-29dc-46d2-8f03-ce8485a4cc70.xml, DXGK_PTE structure [Display Devices], d3dukmdt/DXGK_PTE, _DXGK_PTE, display.dxgk_pte, DXGK_PTE
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : struct
req.header : d3dukmdt.h
req.include-header : D3dkmddi.h
req.target-type : Windows
req.target-min-winverclnt : Available in Windows 7 and later versions of the Windows operating systems.
req.target-min-winversvr : 
req.kmdf-ver : 
req.umdf-ver : 
req.ddi-compliance : 
req.unicode-ansi : 
req.idl : 
req.max-support : 
req.namespace : 
req.assembly : 
req.type-library : 
req.lib : 
req.dll : 
req.irql : 
topictype : 
apitype : 
apilocation : 
apiname : 
product : Windows
targetos : Windows
req.typenames : DXGK_PTE
---

# _DXGK_PTE structure
A page table entry (PTE) provides a physical address of a page and other attributes. The exact format of PTE depends on hardware implementation.

## Syntax
````
typedef struct _DXGK_PTE {
  union {
    struct {
      ULONGLONG Valid  :1;
      ULONGLONG Zero  :1;
      ULONGLONG CacheCoherent  :1;
      ULONGLONG ReadOnly  :1;
      ULONGLONG NoExecute  :1;
      ULONGLONG Segment  :5;
      ULONGLONG LargePage  :1;
      ULONGLONG PhysicalAdapterIndex  :6;
      ULONGLONG PageTablePageSize  :2;
      ULONGLONG Reserved  :45;
    };
    ULONGLONG Flags;
  };
  union {
    ULONGLONG PageAddress;
    ULONGLONG PageTableAddress;
  };
} DXGK_PTE;
````

## Members



## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Available in Windows 7 and later versions of the Windows operating systems. Available in Windows 7 and later versions of the Windows operating systems. |
| **Header** | d3dukmdt.h (include D3dkmddi.h) |