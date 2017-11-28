---
UID: NS.d3dkmddi._DXGKARG_CREATEPROTECTEDSESSION
title: DXGKARG_CREATEPROTECTEDSESSION
author: windows-driver-content
description: Used to create a protected session.
old-location: display\dxgkarg_createprotectedsession.htm
old-project: display
ms.assetid: 37A9A957-344F-48F6-93DE-D81DE5C20076
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: DXGKARG_CREATEPROTECTEDSESSION, DXGKARG_CREATEPROTECTEDSESSION
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: d3dkmddi.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: DXGKARG_CREATEPROTECTEDSESSION
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

# DXGKARG_CREATEPROTECTEDSESSION structure



## -description
<p>Used to create a protected session.</p>


## -syntax

````
typedef struct _DXGKARG_CREATEPROTECTEDSESSION {
  HANDLE hProtectedSession;
  PVOID  pPrivateDriverData;
  UINT   PrivateDriverDataSize;
} DXGKARG_CREATEPROTECTEDSESSION;
````


## -struct-fields
<dl>

### -field <b>hProtectedSession</b>

<dd>
<p>An assigned value for the protected session that was passed to DxgkDdiCreateProtectedSession.
</p>
</dd>

### -field <b>pPrivateDriverData</b>

<dd>
<p>A pointer to the driver data.</p>
</dd>

### -field <b>PrivateDriverDataSize</b>

<dd>
<p>The size of the data.</p>
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
<dt>D3dkmddi.h</dt>
</dl>
</td>
</tr>
</table>