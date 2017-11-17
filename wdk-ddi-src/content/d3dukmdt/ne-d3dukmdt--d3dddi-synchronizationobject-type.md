---
UID: NE.d3dukmdt._D3DDDI_SYNCHRONIZATIONOBJECT_TYPE
title: D3DDDI_SYNCHRONIZATIONOBJECT_TYPE
author: windows-driver-content
description: The D3DDDI_SYNCHRONIZATIONOBJECT_TYPE enumeration indicates the type of synchronization object.
old-location: display\d3dddi_synchronizationobject_type.htm
ms.assetid: afd1aad4-d4cd-420f-bd3f-f171dc818a3e
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: enum
ms.prod: windows-hardware
ms.technology: display
req.header: d3dukmdt.h
req.include-header: D3dukmdt.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: D3DDDI_SYNCHRONIZATIONOBJECT_TYPE
req.alt-loc: d3dukmdt.h
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
ms.keywords: D3DKMT_PRESENT_MULTIPLANE_OVERLAY, D3DKMT_PRESENT_MULTIPLANE_OVERLAY
req.iface: 
---

# D3DDDI_SYNCHRONIZATIONOBJECT_TYPE enumeration



## -description
<p>The <b>D3DDDI_SYNCHRONIZATIONOBJECT_TYPE</b> enumeration indicates the type of synchronization object.</p>


## -syntax

````
typedef enum _D3DDDI_SYNCHRONIZATIONOBJECT_TYPE { 
  D3DDDI_SYNCHRONIZATION_MUTEX  = 1,
  D3DDDI_SEMAPHORE              = 2,
  D3DDDI_FENCE                  = 3,
  D3DDDI_CPU_NOTIFICATION       = 4,
#if ((DXGKDDI_INTERFACE_VERSION >= DXGKDDI_INTERFACE_VERSION_WDDM2_0) || \
     (D3D_UMD_INTERFACE_VERSION >= D3D_UMD_INTERFACE_VERSION_WDDM2_0))
  D3DDDI_MONITORED_FENCE        = 5,
#endif 
#if ((DXGKDDI_INTERFACE_VERSION >= DXGKDDI_INTERFACE_VERSION_WDDM2_0) || \
     (D3D_UMD_INTERFACE_VERSION >= D3D_UMD_INTERFACE_VERSION_WDDM2_0))
  D3DDDI_MONITORED_FENCE        = 6,
#endif 
  
} D3DDDI_SYNCHRONIZATIONOBJECT_TYPE;
````


## -enum-fields
<dl>

### -field <a id="D3DDDI_SYNCHRONIZATION_MUTEX"></a><a id="d3dddi_synchronization_mutex"></a><b>D3DDDI_SYNCHRONIZATION_MUTEX</b>

<dd>
<p>The synchronization object is a synchronization mutex.</p>
<p>Supported starting with Windows Vista.</p>
</dd>

### -field <a id="D3DDDI_SEMAPHORE"></a><a id="d3dddi_semaphore"></a><b>D3DDDI_SEMAPHORE</b>

<dd>
<p>The synchronization object is a semaphore.</p>
<p>Supported starting with Windows Vista.</p>
</dd>

### -field <a id="D3DDDI_FENCE"></a><a id="d3dddi_fence"></a><b>D3DDDI_FENCE</b>

<dd>
<p>The synchronization object is a fence. </p>
<p>Supported starting with Windows 7.</p>
</dd>

### -field <a id="D3DDDI_CPU_NOTIFICATION"></a><a id="d3dddi_cpu_notification"></a><b>D3DDDI_CPU_NOTIFICATION</b>

<dd>
<p>The synchronization object is a CPU notification.</p>
<p>Supported starting with Windows 7.</p>
</dd>

### -field <a id="D3DDDI_MONITORED_FENCE"></a><a id="d3dddi_monitored_fence"></a><b>D3DDDI_MONITORED_FENCE</b>

<dd>
<p>The synchronization object is a monitored fence.</p>
<p>Supported starting with Windows 10.</p>
</dd>

### -field <a id="D3DDDI_MONITORED_FENCE"></a><a id="d3dddi_monitored_fence"></a><b>D3DDDI_MONITORED_FENCE</b>

<dd>
<p>The synchronization object is a periodic monitored fence.</p>
<p>Supported starting with Windows 10.</p>
</dd>

### -field <a id=""></a><b></b>

<dd></dd>
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
<dt>D3dukmdt.h (include D3dukmdt.h)</dt>
</dl>
</td>
</tr>
</table>