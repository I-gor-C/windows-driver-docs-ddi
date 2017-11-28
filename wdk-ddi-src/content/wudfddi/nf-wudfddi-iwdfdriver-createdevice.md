---
UID: NF.wudfddi.IWDFDriver.CreateDevice
title: IWDFDriver::CreateDevice
author: windows-driver-content
description: The CreateDevice method configures and creates a new framework device object.
old-location: wdf\iwdfdriver_createdevice.htm
old-project: wdf
ms.assetid: df921271-b708-43bf-a250-048b7f638cac
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: IWDFDriver, CreateDevice, IWDFDriver::CreateDevice
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: wudfddi.h
req.include-header: Wudfddi.h
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 1.5
req.alt-api: IWDFDriver.CreateDevice
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
req.irql: <= DISPATCH_LEVEL
req.iface: IWDFDriver
req.product: Windows 10 or later.
---

# IWDFDriver::CreateDevice method



## -description
<p class="CCE_Message">[<b>Warning:</b> UMDF 2 is the latest version of UMDF and supersedes UMDF 1.  All new UMDF drivers should be written using UMDF 2.  No new features are being added to UMDF 1 and there is limited support for UMDF 1 on newer versions of Windows 10.  Universal Windows drivers must use UMDF 2.  For more info, see <a href="https://docs.microsoft.com/en-us/windows-hardware/drivers/wdf/getting-started-with-umdf-version-2">Getting Started with UMDF</a>.]</p>
<p>The <b>CreateDevice</b> method configures and creates a new framework device object.</p>


## -syntax

````
HRESULT CreateDevice(
  [in]           IWDFDeviceInitialize *pDeviceInit,
  [in, optional] IUnknown             *pCallbackInterface,
  [out]          IWDFDevice           **ppDevice
);
````


## -parameters
<dl>

### -param <i>pDeviceInit</i> [in]

<dd>
<p>A pointer to the <a href="https://msdn.microsoft.com/library/windows/hardware/ff556965">IWDFDeviceInitialize</a> interface that represents the configuration properties for the new device to create.</p>
</dd>

### -param <i>pCallbackInterface</i> [in, optional]

<dd>
<p>A pointer to the <b>IUnknown</b> interface that the framework uses to obtain the interfaces that the driver provides for the new device object. These interfaces provide the callback functions that the framework calls when relevant events occur. For more information, see the following Remarks section.</p>
</dd>

### -param <i>ppDevice</i> [out]

<dd>
<p>A pointer to a buffer that receives a pointer to the <a href="https://msdn.microsoft.com/library/windows/hardware/ff556917">IWDFDevice</a> interface for the new device object.</p>
</dd>
</dl>

## -returns
<p><b>CreateDevice</b> returns S_OK if the operation succeeds. Otherwise, this method returns one of the error codes that are defined in Winerror.h.</p>

## -remarks
<p>The <b>IUnknown</b> interface that the driver supplies for the <i>pCallbackInterface</i> parameter can support several interfaces. The framework calls the <b>QueryInterface</b> method of the supplied <b>IUnknown</b> interface multiple times to retrieve the interfaces that the driver supports. The driver's <b>QueryInterface</b> method can return the following interfaces:</p><dl>
<dd>
<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff554902">IFileCallbackCleanup</a>
</p>
</dd>
<dd>
<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff554907">IFileCallbackClose</a>
</p>
</dd>
<dd>
<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff556754">IObjectCleanup</a>
</p>
</dd>
<dd>
<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff556762">IPnpCallback</a>
</p>
</dd>
<dd>
<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff556764">IPnpCallbackHardware</a>
</p>
</dd>
<dd>
<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh439727">IPnpCallbackHardware2</a>
</p>
</dd>
<dd>
<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh439744">IPnpCallbackHardwareInterrupt</a>
</p>
</dd>
<dd>
<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff556776">IPnpCallbackSelfManagedIo</a>
</p>
</dd>
<dd>
<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh439744">IPnpCallbackHardwareInterrupt</a>
</p>
</dd>
<dd>
<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff556776">IPnpCallbackSelfManagedIo</a>
</p>
</dd>
<dd>
<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff556815">IPowerPolicyCallbackWakeFromS0</a>
</p>
</dd>
<dd>
<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff556825">IPowerPolicyCallbackWakeFromSx</a>
</p>
</dd>
</dl><p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff554902">IFileCallbackCleanup</a>
</p>

<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff554907">IFileCallbackClose</a>
</p>

<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff556754">IObjectCleanup</a>
</p>

<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff556762">IPnpCallback</a>
</p>

<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff556764">IPnpCallbackHardware</a>
</p>

<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh439727">IPnpCallbackHardware2</a>
</p>

<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh439744">IPnpCallbackHardwareInterrupt</a>
</p>

<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff556776">IPnpCallbackSelfManagedIo</a>
</p>

