---
UID: NN.wudfusb.IWDFUsbTargetDevice~r1
title: IWDFUsbTargetDevice
author: windows-driver-content
description: The IWDFUsbTargetDevice interface exposes a USB device I/O target object.
old-location: wdf\iwdfusbtargetdevice.htm
old-project: wdf
ms.assetid: 627a4633-6857-43a5-af2d-36e4e554ca83
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: IWDFUsbTargetPipe2, ConfigureContinuousReader, IWDFUsbTargetPipe2::ConfigureContinuousReader
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
req.iface: IWDFUsbTargetPipe2
req.product: Windows 10 or later.
---

# IWDFUsbTargetDevice interface



## -description
<p class="CCE_Message">[<b>Warning:</b> UMDF 2 is the latest version of UMDF and supersedes UMDF 1.  All new UMDF drivers should be written using UMDF 2.  No new features are being added to UMDF 1 and there is limited support for UMDF 1 on newer versions of Windows 10.  Universal Windows drivers must use UMDF 2.  For more info, see <a href="https://docs.microsoft.com/en-us/windows-hardware/drivers/wdf/getting-started-with-umdf-version-2">Getting Started with UMDF</a>.]</p>
<p>
<p>The <b>IWDFUsbTargetDevice</b> interface exposes a USB device I/O target object.</p>
</p>
<p>The <b>IWDFUsbTargetDevice</b> interface exposes a USB device I/O target object.</p>


## -inheritance
<p>The <b xmlns:loc="http://microsoft.com/wdcml/l10n">IWDFUsbTargetDevice</b> interface inherits from <a href="..\wudfddi\nn-wudfddi-iwdfiotarget.md">IWDFIoTarget</a>. <b>IWDFUsbTargetDevice</b> also has these types of members:</p>

<p>The <b>IWDFUsbTargetDevice</b> interface has these methods.</p>

<p>The <a href="wdf.iwdfusbtargetdevice_formatrequestforcontroltransfer">FormatRequestForControlTransfer</a> method formats an I/O request object for a USB control transfer.</p>

<p>The <a href="wdf.iwdfusbtargetdevice_getnuminterfaces">GetNumInterfaces</a> method retrieves the number of USB interfaces for the USB device.</p>

<p>The <a href="wdf.iwdfusbtargetdevice_getwinusbhandle">GetWinUsbHandle</a> method retrieves the WinUsb interface handle that is associated with a I/O target device object.</p>

<p>The <a href="wdf.iwdfusbtargetdevice_retrievedescriptor">RetrieveDescriptor</a> method retrieves a USB descriptor, which can describe a device, configuration, or string.</p>

<p>The <a href="wdf.iwdfusbtargetdevice_retrievedeviceinformation">RetrieveDeviceInformation</a> method retrieves device information of the specified type.</p>

<p>The <a href="wdf.iwdfusbtargetdevice_retrievepowerpolicy">RetrievePowerPolicy</a> method retrieves a WinUsb power policy.</p>

<p>The <a href="wdf.iwdfusbtargetdevice_retrieveusbinterface">RetrieveUsbInterface</a> method retrieves the specified USB interface for a USB device.</p>

<p>The <a href="wdf.iwdfusbtargetdevice_setpowerpolicy">SetPowerPolicy</a> method sets the WinUsb power policy.</p>

<p> </p>

