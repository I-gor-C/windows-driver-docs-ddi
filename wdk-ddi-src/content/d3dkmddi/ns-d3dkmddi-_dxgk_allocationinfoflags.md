---
UID: NS:d3dkmddi._DXGK_ALLOCATIONINFOFLAGS
title: "_DXGK_ALLOCATIONINFOFLAGS"
author: windows-driver-content
description: The DXGK_ALLOCATIONINFOFLAGS structure identifies properties for an allocation. The display miniport driver specifies these flags for the video memory manager.
old-location: display\dxgk_allocationinfoflags.htm
old-project: display
ms.assetid: 04bd00c3-83a8-44bb-9493-cf7f43f10602
ms.author: windowsdriverdev
ms.date: 12/29/2017
ms.keywords: DXGK_ALLOCATIONINFOFLAGS structure [Display Devices], DXGK_ALLOCATIONINFOFLAGS, d3dkmddi/DXGK_ALLOCATIONINFOFLAGS, _DXGK_ALLOCATIONINFOFLAGS, display.dxgk_allocationinfoflags, DmStructs_4e6e499c-8427-4c0f-977d-92f648ab027e.xml
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: d3dkmddi.h
req.include-header: D3dkmddi.h
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
req.irql: PASSIVE_LEVEL
topictype:
-	APIRef
-	kbSyntax
apitype:
-	HeaderDef
apilocation:
-	d3dkmddi.h
apiname:
-	DXGK_ALLOCATIONINFOFLAGS
product: Windows
targetos: Windows
req.typenames: DXGK_ALLOCATIONINFOFLAGS
---

# _DXGK_ALLOCATIONINFOFLAGS structure
The DXGK_ALLOCATIONINFOFLAGS structure identifies properties for an allocation. The display miniport driver specifies these flags for the video memory manager.

## Syntax
````
typedef struct _DXGK_ALLOCATIONINFOFLAGS {
  union {
    struct {
      UINT CpuVisible  :1;
      UINT PermanentSysMem  :1;
      UINT Cached  :1;
      UINT Protected  :1;
      UINT ExistingSysMem  :1;
      UINT ExistingKernelSysMem  :1;
      UINT FromEndOfSegment  :1;
      UINT Swizzled  :1;
      UINT Overlay  :1;
      UINT Capture  :1;
      UINT UseAlternateVA  :1;
      UINT SynchronousPaging  :1;
      UINT LinkMirrored  :1;
      UINT LinkInstanced  :1;
      UINT HistoryBuffer  :1;
#if (DXGKDDI_INTERFACE_VERSION >= DXGKDDI_INTERFACE_VERSION_WDDM2_0)
      UINT AccessedPhysically  :1;
      UINT ExplicitResidencyNotification  :1;
      UINT Reserved  :2;
#else 
      UINT Reserved  :4;
#endif 
      UINT DXGK_ALLOC_RESERVED16  :1;
      UINT DXGK_ALLOC_RESERVED15  :1;
      UINT DXGK_ALLOC_RESERVED14  :1;
      UINT DXGK_ALLOC_RESERVED13  :1;
      UINT DXGK_ALLOC_RESERVED12  :1;
      UINT DXGK_ALLOC_RESERVED11  :1;
      UINT DXGK_ALLOC_RESERVED10  :1;
      UINT DXGK_ALLOC_RESERVED9  :1;
      UINT DXGK_ALLOC_RESERVED4  :1;
      UINT DXGK_ALLOC_RESERVED3  :1;
      UINT DXGK_ALLOC_RESERVED2  :1;
      UINT DXGK_ALLOC_RESERVED1  :1;
      UINT DXGK_ALLOC_RESERVED0  :1;
    };
    UINT Value;
  };
} DXGK_ALLOCATIONINFOFLAGS;
````

## Members


## Remarks
You can specify properties of an allocation by setting bits in the 32-bit <b>Value</b> member or by setting individual members of the structure in the union that the <b>DXGK_ALLOCATIONINFOFLAGS</b> structure contains.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Available in Windows Vista and later versions of the Windows operating systems. Available in Windows Vista and later versions of the Windows operating systems. |
| **Header** | d3dkmddi.h (include D3dkmddi.h) |

## See Also

<a href="..\d3dkmddi\nc-d3dkmddi-dxgkddi_buildpagingbuffer.md">DxgkDdiBuildPagingBuffer</a>



<a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi_unlockcb.md">pfnUnlockCb</a>



<a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi_lockcb.md">pfnLockCb</a>



<a href="..\d3dkmddi\ns-d3dkmddi-_dxgk_allocationinfo.md">DXGK_ALLOCATIONINFO</a>



 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20DXGK_ALLOCATIONINFOFLAGS structure%20 RELEASE:%20(12/29/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>