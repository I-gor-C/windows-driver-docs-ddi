---
UID: NF.wdfusb.WdfUsbTargetPipeIsOutEndpoint
title: WdfUsbTargetPipeIsOutEndpoint function
author: windows-driver-content
description: The WdfUsbTargetPipeIsOutEndpoint method determines whether a specified USB pipe is connected to an output endpoint.
old-location: wdf\wdfusbtargetpipeisoutendpoint.htm
old-project: wdf
ms.assetid: 803d282b-f6eb-4cd3-91b3-899f983c9dc5
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: WdfUsbTargetPipeIsOutEndpoint
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: wdfusb.h
req.include-header: Wdfusb.h
req.target-type: Universal
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 1.0
req.umdf-ver: 2.0
req.alt-api: WdfUsbTargetPipeIsOutEndpoint
req.alt-loc: Wdf01000.sys,Wdf01000.sys.dll,WUDFx02000.dll,WUDFx02000.dll.dll
req.ddi-compliance: DriverCreate, KmdfIrql, KmdfIrql2, UsbKmdfIrql, UsbKmdfIrql2
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Wdf01000.sys (KMDF); WUDFx02000.dll (UMDF)
req.dll: 
req.irql: <=DISPATCH_LEVEL
req.product: Windows 10 or later.
---

# WdfUsbTargetPipeIsOutEndpoint function



## -description
<p class="CCE_Message">[Applies to KMDF and UMDF]
The <b>WdfUsbTargetPipeIsOutEndpoint</b> method determines whether a specified USB pipe is connected to an output endpoint.


## -syntax

````
BOOLEAN WdfUsbTargetPipeIsOutEndpoint(
  _In_ WDFUSBPIPE Pipe
);
````


## -parameters

### -param Pipe [in]

A handle to a framework pipe object that represents a bulk pipe or interrupt pipe and was obtained by calling <a href="wdf.wdfusbinterfacegetconfiguredpipe">WdfUsbInterfaceGetConfiguredPipe</a>. 

## -returns
<b>WdfUsbTargetPipeIsOutEndpoint</b> returns <b>TRUE</b> if the pipe that the <i>Pipe</i> handle represents an output endpoint. The method returns <b>FALSE</b> if the endpoint is an input endpoint.

A bug check occurs if the driver supplies an invalid object handle.



## -remarks
For more information about the <b>WdfUsbTargetPipeIsOutEndpoint</b> method and USB I/O targets, see <a href="wdf.usb_i_o_targets">USB I/O Targets</a>.

The following code example determines whether a specified USB pipe is connected to an output endpoint.

## -requirements
<table>
<tr>
<th width="30%">
Target platform
</th>
<td width="70%">
<dl>
<dt><a href="http://go.microsoft.com/fwlink/p/?linkid=531356" target="_blank">Universal</a></dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
Minimum KMDF version
</th>
<td width="70%">
1.0
</td>
</tr>
<tr>
<th width="30%">
Minimum UMDF version
</th>
<td width="70%">
2.0
</td>
</tr>
<tr>
<th width="30%">
Header
</th>
<td width="70%">
<dl>
<dt>Wdfusb.h (include Wdfusb.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
Library
</th>
<td width="70%">
<dl>
<dt>Wdf01000.sys (KMDF); </dt>
<dt>WUDFx02000.dll (UMDF)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
IRQL
</th>
<td width="70%">
&lt;=DISPATCH_LEVEL
</td>
</tr>
<tr>
<th width="30%">
DDI compliance rules
</th>
<td width="70%">
<a href="devtest.kmdf_drivercreate">DriverCreate</a>, <a href="devtest.kmdf_kmdfirql">KmdfIrql</a>, <a href="devtest.kmdf_kmdfirql2">KmdfIrql2</a>, <a href="devtest.kmdf_usbkmdfirql">UsbKmdfIrql</a>, <a href="devtest.kmdf_usbkmdfirql2">UsbKmdfIrql2</a>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="wdf.wdf_usb_pipe_direction_out">WDF_USB_PIPE_DIRECTION_OUT</a>
</dt>
<dt>
<a href="wdf.wdfusbinterfacegetconfiguredpipe">WdfUsbInterfaceGetConfiguredPipe</a>
</dt>
<dt>
<a href="wdf.wdfusbtargetpipeisinendpoint">WdfUsbTargetPipeIsInEndpoint</a>
</dt>
</dl>
 
 
<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20WdfUsbTargetPipeIsOutEndpoint method%20 RELEASE:%20(11/30/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>
