---
UID : NE:d3dkmddi._DXGK_VIDPN_INTERFACE_VERSION
title : _DXGK_VIDPN_INTERFACE_VERSION
author : windows-driver-content
description : The DXGK_VIDPN_INTERFACE_VERSION enumeration indicates the version of a video present network (VidPN) interface.
old-location : display\dxgk_vidpn_interface_version.htm
old-project : display
ms.assetid : 819261a5-bec0-49a8-942a-9313d3b793ca
ms.author : windowsdriverdev
ms.date : 12/29/2017
ms.keywords : _DXGK_VIDPN_INTERFACE_VERSION, DXGK_VIDPN_INTERFACE_VERSION
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : enum
req.header : d3dkmddi.h
req.include-header : D3dkmddi.h
req.target-type : Windows
req.target-min-winverclnt : Available in Windows Vista and later versions of the Windows operating systems.
req.target-min-winversvr : 
req.kmdf-ver : 
req.umdf-ver : 
req.alt-api : DXGK_VIDPN_INTERFACE_VERSION
req.alt-loc : d3dkmddi.h
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
req.typenames : DXGK_VIDPN_INTERFACE_VERSION
---

# _DXGK_VIDPN_INTERFACE_VERSION Enumeration
The DXGK_VIDPN_INTERFACE_VERSION enumeration indicates the version of a video present network (VidPN) interface.

## Syntax
````
typedef enum _DXGK_VIDPN_INTERFACE_VERSION { 
  DXGK_VIDPN_INTERFACE_VERSION_UNINITIALIZED  = 0,
  DXGK_VIDPN_INTERFACE_VERSION_V1             = 1
} DXGK_VIDPN_INTERFACE_VERSION;
````

## Constants

<table>

<tr>
<td>DXGK_VIDPN_INTERFACE_VERSION_UNINITIALIZED</td>
<td>Indicates that a variable of type DXGK_VIDPN_INTERFACE_VERSION has not yet been assigned a meaningful value.</td>
</tr>

<tr>
<td>DXGK_VIDPN_INTERFACE_VERSION_V1</td>
<td>Indicates version 1 of the VidPN interface.</td>
</tr>
</table>

## Remarks

The <i>VidPnInterfaceVersion</i> parameter of the <a href="..\d3dkmddi\nc-d3dkmddi-dxgkcb_queryvidpninterface.md">DxgkCbQueryVidPnInterface</a> function and the <b>Version</b> member of the <a href="..\d3dkmddi\ns-d3dkmddi-_dxgk_vidpn_interface.md">DXGK_VIDPN_INTERFACE</a> structure are DXGK_VIDPN_INTERFACE_VERSION values.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | d3dkmddi.h (include D3dkmddi.h) |

## See Also

<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff570556">VidPn Interface</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20DXGK_VIDPN_INTERFACE_VERSION enumeration%20 RELEASE:%20(12/29/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>