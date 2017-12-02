---
UID: NS.usb._URB_ISOCH_TRANSFER
title: URB_ISOCH_TRANSFER
author: windows-driver-content
description: The _URB_ISOCH_TRANSFER structure is used by USB client drivers to send data to or retrieve data from an isochronous transfer pipe.
old-location: buses\_urb_isoch_transfer.htm
old-project: usbref
ms.assetid: b021211a-3f72-47ff-9e69-bbf3807f4ec4
ms.author: windowsdriverdev
ms.date: 11/20/2017
ms.keywords: URB_ISOCH_TRANSFER,
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: usb.h
req.include-header: Usb.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: _URB_ISOCH_TRANSFER
req.alt-loc: usb.h
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
req.product: Windows 10 or later.
---

# URB_ISOCH_TRANSFER structure



## -description
<p>The <b>_URB_ISOCH_TRANSFER</b> structure is used by USB client drivers to send data to or retrieve data from an isochronous transfer pipe.</p>


## -syntax

````
struct _URB_ISOCH_TRANSFER {
  struct URB_HEADER  Hdr;
  USBD_PIPE_HANDLE           PipeHandle;
  ULONG                      TransferFlags;
  ULONG                      TransferBufferLength;
  PVOID                      TransferBuffer;
  PMDL                       TransferBufferMDL;
  struct URB  *UrbLink;
  struct URB_HCD_AREA  hca;
  ULONG                      StartFrame;
  ULONG                      NumberOfPackets;
  ULONG                      ErrorCount;
  USBD_ISO_PACKET_DESCRIPTOR IsoPacket[1];
};
````


## -struct-fields
<dl>

### -field Hdr

<dd>
<p>A pointer to a <a href="buses._urb_header">_URB_HEADER</a> structure that specifies the URB header information. <b>Hdr.Function</b> must be URB_FUNCTION_ISOCH_TRANSFER, and <b>Hdr.Length</b> must be the size of this variable-length data structure.</p>
</dd>

### -field PipeHandle

<dd>
<p>Specifies an opaque handle to the isochronous pipe. The host controller driver returns this handle when the client driver selects the device configuration with a URB of type URB_FUNCTION_SELECT_CONFIGURATION or when the client driver changes the settings for an interface with a URB of type URB_FUNCTION_SELECT_INTERFACE.   </p>
</dd>

### -field TransferFlags

<dd>
<p>
<p>Specifies zero, one, or a combination of the following flags:</p>
</p>
<table>
<tr>
<th>Value</th>
<th>Meaning</th>
</tr>
<tr>
<td width="40%"><a id="USBD_TRANSFER_DIRECTION_IN"></a><a id="usbd_transfer_direction_in"></a><dl>

### -field USBD_TRANSFER_DIRECTION_IN

</dl>
</td>
<td width="60%">
<p>Is set to request data from a device. To transfer data to a device, this flag must be clear. </p>
</td>
</tr>
<tr>
<td width="40%"><a id="USBD_SHORT_TRANSFER_OK"></a><a id="usbd_short_transfer_ok"></a><dl>

### -field USBD_SHORT_TRANSFER_OK

</dl>
</td>
<td width="60%">
<p>Is set to direct the host controller not to return an error when it receives a packet from the device that is shorter than the maximum packet size for the endpoint. This flag has no effect on an isochronous pipe, because the bus driver does not return an error when it receives short packets on an isochronous pipe.</p>
</td>
</tr>
<tr>
<td width="40%"><a id="USBD_START_ISO_TRANSFER_ASAP"></a><a id="usbd_start_iso_transfer_asap"></a><dl>

### -field USBD_START_ISO_TRANSFER_ASAP

</dl>
</td>
<td width="60%">
<p>Causes the transfer to begin on the next frame, if no transfers have been submitted to the pipe since the pipe was opened or last reset. Otherwise, the transfer begins on the first frame that follows all currently queued requests for the pipe. The actual frame that the transfer begins on will be adjusted for bus latency by the host controller driver.</p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -field TransferBufferLength

<dd>
<p>Specifies the length, in bytes, of the buffer specified in <b>TransferBuffer</b> or described in <b>TransferBufferMDL</b>. The host controller driver returns the number of bytes that are sent to or read from the pipe in this member.</p>
</dd>

### -field TransferBuffer

