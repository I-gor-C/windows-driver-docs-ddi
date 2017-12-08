---
UID: NS.DISPMPRT.PDXGK_BRIGHTNESS_INTERFACE
title: PDXGK_BRIGHTNESS_INTERFACE
author: windows-driver-content
description: The DXGK_BRIGHTNESS_INTERFACE structure contains pointers to functions in the Panel Brightness Control Interface, which is implemented by the display miniport driver.
old-location: display\dxgk_brightness_interface.htm
old-project: display
ms.assetid: 8fa7908c-7ed4-4f85-846c-71fc5c7dc035
ms.author: windowsdriverdev
ms.date: 12/6/2017
ms.keywords: PDXGK_BRIGHTNESS_INTERFACE, DXGK_BRIGHTNESS_INTERFACE, *PDXGK_BRIGHTNESS_INTERFACE
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
req.alt-api: DXGK_BRIGHTNESS_INTERFACE
req.alt-loc: dispmprt.h
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
---

# PDXGK_BRIGHTNESS_INTERFACE structure



## -description
The <b>DXGK_BRIGHTNESS_INTERFACE</b> structure contains pointers to functions in the Panel Brightness Control Interface, which is implemented by the display miniport driver.


## -syntax

````
typedef struct {
  USHORT                       Size;
  USHORT                       Version;
  PVOID                        Context;
  PINTERFACE_REFERENCE         InterfaceReference;
  PINTERFACE_DEREFERENCE       InterfaceDereference;
  DXGK_BRIGHTNESS_GET_POSSIBLE GetPossibleBrightness;
  DXGK_BRIGHTNESS_SET          SetBrightness;
  DXGK_BRIGHTNESS_GET          GetBrightness;
} DXGK_BRIGHTNESS_INTERFACE, *PDXGK_BRIGHTNESS_INTERFACE;
````


## -struct-fields

### -field Size

The size, in bytes, of this structure.

### -field Version

The version number of the brightness interface. Version number constants are defined in Dispmprt.h (for example, <b>DXGK_BRIGHTNESS_INTERFACE_VERSION_1</b>).

### -field Context

A pointer to a private context block.

### -field InterfaceReference

A pointer to an interface reference function that is implemented by the display miniport driver.

### -field InterfaceDereference

A pointer to an interface dereference function that is implemented by the display miniport driver.

### -field GetPossibleBrightness

A pointer to the display miniport driver's <a href="..\dispmprt\nc-dispmprt-dxgk_brightness_get_possible.md">DxgkDdiGetPossibleBrightness</a> function.

### -field SetBrightness

A pointer to the display miniport driver's <a href="..\dispmprt\nc-dispmprt-dxgk_brightness_set.md">DxgkDdiSetBrightness</a> function.

### -field GetBrightness

A pointer to the display miniport driver's <a href="..\dispmprt\nc-dispmprt-dxgk_brightness_get.md">DxgkDdiGetBrightness</a> function.

## -remarks
A kernel-mode component that must use the brightness interface initiates a call to the display miniport driver's <a href="display.dxgkddiqueryinterface">DxgkDdiQueryInterface</a> function to retrieve the interface and passes GUID_DEVINTERFACE_BRIGHTNESS in the <b>InterfaceType</b> member of the <a href="display.query_interface">QUERY_INTERFACE</a> structure that the <i>QueryInterface</i> parameter points to.

## -requirements
<table>
<tr>
<th width="30%">
Version
</th>
<td width="70%">
Available in Windows Vista and later versions of the Windows operating systems.
</td>
</tr>
<tr>
<th width="30%">
Header
</th>
<td width="70%">
<dl>
<dt>Dispmprt.h (include Dispmprt.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="display.dxgk_brightness_interface_2">DXGK_BRIGHTNESS_INTERFACE_2</a>
</dt>
<dt>
<a href="..\dispmprt\nc-dispmprt-dxgk_brightness_get.md">DxgkDdiGetBrightness</a>
</dt>
<dt>
<a href="..\dispmprt\nc-dispmprt-dxgk_brightness_get_possible.md">DxgkDdiGetPossibleBrightness</a>
</dt>
<dt>
<a href="display.dxgkddiqueryinterface">DxgkDdiQueryInterface</a>
</dt>
<dt>
<a href="..\dispmprt\nc-dispmprt-dxgk_brightness_set.md">DxgkDdiSetBrightness</a>
</dt>
<dt>
<a href="display.query_interface">QUERY_INTERFACE</a>
</dt>
</dl>
 
 
<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20DXGK_BRIGHTNESS_INTERFACE structure%20 RELEASE:%20(12/6/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>
