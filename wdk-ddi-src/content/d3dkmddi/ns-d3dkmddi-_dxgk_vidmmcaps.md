---
UID: NS:d3dkmddi._DXGK_VIDMMCAPS
title: "_DXGK_VIDMMCAPS"
author: windows-driver-content
description: The DXGK_VIDMMCAPS structure identifies the video memory management capabilities that a display miniport driver can support.
old-location: display\dxgk_vidmmcaps.htm
old-project: display
ms.assetid: c3df50a0-2388-4760-b6e2-ef6af650d0e2
ms.author: windowsdriverdev
ms.date: 2/26/2018
ms.keywords: DXGK_VIDMMCAPS, DXGK_VIDMMCAPS structure [Display Devices], DmStructs_0ec3e7bb-c14e-41b8-a148-7f77153972e8.xml, _DXGK_VIDMMCAPS, d3dkmddi/DXGK_VIDMMCAPS, display.dxgk_vidmmcaps
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
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	HeaderDef
api_location:
-	d3dkmddi.h
api_name:
-	DXGK_VIDMMCAPS
product: Windows
targetos: Windows
req.typenames: DXGK_VIDMMCAPS
---

# _DXGK_VIDMMCAPS structure
The <b>DXGK_VIDMMCAPS</b> structure identifies the video memory management capabilities that a display miniport driver can support.

## Syntax
````
typedef struct _DXGK_VIDMMCAPS {
  union {
    struct {
      UINT OutOfOrderLock  :1;
#if (DXGKDDI_INTERFACE_VERSION >= DXGKDDI_INTERFACE_VERSION_WIN7)
      UINT DedicatedPagingEngine  :1;
      UINT PagingEngineCanSwizzle  :1;
      UINT SectionBackedPrimary  :1;
#if (DXGKDDI_INTERFACE_VERSION >= DXGKDDI_INTERFACE_VERSION_WDDM1_3)
      UINT CrossAdapterResource  :1;
#if (DXGKDDI_INTERFACE_VERSION >= DXGKDDI_INTERFACE_VERSION_WDDM2_0)
      UINT VirtualAddressingSupported  :1;
      UINT GpuMmuSupported  :1;
      UINT IoMmuSupported  :1;
      UINT ReplicateGdiContent  :1;
      UINT Reserved  :23;
#else 
      UINT Reserved  :27;
#endif 
#else 
      UINT Reserved  :28;
#endif 
#else 
      UINT Reserved  :31;
#endif 
    };
    UINT Value;
  };
  UINT PagingNode;
} DXGK_VIDMMCAPS;
````

## Members


`PagingNode`

The zero-based index of the node to use for paging operations. If the driver does not set the <b>MultiEngineAware</b> bit-field member of the <b>SchedulingCaps</b> member of the <a href="..\d3dkmddi\ns-d3dkmddi-_dxgk_drivercaps.md">DXGK_DRIVERCAPS</a> structure, the DirectX graphics kernel subsystem ignores the setting of <b>PagingNode</b>.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Available in Windows Vista and later versions of the Windows operating systems. Available in Windows Vista and later versions of the Windows operating systems. |
| **Header** | d3dkmddi.h (include D3dkmddi.h) |

## See Also

<a href="..\d3dkmddi\ns-d3dkmddi-_dxgk_drivercaps.md">DXGK_DRIVERCAPS</a>



 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20DXGK_VIDMMCAPS structure%20 RELEASE:%20(2/26/2018)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>