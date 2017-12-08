---
UID: NS.D3DKMTHK._D3DKMT_LOCK2
title: _D3DKMT_LOCK2
author: windows-driver-content
description: D3DKMT_LOCK2 describes parameters for locking an allocation.
old-location: display\d3dkmt_lock2.htm
old-project: display
ms.assetid: AFDA9D5F-2590-4034-B2CF-07990F4553C8
ms.author: windowsdriverdev
ms.date: 12/6/2017
ms.keywords: _D3DKMT_LOCK2, D3DKMT_LOCK2
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: d3dkmthk.h
req.include-header: D3dkmthk.h
req.target-type: Windows
req.target-min-winverclnt: Windows 10
req.target-min-winversvr: Windows Server 2016
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: D3DKMT_LOCK2
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
---

# _D3DKMT_LOCK2 structure



## -description
<b>D3DKMT_LOCK2</b> describes parameters for locking an allocation.


## -syntax

````
typedef struct _D3DKMT_LOCK2 {
  D3DKMT_HANDLE       hDevice;
  D3DKMT_HANDLE       hAllocation;
  D3DDDICB_LOCK2FLAGS Flags;
  PVOID               pData;
} D3DKMT_LOCK2;
````


## -struct-fields

### -field hDevice

The handle to the device.

### -field hAllocation

The handle to the allocation to lock.

### -field Flags

A set of flags to pass to the <a href="display.d3dkmtlock2">Lock2</a> kernel function which will determine how the allocation is locked. See <a href="display.d3dddicb_lock2flags">D3DDDICB_LOCK2FLAGS</a> for details.

### -field pData

A CPU virtual address pointing a valid memory location pointing to the CPU backing store or the GPU frame buffer.

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
Minimum supported client
</th>
<td width="70%">
Windows 10
</td>
</tr>
<tr>
<th width="30%">
Minimum supported server
</th>
<td width="70%">
Windows Server 2016
</td>
</tr>
<tr>
<th width="30%">
Header
</th>
<td width="70%">
<dl>
<dt>D3dkmthk.h (include D3dkmthk.h)</dt>
</dl>
</td>
</tr>
</table>