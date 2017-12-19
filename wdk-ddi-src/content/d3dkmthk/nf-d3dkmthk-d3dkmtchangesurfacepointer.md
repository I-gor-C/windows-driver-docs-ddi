---
UID: NF.d3dkmthk.D3DKMTChangeSurfacePointer
title: D3DKMTChangeSurfacePointer function
author: windows-driver-content
description: The D3DKMTChangeSurfacePointer function is for system use only.
old-location: display\d3dkmtchangesurfacepointer.htm
old-project: display
ms.assetid: 3db4e04b-2707-4eb1-a249-2714304246a8
ms.author: windowsdriverdev
ms.date: 12/15/2017
ms.keywords: D3DKMTChangeSurfacePointer
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: d3dkmthk.h
req.include-header: 
req.target-type: Desktop
req.target-min-winverclnt: Available in Windows Vista and later versions of the Windows operating systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: D3DKMTChangeSurfacePointer
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

# D3DKMTChangeSurfacePointer function



## -description
The <b>D3DKMTChangeSurfacePointer</b> function is for system use only.



## -syntax

````
NTSTATUS APIENTRY D3DKMTChangeSurfacePointer(
  _In_ const D3DKMT_CHANGESURFACEPOINTER *pData
);
````


## -parameters

### -param pData [in]

For system use only.


## -returns
An opaque NTSTATUS value.


## -remarks
This function is for system use only.


## -requirements
<table>
<tr>
<th width="30%">
Target platform

</th>
<td width="70%">
<dl>
<dt>Desktop</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
Version

</th>
<td width="70%">
Available in Windows Vista and later versions of the Windows operating systems.

</td>
</tr>
<tr>
<th width="30%">
Header

</th>
<td width="70%">
<dl>
<dt>D3dkmthk.h</dt>
</dl>
</td>
</tr>
</table>