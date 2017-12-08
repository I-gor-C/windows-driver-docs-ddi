---
UID: NS.D3DKMTHK._D3DKMT_BLTMODEL_PRESENTHISTORYTOKEN
title: _D3DKMT_BLTMODEL_PRESENTHISTORYTOKEN
author: windows-driver-content
description: The D3DKMT_BLTMODEL_PRESENTHISTORYTOKEN structure identifies a bit-block transfer (bitblt) present-history operation.
old-location: display\d3dkmt_bltmodel_presenthistorytoken.htm
old-project: display
ms.assetid: 841c1e6f-4561-4c37-a509-d9c0e9054022
ms.author: windowsdriverdev
ms.date: 12/6/2017
ms.keywords: _D3DKMT_BLTMODEL_PRESENTHISTORYTOKEN, D3DKMT_BLTMODEL_PRESENTHISTORYTOKEN
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: d3dkmthk.h
req.include-header: D3dkmthk.h
req.target-type: Windows
req.target-min-winverclnt: D3DKMT_BLTMODEL_PRESENTHISTORYTOKEN is supported beginning with the Windows 7 operating system.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: D3DKMT_BLTMODEL_PRESENTHISTORYTOKEN
req.alt-loc: d3dkmthk.h
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
---

# _D3DKMT_BLTMODEL_PRESENTHISTORYTOKEN structure



## -description
The D3DKMT_BLTMODEL_PRESENTHISTORYTOKEN structure identifies a bit-block transfer (bitblt) present-history operation.


## -syntax

````
typedef struct _D3DKMT_BLTMODEL_PRESENTHISTORYTOKEN {
  ULONG64             hLogicalSurface;
  ULONG64             hPhysicalSurface;
  ULONG64             EventId;
  D3DKMT_DIRTYREGIONS DirtyRegions;
} D3DKMT_BLTMODEL_PRESENTHISTORYTOKEN;
````


## -struct-fields

### -field hLogicalSurface

[in] A 64-bit value that specifies the handle to a logical surface to copy from. 

### -field hPhysicalSurface

[in] A 64-bit value that specifies the handle to a physical surface to copy to. 

### -field EventId

[in] A 64-bit value that identifies the bitblt event. 

### -field DirtyRegions

[in] A <a href="display.d3dkmt_dirtyregions">D3DKMT_DIRTYREGIONS</a> structure that identifies the active rectangles (dirty regions) of the bitblt surface. 

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
Version
</th>
<td width="70%">
D3DKMT_BLTMODEL_PRESENTHISTORYTOKEN is supported beginning with the Windows 7 operating system. 
</td>
</tr>
<tr>
<th width="30%">
Header
</th>
<td width="70%">
<dl>
<dt>D3dkmthk.h (include D3dkmthk.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="display.d3dkmt_dirtyregions">D3DKMT_DIRTYREGIONS</a>
</dt>
<dt>
<a href="display.d3dkmt_presenthistorytoken">D3DKMT_PRESENTHISTORYTOKEN</a>
</dt>
</dl>
 
 
<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20D3DKMT_BLTMODEL_PRESENTHISTORYTOKEN structure%20 RELEASE:%20(12/6/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>
