---
UID: NS.D3DUKMDT._D3DDDI_WAITFORSYNCHRONIZATIONOBJECTFROMCPU_FLAGS
title: _D3DDDI_WAITFORSYNCHRONIZATIONOBJECTFROMCPU_FLAGS
author: windows-driver-content
description: D3DDDI_WAITFORSYNCHRONIZATIONOBJECTFROMCPU_FLAGS describes the type of input synchronization objects to wait for.
old-location: display\d3dddi_waitforsynchronizationobjectfromcpu_flags.htm
old-project: display
ms.assetid: 2283D20F-D256-48E5-BFD2-D3ACACD7BF1C
ms.author: windowsdriverdev
ms.date: 12/15/2017
ms.keywords: _D3DDDI_WAITFORSYNCHRONIZATIONOBJECTFROMCPU_FLAGS, D3DDDI_WAITFORSYNCHRONIZATIONOBJECTFROMCPU_FLAGS
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
---

# _D3DDDI_WAITFORSYNCHRONIZATIONOBJECTFROMCPU_FLAGS structure



## -description
<b>D3DDDI_WAITFORSYNCHRONIZATIONOBJECTFROMCPU_FLAGS</b> describes the type of input synchronization objects to wait for.



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

### -field WaitAny

<table>
<tr>
<th>Value</th>
<th>Meaning</th>
</tr>
<tr>
<td width="40%">

### -field 0 (FALSE)

</td>
<td width="60%">
[in] The wait condition is considered to be satisfied when all input synchronization objects are signaled to the corresponding input fence values or greater.

</td>
</tr>
<tr>
<td width="40%">

### -field 1 (TRUE)

</td>
<td width="60%">
[in] The wait condition is considered to be satisfied when any of the input synchronization objects is signaled to the corresponding input fence value or greater. 


</td>
</tr>
</table>
 


### -field Reserved

This member is reserved and should be set to zero.


### -field Value

The consolidated value of the bitfields in the nested structure.


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
<dt>D3dukmdt.h (include D3dumddi.h or D3dkmddi.h)</dt>
</dl>
</td>
</tr>
</table>