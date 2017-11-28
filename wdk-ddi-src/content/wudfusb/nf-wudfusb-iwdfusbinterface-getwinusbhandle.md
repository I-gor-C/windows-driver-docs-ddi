---
UID: NF.wudfusb.IWDFUsbInterface.GetWinUsbHandle
title: IWDFUsbInterface::GetWinUsbHandle
author: windows-driver-content
description: The GetWinUsbHandle method retrieves the WinUsb interface handle that is associated with a USB interface.
old-location: wdf\iwdfusbinterface_getwinusbhandle.htm
old-project: wdf
ms.assetid: 31c23596-21b2-4fb2-96bd-5372fe2432ab
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: IWDFUsbInterface, GetWinUsbHandle, IWDFUsbInterface::GetWinUsbHandle
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: wudfusb.h
req.include-header: Wudfusb.h
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 1.5
req.alt-api: IWDFUsbInterface.GetWinUsbHandle
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
req.iface: IWDFUsbInterface
req.product: Windows 10 or later.
---

# IWDFUsbInterface::GetWinUsbHandle method



## -description
<p class="CCE_Message">[<b>Warning:</b> UMDF 2 is the latest version of UMDF and supersedes UMDF 1.  All new UMDF drivers should be written using UMDF 2.  No new features are being added to UMDF 1 and there is limited support for UMDF 1 on newer versions of Windows 10.  Universal Windows drivers must use UMDF 2.  For more info, see <a href="https://docs.microsoft.com/en-us/windows-hardware/drivers/wdf/getting-started-with-umdf-version-2">Getting Started with UMDF</a>.]</p>
<p>The <b>GetWinUsbHandle</b> method retrieves the WinUsb interface handle that is associated with a USB interface.</p>


## -syntax

````
WINUSB_INTERFACE_HANDLE GetWinUsbHandle();
````


## -parameters


## -returns
<p><b>GetWinUsbHandle</b> returns the WinUsb interface handle that is associated with the USB interface.</p>

<p><b>GetWinUsbHandle</b> returns the WinUsb interface handle that is associated with the USB interface.</p>

<p><b>GetWinUsbHandle</b> returns the WinUsb interface handle that is associated with the USB interface.</p>

## -remarks
<p>If called on the default interface, the <b>IWDFUsbInterface::GetWinUsbHandle</b> method returns the same WinUsb interface handle as <a href="https://msdn.microsoft.com/library/windows/hardware/ff560369">IWDFUsbTargetDevice::GetWinUsbHandle</a>. The default interface is identified by index zero.</p>

<p>If called on interfaces with index greater than zero, <b>IWDFUsbInterface::GetWinUsbHandle</b> returns a different handle  than <a href="https://msdn.microsoft.com/library/windows/hardware/ff560369">IWDFUsbTargetDevice::GetWinUsbHandle</a>.</p>

<p>  A UMDF driver can use the WinUsb interface handle to bypass the UMDF interfaces and call <a href="buses.usb_interfaces#client#client">WinUSB Routines</a> directly for interface-related operations.</p>

<p>The UMDF driver should not call the <a href="https://msdn.microsoft.com/library/windows/hardware/ff540233">WinUsb_Free</a> function to free the WinUsb interface handle because the USB interface object owns the handle.</p>

<p>If called on the default interface, the <b>IWDFUsbInterface::GetWinUsbHandle</b> method returns the same WinUsb interface handle as <a href="https://msdn.microsoft.com/library/windows/hardware/ff560369">IWDFUsbTargetDevice::GetWinUsbHandle</a>. The default interface is identified by index zero.</p>

<p>If called on interfaces with index greater than zero, <b>IWDFUsbInterface::GetWinUsbHandle</b> returns a different handle  than <a href="https://msdn.microsoft.com/library/windows/hardware/ff560369">IWDFUsbTargetDevice::GetWinUsbHandle</a>.</p>

<p>  A UMDF driver can use the WinUsb interface handle to bypass the UMDF interfaces and call <a href="buses.usb_interfaces#client#client">WinUSB Routines</a> directly for interface-related operations.</p>

<p>The UMDF driver should not call the <a href="https://msdn.microsoft.com/library/windows/hardware/ff540233">WinUsb_Free</a> function to free the WinUsb interface handle because the USB interface object owns the handle.</p>

<p>If called on the default interface, the <b>IWDFUsbInterface::GetWinUsbHandle</b> method returns the same WinUsb interface handle as <a href="https://msdn.microsoft.com/library/windows/hardware/ff560369">IWDFUsbTargetDevice::GetWinUsbHandle</a>. The default interface is identified by index zero.</p>

<p>If called on interfaces with index greater than zero, <b>IWDFUsbInterface::GetWinUsbHandle</b> returns a different handle  than <a href="https://msdn.microsoft.com/library/windows/hardware/ff560369">IWDFUsbTargetDevice::GetWinUsbHandle</a>.</p>

<p>  A UMDF driver can use the WinUsb interface handle to bypass the UMDF interfaces and call <a href="buses.usb_interfaces#client#client">WinUSB Routines</a> directly for interface-related operations.</p>

<p>The UMDF driver should not call the <a href="https://msdn.microsoft.com/library/windows/hardware/ff540233">WinUsb_Free</a> function to free the WinUsb interface handle because the USB interface object owns the handle.</p>

<p>If called on the default interface, the <b>IWDFUsbInterface::GetWinUsbHandle</b> method returns the same WinUsb interface handle as <a href="https://msdn.microsoft.com/library/windows/hardware/ff560369">IWDFUsbTargetDevice::GetWinUsbHandle</a>. The default interface is identified by index zero.</p>

<p>If called on interfaces with index greater than zero, <b>IWDFUsbInterface::GetWinUsbHandle</b> returns a different handle  than <a href="https://msdn.microsoft.com/library/windows/hardware/ff560369">IWDFUsbTargetDevice::GetWinUsbHandle</a>.</p>

<p>  A UMDF driver can use the WinUsb interface handle to bypass the UMDF interfaces and call <a href="buses.usb_interfaces#client#client">WinUSB Routines</a> directly for interface-related operations.</p>

<p>The UMDF driver should not call the <a href="https://msdn.microsoft.com/library/windows/hardware/ff540233">WinUsb_Free</a> function to free the WinUsb interface handle because the USB interface object owns the handle.</p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff560312">IWDFUsbInterface</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff540233">WinUsb_Free</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff540277">WinUsb_Initialize</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20IWDFUsbInterface::GetWinUsbHandle method%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
