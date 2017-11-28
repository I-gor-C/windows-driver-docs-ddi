---
UID: NS.d3dkmddi._DXGKARGCB_PROTECTEDSESSIONSTATUS
title: DXGKARGCB_PROTECTEDSESSIONSTATUS
author: windows-driver-content
description: Used for information on the status of the protected session.
old-location: display\dxgkargcb_protectedsessionstatus.htm
old-project: display
ms.assetid: 417480C5-8B24-4504-8B2D-DB9D38E4C11B
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: DXGKARGCB_PROTECTEDSESSIONSTATUS, DXGKARGCB_PROTECTEDSESSIONSTATUS
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
req.alt-api: DXGKARGCB_PROTECTEDSESSIONSTATUS
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

# DXGKARGCB_PROTECTEDSESSIONSTATUS structure



## -description
<p>Used for information on the status of the protected session.</p>


## -syntax

````
typedef struct _DXGKARGCB_PROTECTEDSESSIONSTATUS {
  HANDLE                        hProtectedSession;
  DXGK_PROTECTED_SESSION_STATUS Status;
} DXGKARGCB_PROTECTEDSESSIONSTATUS;
````


## -struct-fields
<dl>

### -field <b>hProtectedSession</b>

<dd>
<p>A handle for the protected session that was passed to DxgkDdiCreateProtectedSession.</p>
</dd>

### -field <b>Status</b>

<dd>
<p>The status of the protected session</p>
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