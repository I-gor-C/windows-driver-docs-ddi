---
UID: NF.d3dkmthk.D3DKMTOutputDuplGetFrameInfo
title: D3DKMTOutputDuplGetFrameInfo function
author: windows-driver-content
description: Reserved for system use. Do not use in your driver.
old-location: display\d3dkmtoutputduplgetframeinfo.htm
old-project: display
ms.assetid: c6357e93-9755-44f3-b689-d7a13c309830
ms.author: windowsdriverdev
ms.date: 12/6/2017
ms.keywords: D3DKMTOutputDuplGetFrameInfo
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
req.alt-api: D3DKMTOutputDuplGetFrameInfo
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

# D3DKMTOutputDuplGetFrameInfo function



## -description
Reserved for system use. Do not use in your driver.


## -syntax

````
EXTERN_C _Check_return_ NTSTATUS APIENTRY D3DKMTOutputDuplGetFrameInfo(
  _Inout_ D3DKMT_OUTPUTDUPL_GET_FRAMEINFO *pData
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