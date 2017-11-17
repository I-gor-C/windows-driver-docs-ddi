---
UID: NS.d3dumddi._D3DDDIARG_DRAWTRIPATCH
title: D3DDDIARG_DRAWTRIPATCH
author: windows-driver-content
description: The D3DDDIARG_DRAWTRIPATCH structure describes a triangular patch to draw.
old-location: display\d3dddiarg_drawtripatch.htm
ms.assetid: 296ed752-ddb6-41db-957f-606acc53b3b5
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
req.alt-api: D3DDDIARG_DRAWTRIPATCH
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
ms.keywords: D3DDDIARG_DRAWTRIPATCH, D3DDDIARG_DRAWTRIPATCH
req.iface: 
---

# D3DDDIARG_DRAWTRIPATCH structure



## -description
<p>The D3DDDIARG_DRAWTRIPATCH structure describes a triangular patch to draw. </p>


## -syntax

````
typedef struct _D3DDDIARG_DRAWTRIPATCH {
  UINT Handle;
} D3DDDIARG_DRAWTRIPATCH;
````


## -struct-fields
<dl>

### -field <b>Handle</b>

<dd>
<p>[in] The handle to the patch surface.</p>
</dd>
</dl>

## -remarks
<p>The <b>Handle</b> member refers to the patch surface, so that the next time the patch surface is drawn, the Microsoft Direct3D runtime is not required to re-specify the D3DTRIPATCH_INFO data structure for the patch surface. The user-mode display driver can precompute and cache forward-difference coefficients and any other information, which allows subsequent calls to the driver's <a href="https://msdn.microsoft.com/98e5f2c5-2795-4226-b5c0-9498b37c22df">DrawTriPatch</a> function that use the same handle to run more efficiently.</p>

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
<a href="https://msdn.microsoft.com/98e5f2c5-2795-4226-b5c0-9498b37c22df">DrawTriPatch</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20D3DDDIARG_DRAWTRIPATCH structure%20 RELEASE:%20(10/25/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
