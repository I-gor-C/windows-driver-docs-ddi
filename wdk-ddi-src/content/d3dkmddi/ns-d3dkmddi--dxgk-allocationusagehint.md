---
UID: NS.d3dkmddi._DXGK_ALLOCATIONUSAGEHINT
title: DXGK_ALLOCATIONUSAGEHINT
author: windows-driver-content
description: The DXGK_ALLOCATIONUSAGEHINT structure contains allocation usage and version information that is used as a hint about how to use an allocation.
old-location: display\dxgk_allocationusagehint.htm
old-project: display
ms.assetid: 04cceb5e-d185-4f43-a627-71a61a45b8aa
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: DXGK_ALLOCATIONUSAGEHINT, DXGK_ALLOCATIONUSAGEHINT
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: d3dkmddi.h
req.include-header: D3dkmddi.h
req.target-type: Windows
req.target-min-winverclnt: Available in Windows Vista and later versions of the Windows operating systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: DXGK_ALLOCATIONUSAGEHINT
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
req.iface: 
---

# DXGK_ALLOCATIONUSAGEHINT structure



## -description
<p>The DXGK_ALLOCATIONUSAGEHINT structure contains allocation usage and version information that is used as a hint about how to use an allocation.</p>


## -syntax

````
typedef struct _DXGK_ALLOCATIONUSAGEHINT {
  UINT                      Version;
  DXGK_ALLOCATIONUSAGEINFO1 v1;
} DXGK_ALLOCATIONUSAGEHINT;
````


## -struct-fields
<dl>

### -field <b>Version</b>

<dd>
<p>[out] A positive integer that indicates the version of the allocation.</p>
</dd>

### -field <b>v1</b>

<dd>
<p>[out] A <a href="..\d3dkmddi\ns-d3dkmddi--dxgk-allocationusageinfo1.md">DXGK_ALLOCATIONUSAGEINFO1</a> structure that describes how an allocation can be used in direct memory access (DMA) buffering.</p>
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
<dt>D3dkmddi.h (include D3dkmddi.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\d3dkmddi\ns-d3dkmddi--dxgk-allocationinfo.md">DXGK_ALLOCATIONINFO</a>
</dt>
<dt>
<a href="..\d3dkmddi\ns-d3dkmddi--dxgk-allocationusageinfo1.md">DXGK_ALLOCATIONUSAGEINFO1</a>
</dt>
<dt>
<a href="..\d3dkmddi\ns-d3dkmddi--dxgkarg-createallocation.md">DXGKARG_CREATEALLOCATION</a>
</dt>
<dt>
<a href="display.dxgkddicreateallocation">DxgkDdiCreateAllocation</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20DXGK_ALLOCATIONUSAGEHINT structure%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
