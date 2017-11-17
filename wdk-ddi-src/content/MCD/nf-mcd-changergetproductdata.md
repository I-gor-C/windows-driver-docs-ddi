---
UID: NF.mcd.ChangerGetProductData
title: ChangerGetProductData
author: windows-driver-content
description: ChangerGetProductData handles the device-specific aspects of a device-control IRP with the IOCTL code IOCTL_CHANGER_GET_PRODUCT_DATA.
old-location: storage\changergetproductdata.htm
ms.assetid: b2723a34-d9c2-40c9-b6c9-6441ead63d2e
ms.author: windowsdriverdev
ms.date: 10/24/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: Storage
req.header: mcd.h
req.include-header: Mcd.h, Ntddchgr.h
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: ChangerGetProductData
req.alt-loc: mcd.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: PASSIVE_LEVEL
ms.keywords: ChangerGetProductData
req.iface: 
---

# ChangerGetProductData function



## -description
<p><b>ChangerGetProductData</b> handles the device-specific aspects of a device-control IRP with the IOCTL code IOCTL_CHANGER_GET_PRODUCT_DATA. </p>


## -syntax

````
NTSTATUS ChangerGetProductData(
  _In_ PDEVICE_OBJECT DeviceObject,
  _In_ PIRP           Irp
);
````


## -parameters
<dl>

### -param <i>DeviceObject</i> [in]

<dd>
<p>Pointer to the device object that represents the changer. </p>
</dd>

### -param <i>Irp</i> [in]

<dd>
<p>Pointer to the IRP. </p>
</dd>
</dl>

## -returns
<p><b>ChangerGetProductData</b> always returns STATUS_SUCCESS.</p>

## -remarks
<p>This routine is required.</p>

<p><b>ChangerGetProductData</b> returns product data for a changer.</p>

<p>The changer class driver checks the output buffer length in the I/O stack location before calling <b>ChangerGetProductData</b>. If output buffer length is smaller than <b>sizeof</b>(CHANGER_PRODUCT_DATA) then the changer class driver returns with a value of STATUS_INFO_LENGTH_MISMATCH</p>

<p><b>ChangerGetProductData</b> fills in a <a href="https://msdn.microsoft.com/library/windows/hardware/ff551475">CHANGER_PRODUCT_DATA</a> structure at <i>Irp</i><b>-&gt;AssociatedIrp.SystemBuffer</b> before returning to the changer class driver. If the miniclass driver cached inquiry data in the changer's device extension before returning from <b>ChangerInitialize</b>, all members except <b>DeviceType</b> can be filled in from this data. </p>

<p>This routine is required.</p>

<p><b>ChangerGetProductData</b> returns product data for a changer.</p>

<p>The changer class driver checks the output buffer length in the I/O stack location before calling <b>ChangerGetProductData</b>. If output buffer length is smaller than <b>sizeof</b>(CHANGER_PRODUCT_DATA) then the changer class driver returns with a value of STATUS_INFO_LENGTH_MISMATCH</p>

<p><b>ChangerGetProductData</b> fills in a <a href="https://msdn.microsoft.com/library/windows/hardware/ff551475">CHANGER_PRODUCT_DATA</a> structure at <i>Irp</i><b>-&gt;AssociatedIrp.SystemBuffer</b> before returning to the changer class driver. If the miniclass driver cached inquiry data in the changer's device extension before returning from <b>ChangerInitialize</b>, all members except <b>DeviceType</b> can be filled in from this data. </p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Target platform</p>
</th>
<td width="70%">
<dl>
<dt>Desktop</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Mcd.h (include Mcd.h or Ntddchgr.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>IRQL</p>
</th>
<td width="70%">
<p>PASSIVE_LEVEL</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff551431">ChangerInitialize</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff551475">CHANGER_PRODUCT_DATA</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [Storage\storage]:%20ChangerGetProductData function%20 RELEASE:%20(10/24/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
