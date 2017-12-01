---
UID: NF.udecxurb.UdecxUrbRetrieveBuffer
title: UdecxUrbRetrieveBuffer
author: windows-driver-content
description: Retrieves the transfer buffer of an URB from the specified framework request object sent to the endpoint queue.
old-location: buses\udecxurbretrievebuffer.htm
old-project: usbref
ms.assetid: C2AE51AE-EEB6-49BB-A6E4-BBCE6A25C905
ms.author: windowsdriverdev
ms.date: 11/20/2017
ms.keywords: UdecxUrbRetrieveBuffer
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: udecxurb.h
req.include-header: Udecx.h
req.target-type: Windows
req.target-min-winverclnt: Windows 10
req.target-min-winversvr: Windows Server 2016
req.kmdf-ver: 1.15
req.umdf-ver: 
req.alt-api: UdecxUrbRetrieveBuffer
req.alt-loc: Udecxstub.lib,Udecxstub.dll
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Udecxstub.lib
req.dll: 
req.irql: PASSIVE_LEVEL
req.iface: 
req.product: Windows 10 or later.
---

# UdecxUrbRetrieveBuffer function



## -description
<p>Retrieves the transfer buffer of an URB from the specified framework request object sent to the endpoint queue.
</p>


## -syntax

````
FORCEINLINE NTSTATUS UdecxUrbRetrieveBuffer(
  _In_  WDFREQUEST                         Request,
  _Out_ ptr_result_buffer_(*Length) PUCHAR *TransferBuffer,
  _Out_ PULONG                             Length
);
````


## -parameters
<dl>

### -param <i>Request</i> [in]

<dd>
<p>A handle to a framework request object that contains the <a href="..\usb\ns-usb--urb.md">URB</a> for the transfer.</p>
</dd>

### -param <i>TransferBuffer</i> [out]

<dd>
<p>A pointer to a buffer that receives the transfer buffer of an <a href="..\usb\ns-usb--urb.md">URB</a>.</p>
</dd>

### -param <i>Length</i> [out]

<dd>
<p>A ULONG variable that receives  the length of the buffer pointer to by <i>TransferBuffer</i>.</p>
</dd>
</dl>

## -returns
<p>The method returns STATUS_SUCCESS if the operation succeeds. Otherwise, this method might return an appropriate <a href="https://msdn.microsoft.com/7792201b-63bb-4db5-803d-2af02893d505">NTSTATUS</a> error code. </p><dl>
<dt><b>STATUS_INVALID_PARAMETER</b></dt>
</dl><p>The URB does not contain a transfer buffer.</p><dl>
<dt><b>STATUS_INSUFFICIENT_RESOURCES</b></dt>
</dl><p>The transfer buffer MDL was not valid. </p>

<p> </p>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Minimum supported client</p>
</th>
<td width="70%">
<p>Windows 10</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Minimum supported server</p>
</th>
<td width="70%">
<p>Windows Server 2016</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Minimum KMDF version</p>
</th>
<td width="70%">
<p>1.15</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>UdecxUrb.h (include Udecx.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Library</p>
</th>
<td width="70%">
<dl>
<dt>Udecxstub.lib</dt>
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
<a href="buses.udecxurbsetbytescompleted">UdecxUrbSetBytesCompleted</a>
</dt>
<dt>
<a href="buses.usb_emulated_device__ude__architecture">Architecture: USB Device Emulation (UDE)</a>
</dt>
<dt>
<a href="buses.writing_a_ude_client_driver">Write a UDE client driver</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [usbref\buses]:%20UdecxUrbRetrieveBuffer function%20 RELEASE:%20(11/20/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
