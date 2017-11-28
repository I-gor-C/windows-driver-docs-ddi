---
UID: NS.d3dkmddi._DXGK_CONTEXTINFO_CAPS
title: DXGK_CONTEXTINFO_CAPS
author: windows-driver-content
description: DXGK_CONTEXTINFO_CAPS is used to describe the capabilities supported by a driver.
old-location: display\dxgk_contextinfo_caps.htm
old-project: display
ms.assetid: AC65F790-981F-4B50-BB9E-84F79D8F6C4F
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: DXGK_CONTEXTINFO_CAPS, DXGK_CONTEXTINFO_CAPS
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: d3dkmddi.h
req.include-header: D3dkmddi.h
req.target-type: Windows
req.target-min-winverclnt: Windows 10
req.target-min-winversvr: Windows Server 2016
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: DXGK_CONTEXTINFO_CAPS
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

# DXGK_CONTEXTINFO_CAPS structure



## -description
<p><b>DXGK_CONTEXTINFO_CAPS</b> is used to describe  the capabilities supported by a driver.</p>


## -syntax

````
typedef struct _DXGK_CONTEXTINFO_CAPS {
  union {
    struct {
      UINT NoPatchingRequired  :1;
      UINT DriverManagesResidency  :1;
      UINT UseIoMmu  :1;
      UINT Reserved  :29;
    };
    UINT   Value;
  };
} DXGK_CONTEXTINFO_CAPS;
````


## -struct-fields
<dl>

### -field <b>NoPatchingRequired</b>

<dd>
<p>Indicates that no memory patching is required.</p>
</dd>

### -field <b>DriverManagesResidency</b>

<dd>
<p>Indicates that the driver manages memory residency.</p>
</dd>

### -field <b>UseIoMmu</b>

<dd>
<p>Indicates that the driver supports IoMmu. </p>
</dd>

### -field <b>Reserved</b>

<dd>
<p>This field is reserved and should not be used.</p>
</dd>

### -field <b>Value</b>

<dd>
<p>The consolidated value of the structure.</p>
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
<dt>D3dkmddi.h (include D3dkmddi.h)</dt>
</dl>
</td>
</tr>
</table>