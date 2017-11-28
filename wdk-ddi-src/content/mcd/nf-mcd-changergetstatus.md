---
UID: NF.mcd.ChangerGetStatus
title: ChangerGetStatus
author: windows-driver-content
description: ChangerGetStatus handles the device-specific aspects of a device-control IRP with the IOCTL code IOCTL_CHANGER_GET_STATUS.
old-location: storage\changergetstatus.htm
old-project: storage
ms.assetid: f5719dfa-e48a-4f81-8344-31b349fadb48
ms.author: windowsdriverdev
ms.date: 11/15/2017
ms.keywords: ChangerGetStatus
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: mcd.h
req.include-header: Mcd.h, Ntddchgr.h
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: ChangerGetStatus
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
req.iface: 
---

# ChangerGetStatus function



## -description
<p><b>ChangerGetStatus</b> handles the device-specific aspects of a device-control IRP with the IOCTL code <a href="https://msdn.microsoft.com/library/windows/hardware/ff559405">IOCTL_CHANGER_GET_STATUS</a>. </p>


## -syntax

````
NTSTATUS ChangerGetStatus(
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
<p><b>ChangerGetStatus</b> returns the STATUS_<i>XXX</i> value returned by the system port driver. If there is not enough memory to process the request or to process the STATUS_<i>XXX</i> value returned by the system port driver <b>ChangerGetStatus</b> returns STATUS_INSUFFICIENT_RESOURCES.</p>

## -remarks
<p>This routine is required.</p>

<p><b>ChangerGetStatus</b> indicates whether the changer is able to accept requests. </p>

<p><b>ChangerGetStatus</b> builds an SRB with a CDB to get the changer's status (using the SCSI command TEST UNIT READY or non-SCSI equivalent) and sends it to the system port driver to obtain status of the changer.</p>

<p>This routine is required.</p>

<p><b>ChangerGetStatus</b> indicates whether the changer is able to accept requests. </p>

<p><b>ChangerGetStatus</b> builds an SRB with a CDB to get the changer's status (using the SCSI command TEST UNIT READY or non-SCSI equivalent) and sends it to the system port driver to obtain status of the changer.</p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff551424">ChangerGetElementStatus</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff559405">IOCTL_CHANGER_GET_STATUS</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [storage\storage]:%20ChangerGetStatus function%20 RELEASE:%20(11/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
