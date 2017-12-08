---
UID: NS.D3DKMDT._D3DKMT_WDDM_1_2_CAPS
title: _D3DKMT_WDDM_1_2_CAPS
author: windows-driver-content
description: Reserved for system use. Do not use in your driver.
old-location: display\d3dkmt_wddm_1_2_caps.htm
old-project: display
ms.assetid: 0cd26fad-4772-4631-81fc-da2ddb7dc9a1
ms.author: windowsdriverdev
ms.date: 12/6/2017
ms.keywords: _D3DKMT_WDDM_1_2_CAPS, D3DKMT_WDDM_1_2_CAPS
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
---

# _D3DKMT_WDDM_1_2_CAPS structure



## -description
Reserved for system use. Do not use in your driver.


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

### -field PreemptionCaps


### -field SupportNonVGA


### -field SupportSmoothRotation


### -field SupportPerEngineTDR


### -field SupportKernelModeCommandBuffer


### -field SupportCCD


### -field SupportSoftwareDeviceBitmaps


### -field SupportGammaRamp


### -field SupportHWCursor


### -field SupportHWVSync


### -field SupportSurpriseRemovalInHibernation


### -field Reserved


### -field Value


## -remarks


## -requirements
<table>
<tr>
<th width="30%">
Minimum supported client
</th>
<td width="70%">
Windows 8
</td>
</tr>
<tr>
<th width="30%">
Minimum supported server
</th>
<td width="70%">
Windows Server 2012
</td>
</tr>
<tr>
<th width="30%">
Header
</th>
<td width="70%">
<dl>
<dt>D3dkmdt.h (include D3dkmdt.h)</dt>
</dl>
</td>
</tr>
</table>