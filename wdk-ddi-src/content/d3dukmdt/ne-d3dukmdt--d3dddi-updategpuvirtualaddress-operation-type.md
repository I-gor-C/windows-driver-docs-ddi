---
UID: NE.d3dukmdt._D3DDDI_UPDATEGPUVIRTUALADDRESS_OPERATION_TYPE
title: D3DDDI_UPDATEGPUVIRTUALADDRESS_OPERATION_TYPE
author: windows-driver-content
description: D3DDDI_UPDATEGPUVIRTUALADDRESS_OPERATION_TYPE describes the details of the virtual address update operation being performed.
old-location: display\d3dddi_updategpuvirtualaddress_operation_type.htm
old-project: display
ms.assetid: 47B53DDA-E04B-4DA5-BEAB-8515B6683AE4
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: D3DKMT_PRESENT_MULTIPLANE_OVERLAY, D3DKMT_PRESENT_MULTIPLANE_OVERLAY
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: d3dukmdt.h
req.include-header: D3dumddi.h, D3dkmddi.h
req.target-type: Windows
req.target-min-winverclnt: Windows 10
req.target-min-winversvr: Windows Server 2016
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: D3DDDI_UPDATEGPUVIRTUALADDRESS_OPERATION_TYPE
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

# D3DDDI_UPDATEGPUVIRTUALADDRESS_OPERATION_TYPE enumeration



## -description
<p><b>D3DDDI_UPDATEGPUVIRTUALADDRESS_OPERATION_TYPE</b> describes the  details of the virtual address update operation being performed.
  </p>


## -syntax

````
typedef enum _D3DDDI_UPDATEGPUVIRTUALADDRESS_OPERATION_TYPE { 
  D3DDDI_UPDATEGPUVIRTUALADDRESS_MAP          = 0,
  D3DDDI_UPDATEGPUVIRTUALADDRESS_UNMAP        = 1,
  D3DDDI_UPDATEGPUVIRTUALADDRESS_COPY         = 2,
  D3DDDI_UPDATEGPUVIRTUALADDRESS_MAP_PROTECT  = 3
} D3DDDI_UPDATEGPUVIRTUALADDRESS_OPERATION_TYPE;
````


## -enum-fields
<dl>

### -field D3DDDI_UPDATEGPUVIRTUALADDRESS_MAP

<dd>
<p>Maps the given virtual address range to the given allocation range. The allocation does not have to be resident at the time of submission or at the time of mapping. The read-write protection is set to the pages. <b>DriverProtection</b> for the pages is set to zero.</p>
</dd>

### -field D3DDDI_UPDATEGPUVIRTUALADDRESS_UNMAP

<dd>
<p>Puts the specified virtual address range to the <i>zero</i> state or to the <i>invalid</i> state.</p>
</dd>

### -field D3DDDI_UPDATEGPUVIRTUALADDRESS_COPY

<dd>
<p>The <i>copy</i> operation copies all mappings from source GPU virtual address range to the destination range. The source and destination ranges are allowed to intersect. Both ranges must belong to a reserved (zero) virtual address range.</p>
</dd>

### -field D3DDDI_UPDATEGPUVIRTUALADDRESS_MAP_PROTECT

<dd>
<p>Maps the given virtual address range to the given allocation range. The allocation does not have to be resident at the time of submission or at the time of mapping. The page protection is specified in the operation.</p>
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