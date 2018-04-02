---
UID: NS:dispmprt.DXGK_BRIGHTNESS_INTERFACE_2
title: DXGK_BRIGHTNESS_INTERFACE_2
author: windows-driver-content
description: Contains pointers to functions in the Panel Brightness Control Interface Version 2. Used by Windows Display Driver Model (WDDM) 1.2 and later display miniport drivers that support adaptive and smooth brightness control.
old-location: display\dxgk_brightness_interface_2.htm
old-project: display
ms.assetid: 0c0b877f-cef0-4e98-9f37-60f2d96b81bd
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: "*PDXGK_BRIGHTNESS_INTERFACE_2, DXGK_BRIGHTNESS_INTERFACE_2, DXGK_BRIGHTNESS_INTERFACE_2 structure [Display Devices], PDXGK_BRIGHTNESS_INTERFACE_2, PDXGK_BRIGHTNESS_INTERFACE_2 structure pointer [Display Devices], display.dxgk_brightness_interface_2, dispmprt/DXGK_BRIGHTNESS_INTERFACE_2, dispmprt/PDXGK_BRIGHTNESS_INTERFACE_2"
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: dispmprt.h
req.include-header: Dispmprt.h
req.target-type: Windows
req.target-min-winverclnt: Windows 8
req.target-min-winversvr: Windows Server 2012
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
-	Dispmprt.h
api_name:
-	DXGK_BRIGHTNESS_INTERFACE_2
product: Windows
targetos: Windows
req.typenames: DXGK_BRIGHTNESS_INTERFACE_2, *PDXGK_BRIGHTNESS_INTERFACE_2
---

# DXGK_BRIGHTNESS_INTERFACE_2 structure
Contains pointers to functions in the Panel Brightness Control Interface Version 2. Used by Windows Display Driver Model (WDDM) 1.2 and later display miniport drivers that support adaptive and smooth brightness control.

## Syntax
```
typedef struct DXGK_BRIGHTNESS_INTERFACE_2 {
  IN USHORT                                      Size;
  IN USHORT                                      Version;
  OUT PVOID                                      Context;
  OUT PINTERFACE_REFERENCE                       InterfaceReference;
  OUT PINTERFACE_DEREFERENCE                     InterfaceDereference;
  OUT DXGK_BRIGHTNESS_GET_POSSIBLE               GetPossibleBrightness;
  OUT DXGK_BRIGHTNESS_SET                        SetBrightness;
  OUT DXGK_BRIGHTNESS_GET                        GetBrightness;
  OUT DXGK_BRIGHTNESS_GET_CAPS                   GetBrightnessCaps;
  OUT DXGK_BRIGHTNESS_SET_STATE                  SetBrightnessState;
  OUT DXGK_BRIGHTNESS_SET_BACKLIGHT_OPTIMIZATION SetBacklightOptimization;
  OUT DXGK_BRIGHTNESS_GET_BACKLIGHT_REDUCTION    GetBacklightReduction;
} *PDXGK_BRIGHTNESS_INTERFACE_2, DXGK_BRIGHTNESS_INTERFACE_2;
```

## Members


`Size`

[in] The size, in bytes, of this structure.

`Version`

[in] The version number of the brightness interface. Version number constants are defined in Dispmprt.h (for example, <b>DXGK_BRIGHTNESS_INTERFACE_VERSION_2</b>).

`Context`

[in] A pointer to a private context block.

`InterfaceReference`

[out] A pointer to an interface reference function that is implemented by the display miniport driver.

`InterfaceDereference`

[out] A pointer to an interface dereference function that is implemented by the display miniport driver.

`GetPossibleBrightness`

[out] A pointer to the display miniport driver's <a href="https://msdn.microsoft.com/aed565f5-a9c1-4130-a192-68bb699b4bd1">DxgkDdiGetPossibleBrightness</a> function.

`SetBrightness`

[out] A pointer to the display miniport driver's <a href="https://msdn.microsoft.com/83609679-20df-463d-ac3a-bb8a87897608">DxgkDdiSetBrightness</a> function.

`GetBrightness`

[out] A pointer to the display miniport driver's <a href="https://msdn.microsoft.com/e226cd36-45af-4d80-9aba-8919b267483b">DxgkDdiGetBrightness</a> function.

`GetBrightnessCaps`

[out] A pointer to the display miniport driver's <a href="https://msdn.microsoft.com/3418dd2b-63cb-411f-9bae-390148885907">DxgkDdiGetBrightnessCaps</a> function. This function is available starting with Windows 8.

`SetBrightnessState`

[out] A pointer to the display miniport driver's  <a href="https://msdn.microsoft.com/804046ff-0cc7-4ff0-be07-b574cb40fd2b">DxgkDdiSetBrightnessState</a> function. This function is available starting with Windows 8.

`SetBacklightOptimization`

[out] A pointer to the display miniport driver's  <a href="https://msdn.microsoft.com/b8c37df8-ba86-4cfd-add0-49ba9c90f04a">DxgkDdiSetBacklightOptimization</a> function. This function is available starting with Windows 8.

`GetBacklightReduction`

[out] A pointer to the display miniport driver's  <a href="https://msdn.microsoft.com/018cb4a0-e71d-407e-8fe9-716312099b73">DxgkDdiGetBacklightReduction</a> function. This function is available starting with Windows 8.

## Remarks
This structure provides additional members, beyond those in the <a href="https://msdn.microsoft.com/library/windows/hardware/ff560989">DXGK_BRIGHTNESS_INTERFACE</a> interface, that point to driver-implemented functions that control, measure, and optimize display panel brightness and allow smooth brightness control.

For more information on this interface, see <a href="https://msdn.microsoft.com/library/windows/hardware/jj647485">Brightness Control Interface V. 2 (Adaptive and Smooth Brightness Control)</a>.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Windows 8 Windows 8 |
| **Header** | dispmprt.h (include Dispmprt.h) |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff560989">DXGK_BRIGHTNESS_INTERFACE</a>