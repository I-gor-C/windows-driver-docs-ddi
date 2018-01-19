---
UID : NE:d3dumddi._DXVAHDDDI_FRAME_FORMAT
title : _DXVAHDDDI_FRAME_FORMAT
author : windows-driver-content
description : The DXVAHDDDI_FRAME_FORMAT enumeration contains values that identify the frame format.
old-location : display\dxvahdddi_frame_format.htm
old-project : display
ms.assetid : 82fded96-9321-47a8-8bdd-65c5a75951ac
ms.author : windowsdriverdev
ms.date : 12/29/2017
ms.keywords : _DXVAHDDDI_FRAME_FORMAT, DXVAHDDDI_FRAME_FORMAT
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : enum
req.header : d3dumddi.h
req.include-header : D3dumddi.h
req.target-type : Windows
req.target-min-winverclnt : DXVAHDDDI_FRAME_FORMAT is supported beginning with the Windows 7 operating system.
req.target-min-winversvr : 
req.kmdf-ver : 
req.umdf-ver : 
req.alt-api : DXVAHDDDI_FRAME_FORMAT
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
req.typenames : DXVAHDDDI_FRAME_FORMAT
---

# _DXVAHDDDI_FRAME_FORMAT Enumeration
The DXVAHDDDI_FRAME_FORMAT enumeration contains values that identify the frame format.

## Syntax
````
typedef enum _DXVAHDDDI_FRAME_FORMAT { 
  DXVAHDDDI_FRAME_FORMAT_PROGRESSIVE                    = 0,
  DXVAHDDDI_FRAME_FORMAT_INTERLACED_TOP_FIELD_FIRST     = 1,
  DXVAHDDDI_FRAME_FORMAT_INTERLACED_BOTTOM_FIELD_FIRST  = 2
} DXVAHDDDI_FRAME_FORMAT;
````

## Constants

<table>

<tr>
<td>DXVAHDDDI_FRAME_FORMAT_INTERLACED_BOTTOM_FIELD_FIRST</td>
<td>A value that specifies that the frame format is interlaced with two fields. The bottom (odd) field is displayed first.</td>
</tr>

<tr>
<td>DXVAHDDDI_FRAME_FORMAT_INTERLACED_TOP_FIELD_FIRST</td>
<td>A value that specifies that the frame format is interlaced with two fields. The top (even) field is displayed first.</td>
</tr>

<tr>
<td>DXVAHDDDI_FRAME_FORMAT_PROGRESSIVE</td>
<td>A value that specifies that the frame format is progressive.</td>
</tr>
</table>

## Remarks

The <a href="wdkgloss.f#wdkgloss.fourcc#wdkgloss.fourcc"><i>FOURCC</i></a> format of the surface defines whether the interlaced fields are interleaved or not. For example, NV12 is an interlaced format with interleaved fields whereas NV24 is an interlaced format with non-interleaved fields.

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
<a href="..\d3dumddi\ns-d3dumddi-_dxvahdddi_stream_state_frame_format_data.md">DXVAHDDDI_STREAM_STATE_FRAME_FORMAT_DATA</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20DXVAHDDDI_FRAME_FORMAT enumeration%20 RELEASE:%20(12/29/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>