<dd>
<p>A pointer to a resident buffer for the transfer is <b>NULL</b> if an MDL is supplied in <b>TransferBufferMDL</b>. The contents of this buffer depend on the value of <b>TransferFlags</b>. If USBD_TRANSFER_DIRECTION_IN is specified, this buffer will contain data that is read from the device on return from the host controller driver. Otherwise, this buffer contains driver-supplied data for transfer to the device.</p>
</dd>

### -field TransferBufferMDL

<dd>
<p>A pointer to an MDL that describes a resident buffer is <b>NULL</b> if a buffer is supplied in <b>TransferBuffer</b>. The contents of the buffer depend on the value of <b>TransferFlags</b>. If USBD_TRANSFER_DIRECTION_IN is specified, the described buffer will contain data that is read from the device on return from the host controller driver. Otherwise, the buffer contains driver-supplied data for transfer to the device. This MDL must be allocated from nonpaged pool.</p>
</dd>

### -field UrbLink

<dd>
<p>Reserved. Do not use.</p>
</dd>

### -field hca

<dd>
<p>Reserved. Do not use.</p>
</dd>

### -field StartFrame

<dd>
<p>Specifies the frame number that the transfer should begin on. This variable must be within a system-defined range of the current frame. The range is specified by the constant USBD_ISO_START_FRAME_RANGE.</p>
<p>If START_ISO_TRANSFER_ASAP is set in <b>TransferFlags</b>, this member contains the frame number that the transfer began on, when the request is returned by the host controller driver. Otherwise, this member must contain the frame number that this transfer begins on.</p>
</dd>

### -field NumberOfPackets

<dd>
<p>Specifies the number of packets that are described by the variable-length array member <b>IsoPacket</b>.</p>
</dd>

### -field ErrorCount

<dd>
<p>Contains the number of packets that completed with an error condition on return from the host controller driver.</p>
</dd>

### -field IsoPacket

<dd>
<p>Contains a variable-length array of <a href="..\usb\ns-usb--usbd-iso-packet-descriptor.md">USBD_ISO_PACKET_DESCRIPTOR</a> structures that describe the isochronous transfer packets to be transferred on the USB bus.  For more information about this member see the Remarks section.</p>
</dd>
</dl>

## -remarks
<p>The USB bus driver always returns a value of USBD_STATUS_SUCCESS in <b>Hdr.Status</b>, unless  every packet in the transfer generated an error or the request was not well-formed and could not be executed at all. The following table includes possible error codes returned in <b>Hdr.Status</b>.</p>

<p>USBD_STATUS_ISOCH_REQUEST_FAILED</p>

<p>Indicates that every packet of an isochronous request was completed with errors. </p>

<p>USBD_STATUS_BAD_START_FRAME</p>

<p>Indicates that the requested start frame is not within USBD_ISO_START_FRAME_RANGE of the current USB frame. </p>

<p>USBD_ISO_NOT_ACCESSED_LATE</p>

<p>Indicates that every packet was submitted too late for the packet to be sent, based on the requested start frame. </p>

<p>USBD_STATUS_INVALID_PARAMETER</p>

<p>Indicates that one of the URB parameters was incorrect. </p>

<p>Before the host controller sends an isochronous request to a USB device, it requires information about the device's endpoint to which it must send or receive data. This information is stored in endpoint descriptors (<a href="..\usbspec\ns-usbspec--usb-endpoint-descriptor.md">USB_ENDPOINT_DESCRIPTOR</a>) that are retrieved from the selected configuration descriptor. 
After the bus driver gets the endpoint descriptor, it creates an isochronous transfer pipe to set up the data transfer. The pipe's attributes are stored in the <a href="..\usb\ns-usb--usbd-pipe-information.md">USBD_PIPE_INFORMATION</a> structure. For isochronous transfers, the members are set as follows:<ul>
<li>The  <b>PipeType</b> member specifies the type of transfer and is set to UsbdPipeTypeIsochronous.</li>
<li>The <b>MaximumPacketSize</b> member specifies the amount of data, in bytes, that constitutes one packet. For isochronous transfers, the packet size is fixed and can be a value from 0-1024. The packet size either equals or is less than the <b>wMaxPacketSize</b> value of the endpoint descriptor.</li>
<li>The <b>Interval</b> member is derived from the <b>bInterval</b> value of the endpoint descriptor. This value is used to calculate the polling period that indicates the frequency at which data is sent on the bus. For full speed devices, the period is measured in units of 1 millisecond frames; for high speed devices, the period is measured in microframes.</li>
</ul>The host controller also determines the amount of data that can be transferred (within a frame or a microframe) depending on the type of device. This information is available in bits <b>12.. 11</b> of  <b>wMaxPacketSize</b> in the endpoint descriptor. </p>

