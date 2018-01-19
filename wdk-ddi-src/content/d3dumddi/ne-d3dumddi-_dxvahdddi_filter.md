---
UID : NE:d3dumddi._DXVAHDDDI_FILTER
title : _DXVAHDDDI_FILTER
author : windows-driver-content
description : The DXVAHDDDI_FILTER enumeration contains values that identify the filter range, which the driver should retrieve when the driver's GetCaps function is called with the D3DDDICAPS_DXVAHD_GETVPFILTERRANGE value set.
old-location : display\dxvahdddi_filter.htm
old-project : display
ms.assetid : dbf65c28-b4f2-4930-8d01-050c45f87bb4
ms.author : windowsdriverdev
ms.date : 12/29/2017
ms.keywords : _DXVAHDDDI_FILTER, DXVAHDDDI_FILTER
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : enum
req.header : d3dumddi.h
req.include-header : D3dumddi.h
req.target-type : Windows
req.target-min-winverclnt : DXVAHDDDI_FILTER is supported beginning with the Windows 7 operating system.
req.target-min-winversvr : 
req.kmdf-ver : 
req.umdf-ver : 
req.alt-api : DXVAHDDDI_FILTER
req.alt-loc : d3dumddi.h
req.ddi-compliance : 
req.unicode-ansi : 
req.idl : 
req.max-support : 
req.namespace : 
req.assembly : 
req.type-library : 
req.lib : 
req.dll : 
req.irql : 
req.typenames : DXVAHDDDI_FILTER
---

# _DXVAHDDDI_FILTER Enumeration
The DXVAHDDDI_FILTER enumeration contains values that identify the filter range, which the driver should retrieve when the driver's <a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi_getcaps.md">GetCaps</a> function is called with the D3DDDICAPS_DXVAHD_GETVPFILTERRANGE value set.

## Syntax
````
typedef enum _DXVAHDDDI_FILTER { 
  DXVAHDDDI_FILTER_BRIGHTNESS          = 0,
  DXVAHDDDI_FILTER_CONTRAST            = 1,
  DXVAHDDDI_FILTER_HUE                 = 2,
  DXVAHDDDI_FILTER_SATURATION          = 3,
  DXVAHDDDI_FILTER_NOISE_REDUCTION     = 4,
  DXVAHDDDI_FILTER_EDGE_ENHANCEMENT    = 5,
  DXVAHDDDI_FILTER_ANAMORPHIC_SCALING  = 6
} DXVAHDDDI_FILTER;
````

## Constants

<table>

<tr>
<td>DXVAHDDDI_FILTER_ANAMORPHIC_SCALING</td>
<td>A value that specifies that the filter range of anamorphic scaling.</td>
</tr>

<tr>
<td>DXVAHDDDI_FILTER_BRIGHTNESS</td>
<td>A value that specifies the filter range of the brightness ProcAmp.</td>
</tr>

<tr>
<td>DXVAHDDDI_FILTER_CONTRAST</td>
<td>A value that specifies the filter range of the contrast ProcAmp.</td>
</tr>

<tr>
<td>DXVAHDDDI_FILTER_EDGE_ENHANCEMENT</td>
<td>A value that specifies the filter range of the edge enhancement filter.</td>
</tr>

<tr>
<td>DXVAHDDDI_FILTER_HUE</td>
<td>A value that specifies the filter range of the hue ProcAmp.</td>
</tr>

<tr>
<td>DXVAHDDDI_FILTER_NOISE_REDUCTION</td>
<td>A value that specifies the filter range of the noise reduction filter.</td>
</tr>

<tr>
<td>DXVAHDDDI_FILTER_SATURATION</td>
<td>A value that specifies the filter range of the saturation ProcAmp.</td>
</tr>
</table>


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | d3dumddi.h (include D3dumddi.h) |

## See Also

<dl>
<dt>
<a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi_getcaps.md">GetCaps</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20DXVAHDDDI_FILTER enumeration%20 RELEASE:%20(12/29/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>