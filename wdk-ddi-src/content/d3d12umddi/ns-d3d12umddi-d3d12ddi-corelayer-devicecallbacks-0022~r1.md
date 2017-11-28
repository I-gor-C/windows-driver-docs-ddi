---
UID: NS.d3d12umddi.D3D12DDI_CORELAYER_DEVICECALLBACKS_0022~r1
title: D3D12DDI_CORELAYER_DEVICECALLBACKS_0022
author: windows-driver-content
description: This structure contains runtime callback functions that the user-mode display driver can use.
old-location: display\d3d12ddi_corelayer_devicecallbacks_0022.htm
old-project: display
ms.assetid: E5B7FDB6-3351-489E-B0BB-8B8DD605FCF4
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: D3D12DDI_CORELAYER_DEVICECALLBACKS_0022, D3D12DDI_CORELAYER_DEVICECALLBACKS_0022
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: d3d12umddi.h
req.include-header: D3d12umddi.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: D3D12DDI_CORELAYER_DEVICECALLBACKS_0022
req.alt-loc: D3d12umddi.h
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

# D3D12DDI_CORELAYER_DEVICECALLBACKS_0022 structure



## -description
<p>This structure contains runtime callback functions that the user-mode display driver can use.</p>


## -syntax

````
typedef struct D3D12DDI_CORELAYER_DEVICECALLBACKS_0022 {
  PFND3D12DDI_SETERROR_CB               pfnSetErrorCb;
  PFND3D12DDI_SETCOMMANDLISTERROR_CB    pfnSetCommandListErrorCb;
  PFND3D12DDI_SETCOMMANDLISTDDITABLE_CB pfnSetCommandListDDITableCb;
  PFND3D12DDI_CREATECONTEXT_CB          pfnCreateContextCb;
  PFND3D12DDI_CREATECONTEXTVIRTUAL_CB   pfnCreateContextVirtualCb;
  PFND3D12DDI_DESTROYCONTEXT_CB         pfnDestroyContextCb;
  PFND3D12DDI_CREATEPAGINGQUEUE_CB      pfnCreatePagingQueueCb;
  PFND3D12DDI_DESTROYPAGINGQUEUE_CB     pfnDestroyPagingQueueCb;
  PFND3D12DDI_MAKERESIDENT_CB           pfnMakeResidentCb;
  PFND3D12DDI_EVICT_CB                  pfnEvictCb;
  PFND3D12DDI_RECLAIMALLOCATIONS2_CB    pfnReclaimAllocations2Cb;
  PFND3D12DDI_OFFERALLOCATIONS_CB       pfnOfferAllocationsCb;
  PFND3D12DDI_ALLOCATE_CB_0022          pfnAllocateCb;
  PFND3D12DDI_DEALLOCATE_CB_0022        pfnDeallocateCb;
} D3D12DDI_CORELAYER_DEVICECALLBACKS_0022;
````


## -struct-fields
<dl>

### -field <b>pfnSetErrorCb</b>

<dd>
<p>A pointer to the pfnSetErrorCb function.</p>
</dd>

### -field <b>pfnSetCommandListErrorCb</b>

<dd>
<p>A pointer to the function.</p>
</dd>

### -field <b>pfnSetCommandListDDITableCb</b>

<dd>
<p>A pointer to the pfnSetCommandListErrorCb function.</p>
</dd>

### -field <b>pfnCreateContextCb</b>

<dd>
<p>A pointer to the pfnCreateContextCb function.</p>
</dd>

### -field <b>pfnCreateContextVirtualCb</b>

<dd>
<p>A pointer to the pfnCreateContextVirtualCb function.</p>
</dd>

### -field <b>pfnDestroyContextCb</b>

<dd>
<p>A pointer to the pfnDestroyContextCb function.</p>
</dd>

### -field <b>pfnCreatePagingQueueCb</b>

<dd>
<p>A pointer to the pfnCreatePagingQueueCb function.</p>
</dd>

### -field <b>pfnDestroyPagingQueueCb</b>

<dd>
<p>A pointer to the pfnDestroyPagingQueueCb function.</p>
</dd>

### -field <b>pfnMakeResidentCb</b>

<dd>
<p>A pointer to the pfnMakeResidentCb function.</p>
</dd>

### -field <b>pfnEvictCb</b>

<dd>
<p>A pointer to the pfnEvictCb function.</p>
</dd>

### -field <b>pfnReclaimAllocations2Cb</b>

<dd>
<p>A pointer to the pfnReclaimAllocations2Cb function.</p>
</dd>

### -field <b>pfnOfferAllocationsCb</b>

<dd>
<p>A pointer to the pfnOfferAllocationsCb function.</p>
</dd>

### -field <b>pfnAllocateCb</b>

<dd>
<p>A pointer to the <a href="..\d3d12umddi\nc-d3d12umddi-pfnd3d12ddi-allocate-cb-0022.md">pfnAllocateCb</a> function.</p>
</dd>

### -field <b>pfnDeallocateCb</b>

<dd>
<p>A pointer to the <a href="..\d3d12umddi\nc-d3d12umddi-pfnd3d12ddi-deallocate-cb-0022.md">pfnDeallocateCb</a> function.</p>
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
<dt>D3d12umddi.h (include D3d12umddi.h)</dt>
</dl>
</td>
</tr>
</table>