<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh439744">IPnpCallbackHardwareInterrupt</a>
</p>

<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff556776">IPnpCallbackSelfManagedIo</a>
</p>

<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff556815">IPowerPolicyCallbackWakeFromS0</a>
</p>

<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff556825">IPowerPolicyCallbackWakeFromSx</a>
</p>

<p>When the device changes state, the framework calls the method that is related to the change (such as the <a href="https://msdn.microsoft.com/library/windows/hardware/ff556799">IPnpCallback::OnD0Entry</a> method) to notify the driver. </p>

<p>If the call to <b>CreateDevice</b> is successful, the driver must eventually call the <b>IWDFDevice::Release</b> method. Note that the framework has its own reference count on the object.</p>

<p>For more information, see <a href="wdf.adding_a_device">Adding a Device</a>.</p>

<p>The following code example shows an implementation of the <a href="wdf.idriverentry_ondeviceadd">OnDeviceAdd</a> method of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff554885">IDriverEntry</a> interface. The framework calls <b>OnDeviceAdd</b> when a device is added to a computer.</p>

<p>The <b>IUnknown</b> interface that the driver supplies for the <i>pCallbackInterface</i> parameter can support several interfaces. The framework calls the <b>QueryInterface</b> method of the supplied <b>IUnknown</b> interface multiple times to retrieve the interfaces that the driver supports. The driver's <b>QueryInterface</b> method can return the following interfaces:</p><dl>
<dd>
<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff554902">IFileCallbackCleanup</a>
</p>
</dd>
<dd>
<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff554907">IFileCallbackClose</a>
</p>
</dd>
<dd>
<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff556754">IObjectCleanup</a>
</p>
</dd>
<dd>
<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff556762">IPnpCallback</a>
</p>
</dd>
<dd>
<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff556764">IPnpCallbackHardware</a>
</p>
</dd>
<dd>
<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh439727">IPnpCallbackHardware2</a>
</p>
</dd>
<dd>
<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh439744">IPnpCallbackHardwareInterrupt</a>
</p>
</dd>
<dd>
<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff556776">IPnpCallbackSelfManagedIo</a>
</p>
</dd>
<dd>
<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh439744">IPnpCallbackHardwareInterrupt</a>
</p>
</dd>
<dd>
<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff556776">IPnpCallbackSelfManagedIo</a>
</p>
</dd>
<dd>
<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff556815">IPowerPolicyCallbackWakeFromS0</a>
</p>
</dd>
<dd>
<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff556825">IPowerPolicyCallbackWakeFromSx</a>
</p>
</dd>
</dl><p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff554902">IFileCallbackCleanup</a>
</p>

<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff554907">IFileCallbackClose</a>
</p>

<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff556754">IObjectCleanup</a>
</p>

<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff556762">IPnpCallback</a>
</p>

<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff556764">IPnpCallbackHardware</a>
</p>

<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh439727">IPnpCallbackHardware2</a>
</p>

<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh439744">IPnpCallbackHardwareInterrupt</a>
</p>

<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff556776">IPnpCallbackSelfManagedIo</a>
</p>

<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh439744">IPnpCallbackHardwareInterrupt</a>
</p>

<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff556776">IPnpCallbackSelfManagedIo</a>
</p>

<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff556815">IPowerPolicyCallbackWakeFromS0</a>
</p>

<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff556825">IPowerPolicyCallbackWakeFromSx</a>
</p>

<p>When the device changes state, the framework calls the method that is related to the change (such as the <a href="https://msdn.microsoft.com/library/windows/hardware/ff556799">IPnpCallback::OnD0Entry</a> method) to notify the driver. </p>

<p>If the call to <b>CreateDevice</b> is successful, the driver must eventually call the <b>IWDFDevice::Release</b> method. Note that the framework has its own reference count on the object.</p>

<p>For more information, see <a href="wdf.adding_a_device">Adding a Device</a>.</p>

<p>The following code example shows an implementation of the <a href="wdf.idriverentry_ondeviceadd">OnDeviceAdd</a> method of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff554885">IDriverEntry</a> interface. The framework calls <b>OnDeviceAdd</b> when a device is added to a computer.</p>

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
<dt>Wudfddi.h (include Wudfddi.h)</dt>
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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff558893">IWDFDriver</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff554896">IDriverEntry::OnDeviceAdd</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff554902">IFileCallbackCleanup</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff554907">IFileCallbackClose</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff556754">IObjectCleanup</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff556762">IPnpCallback</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff556799">IPnpCallback::OnD0Entry</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff556764">IPnpCallbackHardware</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff556776">IPnpCallbackSelfManagedIo</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff556917">IWDFDevice</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff556965">IWDFDeviceInitialize</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20IWDFDriver::CreateDevice method%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
