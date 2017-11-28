---
UID: NS.d3dukmdt._D3DDDI_WAITFORSYNCHRONIZATIONOBJECTFROMCPU_FLAGS
title: D3DDDI_WAITFORSYNCHRONIZATIONOBJECTFROMCPU_FLAGS
author: windows-driver-content
description: D3DDDI_WAITFORSYNCHRONIZATIONOBJECTFROMCPU_FLAGS describes the type of input synchronization objects to wait for.
old-location: display\d3dddi_waitforsynchronizationobjectfromcpu_flags.htm
old-project: display
ms.assetid: 2283D20F-D256-48E5-BFD2-D3ACACD7BF1C
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: D3DDDI_WAITFORSYNCHRONIZATIONOBJECTFROMCPU_FLAGS, D3DDDI_WAITFORSYNCHRONIZATIONOBJECTFROMCPU_FLAGS
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: d3dukmdt.h
req.include-header: D3dumddi.h, D3dkmddi.h
req.target-type: Windows
req.target-min-winverclnt: Windows 10
req.target-min-winversvr: Windows Server 2016
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: D3DDDI_WAITFORSYNCHRONIZATIONOBJECTFROMCPU_FLAGS
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
req.iface: 
---

# D3DDDI_WAITFORSYNCHRONIZATIONOBJECTFROMCPU_FLAGS structure



## -description
<p><b>D3DDDI_WAITFORSYNCHRONIZATIONOBJECTFROMCPU_FLAGS</b> describes the type of input synchronization objects to wait for.</p>


## -syntax

````
typedef struct _D3DDDI_WAITFORSYNCHRONIZATIONOBJECTFROMCPU_FLAGS {
  union {
    struct {
      UINT WaitAny  :1;
      UINT Reserved  :31;
    };
    UINT Value;
  };
} D3DDDI_WAITFORSYNCHRONIZATIONOBJECTFROMCPU_FLAGS;
````


## -struct-fields
<dl>

### -field <b>WaitAny</b>

<dd>
<table>
<tr>
<th>Value</th>
<th>Meaning</th>
</tr>
<tr>
<td width="40%">
<dl>

### -field 0 (FALSE)

</dl>
</td>
<td width="60%">
<p>[in] The wait condition is considered to be satisfied when all input synchronization objects are signaled to the corresponding input fence values or greater.</p>
</td>
</tr>
<tr>
<td width="40%">
<dl>

### -field 1 (TRUE)

</dl>
</td>
<td width="60%">
<p>[in] The wait condition is considered to be satisfied when any of the input synchronization objects is signaled to the corresponding input fence value or greater. 
</p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -field <b>Reserved</b>

<dd>
<p>This member is reserved and should be set to zero.</p>
</dd>

### -field <b>Value</b>

<dd>
<p>The consolidated value of the bitfields in the nested structure.</p>
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
<dt>D3dukmdt.h (include D3dumddi.h or D3dkmddi.h)</dt>
</dl>
</td>
</tr>
</table>