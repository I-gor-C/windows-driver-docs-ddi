---
UID: NS:dispmprt.DXGK_BRIGHTNESS_INTERFACE
title: DXGK_BRIGHTNESS_INTERFACE
author: windows-driver-content
description: The DXGK_BRIGHTNESS_INTERFACE structure contains pointers to functions in the Panel Brightness Control Interface, which is implemented by the display miniport driver.
old-location: display\dxgk_brightness_interface.htm
old-project: display
ms.assetid: 8fa7908c-7ed4-4f85-846c-71fc5c7dc035
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: "*PDXGK_BRIGHTNESS_INTERFACE, DXGK_BRIGHTNESS_INTERFACE, DXGK_BRIGHTNESS_INTERFACE structure [Display Devices], DmStructs_f750f3c3-0754-49b9-8ad5-cd93f84697c4.xml, PDXGK_BRIGHTNESS_INTERFACE, PDXGK_BRIGHTNESS_INTERFACE structure pointer [Display Devices], display.dxgk_brightness_interface, dispmprt/DXGK_BRIGHTNESS_INTERFACE, dispmprt/PDXGK_BRIGHTNESS_INTERFACE"
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: dispmprt.h
req.include-header: Dispmprt.h
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
-	dispmprt.h
api_name:
-	DXGK_BRIGHTNESS_INTERFACE
product: Windows
targetos: Windows
req.typenames: DXGK_BRIGHTNESS_INTERFACE, *PDXGK_BRIGHTNESS_INTERFACE
---

# DXGK_BRIGHTNESS_INTERFACE structure
The <b>DXGK_BRIGHTNESS_INTERFACE</b> structure contains pointers to functions in the Panel Brightness Control Interface, which is implemented by the display miniport driver.

## Syntax
```
typedef struct DXGK_BRIGHTNESS_INTERFACE {
  IN USHORT                        Size;
  IN USHORT                        Version;
  OUT PVOID                        Context;
  OUT PINTERFACE_REFERENCE         InterfaceReference;
  OUT PINTERFACE_DEREFERENCE       InterfaceDereference;
  OUT DXGK_BRIGHTNESS_GET_POSSIBLE GetPossibleBrightness;
  OUT DXGK_BRIGHTNESS_SET          SetBrightness;
  OUT DXGK_BRIGHTNESS_GET          GetBrightness;
} *PDXGK_BRIGHTNESS_INTERFACE, DXGK_BRIGHTNESS_INTERFACE;
```

## Members


`Size`

The size, in bytes, of this structure.

`Version`

The version number of the brightness interface. Version number constants are defined in Dispmprt.h (for example, <b>DXGK_BRIGHTNESS_INTERFACE_VERSION_1</b>).

`Context`

A pointer to a private context block.

`InterfaceReference`

A pointer to an interface reference function that is implemented by the display miniport driver.

`InterfaceDereference`

A pointer to an interface dereference function that is implemented by the display miniport driver.

`GetPossibleBrightness`

A pointer to the display miniport driver's <a href="https://msdn.microsoft.com/aed565f5-a9c1-4130-a192-68bb699b4bd1">DxgkDdiGetPossibleBrightness</a> function.

`SetBrightness`

A pointer to the display miniport driver's <a href="https://msdn.microsoft.com/83609679-20df-463d-ac3a-bb8a87897608">DxgkDdiSetBrightness</a> function.

`GetBrightness`

A pointer to the display miniport driver's <a href="https://msdn.microsoft.com/e226cd36-45af-4d80-9aba-8919b267483b">DxgkDdiGetBrightness</a> function.

## Remarks
A kernel-mode component that must use the brightness interface initiates a call to the display miniport driver's <a href="https://msdn.microsoft.com/d8255f36-be3a-4b19-ac8d-8748ac9b6a24">DxgkDdiQueryInterface</a> function to retrieve the interface and passes GUID_DEVINTERFACE_BRIGHTNESS in the <b>InterfaceType</b> member of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff569225">QUERY_INTERFACE</a> structure that the <i>QueryInterface</i> parameter points to.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Available in Windows Vista and later versions of the Windows operating systems. Available in Windows Vista and later versions of the Windows operating systems. |
| **Header** | dispmprt.h (include Dispmprt.h) |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/jj128360">DXGK_BRIGHTNESS_INTERFACE_2</a>



<a href="https://msdn.microsoft.com/e226cd36-45af-4d80-9aba-8919b267483b">DxgkDdiGetBrightness</a>



<a href="https://msdn.microsoft.com/aed565f5-a9c1-4130-a192-68bb699b4bd1">DxgkDdiGetPossibleBrightness</a>



<a href="https://msdn.microsoft.com/d8255f36-be3a-4b19-ac8d-8748ac9b6a24">DxgkDdiQueryInterface</a>



<a href="https://msdn.microsoft.com/83609679-20df-463d-ac3a-bb8a87897608">DxgkDdiSetBrightness</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff569225">QUERY_INTERFACE</a>