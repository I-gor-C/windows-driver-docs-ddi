---
UID: NF.wudfusb.IWDFUsbTargetDevice.GetNumInterfaces
title: IWDFUsbTargetDevice::GetNumInterfaces
author: windows-driver-content
description: The GetNumInterfaces method retrieves the number of USB interfaces for the USB device.
old-location: wdf\iwdfusbtargetdevice_getnuminterfaces.htm
ms.assetid: 4da2f2b0-f2ad-465d-b63e-f11406d4c210
ms.author: windowsdriverdev
ms.date: 11/2/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: wdf
req.header: wudfusb.h
req.include-header: Wudfusb.h
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 1.5
req.alt-api: IWDFUsbTargetDevice.GetNumInterfaces
req.alt-loc: WUDFx.dll
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: Unavailable in UMDF 2.0 and later.
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: WUDFx.dll
req.irql: 
ms.keywords: IWDFUsbTargetDevice, GetNumInterfaces, IWDFUsbTargetDevice::GetNumInterfaces
req.iface: IWDFUsbTargetDevice
req.product: Windows 10 or later.
---

# IWDFUsbTargetDevice::GetNumInterfaces method



## -description
<p class="CCE_Message">[<b>Warning:</b> UMDF 2 is the latest version of UMDF and supersedes UMDF 1.  All new UMDF drivers should be written using UMDF 2.  No new features are being added to UMDF 1 and there is limited support for UMDF 1 on newer versions of Windows 10.  Universal Windows drivers must use UMDF 2.  For more info, see <a href="https://docs.microsoft.com/en-us/windows-hardware/drivers/wdf/getting-started-with-umdf-version-2">Getting Started with UMDF</a>.]</p>
<p>The <b>GetNumInterfaces</b> method retrieves the number of USB interfaces for the USB device.</p>


## -syntax

````
UCHAR GetNumInterfaces();
````


## -parameters


## -returns
<p><b>GetNumInterfaces</b> returns the number of <a href="https://msdn.microsoft.com/library/windows/hardware/ff560312">IWDFUsbInterface</a> interfaces for the USB device in the default configuration. The default configuration is identified by index zero.</p>

<p><b>GetNumInterfaces</b> returns the number of <a href="https://msdn.microsoft.com/library/windows/hardware/ff560312">IWDFUsbInterface</a> interfaces for the USB device in the default configuration. The default configuration is identified by index zero.</p>

<p><b>GetNumInterfaces</b> returns the number of <a href="https://msdn.microsoft.com/library/windows/hardware/ff560312">IWDFUsbInterface</a> interfaces for the USB device in the default configuration. The default configuration is identified by index zero.</p>

## -remarks
<p>UMDF USB I/O target devices do not support multiple configurations. </p>

<p>The following code example retrieves the number of USB interfaces for the USB device.</p>

<p>UMDF USB I/O target devices do not support multiple configurations. </p>

<p>The following code example retrieves the number of USB interfaces for the USB device.</p>

<p>UMDF USB I/O target devices do not support multiple configurations. </p>

<p>The following code example retrieves the number of USB interfaces for the USB device.</p>

<p>UMDF USB I/O target devices do not support multiple configurations. </p>

<p>The following code example retrieves the number of USB interfaces for the USB device.</p>

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
<p>End of support</p>
</th>
<td width="70%">
<p>Unavailable in UMDF 2.0 and later.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Minimum UMDF version</p>
</th>
<td width="70%">
<p>1.5</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Wudfusb.h (include Wudfusb.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>DLL</p>
</th>
<td width="70%">
<dl>
<dt>WUDFx.dll</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff560362">IWDFUsbTargetDevice</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff560312">IWDFUsbInterface</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20IWDFUsbTargetDevice::GetNumInterfaces method%20 RELEASE:%20(11/2/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
