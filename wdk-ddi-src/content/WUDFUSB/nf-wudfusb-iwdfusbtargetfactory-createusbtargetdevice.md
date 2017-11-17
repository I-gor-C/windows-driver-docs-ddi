---
UID: NF.wudfusb.IWDFUsbTargetFactory.CreateUsbTargetDevice
title: IWDFUsbTargetFactory::CreateUsbTargetDevice
author: windows-driver-content
description: The CreateUsbTargetDevice method creates a USB device object that is also an I/O target.
old-location: wdf\iwdfusbtargetfactory_createusbtargetdevice.htm
ms.assetid: c5aeb5f4-be62-4418-981c-1dd4acdccf07
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
req.alt-api: IWDFUsbTargetFactory.CreateUsbTargetDevice
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
ms.keywords: IWDFUsbTargetFactory, CreateUsbTargetDevice, IWDFUsbTargetFactory::CreateUsbTargetDevice
req.iface: IWDFUsbTargetFactory
req.product: Windows 10 or later.
---

# IWDFUsbTargetFactory::CreateUsbTargetDevice method



## -description
<p class="CCE_Message">[<b>Warning:</b> UMDF 2 is the latest version of UMDF and supersedes UMDF 1.  All new UMDF drivers should be written using UMDF 2.  No new features are being added to UMDF 1 and there is limited support for UMDF 1 on newer versions of Windows 10.  Universal Windows drivers must use UMDF 2.  For more info, see <a href="https://docs.microsoft.com/en-us/windows-hardware/drivers/wdf/getting-started-with-umdf-version-2">Getting Started with UMDF</a>.]</p>
<p>The <b>CreateUsbTargetDevice</b> method creates a USB device object that is also an I/O target.</p>


## -syntax

````
HRESULT CreateUsbTargetDevice(
  [out] IWDFUsbTargetDevice **ppDevice
);
````


## -parameters
<dl>

### -param <i>ppDevice</i> [out]

<dd>
<p>A pointer to a buffer that receives a pointer to the <a href="https://msdn.microsoft.com/library/windows/hardware/ff560362">IWDFUsbTargetDevice</a> interface for the USB target device object.</p>
</dd>
</dl>

## -returns
<p><b>CreateUsbTargetDevice</b> returns one of the following values: </p><dl>
<dt><b>S_OK </b></dt>
</dl><p>
<a href="https://msdn.microsoft.com/c5aeb5f4-be62-4418-981c-1dd4acdccf07">CreateUsbTargetDevice</a> successfully created a USB device object that is also an I/O target. </p><dl>
<dt><b>E_OUTOFMEMORY </b></dt>
</dl><p>
<a href="https://msdn.microsoft.com/c5aeb5f4-be62-4418-981c-1dd4acdccf07">CreateUsbTargetDevice</a> encountered an allocation failure.</p><dl>
<dt><b>An error code that is defined in Winerror.h</b></dt>
</dl><p>This value corresponds to the error code that the <a href="https://msdn.microsoft.com/library/windows/hardware/ff540277">WinUsb_Initialize</a> function returned.</p>

<p> </p>

## -remarks
<p>A UMDF driver should release the <a href="https://msdn.microsoft.com/library/windows/hardware/ff560362">IWDFUsbTargetDevice</a> interface pointer that the <b>CreateUsbTargetDevice</b> method returns in the <i>ppDevice</i> parameter when the driver is done with the interface.</p>

<p>If the file object that is associated with the created I/O target object is required, the driver should call the <a href="https://msdn.microsoft.com/library/windows/hardware/ff559243">IWDFIoTarget::GetTargetFile</a> method. For more information about this file object, see <a href="wdf.file_creation_by_a_usb_i_o_target">File Creation by a USB I/O Target</a>.</p>

<p>To use the newly created USB I/O target object in a device stack, the INF file that installs the UMDF driver must contain the <b>UmdfDispatcher</b> directive and set <b>UmdfDispatcher</b> to <b>WinUsb</b> (<code>UmdfDispatcher=WinUsb</code>) in the <b>DDInstall.WDF</b> section. <b>UmdfDispatcher</b> is required to inform the UMDF platform that it can allow access to the USB I/O target. For more information about <b>UmdfDispatcher</b>, see <a href="wdf.specifying_wdf_directives_in_inf_files">Specifying WDF Directives</a>.</p>

<p>The following code example shows how to create and use a USB device object in an implementation of the UMDF driver's <a href="https://msdn.microsoft.com/library/windows/hardware/ff556766">IPnpCallbackHardware::OnPrepareHardware</a> method.</p>

<p>A UMDF driver should release the <a href="https://msdn.microsoft.com/library/windows/hardware/ff560362">IWDFUsbTargetDevice</a> interface pointer that the <b>CreateUsbTargetDevice</b> method returns in the <i>ppDevice</i> parameter when the driver is done with the interface.</p>

<p>If the file object that is associated with the created I/O target object is required, the driver should call the <a href="https://msdn.microsoft.com/library/windows/hardware/ff559243">IWDFIoTarget::GetTargetFile</a> method. For more information about this file object, see <a href="wdf.file_creation_by_a_usb_i_o_target">File Creation by a USB I/O Target</a>.</p>

<p>To use the newly created USB I/O target object in a device stack, the INF file that installs the UMDF driver must contain the <b>UmdfDispatcher</b> directive and set <b>UmdfDispatcher</b> to <b>WinUsb</b> (<code>UmdfDispatcher=WinUsb</code>) in the <b>DDInstall.WDF</b> section. <b>UmdfDispatcher</b> is required to inform the UMDF platform that it can allow access to the USB I/O target. For more information about <b>UmdfDispatcher</b>, see <a href="wdf.specifying_wdf_directives_in_inf_files">Specifying WDF Directives</a>.</p>

<p>The following code example shows how to create and use a USB device object in an implementation of the UMDF driver's <a href="https://msdn.microsoft.com/library/windows/hardware/ff556766">IPnpCallbackHardware::OnPrepareHardware</a> method.</p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff560387">IWDFUsbTargetFactory</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff540277">WinUsb_Initialize</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff559170">IWDFIoTarget</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff559243">IWDFIoTarget::GetTargetFile</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff560362">IWDFUsbTargetDevice</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20IWDFUsbTargetFactory::CreateUsbTargetDevice method%20 RELEASE:%20(11/2/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
