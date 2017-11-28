---
UID: NF.d3dkmthk.D3DKMTSetVidPnSourceOwner2
title: D3DKMTSetVidPnSourceOwner2
author: windows-driver-content
description: Used to set the VidPN source owner.
old-location: display\d3dkmtsetvidpnsourceowner2.htm
old-project: display
ms.assetid: 14ba3307-753f-4dca-8d4d-c87b3fee00a5
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: D3DKMTSetVidPnSourceOwner2
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: d3dkmthk.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: Windows 10
req.target-min-winversvr: Windows Server 2016
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: D3DKMTSetVidPnSourceOwner2
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
req.iface: 
---

# D3DKMTSetVidPnSourceOwner2 function



## -description
<p>
			
            Used to set the VidPN source owner.</p>


## -syntax

````
NTSTATUS  D3DKMTSetVidPnSourceOwner2(
  _In_ const D3DKMT_SETVIDPNSOURCEOWNER2   D3dkmt_setvidpnsourceowner2
);
````


## -parameters
<dl>

### -param <i>D3dkmt_setvidpnsourceowner2</i> [in]

<dd>
<p>Indicates the source owner.</p>
</dd>
</dl>

## -returns
<p>Returns STATUS_SUCCESS if used successfully.</p>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Minimum supported client</p>
</th>
<td width="70%">
<p>Windows 10</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Minimum supported server</p>
</th>
<td width="70%">
<p>Windows Server 2016</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>D3dkmthk.h</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>IRQL</p>
</th>
<td width="70%">
<p></p>
</td>
</tr>
</table>