## -members
<p>The <b>IWDFUsbTargetDevice</b> interface has these methods.</p><table class="members" id="memberListMethods">
<tr>
<th align="left" width="37%">Method</th>
<th align="left" width="63%">Description</th>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="wdf.iwdfusbtargetdevice_formatrequestforcontroltransfer">IWDFUsbTargetDevice::FormatRequestForControlTransfer</a>
</td>
<td align="left" width="63%">
<p>The <a href="wdf.iwdfusbtargetdevice_formatrequestforcontroltransfer">FormatRequestForControlTransfer</a> method formats an I/O request object for a USB control transfer.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="wdf.iwdfusbtargetdevice_getnuminterfaces">IWDFUsbTargetDevice::GetNumInterfaces</a>
</td>
<td align="left" width="63%">
<p>The <a href="wdf.iwdfusbtargetdevice_getnuminterfaces">GetNumInterfaces</a> method retrieves the number of USB interfaces for the USB device.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="wdf.iwdfusbtargetdevice_getwinusbhandle">IWDFUsbTargetDevice::GetWinUsbHandle</a>
</td>
<td align="left" width="63%">
<p>The <a href="wdf.iwdfusbtargetdevice_getwinusbhandle">GetWinUsbHandle</a> method retrieves the WinUsb interface handle that is associated with a I/O target device object.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="wdf.iwdfusbtargetdevice_retrievedescriptor">IWDFUsbTargetDevice::RetrieveDescriptor</a>
</td>
<td align="left" width="63%">
<p>The <a href="wdf.iwdfusbtargetdevice_retrievedescriptor">RetrieveDescriptor</a> method retrieves a USB descriptor, which can describe a device, configuration, or string.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="wdf.iwdfusbtargetdevice_retrievedeviceinformation">IWDFUsbTargetDevice::RetrieveDeviceInformation</a>
</td>
<td align="left" width="63%">
<p>The <a href="wdf.iwdfusbtargetdevice_retrievedeviceinformation">RetrieveDeviceInformation</a> method retrieves device information of the specified type.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="wdf.iwdfusbtargetdevice_retrievepowerpolicy">IWDFUsbTargetDevice::RetrievePowerPolicy</a>
</td>
<td align="left" width="63%">
<p>The <a href="wdf.iwdfusbtargetdevice_retrievepowerpolicy">RetrievePowerPolicy</a> method retrieves a WinUsb power policy.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="wdf.iwdfusbtargetdevice_retrieveusbinterface">IWDFUsbTargetDevice::RetrieveUsbInterface</a>
</td>
<td align="left" width="63%">
<p>The <a href="wdf.iwdfusbtargetdevice_retrieveusbinterface">RetrieveUsbInterface</a> method retrieves the specified USB interface for a USB device.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="wdf.iwdfusbtargetdevice_setpowerpolicy">IWDFUsbTargetDevice::SetPowerPolicy</a>
</td>
<td align="left" width="63%">
<p>The <a href="wdf.iwdfusbtargetdevice_setpowerpolicy">SetPowerPolicy</a> method sets the WinUsb power policy.</p>
</td>
</tr>
</table><p>The <a href="wdf.iwdfusbtargetdevice_formatrequestforcontroltransfer">FormatRequestForControlTransfer</a> method formats an I/O request object for a USB control transfer.</p>

<p>The <a href="wdf.iwdfusbtargetdevice_getnuminterfaces">GetNumInterfaces</a> method retrieves the number of USB interfaces for the USB device.</p>

<p>The <a href="wdf.iwdfusbtargetdevice_getwinusbhandle">GetWinUsbHandle</a> method retrieves the WinUsb interface handle that is associated with a I/O target device object.</p>

<p>The <a href="wdf.iwdfusbtargetdevice_retrievedescriptor">RetrieveDescriptor</a> method retrieves a USB descriptor, which can describe a device, configuration, or string.</p>

<p>The <a href="wdf.iwdfusbtargetdevice_retrievedeviceinformation">RetrieveDeviceInformation</a> method retrieves device information of the specified type.</p>

<p>The <a href="wdf.iwdfusbtargetdevice_retrievepowerpolicy">RetrievePowerPolicy</a> method retrieves a WinUsb power policy.</p>

<p>The <a href="wdf.iwdfusbtargetdevice_retrieveusbinterface">RetrieveUsbInterface</a> method retrieves the specified USB interface for a USB device.</p>

<p>The <a href="wdf.iwdfusbtargetdevice_setpowerpolicy">SetPowerPolicy</a> method sets the WinUsb power policy.</p>

<p> </p>

## -remarks


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
<dt>Wudfusb.h</dt>
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