<p>For full-speed devices, only one packet can be transferred within a frame; bits <b>12.. 11</b> are reserved and set to zero. </p>

<p>For high speed devices, data can be transferred in a single packet or might span multiple packets, within a microframe. 
If bits <b>12.. 11</b> are set to <i>n</i>,  you can transfer <code>(n+1)*MaximumPacketSize</code> bytes per microframe. Bits <b>12.. 11</b> set to zero indicate that only one packet can be transferred in a microframe. If bits <b>12.. 11</b> are set to 1,  the host controller can transfer two packets in a microframe.</p>

<p>
The <b>IsoPacket</b> member of <b>_URB_ISOCH_TRANSFER</b> is an array of <a href="..\usb\ns-usb--usbd-iso-packet-descriptor.md">USBD_ISO_PACKET_DESCRIPTOR</a> that describes the transfer buffer layout. Each element in the array correlates to data that is transferred in one microframe. If <b>IsoPacket</b> has <i>n</i> elements,  the host controller transfers use <i>n</i> frames (for full speed devices) or microframes (for high speed devices) to transfer data. The <b>IsoPacket[</b>i<b>].Offset</b> member is used to track the amount of data to send or receive. This is done  by setting a byte offset from the start of the entire transfer buffer for the request. </p>

<p>For example, there are five microframes available to transfer 1024 byte-sized packets.</p>

<p>If bits <b>12.. 11</b> are set to zero (indicating a single packet per microframe transfer),  <b>IsoPacket</b> contains the following entries:</p>

<p>Microframe 1<code> IsoPacket.Element[0].Offset = 0</code> (start address) </p>

<p>Microframe 2<code> IsoPacket.Element[1].Offset = 1024</code></p>

<p>Microframe 3<code> IsoPacket.Element[2].Offset = 2048</code></p>

<p>Microframe 4<code> IsoPacket.Element[3].Offset = 3072</code></p>

<p>Microframe 5<code> IsoPacket.Element[4].Offset = 4096</code></p>

<p>If bits <b>12.. 11</b> are set to 1 (indicating two packets per microframe),  <b>IsoPacket</b> contains the following entries:</p>

<p>Microframe 2<code> IsoPacket.Element[1].Offset = 2048</code></p>

<p>Microframe 3<code> IsoPacket.Element[2].Offset = 4096</code></p>

<p>Microframe 4<code> IsoPacket.Element[3].Offset = 6144</code></p>

<p>Microframe 5<code> IsoPacket.Element[4].Offset = 8192</code></p>

<p><b>Note</b>  For multiple packets, the offset value indicates sizes for all the packets within the microframe.</p>

<p>The <b>IsoPacket[</b>i<b>].Length</b> member is updated by the host controller to indicate the actual number of bytes  that are received from the device for isochronous IN transfers. <b>IsoPacket[</b>i<b>].Length</b> is not used for isochronous OUT transfers.</p>

<p>Drivers can use the <a href="..\usbdlib\nf-usbdlib-get-iso-urb-size.md">GET_ISO_URB_SIZE</a> macro to determine the size that is needed to hold the entire URB. If the length is too small to fill the space set aside for this packet, the bus driver leaves a gap from the end of the retrieved data to the offset for the next packet. The bus driver will not adjust the offsets to avoid wasting buffer space. </p>

<p>The <b>TransferBuffer</b> or <b>TransferBufferMDL</b> members must specify a virtually contiguous buffer.</p>

<p>Treat other members that are part of this structure but not described here as opaque. They are reserved for system use. </p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Usb.h (include Usb.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\usbdlib\nf-usbdlib-usbd-isochurballocate.md">USBD_IsochUrbAllocate</a>
</dt>
<dt>
<a href="..\usb\ns-usb--usbd-iso-packet-descriptor.md">USBD_ISO_PACKET_DESCRIPTOR</a>
</dt>
<dt>
<a href="..\usb\ns-usb--urb.md">URB</a>
</dt>
<dt>
<a href="buses._urb_header">_URB_HEADER</a>
</dt>
<dt>
<a href="buses.transfer_data_to_isochronous_endpoints">How to Transfer Data to USB Isochronous Endpoints</a>
</dt>
<dt>
<a href="buses.usb_structures_and_enumerations">USB Structures</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [usbref\buses]:%20_URB_ISOCH_TRANSFER structure%20 RELEASE:%20(11/20/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
