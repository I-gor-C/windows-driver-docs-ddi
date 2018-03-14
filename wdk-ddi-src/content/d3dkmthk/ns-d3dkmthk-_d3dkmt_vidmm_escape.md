---
UID: NS:d3dkmthk._D3DKMT_VIDMM_ESCAPE
title: "_D3DKMT_VIDMM_ESCAPE"
author: windows-driver-content
description: The D3DKMT_VIDMM_ESCAPE structure describes how to control the video memory manager (which is part of Dxgkrnl.sys) in a call to the D3DKMTEscape function.
old-location: display\d3dkmt_vidmm_escape.htm
old-project: display
ms.assetid: b9fb9960-9e6a-4c41-9c40-8ad307f83f0e
ms.author: windowsdriverdev
ms.date: 2/26/2018
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

The D3DKMT_VIDMM_ESCAPE structure describes how to control the video memory manager (which is part of Dxgkrnl.sys) in a call to the <a href="..\d3dkmthk\nf-d3dkmthk-d3dkmtescape.md">D3DKMTEscape</a> function.

## Syntax
````
typedef struct _D3DKMT_VIDMM_ESCAPE {
  D3DKMT_VIDMMESCAPETYPE Type;
  union {
    struct {
      union {
        struct {
          ULONG ProbeAndLock  :1;
          ULONG SplitPoin  :1;
          ULONG HotAddMemory  :1;
          ULONG SwizzlingAperture  :1;
          ULONG PagingPathLockSubRange  :1;
          ULONG PagingPathLockMinRange  :1;
          ULONG ComplexLock  :1;
          ULONG FailVARotation  :1;
          ULONG NoWriteCombined  :1;
          ULONG NoPrePatching  :1;
          ULONG AlwaysRepatch  :1;
          ULONG ExpectPreparationFailure  :1;
          ULONG FailUserModeVAMapping  :1;
#if (DXGKDDI_INTERFACE_VERSION >= DXGKDDI_INTERFACE_VERSION_WIN8)
          ULONG NeverDiscardOfferedAllocation  :1;
          ULONG AlwaysDiscardOfferedAllocation  :1;
          ULONG Reserved  :17;
#else 
          ULONG Reserved  :19;
#endif 
        };
        ULONG Value;
      };
    } SetFault;
    struct {
      D3DKMT_HANDLE ResourceHandle;
      D3DKMT_HANDLE AllocationHandle;
    } Evict;
    struct {
      UINT64 NtHandle;
    } EvictByNtHandle;
  };
} D3DKMT_VIDMM_ESCAPE;
````

## Members


`Type`




## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Available in Windows Vista and later versions of the Windows operating systems. Available in Windows Vista and later versions of the Windows operating systems. |
| **Header** | d3dkmthk.h (include D3dkmthk.h) |

## See Also

<a href="..\d3dkmthk\ns-d3dkmthk-_d3dkmt_escape.md">D3DKMT_ESCAPE</a>



<a href="..\d3dkmthk\nf-d3dkmthk-d3dkmtescape.md">D3DKMTEscape</a>



 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20D3DKMT_VIDMM_ESCAPE structure%20 RELEASE:%20(2/26/2018)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>