---
UID: NS:d3dkmddi._DXGK_FLIPCAPS
title: "_DXGK_FLIPCAPS"
author: windows-driver-content
description: The DXGK_FLIPCAPS structure identifies flipping capabilities of the display miniport driver that the driver provides through a call to its DxgkDdiQueryAdapterInfo function.
old-location: display\dxgk_flipcaps.htm
old-project: display
ms.assetid: 33399b7c-ce67-4c49-be26-2b2d759ff5a0
ms.author: windowsdriverdev
ms.date: 12/29/2017
ms.keywords: DXGK_FLIPCAPS structure [Display Devices], DmStructs_11bba63e-8001-41d2-9c60-978024921994.xml, display.dxgk_flipcaps, d3dkmddi/DXGK_FLIPCAPS, _DXGK_FLIPCAPS, DXGK_FLIPCAPS
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
-	DXGK_FLIPCAPS
product: Windows
targetos: Windows
req.typenames: DXGK_FLIPCAPS
---

# _DXGK_FLIPCAPS structure
The <b>DXGK_FLIPCAPS</b> structure identifies flipping capabilities of the display miniport driver that the driver provides through a call to its <a href="..\d3dkmddi\nc-d3dkmddi-dxgkddi_queryadapterinfo.md">DxgkDdiQueryAdapterInfo</a> function.

## Syntax
````
typedef struct _DXGK_FLIPCAPS {
  union {
    struct {
      UINT FlipOnVSyncWithNoWait  :1;
      UINT FlipOnVSyncMmIo  :1;
      UINT FlipInterval  :1;
      UINT FlipImmediateMmIo  :1;
#if (DXGKDDI_INTERFACE_VERSION >= DXGKDDI_INTERFACE_VERSION_WDDM1_3)
      UINT FlipIndependent  :1;
      UINT Reserved  :27;
#endif 
      UINT Reserved  :28;
    };
    UINT Value;
  };
} DXGK_FLIPCAPS;
````

## Members



## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Available in Windows Vista and later versions of the Windows operating systems. Available in Windows Vista and later versions of the Windows operating systems. |
| **Header** | d3dkmddi.h (include D3dkmddi.h) |

## See Also

<a href="..\d3dkmddi\ns-d3dkmddi-_dxgkarg_queryadapterinfo.md">DXGKARG_QUERYADAPTERINFO</a>



<a href="..\d3dkmddi\ns-d3dkmddi-_dxgk_drivercaps.md">DXGK_DRIVERCAPS</a>



<a href="https://msdn.microsoft.com/488c929b-3816-457f-b5c2-c176b93d5546">DxgkDdiSetVidPnSourceAddress</a>



<a href="..\d3dkmddi\ns-d3dkmddi-_dxgkargcb_notify_interrupt_data.md">DXGKARGCB_NOTIFY_INTERRUPT_DATA</a>



<a href="..\d3dkmddi\nc-d3dkmddi-dxgkddi_queryadapterinfo.md">DxgkDdiQueryAdapterInfo</a>



<a href="..\d3dkmddi\nc-d3dkmddi-dxgkcb_notify_dpc.md">DxgkCbNotifyDpc</a>



<a href="..\d3dkmddi\nc-d3dkmddi-dxgkddi_present.md">DxgkDdiPresent</a>



<a href="..\d3dkmddi\ns-d3dkmddi-_dxgkarg_present.md">DXGKARG_PRESENT</a>



<a href="..\d3dkmddi\nc-d3dkmddi-dxgkcb_notify_interrupt.md">DxgkCbNotifyInterrupt</a>



<a href="..\d3dkmddi\ns-d3dkmddi-_dxgkarg_setvidpnsourceaddress.md">DXGKARG_SETVIDPNSOURCEADDRESS</a>



 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20DXGK_FLIPCAPS structure%20 RELEASE:%20(12/29/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>