---
UID: NS:d3dukmdt.D3DDDI_UPDATEALLOCPROPERTY
title: D3DDDI_UPDATEALLOCPROPERTY
author: windows-driver-content
description: D3DDDI_UPDATEALLOCPROPERTY describes the parameters needed to update an allocation.
old-location: display\d3dddi_updateallocproperty.htm
old-project: display
ms.assetid: 4A8EBF10-23A3-4D91-BCF7-8FD4D0708949
ms.author: windowsdriverdev
ms.date: 2/24/2018
ms.keywords: D3DDDI_UPDATEALLOCPROPERTY, D3DDDI_UPDATEALLOCPROPERTY structure [Display Devices], d3dukmdt/D3DDDI_UPDATEALLOCPROPERTY, display.d3dddi_updateallocproperty
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: d3dukmdt.h
req.include-header: D3dumddi.h
req.target-type: Windows
req.target-min-winverclnt: Available in Windows 10 and later versions of the Windows operating systems.
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
-	d3dukmdt.h
api_name:
-	D3DDDI_UPDATEALLOCPROPERTY
product: Windows
targetos: Windows
req.typenames: D3DDDI_UPDATEALLOCPROPERTY
---

# D3DDDI_UPDATEALLOCPROPERTY structure
D3DDDI_UPDATEALLOCPROPERTY describes the parameters needed to update an allocation.

## Syntax
````
typedef struct D3DDDI_UPDATEALLOCPROPERTY {
  D3DKMT_HANDLE                        hPagingQueue;
  D3DKMT_HANDLE                        hAllocation;
  UINT                                 SupportedSegmentSet;
  DXGK_SEGMENTPREFERENCE               PreferredSegment;
  D3DDDI_UPDATEALLOCPROPERTY_FLAGS     Flags;
  UINT64                               PagingFenceValue;
  union {
    struct {
      UINT SetAccessedPhysically   :1;
      UINT SetSupportedSegmentSet   :1;
      UINT SetPreferredSegment   :1;
      UINT Reserved  :29;
    };
    UINT   PropertyMaskValue;
  };
} D3DDDI_UPDATEALLOCPROPERTY;
````

## Members


`Flags`

[in] The flags that will be used to update the allocation.

`hAllocation`

[in] A handle to the allocation that will be updated.

`hPagingQueue`

[in] A Handle to the paging queue used to synchronize paging operations for this call.

`PagingFenceValue`

[out] The paging fence value that will be synchronized with before using the new allocation. Applies to the monitored fence synchronization object associated with hPagingQueue.

`PreferredSegment`

[in] An index for the new preferred segment set. If the current preferred segment set is the same, then this will be ignored.

`SupportedSegmentSet`

[in] An index for the new supported segment set. If the current supported segment set is the same, then this will be ignored.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Available in Windows 10 and later versions of the Windows operating systems. Available in Windows 10 and later versions of the Windows operating systems. |
| **Header** | d3dukmdt.h (include D3dumddi.h) |