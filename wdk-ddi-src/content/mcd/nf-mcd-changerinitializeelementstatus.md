---
UID: NF.mcd.ChangerInitializeElementStatus
title: ChangerInitializeElementStatus
author: windows-driver-content
description: ChangerInitializeElementStatus handles the device-specific aspects of a device-control IRP with the IOCTL code IOCTL_CHANGER_INITIALIZE_ELEMENT_STATUS.
old-location: storage\changerinitializeelementstatus.htm
old-project: storage
ms.assetid: 1f8f13e0-b0d3-4c94-bd1f-0e42bb75142d
ms.author: windowsdriverdev
ms.date: 11/15/2017
ms.keywords: ChangerInitializeElementStatus
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
req.alt-api: ChangerInitializeElementStatus
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

# ChangerInitializeElementStatus function



## -description
<p><b>ChangerInitializeElementStatus</b> handles the device-specific aspects of a device-control IRP with the IOCTL code <a href="https://msdn.microsoft.com/library/windows/hardware/ff559409">IOCTL_CHANGER_INITIALIZE_ELEMENT_STATUS</a>.</p>


## -syntax

````
NTSTATUS ChangerInitializeElementStatus(
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
<p><b>ChangerInitializeElementStatus</b> returns the status returned by the system port driver or one of the following values:
      </p>

<p>STATUS_SUCCESS</p>

<p>STATUS_INVALID_PARAMETER</p>

<p>STATUS_INSUFFICIENT_RESOURCES</p>

<p>If the changer does not support initializing a range of elements of a particular type and ChangerInitializeElementStatus is called with an element type other than AllElements, it returns STATUS_INVALID_PARAMETER.</p>

## -remarks
<p>This routine is required.</p>

<p><b>ChangerInitializeElementStatus</b> updates the changer's internal memory with current information about its elements.</p>

<p>The changer class driver checks the input buffer length in the I/O stack location before calling <b>ChangerInitializeElementStatus</b>.</p>

<p><i>Irp</i><b>-&gt;SystemBuffer</b> points to a <a href="https://msdn.microsoft.com/library/windows/hardware/ff551468">CHANGER_INITIALIZE_ELEMENT_STATUS</a> structure as an input parameter that indicates the elements for which to initialize status and whether to initialize element status with data obtained from bar code labels. </p>

<p>For a SCSI changer, <b>ChangerInitializeElementStatus</b> builds an SRB with a CDB to initialize element status, translates zero-based element addresses to device-specific addresses, and sends the SRB to the system port driver. </p>

<p><b>ChangerInitializeElementStatus</b> sets the <b>Information</b> field in the I/O status block to <b>sizeof</b>(CHANGER_INITIALIZE_ELEMENT_STATUS) before returning to the changer class driver.</p>

<p>This routine is required.</p>

<p><b>ChangerInitializeElementStatus</b> updates the changer's internal memory with current information about its elements.</p>

<p>The changer class driver checks the input buffer length in the I/O stack location before calling <b>ChangerInitializeElementStatus</b>.</p>

<p><i>Irp</i><b>-&gt;SystemBuffer</b> points to a <a href="https://msdn.microsoft.com/library/windows/hardware/ff551468">CHANGER_INITIALIZE_ELEMENT_STATUS</a> structure as an input parameter that indicates the elements for which to initialize status and whether to initialize element status with data obtained from bar code labels. </p>

<p>For a SCSI changer, <b>ChangerInitializeElementStatus</b> builds an SRB with a CDB to initialize element status, translates zero-based element addresses to device-specific addresses, and sends the SRB to the system port driver. </p>

<p><b>ChangerInitializeElementStatus</b> sets the <b>Information</b> field in the I/O status block to <b>sizeof</b>(CHANGER_INITIALIZE_ELEMENT_STATUS) before returning to the changer class driver.</p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff551459">CHANGER_ELEMENT_LIST</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff551468">CHANGER_INITIALIZE_ELEMENT_STATUS</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [storage\storage]:%20ChangerInitializeElementStatus function%20 RELEASE:%20(11/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
