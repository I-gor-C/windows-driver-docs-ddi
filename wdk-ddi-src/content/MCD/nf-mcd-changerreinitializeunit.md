---
UID: NF.mcd.ChangerReinitializeUnit
title: ChangerReinitializeUnit
author: windows-driver-content
description: ChangerReinitializeUnit handles the device-specific aspects of a device-control IRP with the IOCTL code IOCTL_CHANGER_REINITIALIZE_TRANSPORT.
old-location: storage\changerreinitializeunit.htm
ms.assetid: 161156e3-0da0-458d-b623-67665b2a56c0
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
req.alt-api: ChangerReinitializeUnit
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
ms.keywords: ChangerReinitializeUnit
req.iface: 
---

# ChangerReinitializeUnit function



## -description
<p><b>ChangerReinitializeUnit</b> handles the device-specific aspects of a device-control IRP with the IOCTL code <a href="https://msdn.microsoft.com/library/windows/hardware/ff559419">IOCTL_CHANGER_REINITIALIZE_TRANSPORT</a>. </p>


## -syntax

````
NTSTATUS ChangerReinitializeUnit(
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
<p>If the changer supports recalibrating a transport element, <b>ChangerReinitializeUnit</b> returns the STATUS_<i>XXX</i> value returned by the system port driver, or one of the following values:
      </p>

<p>STATUS_SUCCESS</p>

<p>STATUS_INVALID_ELEMENT_ADDRESS</p>

<p>STATUS_INVALID_PARAMETER</p>

<p>STATUS_INSUFFICIENT_RESOURCES</p>

<p>If the changer does not support recalibrating a transport element, ChangerReinitializeUnit returns STATUS_INVALID_DEVICE_REQUEST.</p>

## -remarks
<p>This routine is required.</p>

<p><b>ChangerReinitializeUnit</b> causes the changer to recalibrate its transport element. Depending on the changer, this may return the transport to a "home" position. The changer class driver typically calls <b>ChangerReinitializeUnit</b> after the changer has been powered on or a calling application has initiated a recovery operation. The CHANGER_DEVICE_REINITIALIZE_CAPABLE flag in <b>Features0</b> of <a href="https://msdn.microsoft.com/library/windows/hardware/ff554979">GET_CHANGER_PARAMETERS</a> indicates whether the changer's transport supports recalibration in those circumstances.</p>

<p>The changer class driver checks the input buffer length in the I/O stack location before calling <b>ChangerReinitializeUnit</b>. <i>Irp</i><b>-&gt;SystemBuffer</b> points to a <a href="https://msdn.microsoft.com/library/windows/hardware/ff551457">CHANGER_ELEMENT</a> structure that indicates the element to recalibrate. </p>

<p><b>ChangerReinitializeUnit</b> builds an SRB with a CDB to position the transport element and sends it to the system port driver.</p>

<p><b>ChangerReinitializeUnit</b> sets the <b>Information</b> field in the I/O status block to <b>sizeof</b>(CHANGER_ELEMENT) before returning to the changer class driver.</p>

<p>This routine is required.</p>

<p><b>ChangerReinitializeUnit</b> causes the changer to recalibrate its transport element. Depending on the changer, this may return the transport to a "home" position. The changer class driver typically calls <b>ChangerReinitializeUnit</b> after the changer has been powered on or a calling application has initiated a recovery operation. The CHANGER_DEVICE_REINITIALIZE_CAPABLE flag in <b>Features0</b> of <a href="https://msdn.microsoft.com/library/windows/hardware/ff554979">GET_CHANGER_PARAMETERS</a> indicates whether the changer's transport supports recalibration in those circumstances.</p>

<p>The changer class driver checks the input buffer length in the I/O stack location before calling <b>ChangerReinitializeUnit</b>. <i>Irp</i><b>-&gt;SystemBuffer</b> points to a <a href="https://msdn.microsoft.com/library/windows/hardware/ff551457">CHANGER_ELEMENT</a> structure that indicates the element to recalibrate. </p>

<p><b>ChangerReinitializeUnit</b> builds an SRB with a CDB to position the transport element and sends it to the system port driver.</p>

<p><b>ChangerReinitializeUnit</b> sets the <b>Information</b> field in the I/O status block to <b>sizeof</b>(CHANGER_ELEMENT) before returning to the changer class driver.</p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff551457">CHANGER_ELEMENT</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff554979">GET_CHANGER_PARAMETERS</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/35b40514-a7a6-4860-a633-fe273ef21ba2">, IOCTL_CHANGER_REINITIALIZE_TRANSPORT</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [Storage\storage]:%20ChangerReinitializeUnit function%20 RELEASE:%20(10/24/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
