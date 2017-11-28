---
UID: NF.ks.KsForwardAndCatchIrp
title: KsForwardAndCatchIrp
author: windows-driver-content
description: The KsForwardAndCatchIrp function forwards an IRP to the specified driver after initializing the next stack location, and regains control of the IRP on completion from that driver.
old-location: stream\ksforwardandcatchirp.htm
old-project: stream
ms.assetid: 87a873c2-07d3-4f76-bc26-5fcae4b960e7
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: KsForwardAndCatchIrp
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: ks.h
req.include-header: Ks.h
req.target-type: Universal
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: KsForwardAndCatchIrp
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
req.iface: 
---

# KsForwardAndCatchIrp function



## -description
<p>The <b>KsForwardAndCatchIrp</b> function forwards an IRP to the specified driver after initializing the next stack location, and regains control of the IRP on completion from that driver. The function is used with devices that can be stacked and do not use file objects to communicate.</p>
<p>If a file object is being used, the caller must initialize the current stack location with that file object before calling the <b>KsForwardAndCatchIrp</b> function. The function verifies that there is a new stack location to copy into before attempting to do so. If there is not a new stack location, the function returns STATUS_INVALID_DEVICE_REQUEST. Regardless of whether a new stack location is present, the IRP is not completed.</p>


## -syntax

````
NTSTATUS KsForwardAndCatchIrp(
  _In_ PDEVICE_OBJECT DeviceObject ,
  _In_ PIRP           Irp ,
  _In_ PFILE_OBJECT   FileObject ,
  _In_ KSSTACK_USE    StackUse 
);
````


## -parameters
<dl>

### -param <i>DeviceObject </i> [in]

<dd>
<p>Specifies the device to forward the IRP to.</p>
</dd>

### -param <i>Irp </i> [in]

<dd>
<p>Specifies the IRP that is being forwarded to the specified driver.</p>
</dd>

### -param <i>FileObject </i> [in]

<dd>
<p>Specifies a file object value to copy to the next stack location. This can be <b>NULL</b> in order to set no file object, but the value is always copied to the next stack location. If the current file object is to be preserved, it must be passed in this parameter. </p>
</dd>

### -param <i>StackUse </i> [in]

<dd>
<p>Specifies a value enumerated by KSSTACK_USE. If the value is <i>KsStackCopyToNewLocation</i>, the parameters are copied to the next stack location. If the value is <i>KsStackReuseCurrentLocation</i>, the current stack location is reused when the IRP is forwarded and the stack location is returned to the current location. If the value is <i>KsStackUseNewLocation</i>, the new stack location is used as is.</p>
</dd>
</dl>

## -returns
<p>The <b>KsForwardAndCatchIrp</b> function returns the result of the <b>IoCallDriver</b>, or it returns an invalid status if no more stack depth is available.</p>

## -remarks
<p>The type KSSTACK_USE enumeration specifies how the IRP stack is used when forwarding the IRP to the next driver.</p>

<p>KsStackCopyToNewLocation</p>

<p>Indicates that the parameters are to be copied to the next stack location.</p>

<p>KsStackReuseCurrentLocation</p>

<p>Indicates that the current stack location is to be reused.</p>

<p>KsStackUseNewLocation</p>

<p>Indicates that the next stack location is to be used without modification.</p>

<p> </p>

<p>The type KSSTACK_USE enumeration specifies how the IRP stack is used when forwarding the IRP to the next driver.</p>

<p>KsStackCopyToNewLocation</p>

<p>Indicates that the parameters are to be copied to the next stack location.</p>

<p>KsStackReuseCurrentLocation</p>

<p>Indicates that the current stack location is to be reused.</p>

<p>KsStackUseNewLocation</p>

<p>Indicates that the next stack location is to be used without modification.</p>

<p> </p>

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
<dt>Ks.h (include Ks.h)</dt>
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