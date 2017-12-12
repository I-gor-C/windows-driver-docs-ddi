---
UID: NN.wudfusb.IWDFUsbTargetDevice~r1
title: IWDFUsbTargetDevice
author: windows-driver-content
description: The IWDFUsbTargetDevice interface exposes a USB device I/O target object.
old-location: wdf\iwdfusbtargetdevice.htm
old-project: wdf
ms.assetid: 627a4633-6857-43a5-af2d-36e4e554ca83
ms.author: windowsdriverdev
ms.date: 12/7/2017
ms.keywords: _WDF_USB_REQUEST_TYPE, *PWDF_USB_REQUEST_TYPE, WDF_USB_REQUEST_TYPE
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: interface
req.header: wudfusb.h
req.include-header: 
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 1.5
req.alt-api: IWDFUsbTargetDevice
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
req.product: Windows 10 or later.
---

# IWDFUsbTargetDevice interface



## -description
<p class="CCE_Message">[<b>Warning:</b> UMDF 2 is the latest version of UMDF and supersedes UMDF 1.  All new UMDF drivers should be written using UMDF 2.  No new features are being added to UMDF 1 and there is limited support for UMDF 1 on newer versions of Windows 10.  Universal Windows drivers must use UMDF 2.  For more info, see <a href="https://docs.microsoft.com/en-us/windows-hardware/drivers/wdf/getting-started-with-umdf-version-2">Getting Started with UMDF</a>.]


The <b>IWDFUsbTargetDevice</b> interface exposes a USB device I/O target object.



The <b>IWDFUsbTargetDevice</b> interface exposes a USB device I/O target object.



## -inheritance
The <b xmlns:loc="http://microsoft.com/wdcml/l10n">IWDFUsbTargetDevice</b> interface inherits from <a href="..\wudfddi\nn-wudfddi-iwdfiotarget.md">IWDFIoTarget</a>. <b>IWDFUsbTargetDevice</b> also has these types of members:

The <b>IWDFUsbTargetDevice</b> interface has these methods.

The <a href="wdf.iwdfusbtargetdevice_formatrequestforcontroltransfer">FormatRequestForControlTransfer</a> method formats an I/O request object for a USB control transfer.

The <a href="wdf.iwdfusbtargetdevice_getnuminterfaces">GetNumInterfaces</a> method retrieves the number of USB interfaces for the USB device.

The <a href="wdf.iwdfusbtargetdevice_getwinusbhandle">GetWinUsbHandle</a> method retrieves the WinUsb interface handle that is associated with a I/O target device object.

The <a href="wdf.iwdfusbtargetdevice_retrievedescriptor">RetrieveDescriptor</a> method retrieves a USB descriptor, which can describe a device, configuration, or string.

The <a href="wdf.iwdfusbtargetdevice_retrievedeviceinformation">RetrieveDeviceInformation</a> method retrieves device information of the specified type.

The <a href="wdf.iwdfusbtargetdevice_retrievepowerpolicy">RetrievePowerPolicy</a> method retrieves a WinUsb power policy.

The <a href="wdf.iwdfusbtargetdevice_retrieveusbinterface">RetrieveUsbInterface</a> method retrieves the specified USB interface for a USB device.

The <a href="wdf.iwdfusbtargetdevice_setpowerpolicy">SetPowerPolicy</a> method sets the WinUsb power policy.

 


## -members
The <b>IWDFUsbTargetDevice</b> interface has these methods.
<table class="members" id="memberListMethods">
<tr>
<th align="left" width="37%">Method</th>
<th align="left" width="63%">Description</th>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="wdf.iwdfusbtargetdevice_formatrequestforcontroltransfer">IWDFUsbTargetDevice::FormatRequestForControlTransfer</a>
</td>
<td align="left" width="63%">
The <a href="wdf.iwdfusbtargetdevice_formatrequestforcontroltransfer">FormatRequestForControlTransfer</a> method formats an I/O request object for a USB control transfer.

</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="wdf.iwdfusbtargetdevice_getnuminterfaces">IWDFUsbTargetDevice::GetNumInterfaces</a>
</td>
<td align="left" width="63%">
The <a href="wdf.iwdfusbtargetdevice_getnuminterfaces">GetNumInterfaces</a> method retrieves the number of USB interfaces for the USB device.

