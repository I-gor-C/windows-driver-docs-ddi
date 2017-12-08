---
UID: NF.d3dkmthk.D3DKMTOutputDuplGetPointerShapeData
title: D3DKMTOutputDuplGetPointerShapeData function
author: windows-driver-content
description: Reserved for system use. Do not use in your driver.
old-location: display\d3dkmtoutputduplgetpointershapedata.htm
old-project: display
ms.assetid: eb1352b2-5e04-40e3-836b-a517590bfab3
ms.author: windowsdriverdev
ms.date: 12/6/2017
ms.keywords: D3DKMTOutputDuplGetPointerShapeData
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: d3dkmthk.h
req.include-header: D3dkmthk.h
req.target-type: Universal
req.target-min-winverclnt: Windows 8
req.target-min-winversvr: Windows Server 2012
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: D3DKMTOutputDuplGetPointerShapeData
req.alt-loc: Gdi32.dll,API-MS-Win-dx-d3dkmt-l1-1-0.dll,API-MS-Win-dx-d3dkmt-l1-1-1.dll,API-MS-Win-DX-D3DKMT-L1-1-2.dll
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Gdi32.lib
req.dll: Gdi32.dll
req.irql: 
---

# D3DKMTOutputDuplGetPointerShapeData function



## -description
Reserved for system use. Do not use in your driver.


## -syntax

````
EXTERN_C _Check_return_ NTSTATUS APIENTRY D3DKMTOutputDuplGetPointerShapeData(
  _Inout_ D3DKMT_OUTPUTDUPL_GET_POINTER_SHAPE_DATA *pData
);
````


## -parameters

### -param pData [in, out]


## -remarks


## -requirements
<table>
<tr>
<th width="30%">
Minimum supported client
</th>
<td width="70%">
Windows 8
</td>
</tr>
<tr>
<th width="30%">
Minimum supported server
</th>
<td width="70%">
Windows Server 2012
</td>
</tr>
<tr>
<th width="30%">
Target platform
</th>
<td width="70%">
<dl>
<dt><a href="http://go.microsoft.com/fwlink/p/?linkid=531356" target="_blank">Universal</a></dt>
</dl>
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
<tr>
<th width="30%">
Library
</th>
<td width="70%">
<dl>
<dt>Gdi32.lib</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
DLL
</th>
<td width="70%">
<dl>
<dt>Gdi32.dll</dt>
</dl>
</td>
</tr>
</table>