---
UID: NC.d3dkmthk.PDXGK_REMOVAL_NOTIFICATION
title: PDXGK_REMOVAL_NOTIFICATION
author: windows-driver-content
description: A callback indicating that the graphics device is being removed.
old-location: display\pdxgk_removal_notification.htm
old-project: display
ms.assetid: F9AA5859-8E8A-491D-B149-F42E418A64DC
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: DXGKMDT_OPM_STANDARD_INFORMATION, DXGKMDT_OPM_STANDARD_INFORMATION
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: callback
req.header: d3dkmthk.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: *PDXGK_REMOVAL_NOTIFICATION
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

# PDXGK_REMOVAL_NOTIFICATION callback



## -description
<p>A callback indicating that the graphics device is being removed.</p>


## -prototype

````
VOID *PDXGK_REMOVAL_NOTIFICATION(
   PVOID GraphicsDeviceHandle
);
````


## -parameters
<dl>

### -param GraphicsDeviceHandle 

<dd>
<p>A handle to the graphics device.</p>
</dd>
</dl>

## -returns
<p>This callback function does not return a value.</p>

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