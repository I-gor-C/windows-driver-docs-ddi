---
UID : NE:d3dkmdt._D3DKMDT_VIDPN_SOURCE_MODE_TYPE
title : _D3DKMDT_VIDPN_SOURCE_MODE_TYPE
author : windows-driver-content
description : The D3DKMDT_VIDPN_SOURCE_MODE_TYPE enumeration is used to indicate whether a video present network (VidPN) source mode is a graphics mode, a text mode, or a stereo mode.
old-location : display\d3dkmdt_vidpn_source_mode_type.htm
old-project : display
ms.assetid : c2a48cf2-f595-4f78-b779-416d324e90d7
ms.author : windowsdriverdev
ms.date : 12/29/2017
ms.keywords : _D3DKMDT_VIDPN_SOURCE_MODE_TYPE, D3DKMDT_VIDPN_SOURCE_MODE_TYPE
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : enum
req.header : d3dkmdt.h
req.include-header : D3dkmdt.h
req.target-type : Windows
req.target-min-winverclnt : Available in Windows Vista and later versions of the Windows operating systems.
req.target-min-winversvr : 
req.kmdf-ver : 
req.umdf-ver : 
req.alt-api : D3DKMDT_VIDPN_SOURCE_MODE_TYPE
req.alt-loc : d3dkmdt.h
req.ddi-compliance : 
req.unicode-ansi : 
req.idl : 
req.max-support : 
req.namespace : 
req.assembly : 
req.type-library : 
req.lib : 
req.dll : 
req.irql : PASSIVE_LEVEL
req.typenames : D3DKMDT_VIDPN_SOURCE_MODE_TYPE
---

# _D3DKMDT_VIDPN_SOURCE_MODE_TYPE Enumeration
The D3DKMDT_VIDPN_SOURCE_MODE_TYPE enumeration is used to indicate whether a video present network (VidPN) source mode is a graphics mode, a text mode, or a stereo mode.

## Syntax
````
typedef enum _D3DKMDT_VIDPN_SOURCE_MODE_TYPE { 
  D3DKMDT_RMT_UNINITIALIZED                  = 0,
  D3DKMDT_RMT_GRAPHICS                       = 1,
  D3DKMDT_RMT_TEXT                           = 2,
  D3DKMDT_RMT_GRAPHICS_STEREO                = 3,
  D3DKMDT_RMT_GRAPHICS_STEREO_ADVANCED_SCAN  = 4
} D3DKMDT_VIDPN_SOURCE_MODE_TYPE;
````

## Constants

<table>

<tr>
<td>D3DKMDT_RMT_GRAPHICS</td>
<td>Indicates that the VidPN source mode is a graphics mode.</td>
</tr>

<tr>
<td>D3DKMDT_RMT_GRAPHICS_STEREO</td>
<td>Available beginning with Windows 8.

Indicates that the VidPN source mode is stereo, and the allocation can only be scanned by the display miniport driver as both left and right channels.</td>
</tr>

<tr>
<td>D3DKMDT_RMT_GRAPHICS_STEREO_ADVANCED_SCAN</td>
<td>Available beginning with Windows 8.

Indicates that the VidPN source mode is stereo, and the allocation can only be scanned by the display miniport driver as both left and right channels, or as only the left channel, or as only  the right channel.

If mono content needs to be displayed in a stereo mode, the operating system can better manage resources if <b>D3DKMDT_RMT_GRAPHICS_STEREO_ADVANCED_SCAN</b> is set instead of <b>D3DKMDT_RMT_GRAPHICS_STEREO</b>.</td>
</tr>

<tr>
<td>D3DKMDT_RMT_TEXT</td>
<td>Indicates that the VidPN source mode is a text mode.</td>
</tr>

<tr>
<td>D3DKMDT_RMT_UNINITIALIZED</td>
<td>Indicates that a variable of type D3DKMDT_VIDPN_SOURCE_MODE_TYPE has not yet been assigned a meaningful value.</td>
</tr>
</table>

## Remarks

The <b>Type</b> member of the <a href="..\d3dkmdt\ns-d3dkmdt-_d3dkmdt_vidpn_source_mode.md">D3DKMDT_VIDPN_SOURCE_MODE</a> structure is a D3DKMDT_VIDPN_SOURCE_MODE_TYPE value.</p>

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | d3dkmdt.h (include D3dkmdt.h) |