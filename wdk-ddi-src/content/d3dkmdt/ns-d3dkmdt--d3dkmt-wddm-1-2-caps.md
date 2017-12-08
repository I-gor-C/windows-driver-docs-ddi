---
UID: NS.d3dkmdt._D3DKMT_WDDM_1_2_CAPS
title: D3DKMT_WDDM_1_2_CAPS
author: windows-driver-content
description: Reserved for system use. Do not use in your driver.
old-location: display\d3dkmt_wddm_1_2_caps.htm
old-project: display
ms.assetid: 0cd26fad-4772-4631-81fc-da2ddb7dc9a1
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: D3DKMT_WDDM_1_2_CAPS, D3DKMT_WDDM_1_2_CAPS
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: d3dkmdt.h
req.include-header: D3dkmdt.h
req.target-type: Windows
req.target-min-winverclnt: Windows 8
req.target-min-winversvr: Windows Server 2012
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: D3DKMT_WDDM_1_2_CAPS
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

# D3DKMT_WDDM_1_2_CAPS structure



## -description
<p>Reserved for system use. Do not use in your driver.</p>


## -syntax

````
typedef struct _D3DKMT_WDDM_1_2_CAPS {
  D3DKMDT_PREEMPTION_CAPS PreemptionCaps;
  union {
    struct {
      UINT SupportNonVGA  :1;
      UINT SupportSmoothRotation  :1;
      UINT SupportPerEngineTDR  :1;
      UINT SupportKernelModeCommandBuffer  :1;
      UINT SupportCCD  :1;
      UINT SupportSoftwareDeviceBitmaps  :1;
      UINT SupportGammaRamp  :1;
      UINT SupportHWCursor  :1;
      UINT SupportHWVSync  :1;
      UINT SupportSurpriseRemovalInHibernation  :1;
      UINT Reserved  :22;
    };
    UINT   Value;
  };
} D3DKMT_WDDM_1_2_CAPS;
````


## -struct-fields
<dl>

### -field PreemptionCaps

<dd></dd>

### -field SupportNonVGA

<dd></dd>

### -field SupportSmoothRotation

<dd></dd>

### -field SupportPerEngineTDR

<dd></dd>

### -field SupportKernelModeCommandBuffer

<dd></dd>

### -field SupportCCD

<dd></dd>

### -field SupportSoftwareDeviceBitmaps

<dd></dd>

### -field SupportGammaRamp

<dd></dd>

### -field SupportHWCursor

<dd></dd>

### -field SupportHWVSync

<dd></dd>

### -field SupportSurpriseRemovalInHibernation

<dd></dd>

### -field Reserved

<dd></dd>

### -field Value

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
<p>Windows 8</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Minimum supported server</p>
</th>
<td width="70%">
<p>Windows Server 2012</p>
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