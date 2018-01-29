---
UID : NC:d3dumddi.PFND3DDDI_UPDATEALLOCATIONPROPERTYCB
title : PFND3DDDI_UPDATEALLOCATIONPROPERTYCB
author : windows-driver-content
description : The pfnUpdateAllocationPropertyCb functions updates the property of an allocation without creating a new allocation.
old-location : display\pfnupdateallocationpropertycb.htm
old-project : display
ms.assetid : 49E4189A-2183-4033-BF17-ADFAC1CF1EF2
ms.author : windowsdriverdev
ms.date : 12/29/2017
ms.keywords : display.pfnupdateallocationpropertycb, pfnUpdateAllocationPropertyCb callback function [Display Devices], pfnUpdateAllocationPropertyCb, PFND3DDDI_UPDATEALLOCATIONPROPERTYCB, PFND3DDDI_UPDATEALLOCATIONPROPERTYCB, d3dumddi/pfnUpdateAllocationPropertyCb
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : callback
req.header : d3dumddi.h
req.include-header : TBD
req.target-type : Windows
req.target-min-winverclnt : 
req.target-min-winversvr : 
req.kmdf-ver : 
req.umdf-ver : 
req.ddi-compliance : 
req.unicode-ansi : 
req.idl : 
req.max-support : 
req.namespace : 
req.assembly : 
req.type-library : 
req.lib : 
req.dll : 
req.irql : 
topictype : 
apitype : 
apilocation : 
apiname : 
product : Windows
targetos : Windows
req.typenames : DXGK_PTE
---


# PFND3DDDI_UPDATEALLOCATIONPROPERTYCB callback function
The <b>pfnUpdateAllocationPropertyCb</b> functions updates the property of an allocation without creating a new allocation.

## Syntax

```
PFND3DDDI_UPDATEALLOCATIONPROPERTYCB Pfnd3dddiUpdateallocationpropertycb;

HRESULT Pfnd3dddiUpdateallocationpropertycb(
  HANDLE hDevice,
  D3DDDI_UPDATEALLOCPROPERTY *
)
{...}
```

## Parameters

`hDevice`

A handle to the display device associated with the allocation

`*`




## Return Value

<b>pfnUpdateAllocationPropertyCb</b> returns one of the following values:
<table>
<tr>
<th>Return code</th>
<th>Description</th>
</tr>
<tr>
<td width="40%">
<dl>
<dt><b>STATUS_SUCCESS</b></dt>
</dl>
</td>
<td width="60%">
The properties were successfully updated. The driver can start using the allocation with its new property immediately. PagingFenceValue is invalid, though the driver shouldn't wait on it.

</td>
</tr>
<tr>
<td width="40%">
<dl>
<dt><b>STATUS_PENDING</b></dt>
</dl>
</td>
<td width="60%">
The request has successfully been queued to VidMm and is being processed. The driver must synchronize against the returned PagingFenceValue before using the allocation with its new property. Note that if the driver request is invalid it may still fail at a later point, in which case the device will be put in error.

</td>
</tr>
<tr>
<td width="40%">
<dl>
<dt><b>E_INVALIDARG</b></dt>
</dl>
</td>
<td width="60%">
Invalid call with bad arguments provided.

</td>
</tr>
<tr>
<td width="40%">
<dl>
<dt><b>E_OUTOFMEMORY</b></dt>
</dl>
</td>
<td width="60%">
Desired supported memory segment is full.

</td>
</tr>
<tr>
<td width="40%">
<dl>
<dt><b>E_FAIL</b></dt>
</dl>
</td>
<td width="60%">
An unknown error has occurred. 

</td>
</tr>
</table>


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Target platform** | Windows |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | d3dumddi.h (include TBD) |
| **Library** |  |
| **IRQL** |  |
| **DDI compliance rules** |  |