</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="wdf.iwdfusbtargetdevice_getwinusbhandle">IWDFUsbTargetDevice::GetWinUsbHandle</a>
</td>
<td align="left" width="63%">
The <a href="wdf.iwdfusbtargetdevice_getwinusbhandle">GetWinUsbHandle</a> method retrieves the WinUsb interface handle that is associated with a I/O target device object.

</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="wdf.iwdfusbtargetdevice_retrievedescriptor">IWDFUsbTargetDevice::RetrieveDescriptor</a>
</td>
<td align="left" width="63%">
The <a href="wdf.iwdfusbtargetdevice_retrievedescriptor">RetrieveDescriptor</a> method retrieves a USB descriptor, which can describe a device, configuration, or string.

</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="wdf.iwdfusbtargetdevice_retrievedeviceinformation">IWDFUsbTargetDevice::RetrieveDeviceInformation</a>
</td>
<td align="left" width="63%">
The <a href="wdf.iwdfusbtargetdevice_retrievedeviceinformation">RetrieveDeviceInformation</a> method retrieves device information of the specified type.

</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="wdf.iwdfusbtargetdevice_retrievepowerpolicy">IWDFUsbTargetDevice::RetrievePowerPolicy</a>
</td>
<td align="left" width="63%">
The <a href="wdf.iwdfusbtargetdevice_retrievepowerpolicy">RetrievePowerPolicy</a> method retrieves a WinUsb power policy.

</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="wdf.iwdfusbtargetdevice_retrieveusbinterface">IWDFUsbTargetDevice::RetrieveUsbInterface</a>
</td>
<td align="left" width="63%">
The <a href="wdf.iwdfusbtargetdevice_retrieveusbinterface">RetrieveUsbInterface</a> method retrieves the specified USB interface for a USB device.

</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="wdf.iwdfusbtargetdevice_setpowerpolicy">IWDFUsbTargetDevice::SetPowerPolicy</a>
</td>
<td align="left" width="63%">
The <a href="wdf.iwdfusbtargetdevice_setpowerpolicy">SetPowerPolicy</a> method sets the WinUsb power policy.

</td>
</tr>
</table>The <a href="wdf.iwdfusbtargetdevice_formatrequestforcontroltransfer">FormatRequestForControlTransfer</a> method formats an I/O request object for a USB control transfer.

The <a href="wdf.iwdfusbtargetdevice_getnuminterfaces">GetNumInterfaces</a> method retrieves the number of USB interfaces for the USB device.

The <a href="wdf.iwdfusbtargetdevice_getwinusbhandle">GetWinUsbHandle</a> method retrieves the WinUsb interface handle that is associated with a I/O target device object.

The <a href="wdf.iwdfusbtargetdevice_retrievedescriptor">RetrieveDescriptor</a> method retrieves a USB descriptor, which can describe a device, configuration, or string.

The <a href="wdf.iwdfusbtargetdevice_retrievedeviceinformation">RetrieveDeviceInformation</a> method retrieves device information of the specified type.

The <a href="wdf.iwdfusbtargetdevice_retrievepowerpolicy">RetrievePowerPolicy</a> method retrieves a WinUsb power policy.

The <a href="wdf.iwdfusbtargetdevice_retrieveusbinterface">RetrieveUsbInterface</a> method retrieves the specified USB interface for a USB device.

The <a href="wdf.iwdfusbtargetdevice_setpowerpolicy">SetPowerPolicy</a> method sets the WinUsb power policy.

 


## -remarks


## -requirements
<table>
<tr>
<th width="30%">
Target platform

</th>
<td width="70%">
<dl>
<dt>Desktop</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
End of support

</th>
<td width="70%">
Unavailable in UMDF 2.0 and later.

</td>
</tr>
<tr>
<th width="30%">
Minimum UMDF version

</th>
<td width="70%">
1.5

</td>
</tr>
<tr>
<th width="30%">
Header

</th>
<td width="70%">
<dl>
<dt>Wudfusb.h</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
DLL

</th>
<td width="70%">
<dl>
<dt>WUDFx.dll</dt>
</dl>
</td>
</tr>
</table>