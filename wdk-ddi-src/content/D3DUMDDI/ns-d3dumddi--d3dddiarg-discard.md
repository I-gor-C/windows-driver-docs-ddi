---
UID: NS.d3dumddi._D3DDDIARG_DISCARD
title: D3DDDIARG_DISCARD
author: windows-driver-content
description: Defines video display memory that can be discarded because the contents are no longer needed.
old-location: display\d3dddiarg_discard.htm
ms.assetid: 6efee74e-9e82-4631-8360-19061b0c015d
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: display
req.header: d3dumddi.h
req.include-header: D3dumddi.h
req.target-type: Windows
req.target-min-winverclnt: Windows 8
req.target-min-winversvr: Windows Server 2012
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: D3DDDIARG_DISCARD
req.alt-loc: D3dumddi.h
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
ms.keywords: D3DDDIARG_DISCARD, D3DDDIARG_DISCARD
req.iface: 
---

# D3DDDIARG_DISCARD structure



## -description
<p>Defines video display memory that can be discarded because the contents are no longer needed.</p>


## -syntax

````
typedef struct _D3DDDIARG_DISCARD {
  HANDLE     hResource;
  UINT       FirstSubResource;
  UINT       NumSubResources;
  const RECT *pRects;
  UINT       NumRects;
} D3DDDIARG_DISCARD;
````


## -struct-fields
<dl>

### -field <b>hResource</b>

<dd>
<p>A handle to the resource in which subresources are to be discarded.</p>
</dd>

### -field <b>FirstSubResource</b>

<dd>
<p>The index of the first subresource to be discarded.</p>
</dd>

### -field <b>NumSubResources</b>

<dd>
<p>The number of subresources to be discarded.</p>
</dd>

### -field <b>pRects</b>

<dd>
<p>An array of <a href="https://msdn.microsoft.com/library/windows/hardware/ff569234">RECT</a> structures for the rectangles in the resource view to discard. If <b>NULL</b>, the <a href="https://msdn.microsoft.com/F3EC7AAE-9DB8-43A1-B756-5F5C91F8372E">Discard</a> function discards the entire surface.</p>
</dd>

### -field <b>NumRects</b>

<dd>
<p>The number of rectangles in the array that the  <b>pRects</b> member specifies.</p>
</dd>
</dl>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Minimum supported client</p>
</th>
<td width="70%">
<p>Windows 8</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Minimum supported server</p>
</th>
<td width="70%">
<p>Windows Server 2012</p>
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
<a href="https://msdn.microsoft.com/F3EC7AAE-9DB8-43A1-B756-5F5C91F8372E">Discard</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff569234">RECT</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20D3DDDIARG_DISCARD structure%20 RELEASE:%20(10/25/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
