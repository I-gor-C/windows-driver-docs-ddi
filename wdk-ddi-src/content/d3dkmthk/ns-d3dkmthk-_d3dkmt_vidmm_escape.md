---
UID: NS:d3dkmthk._D3DKMT_VIDMM_ESCAPE
title: "_D3DKMT_VIDMM_ESCAPE"
author: windows-driver-content
description: The D3DKMT_VIDMM_ESCAPE structure describes how to control the video memory manager (which is part of Dxgkrnl.sys) in a call to the D3DKMTEscape function.
old-location: display\d3dkmt_vidmm_escape.htm
old-project: display
ms.assetid: b9fb9960-9e6a-4c41-9c40-8ad307f83f0e
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: D3DKMT_VIDMM_ESCAPE, D3DKMT_VIDMM_ESCAPE structure [Display Devices], OpenGL_Structs_9a9c243b-b99e-43f2-a749-afbb839fb7c0.xml, _D3DKMT_VIDMM_ESCAPE, d3dkmthk/D3DKMT_VIDMM_ESCAPE, display.d3dkmt_vidmm_escape
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: d3dkmthk.h
req.include-header: D3dkmthk.h
req.target-type: Windows
req.target-min-winverclnt: Available in Windows Vista and later versions of the Windows operating systems.
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
-	d3dkmthk.h
api_name:
-	D3DKMT_VIDMM_ESCAPE
product: Windows
targetos: Windows
req.typenames: D3DKMT_VIDMM_ESCAPE
---

# _D3DKMT_VIDMM_ESCAPE structure
<b>Do not use the D3DKMT_VIDMM_ESCAPE structure; it is for testing purposes only.</b>

The D3DKMT_VIDMM_ESCAPE structure describes how to control the video memory manager (which is part of Dxgkrnl.sys) in a call to the <a href="https://msdn.microsoft.com/library/windows/hardware/ff546940">D3DKMTEscape</a> function.

## Syntax
```
typedef struct _D3DKMT_VIDMM_ESCAPE {
  D3DKMT_VIDMMESCAPETYPE Type;
  union {
    D3DKMT_EVICTION_CRITERIA EvictByCriteria;
    struct {
      union {
        struct {
          ULONG  : 1  ProbeAndLock;
          ULONG  : 1  SplitPoint;
          ULONG  : 1  NoDemotion;
          ULONG  : 1  SwizzlingAperture;
          ULONG  : 1  PagingPathLockSubRange;
          ULONG  : 1  PagingPathLockMinRange;
          ULONG  : 1  ComplexLock;
          ULONG  : 1  FailVARotation;
          ULONG  : 1  NoWriteCombined;
          ULONG  : 1  NoPrePatching;
          ULONG  : 1  AlwaysRepatch;
          ULONG  : 1  ExpectPreparationFailure;
          ULONG  : 1  FailUserModeVAMapping;
          ULONG  : 1  NeverDiscardOfferedAllocation;
          ULONG  : 1  AlwaysDiscardOfferedAllocation;
          ULONG  : 17 Reserved;
          ULONG  : 19 Reserved;
        };
        ULONG Value;
      };
    } SetFault;
    struct {
      D3DKMT_HANDLE ResourceHandle;
      D3DKMT_HANDLE AllocationHandle;
      HANDLE        hProcess;
    } Evict;
    struct {
      UINT64 NtHandle;
    } EvictByNtHandle;
    struct {
      union {
        D3DKMT_GET_GPUMMU_CAPS  GetGpuMmuCaps;
        struct {
          UINT NumVads;
        } GetNumVads;
        D3DKMT_GET_PTE          GetPte;
        D3DKMT_GET_SEGMENT_CAPS GetSegmentCaps;
        D3DKMT_VAD_DESC         GetVad;
        D3DKMT_VA_RANGE_DESC    GetVadRange;
      };
      D3DKMT_VAD_ESCAPE_COMMAND Command;
      NTSTATUS                  Status;
    } GetVads;
    struct {
      ULONGLONG LocalMemoryBudget;
      ULONGLONG SystemMemoryBudget;
    } SetBudget;
    struct {
      HANDLE hProcess;
      BOOL   bAllowWakeOnSubmission;
    } SuspendProcess;
    struct {
      HANDLE hProcess;
    } ResumeProcess;
    struct {
      UINT64 NumBytesToTrim;
    } GetBudget;
    struct {
      ULONG MinTrimInterval;
      ULONG MaxTrimInterval;
      ULONG IdleTrimInterval;
    } SetTrimIntervals;
    struct {
      BOOL bFlush;
    } Wake;
    struct {
      D3DKMT_DEFRAG_ESCAPE_OPERATION Operation;
      UINT                           SegmentId;
      ULONGLONG                      TotalCommitted;
      ULONGLONG                      TotalFree;
      ULONGLONG                      LargestGapBefore;
      ULONGLONG                      LargestGapAfter;
    } Defrag;
  };
} D3DKMT_VIDMM_ESCAPE;
```

## Members


`Type`




## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Available in Windows Vista and later versions of the Windows operating systems. Available in Windows Vista and later versions of the Windows operating systems. |
| **Header** | d3dkmthk.h (include D3dkmthk.h) |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff546940">D3DKMTEscape</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff547970">D3DKMT_ESCAPE</a>