---
UID: NS.wiamicro._SCANWINDOW
title: SCANWINDOW
author: windows-driver-content
description: The SCANWINDOW structure is used by the WIA Flatbed driver to tell the microdriver what image area to scan.
old-location: image\scanwindow.htm
old-project: image
ms.assetid: c4b507ac-af32-4949-add0-e19c00e328fe
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: SCANWINDOW, SCANWINDOW, *PSCANWINDOW
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: wiamicro.h
req.include-header: Wiamicro.h
req.target-type: Windows
req.target-min-winverclnt: Available in Windows Me and in Windows XP and later versions of the Windows operating systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: SCANWINDOW
req.alt-loc: wiamicro.h
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
req.product: Windows 10 or later.
---

# SCANWINDOW structure



## -description
<p>The SCANWINDOW structure is used by the WIA Flatbed driver to tell the microdriver what image area to scan.</p>


## -syntax

````
typedef struct _SCANWINDOW {
  LONG xPos;
  LONG yPos;
  LONG xExtent;
  LONG yExtent;
} SCANWINDOW, *PSCANWINDOW;
````


## -struct-fields
<dl>

### -field <b>xPos</b>

<dd>
<p>Specifies the horizontal position of the left edge of the scan window in pixels.</p>
</dd>

### -field <b>yPos</b>

<dd>
<p>Specifies the vertical position of the top edge of the scan window in pixels.</p>
</dd>

### -field <b>xExtent</b>

<dd>
<p>Specifies the width of the scan window in pixels.</p>
</dd>

### -field <b>yExtent</b>

<dd>
<p>Specifies the height of the scan window in pixels.</p>
</dd>
</dl>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Available in Windows Me and in Windows XP and later versions of the Windows operating systems.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Wiamicro.h (include Wiamicro.h)</dt>
</dl>
</td>
</tr>
</table>