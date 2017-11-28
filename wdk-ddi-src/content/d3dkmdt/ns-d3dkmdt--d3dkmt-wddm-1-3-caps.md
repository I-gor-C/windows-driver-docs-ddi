---
UID: NS.d3dkmdt._D3DKMT_WDDM_1_3_CAPS
title: D3DKMT_WDDM_1_3_CAPS
author: windows-driver-content
description: Reserved for system use. Do not use in your driver.
old-location: display\d3dkmt_wddm_1_3_caps.htm
old-project: display
ms.assetid: 53DB51B2-482C-4A1D-AD03-FEB73B77F9A9
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: D3DKMT_WDDM_1_3_CAPS, D3DKMT_WDDM_1_3_CAPS
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: d3dkmdt.h
req.include-header: D3dkmdt.h
req.target-type: Windows
req.target-min-winverclnt: Windows 8.1
req.target-min-winversvr: Windows Server 2012 R2
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: D3DKMT_WDDM_1_3_CAPS
req.alt-loc: D3dkmdt.h
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

# D3DKMT_WDDM_1_3_CAPS structure



## -description
<p>Reserved for system use. Do not use in your driver.</p>


## -syntax

````
typedef struct _D3DKMT_WDDM_1_3_CAPS {
  union {
    struct {
      UINT SupportMiracast  :1;
      UINT IsHybridIntegratedGPU  :1;
      UINT IsHybridDiscreteGPU  :1;
      UINT SupportPowerManagementPStates  :1;
      UINT Reserved  :28;
    };
  };
} D3DKMT_WDDM_1_3_CAPS;
````


## -struct-fields
<dl>

### -field <b>SupportMiracast</b>

<dd></dd>

### -field <b>IsHybridIntegratedGPU</b>

<dd></dd>

### -field <b>IsHybridDiscreteGPU</b>

<dd></dd>

### -field <b>SupportPowerManagementPStates</b>

<dd></dd>

### -field <b>Reserved</b>

<dd></dd>
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
<dt>D3dkmdt.h (include D3dkmdt.h)</dt>
</dl>
</td>
</tr>
</table>