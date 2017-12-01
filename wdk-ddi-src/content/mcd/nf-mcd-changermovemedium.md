---
UID: NF.mcd.ChangerMoveMedium
title: ChangerMoveMedium
author: windows-driver-content
description: ChangerMoveMedium handles the device-specific aspects of a device-control IRP with the IOCTL code IOCTL_CHANGER_MOVE_MEDIUM.
old-location: storage\changermovemedium.htm
old-project: storage
ms.assetid: 7532c8b5-e77b-4fd0-bac2-78254f6eb9f6
ms.author: windowsdriverdev
ms.date: 11/15/2017
ms.keywords: ChangerMoveMedium
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
req.alt-api: ChangerMoveMedium
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

# ChangerMoveMedium function



## -description
<p><b>ChangerMoveMedium</b> handles the device-specific aspects of a device-control IRP with the IOCTL code <a href="..\ntddchgr\ni-ntddchgr-ioctl-changer-move-medium.md">IOCTL_CHANGER_MOVE_MEDIUM</a>. </p>


## -syntax

````
NTSTATUS ChangerMoveMedium(
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
<p><b>ChangerMoveMedium</b> returns the status returned by the system port driver, or one of the following values:
      </p>

<p>STATUS_SUCCESS</p>

<p>STATUS_DESTINATION_ELEMENT_FULL</p>

<p>STATUS_INVALID_ELEMENT_ADDRESS</p>

<p>STATUS_INVALID_DEVICE_REQUEST</p>

<p>STATUS_INVALID_PARAMETER</p>

<p>STATUS_INSUFFICIENT_RESOURCES</p>

<p>STATUS_SOURCE_ELEMENT_EMPTY</p>

## -remarks
<p>This routine is required.</p>

<p><b>ChangerMoveMedium</b> moves a piece of media from one element to another.</p>

<p>The changer class driver checks the input buffer length in the I/O stack location before calling <b>ChangerMoveMedium</b>. <i>Irp</i><b>-&gt;SystemBuffer </b>points to a <a href="..\ntddchgr\ns-ntddchgr--changer-move-medium.md">CHANGER_MOVE_MEDIUM</a> structure that indicates the transport element, the source, the destination, and whether to flip the medium. </p>

<p><b>ChangerMoveMedium</b> first verifies that the transport, source, and destination element addresses are valid and then converts zero-based element addresses to device-specific addresses. It then builds an SRB with a CDB to move the piece of media and sends it to the system port driver.</p>

<p><b>ChangerMoveMedium</b> sets the <b>Information</b> field in the I/O status block to <b>sizeof</b>(CHANGER_MOVE_MEDIUM) before returning to the changer class driver. </p>

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
<a href="..\mcd\nf-mcd-changerexchangemedium.md">ChangerExchangeMedium</a>
</dt>
<dt>
<a href="..\ntddchgr\ns-ntddchgr--changer-move-medium.md">CHANGER_MOVE_MEDIUM</a>
</dt>
<dt>
<a href="..\ntddchgr\ni-ntddchgr-ioctl-changer-move-medium.md">,</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [storage\storage]:%20ChangerMoveMedium function%20 RELEASE:%20(11/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
