---
UID: NS.ntddvdeo._VIDEO_WIN32K_CALLBACKS_PARAMS
title: VIDEO_WIN32K_CALLBACKS_PARAMS
author: windows-driver-content
description: The VIDEO_WIN32K_CALLBACKS_PARAMS structure and the VIDEO_WIN32K_CALLBACKS_PARAMS_TYPE enumeration are reserved for system use.
old-location: display\video_win32k_callbacks_params.htm
old-project: display
ms.assetid: d533721f-b4c8-44f9-9c39-f312e1ec9895
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: VIDEO_WIN32K_CALLBACKS_PARAMS, VIDEO_WIN32K_CALLBACKS_PARAMS, *PVIDEO_WIN32K_CALLBACKS_PARAMS
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: ntddvdeo.h
req.include-header: Ntddvdeo.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: VIDEO_WIN32K_CALLBACKS_PARAMS
req.alt-loc: ntddvdeo.h
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

# VIDEO_WIN32K_CALLBACKS_PARAMS structure



## -description
<p>The VIDEO_WIN32K_CALLBACKS_PARAMS structure and the VIDEO_WIN32K_CALLBACKS_PARAMS_TYPE enumeration are reserved for system use.</p>


## -syntax

````
typedef struct _VIDEO_WIN32K_CALLBACKS_PARAMS {
  VIDEO_WIN32K_CALLBACKS_PARAMS_TYPE CalloutType;
  PVOID                              PhysDisp;
  ULONG_PTR                          Param;
  LONG                               Status;
} VIDEO_WIN32K_CALLBACKS_PARAMS, *PVIDEO_WIN32K_CALLBACKS_PARAMS;
````


## -struct-fields
<dl>

### -field <b>CalloutType</b>

<dd>
<p>Reserved for system use.</p>
</dd>

### -field <b>PhysDisp</b>

<dd>
<p>Reserved for system use.</p>
</dd>

### -field <b>Param</b>

<dd>
<p>Reserved for system use.</p>
</dd>

### -field <b>Status</b>

<dd>
<p>Reserved for system use.</p>
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
<dt>Ntddvdeo.h (include Ntddvdeo.h)</dt>
</dl>
</td>
</tr>
</table>