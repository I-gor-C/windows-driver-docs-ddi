---
UID: NS.d3dkmddi._DXGKARG_ENUMVIDPNCOFUNCMODALITY
title: DXGKARG_ENUMVIDPNCOFUNCMODALITY
author: windows-driver-content
description: The DXGKARG_ENUMVIDPNCOFUNCMODALITY structure contains arguments for the DxgkDdiEnumVidPnCofuncModality function.
old-location: display\dxgkarg_enumvidpncofuncmodality.htm
ms.assetid: a67c9e20-68bf-45d5-bbf0-d324643b2a5d
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: display
req.header: d3dkmddi.h
req.include-header: D3dkmddi.h
req.target-type: Windows
req.target-min-winverclnt: Available in Windows Vista and later versions of the Windows operating systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: DXGKARG_ENUMVIDPNCOFUNCMODALITY
req.alt-loc: d3dkmddi.h
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
ms.keywords: DXGKARG_ENUMVIDPNCOFUNCMODALITY, DXGKARG_ENUMVIDPNCOFUNCMODALITY
req.iface: 
---

# DXGKARG_ENUMVIDPNCOFUNCMODALITY structure



## -description
<p>The DXGKARG_ENUMVIDPNCOFUNCMODALITY structure contains arguments for the <a href="https://msdn.microsoft.com/6dda82bd-1a43-4ffe-b398-a9f8cee6d1c1">DxgkDdiEnumVidPnCofuncModality</a> function. The <i>DxgkDdiEnumVidPnCofuncModality</i> function makes the source and target mode sets of a VidPN cofunctional with the VidPN's topology and the modes that have already been pinned.</p>


## -syntax

````
typedef struct _DXGKARG_ENUMVIDPNCOFUNCMODALITY {
  D3DKMDT_HVIDPN                        hConstrainingVidPn;
  D3DKMDT_ENUMCOFUNCMODALITY_PIVOT_TYPE EnumPivotType;
  DXGK_ENUM_PIVOT                       EnumPivot;
} DXGKARG_ENUMVIDPNCOFUNCMODALITY;
````


## -struct-fields
<dl>

### -field <b>hConstrainingVidPn</b>

<dd>
<p>A handle to the VidPn object for which the cofunctional modes are being requested.</p>
</dd>

### -field <b>EnumPivotType</b>

<dd>
<p>A <a href="https://msdn.microsoft.com/library/windows/hardware/ff546003">D3DKMDT_ENUMCOFUNCMODALITY_PIVOT_TYPE</a> enumerator that supplies the enumeration pivot type.</p>
</dd>

### -field <b>EnumPivot</b>

<dd>
<p>A <a href="https://msdn.microsoft.com/library/windows/hardware/ff561064">DXGK_ENUM_PIVOT</a> structure.</p>
</dd>
</dl>

## -remarks
<p>If a particular video present source or target is designated as the pivot of the enumeration, then <i>DxgkDdiEnumVidPnCofuncModality</i> must not change the mode set for that source or target.</p>

<p>The D3DKMDT_HVIDPN data type is defined in <i>D3dkmdt.h</i>. The D3DDDI_VIDEO_PRESENT_SOURCE_ID and D3DDDI_VIDEO_PRESENT_TARGET_ID data types are defined in <i>D3dukmdt.h</i>.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Available in Windows Vista and later versions of the Windows operating systems.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>D3dkmddi.h (include D3dkmddi.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff561064">DXGK_ENUM_PIVOT</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/6dda82bd-1a43-4ffe-b398-a9f8cee6d1c1">DxgkDdiEnumVidPnCofuncModality</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff546003">D3DKMDT_ENUMCOFUNCMODALITY_PIVOT_TYPE</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20DXGKARG_ENUMVIDPNCOFUNCMODALITY structure%20 RELEASE:%20(10/25/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
