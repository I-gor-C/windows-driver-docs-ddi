---
UID: NF.mcd.ChangerQueryVolumeTags
title: ChangerQueryVolumeTags
author: windows-driver-content
description: ChangerQueryVolumeTags handles the device-specific aspects of a device-control IRP with the IOCTL code of IOCTL_CHANGER_QUERY_VOLUME_TAGS.
old-location: storage\changerqueryvolumetags.htm
old-project: storage
ms.assetid: 65579299-829c-48e2-b2f6-dc1a09578e9a
ms.author: windowsdriverdev
ms.date: 11/15/2017
ms.keywords: ChangerQueryVolumeTags
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
req.alt-api: ChangerQueryVolumeTags
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

# ChangerQueryVolumeTags function



## -description
<p><b>ChangerQueryVolumeTags</b> handles the device-specific aspects of a device-control IRP with the IOCTL code of <a href="..\ntddchgr\ni-ntddchgr-ioctl-changer-query-volume-tags.md">IOCTL_CHANGER_QUERY_VOLUME_TAGS</a>. </p>


## -syntax

````
NTSTATUS ChangerQueryVolumeTags(
  _In_ PDEVICE_OBJECT DeviceObject,
  _In_ PIRP           Irp
);
````


## -parameters
<dl>

### -param DeviceObject [in]

<dd>
<p>Pointer to the device object that represents the changer. </p>
</dd>

### -param Irp [in]

<dd>
<p>Pointer to the IRP. </p>
</dd>
</dl>

## -returns
<p>If the changer supports retrieval of volume tag information, <b>ChangerQueryVolumeTags</b> returns the STATUS_<i>XXX</i> value returned by the system port driver, or one of the following values:
      </p>

<p>STATUS_SUCCESS</p>

<p>STATUS_INVALID_ELEMENT_ADDRESS</p>

<p>STATUS_INSUFFICIENT_RESOURCES</p>

<p>If the changer does not support retrieval of volume tag information, ChangerQueryVolumeTags returns STATUS_INVALID_DEVICE_REQUEST.</p>

## -remarks
<p>This routine combines the functionality of two SCSI commands: SEND VOLUME TAGS and REQUEST VOLUME ELEMENT ADDRESS. This routine is required.</p>

<p><b>ChangerQueryVolumeTags</b> retrieves volume tag information for specified elements. It can also be used to define or clear volume tag information if the changer supports these operations. The CHANGER_VOLUME_IDENTIFICATION flag in the <b>Features0</b> member of the <a href="..\ntddchgr\ns-ntddchgr--get-changer-parameters.md">GET_CHANGER_PARAMETERS</a> structure indicates whether the changer supports this functionality.</p>

<p>The changer class driver checks the input and output buffer lengths in the I/O stack location before calling <b>ChangerQueryVolumeTags</b>. <i>Irp</i><b>-&gt;SystemBuffer</b> points to a <a href="..\ntddchgr\ns-ntddchgr--changer-send-volume-tag-information.md">CHANGER_SEND_VOLUME_TAG_INFORMATION</a> structure that indicates the elements, the operation to perform, and a template that specifies the volume ID to search for or to set. </p>

<p><b>ChangerQueryVolumeTags</b> first checks the action code for unsupported operations, and returns STATUS_INVALID_DEVICE_REQUEST for those it does not support. Next, it builds an SRB with a CDB to indicate the device-specific address of the starting element and sends it to the system port driver, passing the volume ID template as a parameter. (For a SCSI changer, the miniclass driver uses the SCSI command SEND VOLUME TAG.)</p>

<p>If the first SRB succeeds, <b>ChangerQueryVolumeTags</b> builds a second SRB with a CDB to transfer the results of the previous SRB. (For a SCSI changer, the miniclass driver uses the SCSI command REQUEST VOLUME ELEMENT ADDRESS.)</p>

<p><b>ChangerQueryVolumeTags</b> then fills in a <a href="..\ntddchgr\ns-ntddchgr--read-element-address-info.md">READ_ELEMENT_ADDRESS_INFO</a> structure at <i>Irp</i><b>-&gt;AssociatedIrp.SystemBuffer</b> that indicates the number of elements for which volume tag information was transferred, and the information for each element. </p>

<p>After filling in the system buffer, <b>ChangerQueryVolumeTags</b> sets the <b>Information</b> field in the I/O status block to the number of bytes written to the buffer before returning to the changer class driver.</p>

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
<a href="..\ntddchgr\ns-ntddchgr--changer-element.md">CHANGER_ELEMENT</a>
</dt>
<dt>
<a href="..\ntddchgr\ns-ntddchgr--changer-element-status.md">CHANGER_ELEMENT_STATUS</a>
</dt>
<dt>
<a href="..\mcd\nf-mcd-changergetelementstatus.md">ChangerGetElementStatus</a>
</dt>
<dt>
<a href="..\ntddchgr\ns-ntddchgr--read-element-address-info.md">READ_ELEMENT_ADDRESS_INFO</a>
</dt>
<dt>
<a href="..\ntddchgr\ns-ntddchgr--get-changer-parameters.md">, GET_CHANGER_PARAMETERS</a>
</dt>
<dt>
<a href="..\ntddchgr\ns-ntddchgr--changer-send-volume-tag-information.md">CHANGER_SEND_VOLUME_TAG_INFORMATION</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [storage\storage]:%20ChangerQueryVolumeTags function%20 RELEASE:%20(11/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
