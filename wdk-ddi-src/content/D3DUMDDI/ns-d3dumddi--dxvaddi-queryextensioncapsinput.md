---
UID: NS.d3dumddi._DXVADDI_QUERYEXTENSIONCAPSINPUT
title: DXVADDI_QUERYEXTENSIONCAPSINPUT
author: windows-driver-content
description: The DXVADDI_QUERYEXTENSIONCAPSINPUT structure describes a capability of an extension GUID that information is requested for.
old-location: display\dxvaddi_queryextensioncapsinput.htm
ms.assetid: 6907eb45-8d29-4cdc-80eb-2d8cafbbd9bd
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: display
req.header: d3dumddi.h
req.include-header: D3dumddi.h
req.target-type: Windows
req.target-min-winverclnt: Available in Windows Vista and later versions of the Windows operating systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: DXVADDI_QUERYEXTENSIONCAPSINPUT
req.alt-loc: d3dumddi.h
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
ms.keywords: DXVADDI_QUERYEXTENSIONCAPSINPUT, DXVADDI_QUERYEXTENSIONCAPSINPUT
req.iface: 
---

# DXVADDI_QUERYEXTENSIONCAPSINPUT structure



## -description
<p>The DXVADDI_QUERYEXTENSIONCAPSINPUT structure describes a capability of an extension GUID that information is requested for.</p>


## -syntax

````
typedef struct _DXVADDI_QUERYEXTENSIONCAPSINPUT {
  const GUID          *pGuid;
  UINT                CapType;
  DXVADDI_PRIVATEDATA *pPrivate;
} DXVADDI_QUERYEXTENSIONCAPSINPUT;
````


## -struct-fields
<dl>

### -field <b>pGuid</b>

<dd>
<p>[in] A pointer to a GUID that represents the extension device type. </p>
</dd>

### -field <b>CapType</b>

<dd>
<p>[in] A capability type that information is requested for. A capability type can apply to one of the following categories of video acceleration:</p>
<ul>
<li>
<p>DXVADDI_EXTENSION_CATEGORY_DECODER (0x0001)</p>
</li>
<li>
<p>DXVADDI_EXTENSION_CATEGORY_ENCODER (0x0002)</p>
</li>
<li>
<p>DXVADDI_EXTENSION_CATEGORY_PROCESSOR (0x0004)</p>
</li>
<li>
<p>DXVADDI_EXTENSION_CATEGORY_ALL (0x0007)</p>
</li>
</ul>
<p>Extension capability types can be defined from DXVADDI_EXTENSION_CAPTYPE_MIN (300) to DXVADDI_EXTENSION_CAPTYPE_MAX (400).</p>
</dd>

### -field <b>pPrivate</b>

<dd>
<p>[in] A pointer to a <a href="https://msdn.microsoft.com/library/windows/hardware/ff562916">DXVADDI_PRIVATEDATA</a> structure that contains data that the driver requires to retrieve information about the extension capability.</p>
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
<p>Available in Windows Vista and later versions of the Windows operating systems.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>D3dumddi.h (include D3dumddi.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff543148">D3DDDIARG_GETCAPS</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff544132">D3DDDICAPS_TYPE</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff562916">DXVADDI_PRIVATEDATA</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/cf6c61ce-7b53-46d0-b3ff-ed5b2b964c65">GetCaps</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20DXVADDI_QUERYEXTENSIONCAPSINPUT structure%20 RELEASE:%20(10/25/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
