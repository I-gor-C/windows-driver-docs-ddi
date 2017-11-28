---
UID: NS.d3dkmthk._D3DKMT_CREATEPROTECTEDSESSION
title: D3DKMT_CREATEPROTECTEDSESSION
author: windows-driver-content
description: Used to create a protected session.
old-location: display\d3dkmt-createprotectedsession.htm
old-project: display
ms.assetid: 4ec42f5a-df33-4da3-a959-64cb400f3177
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: D3DKMT_CREATEPROTECTEDSESSION, D3DKMT_CREATEPROTECTEDSESSION
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: d3dkmthk.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: D3DKMT_CREATEPROTECTEDSESSION
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

# D3DKMT_CREATEPROTECTEDSESSION structure



## -description
<p>Used to create a protected session.</p>


## -syntax

````
typedef struct _D3DKMT_CREATEPROTECTEDSESSION {
  D3DKMT_HANDLE hDevice;
  D3DKMT_HANDLE hSyncObject;
  const VOID    *pPrivateDriverData;
  UINT          PrivateDriverDataSize;
  const VOID    *pPrivateRuntimeData;
  UINT          PrivateRuntimeDataSize;
  D3DKMT_HANDLE hHandle;
} D3DKMT_CREATEPROTECTEDSESSION;
````


## -struct-fields
<dl>

### -field <b>hDevice</b>

<dd>
<p>A handle for the device.</p>
</dd>

### -field <b>hSyncObject</b>

<dd>
<p>A monitored fence handle associated with the session.</p>
</dd>

### -field <b>pPrivateDriverData</b>

<dd>
<p>Private driver data.</p>
</dd>

### -field <b>PrivateDriverDataSize</b>

<dd>
<p>Size of private driver data.</p>
</dd>

### -field <b>pPrivateRuntimeData</b>

<dd>
<p>Private runtime data.</p>
</dd>

### -field <b>PrivateRuntimeDataSize</b>

<dd>
<p>Size of private runtime data.</p>
</dd>

### -field <b>hHandle</b>

<dd>
<p>The protected session handle.</p>
</dd>
</dl>

## -remarks


## -requirements
<table>
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
</table>