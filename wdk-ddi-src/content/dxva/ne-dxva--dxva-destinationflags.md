---
UID: NE.dxva._DXVA_DestinationFlags
title: DXVA_DestinationFlags
author: windows-driver-content
description: The DXVA_DestinationFlags enumeration type contains a collection of flags that identify changes in the current destination surface from the previous destination surface.
old-location: display\dxva_destinationflags.htm
old-project: display
ms.assetid: 842c6ece-5304-428c-afbe-2990d239f38a
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: DXGI_GAMMA_CONTROL_CAPABILITIES, DXGI_GAMMA_CONTROL_CAPABILITIES
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: dxva.h
req.include-header: Dxva.h
req.target-type: Windows
req.target-min-winverclnt: This enumeration type applies only to Windows Server 2003 with SP1 and later, and Windows XP with SP2 and later.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: DXVA_DestinationFlags
req.alt-loc: dxva.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: 
req.iface: 
---

# DXVA_DestinationFlags enumeration



## -description
<p>The DXVA_DestinationFlags enumeration type contains a collection of flags that identify changes in the current destination surface from the previous destination surface.</p>


## -syntax

````
typedef enum _DXVA_DestinationFlags { 
  DXVA_DestinationFlagMask                 = DXVABit(3)|DXVABit(2)|DXVABit(1)|DXVABit(0),
  DXVA_DestinationFlag_Background_Changed  = 0x0001,
  DXVA_DestinationFlag_TargetRect_Changed  = 0x0002,
  DXVA_DestinationFlag_ColorData_Changed   = 0x0004,
  DXVA_DestinationFlag_Alpha_Changed       = 0x0008
} DXVA_DestinationFlags;
````


## -enum-fields
<dl>

### -field DXVA_DestinationFlagMask

<dd>
<p>Specifies the destination-flag mask, which consists of the first 4 bits of a DWORD.</p>
</dd>

### -field DXVA_DestinationFlag_Background_Changed

<dd>
<p>Indicates that the background color of the destination surface changed. </p>
</dd>

### -field DXVA_DestinationFlag_TargetRect_Changed

<dd>
<p>Indicates that the target rectangle of the destination surface changed. </p>
</dd>

### -field DXVA_DestinationFlag_ColorData_Changed

<dd>
<p>Indicates that format information for the destination surface changed. 
</p>
</dd>

### -field DXVA_DestinationFlag_Alpha_Changed

<dd>
<p>Indicates that the planar alpha value for the destination surface changed.</p>
</dd>
</dl>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>This enumeration type applies only to Windows Server 2003 with SP1 and later, and Windows XP with SP2 and later.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Dxva.h (include Dxva.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="display.dxva_deinterlacebobdeviceclass_deinterlacebltex">DeinterlaceBltEx</a>
</dt>
<dt>
<a href="..\dxva\ns-dxva--dxva-deinterlacebltex.md">DXVA_DeinterlaceBltEx</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20DXVA_DestinationFlags enumeration%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
