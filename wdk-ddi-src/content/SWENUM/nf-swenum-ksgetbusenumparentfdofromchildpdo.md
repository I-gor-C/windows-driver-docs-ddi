---
UID: NF.swenum.KsGetBusEnumParentFDOFromChildPDO
title: KsGetBusEnumParentFDOFromChildPDO
author: windows-driver-content
description: The KsGetBusEnumParentFDOFromChildPDO function retrieves the FDO of the parent of the given child PDO.
old-location: stream\ksgetbusenumparentfdofromchildpdo.htm
ms.assetid: 5d860c5c-e29e-4ea2-b6f7-bcaab0d4584d
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: stream
req.header: swenum.h
req.include-header: Swenum.h
req.target-type: Universal
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: KsGetBusEnumParentFDOFromChildPDO
req.alt-loc: Ks.lib,Ks.dll
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Ks.lib
req.dll: 
req.irql: 
ms.keywords: KsGetBusEnumParentFDOFromChildPDO
req.iface: 
req.product: Windows 10 or later.
---

# KsGetBusEnumParentFDOFromChildPDO function



## -description
<p><i>This function is intended for internal use only.</i></p>
<p>The <b>KsGetBusEnumParentFDOFromChildPDO </b>function retrieves the FDO of the parent of the given child PDO. </p>


## -syntax

````
NTSTATUS KsGetBusEnumParentFDOFromChildPDO(
  _In_  PDEVICE_OBJECT DeviceObject,
  _Out_ PDEVICE_OBJECT *FunctionalDeviceObject
);
````


## -parameters
<dl>

### -param <i>DeviceObject</i> [in]

<dd>
<p>Pointer to the child's PDO.</p>
</dd>

### -param <i>FunctionalDeviceObject</i> [out]

<dd>
<p>Pointer to the device object to receive the parent's FDO.</p>
</dd>
</dl>

## -returns
<p>Returns STATUS_SUCCESS if successful, or STATUS_INVALID_PARAMETER if <i>DeviceObject</i> does not contain a device extension, or if the device extension specified in <i>DeviceObject </i>is not that of a PDO.</p>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Target platform</p>
</th>
<td width="70%">
<dl>
<dt><a href="http://go.microsoft.com/fwlink/p/?linkid=531356" target="_blank">Universal</a></dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Swenum.h (include Swenum.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Library</p>
</th>
<td width="70%">
<dl>
<dt>Ks.lib</dt>
</dl>
</td>
</tr>
</table>