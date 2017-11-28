---
UID: NE.d3d10umddi.D3DWDDM1_3DDI_MARKER_TYPE
title: D3DWDDM1_3DDI_MARKER_TYPE
author: windows-driver-content
description: Indicates the type of marker that the user-mode display driver supports.
old-location: display\d3dwddm1_3ddi_marker_type.htm
old-project: display
ms.assetid: E57CA17F-FB96-4E9B-A38D-67A4F925D3B4
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: SETRESULT_INFO, SETRESULT_INFO, *PSETRESULT_INFO
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: d3d10umddi.h
req.include-header: D3d10umddi.h
req.target-type: Windows
req.target-min-winverclnt: Windows 8.1
req.target-min-winversvr: Windows Server 2012 R2
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: D3DWDDM1_3DDI_MARKER_TYPE
req.alt-loc: D3d10umddi.h
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

# D3DWDDM1_3DDI_MARKER_TYPE enumeration



## -description
<p>Indicates the type of marker that the user-mode display driver supports.</p>


## -syntax

````
typedef enum D3DWDDM1_3DDI_MARKER_TYPE { 
  D3DWDDM1_3DDI_MARKER_TYPE_NONE,
  D3DWDDM1_3DDI_MARKER_TYPE_PROFILE
} D3DWDDM1_3DDI_MARKER_TYPE;
````


## -enum-fields
<dl>

### -field <a id="D3DWDDM1_3DDI_MARKER_TYPE_NONE"></a><a id="d3dwddm1_3ddi_marker_type_none"></a><b>D3DWDDM1_3DDI_MARKER_TYPE_NONE</b>

<dd>
<p>No marker type is supported.</p>
</dd>

### -field <a id="D3DWDDM1_3DDI_MARKER_TYPE_PROFILE"></a><a id="d3dwddm1_3ddi_marker_type_profile"></a><b>D3DWDDM1_3DDI_MARKER_TYPE_PROFILE</b>

<dd>
<p>The context submits GPU work for single-threaded user-mode DDIs. In this case, each time stamp denotes the end of GPU work.</p>
</dd>
</dl>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Minimum supported client</p>
</th>
<td width="70%">
<p>Windows 8.1</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Minimum supported server</p>
</th>
<td width="70%">
<p>Windows Server 2012 R2</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>D3d10umddi.h (include D3d10umddi.h)</dt>
</dl>
</td>
</tr>
</table>