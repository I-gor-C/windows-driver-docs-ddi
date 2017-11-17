---
UID: NS.d3dkmthk._D3DKMT_UPDATEGPUVIRTUALADDRESS
title: D3DKMT_UPDATEGPUVIRTUALADDRESS
author: windows-driver-content
description: D3DKMT_UPDATEGPUVIRTUALADDRESS is used with UpdateGpuVirtualAddress to allow the driver to specify a number of mapping operations to be applied to the process virtual address space in a single batch of page table updates.
old-location: display\d3dkmt_updategpuvirtualaddress.htm
ms.assetid: B6586406-6CAD-479F-AE41-93EFBA195B99
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: display
req.header: d3dkmthk.h
req.include-header: D3dkmthk.h
req.target-type: Windows
req.target-min-winverclnt: Windows 10
req.target-min-winversvr: Windows Server 2016
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: D3DKMT_UPDATEGPUVIRTUALADDRESS
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
ms.keywords: D3DKMT_UPDATEGPUVIRTUALADDRESS, D3DKMT_UPDATEGPUVIRTUALADDRESS
req.iface: 
---

# D3DKMT_UPDATEGPUVIRTUALADDRESS structure



## -description
<p><b>D3DKMT_UPDATEGPUVIRTUALADDRESS</b> is used with <a href="https://msdn.microsoft.com/3390A01D-BD4B-4399-AA3E-91BB32264A13">UpdateGpuVirtualAddress</a> to allow the driver to specify a number of mapping operations to be applied to the process virtual address space in a single batch of page table updates. 
</p>


## -syntax

````
typedef struct _D3DKMT_UPDATEGPUVIRTUALADDRESS {
  D3DKMT_HANDLE                            hDevice;
  D3DKMT_HANDLE                            hContext;
  D3DKMT_HANDLE                            hFenceObject;
  UINT                                     NumOperations;
  D3DDDI_UPDATEGPUVIRTUALADDRESS_OPERATION *Operations;
  UINT                                     Reserved0;
  UINT64                                   Reserved1;
  UINT64                                   FenceValue;
  union {
    struct {
      UINT DoNotWait  :1;
      UINT Reserved  :31;
    };
    UINT   Value;
  } Flags;
} D3DKMT_UPDATEGPUVIRTUALADDRESS;
````


## -struct-fields
<dl>

### -field <b>hDevice</b>

<dd>
<p>A handle to the device.</p>
</dd>

### -field <b>hContext</b>

<dd>
<p>A handle to a context that the map operation will be synchronized against. This also determines which kernel context the map operation will be executed against. In an linked display adapter (LDA) configuration <b>hContext</b> defines a physical GPU whose page tables are modified.</p>
</dd>

### -field <b>hFenceObject</b>

<dd>
<p>Specifies the monitored fence object to use for synchronization. This should typically be set to the monitored fence used by the user mode driver to track progress of <b>hContext</b>. </p>
</dd>

### -field <b>NumOperations</b>

<dd>
<p>Specifies the number of operations in the <b>Operations</b> array.</p>
</dd>

### -field <b>Operations</b>

<dd>
<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/dn906329">D3DDDI_UPDATEGPUVIRTUALADDRESS_OPERATION</a> array of operations to perform on the GPU virtual address space.</p>
</dd>

### -field <b>Reserved0</b>

<dd>
<p>This member is reserved and should be set to zero.</p>
</dd>

### -field <b>Reserved1</b>

<dd>
<p>This member is reserved and should be set to zero.</p>
</dd>

### -field <b>FenceValue</b>

<dd>
<p>Specifies the <b>FenceValue</b> for <b>hFenceObject</b> that the map operation should wait on (unless <b>DoNotWait</b> is 1). When the map operation completes, the fence object will signal <b>hFenceObject</b> with <b>FenceValue</b>+1.</p>
</dd>

### -field <b>Flags</b>

<dd>
<dl>

### -field <b>DoNotWait</b>

<dd>
<p>When set to 1, there will be no wait for the sync objects before executing the operations.</p>
</dd>

### -field <b>Reserved</b>

<dd>
<p>This member is reserved and should be set to zero.</p>
</dd>

### -field <b>Value</b>

<dd>
<p>The consolidated value of the <b>Flags</b> union.</p>
</dd>
</dl>
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
<dt>D3dkmthk.h (include D3dkmthk.h)</dt>
</dl>
</td>
</tr>
</table>