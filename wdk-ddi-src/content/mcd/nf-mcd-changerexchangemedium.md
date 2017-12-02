---
UID: NF.mcd.ChangerExchangeMedium
title: ChangerExchangeMedium
author: windows-driver-content
description: ChangerExchangeMedium handles the device-specific aspects of a device-control IRP with the IOCTL code IOCTL_CHANGER_EXCHANGE_MEDIUM.
old-location: storage\changerexchangemedium.htm
old-project: storage
ms.assetid: 4cb6e9af-ddd0-48d9-9f07-43c828e4187b
ms.author: windowsdriverdev
ms.date: 11/15/2017
ms.keywords: ChangerExchangeMedium
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
req.alt-api: ChangerExchangeMedium
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

# ChangerExchangeMedium function



## -description
<p><b>ChangerExchangeMedium</b> handles the device-specific aspects of a device-control IRP with the IOCTL code <a href="..\ntddchgr\ni-ntddchgr-ioctl-changer-exchange-medium.md">IOCTL_CHANGER_EXCHANGE_MEDIUM</a>. </p>


## -syntax

````
NTSTATUS ChangerExchangeMedium(
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
<p>If the changer supports exchanging media, <b>ChangerExchangeMedium</b> returns the status returned by the system port driver, or one of the following values:
      </p>

<p>STATUS_SUCCESS</p>

<p>STATUS_DESTINATION_ELEMENT_FULL</p>

<p>STATUS_INVALID_ELEMENT_ADDRESS</p>

<p>STATUS_SOURCE_ELEMENT_EMPTY</p>

<p>If the changer does not support exchanging media, ChangerExchangeMedium returns STATUS_INVALID_DEVICE_REQUEST.</p>

## -remarks
<p>This routine is required.</p>

<p><b>ChangerExchangeMedium</b> moves a piece of media from a source element to one destination and from that destination to another destination. The source and second destination are often the same, resulting in a simple exchange of media.</p>

<p>The CHANGER_EXCHANGE_MEDIA flag in <b>Features0</b> of the <a href="..\ntddchgr\ns-ntddchgr--get-changer-parameters.md">GET_CHANGER_PARAMETERS</a> structure indicates whether the changer supports this functionality. A changer that supports exchanging media typically has two picker mechanisms on a single transport element, or at least two transport elements. A changer that has a single picker mechanism might support exchanging medium through emulation of the command. </p>

<p>The changer class driver checks the input buffer length in the I/O stack location before calling a miniclass driver's <b>ChangerExchangeMedium</b> routine. <i>Irp</i><b>-&gt;SystemBuffer</b> points to a <a href="..\ntddchgr\ns-ntddchgr--changer-exchange-medium.md">CHANGER_EXCHANGE_MEDIUM</a> structure as an input parameter that indicates the transport element and the destination to set. </p>

<p><b>ChangerExchangeMedium</b> first verifies that the transport, source, and destination element addresses are valid, then converts zero-based element addresses to device-specific element addresses. It then builds an SRB with a CDB to exchange the media and sends it to the system port driver. </p>

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
<a href="..\mcd\nf-mcd-changermovemedium.md">ChangerMoveMedium</a>
</dt>
<dt>
<a href="..\ntddchgr\ns-ntddchgr--get-changer-parameters.md">GET_CHANGER_PARAMETERS</a>
</dt>
<dt>
<a href="..\ntddchgr\ns-ntddchgr--changer-exchange-medium.md">CHANGER_EXCHANGE_MEDIUM</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [storage\storage]:%20ChangerExchangeMedium function%20 RELEASE:%20(11/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
