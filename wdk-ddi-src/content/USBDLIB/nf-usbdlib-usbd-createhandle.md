---
UID: NF.usbdlib.USBD_CreateHandle
title: USBD_CreateHandle
author: windows-driver-content
description: The USBD_CreateHandle routine is called by a WDM USB client driver to obtain a USBD handle. The routine registers the client driver with the underlying USB driver stack.
old-location: buses\usbd_register.htm
ms.assetid: 97757CBA-8291-40A3-B247-D41E7FEB1D7C
ms.author: windowsdriverdev
ms.date: 11/3/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: usbref
req.header: usbdlib.h
req.include-header: 
req.target-type: Desktop
req.target-min-winverclnt: Requires WDK for Windows 8. Targets Windows Vista and later versions of the Windows operating system.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: USBD_CreateHandle
req.alt-loc: Usbdex.lib,Usbdex.dll,Ntstrsafe.lib,Ntstrsafe.dll
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Usbdex.lib; 
Ntstrsafe.lib
req.dll: 
req.irql: PASSIVE_LEVEL
ms.keywords: USBD_CreateHandle
req.iface: 
req.product: Windows 10 or later.
---

# USBD_CreateHandle function



## -description
<p>The  <b>USBD_CreateHandle</b> routine is called by a WDM USB client driver to obtain a USBD handle. The routine registers the client driver with the underlying USB driver stack.</p>
<p><b>Note for Windows Driver Framework (WDF) Drivers:  </b>If your client driver is a WDF-based driver, then you do not need the USBD handle. The client driver is registered in its call to the the <a href="https://msdn.microsoft.com/library/windows/hardware/hh439428">WdfUsbTargetDeviceCreateWithParameters</a> method.</p>


## -syntax

````
NTSTATUS USBD_CreateHandle(
  _In_  PDEVICE_OBJECT DeviceObject,
  _In_  PDEVICE_OBJECT TargetDeviceObject,
  _In_  ULONG          USBDClientContractVersion,
  _In_  ULONG          PoolTag,
  _Out_ USBD_HANDLE    *USBDHandle
);
````


## -parameters
<dl>

### -param <i>DeviceObject</i> [in]

<dd>
<p>Pointer to the device object for the client driver.</p>
</dd>

### -param <i>TargetDeviceObject</i> [in]

<dd>
<p>Pointer to the next lower device object in the device stack. The client driver receives a pointer to that device object in a previous call to <a href="https://msdn.microsoft.com/library/windows/hardware/ff548300">IoAttachDeviceToDeviceStack</a>.</p>
</dd>

### -param <i>USBDClientContractVersion</i> [in]

<dd>
<p>The contract version that the client driver supports. <i>USBDClientContractVersion</i> must be  USBD_CLIENT_CONTRACT_VERSION_602. For more information, see Remarks.</p>
</dd>

### -param <i>PoolTag</i> [in]

<dd>
<p>The pool tag used for memory allocations.</p>
</dd>

### -param <i>USBDHandle</i> [out]

<dd>
<p>Opaque handle that indicates that the client driver was registered with the USB driver stack. For more information, see Remarks.</p>
</dd>
</dl>

## -returns
<p>The routine returns an NTSTATUS code. Possible  values include but are not limited to, these values in the following table.</p><dl>
<dt><b>STATUS_SUCCESS</b></dt>
</dl><p>The routine call succeeded.</p><dl>
<dt><b>STATUS_INVALID_LEVEL</b></dt>
</dl><p>The caller is not running at the IRQL value PASSIVE_LEVEL.</p><dl>
<dt><b>STATUS_INVALID_PARAMETER</b></dt>
</dl><p>The caller passed one of the following invalid parameter values:</p>

<p> </p>

## -remarks
<p>Windows 8 includes a new USB driver stack to support USB 3.0 devices. The new USB driver stack provides several new capabilities, such as stream support, chained MDLs, and so on. 
Before your client driver can use any of those USB capabilities, you must register the client driver with the USB driver stack and obtain a USBD handle. The handle is required in order to call routines that use or configure the new capabilities. To obtain a USBD handle, call <b>USBD_CreateHandle</b>. </p>

<p>The client driver must call <b>USBD_CreateHandle</b> regardless of whether the device is attached to a USB 3.0, 2.0, or 1.1 host controller. If the device is attached to a USB 3.0 host controller, Windows loads the USB 3.0 driver stack. Otherwise, USB 2.0 driver stack is loaded.   In either case, the client driver is <i>not</i> required to know the version supported by the underlying USB driver stack. <b>USBD_CreateHandle</b> assesses the driver stack version and allocates resources appropriately. </p>

<p>The client driver must specify  USBD_CLIENT_CONTRACT_VERSION_602 in the <i>USBDClientContractVersion</i> parameter and follow the set of rules described in <a href="https://msdn.microsoft.com/library/windows/hardware/hh406258">Best Practices: Using URBs</a>. </p>

<p>The <b>USBD_CreateHandle</b> routine must be called by a Windows Driver Model (WDM) client driver before the driver  send any other requests, through URBs or IOCTLs, to the USB driver stack. Typically, the client driver obtains the USBD handle in its  AddDevice routine.   </p>

<p>A Windows Driver Frameworks (WDF) client driver is not required to call <b>USBD_CreateHandle</b> because the framework calls this routine on behalf of the client driver during the device initialization phase. Instead, the client driver can specify its client contract version in the <a href="https://msdn.microsoft.com/library/windows/hardware/hh406503">WDF_USB_DEVICE_CREATE_CONFIG</a> structure and pass it in the call to <a href="https://msdn.microsoft.com/library/windows/hardware/hh439428">WdfUsbTargetDeviceCreateWithParameters</a>.</p>

<p>If the  <b>USBD_CreateHandle</b> call succeeds,  a valid <i>USBD handle</i> is obtained in the <i>USBDHandle</i> parameter. The client driver must use the USBD handle in the client driver's future requests to the USB driver stack. </p>

<p>If the <b>USBD_CreateHandle</b> call fails,  the client driver can fail the AddDevice routine.</p>

<p>After the client driver is finished using the USBD handle, the driver must close the handle  by calling the <a href="https://msdn.microsoft.com/library/windows/hardware/hh406248">USBD_CloseHandle</a> routine.</p>

<p>The following example code shows how to register a client driver by calling <b>USBD_CreateHandle</b>.</p>

<p>Windows 8 includes a new USB driver stack to support USB 3.0 devices. The new USB driver stack provides several new capabilities, such as stream support, chained MDLs, and so on. 
Before your client driver can use any of those USB capabilities, you must register the client driver with the USB driver stack and obtain a USBD handle. The handle is required in order to call routines that use or configure the new capabilities. To obtain a USBD handle, call <b>USBD_CreateHandle</b>. </p>

<p>The client driver must call <b>USBD_CreateHandle</b> regardless of whether the device is attached to a USB 3.0, 2.0, or 1.1 host controller. If the device is attached to a USB 3.0 host controller, Windows loads the USB 3.0 driver stack. Otherwise, USB 2.0 driver stack is loaded.   In either case, the client driver is <i>not</i> required to know the version supported by the underlying USB driver stack. <b>USBD_CreateHandle</b> assesses the driver stack version and allocates resources appropriately. </p>

<p>The client driver must specify  USBD_CLIENT_CONTRACT_VERSION_602 in the <i>USBDClientContractVersion</i> parameter and follow the set of rules described in <a href="https://msdn.microsoft.com/library/windows/hardware/hh406258">Best Practices: Using URBs</a>. </p>

<p>The <b>USBD_CreateHandle</b> routine must be called by a Windows Driver Model (WDM) client driver before the driver  send any other requests, through URBs or IOCTLs, to the USB driver stack. Typically, the client driver obtains the USBD handle in its  AddDevice routine.   </p>

<p>A Windows Driver Frameworks (WDF) client driver is not required to call <b>USBD_CreateHandle</b> because the framework calls this routine on behalf of the client driver during the device initialization phase. Instead, the client driver can specify its client contract version in the <a href="https://msdn.microsoft.com/library/windows/hardware/hh406503">WDF_USB_DEVICE_CREATE_CONFIG</a> structure and pass it in the call to <a href="https://msdn.microsoft.com/library/windows/hardware/hh439428">WdfUsbTargetDeviceCreateWithParameters</a>.</p>

<p>If the  <b>USBD_CreateHandle</b> call succeeds,  a valid <i>USBD handle</i> is obtained in the <i>USBDHandle</i> parameter. The client driver must use the USBD handle in the client driver's future requests to the USB driver stack. </p>

<p>If the <b>USBD_CreateHandle</b> call fails,  the client driver can fail the AddDevice routine.</p>

<p>After the client driver is finished using the USBD handle, the driver must close the handle  by calling the <a href="https://msdn.microsoft.com/library/windows/hardware/hh406248">USBD_CloseHandle</a> routine.</p>

<p>The following example code shows how to register a client driver by calling <b>USBD_CreateHandle</b>.</p>

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
<p>Version</p>
</th>
<td width="70%">
<p>Requires WDK for Windows 8. Targets Windows Vista and later versions of the Windows operating system.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Usbdlib.h</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Library</p>
</th>
<td width="70%">
<dl>
<dt>Usbdex.lib; </dt>
<dt>Ntstrsafe.lib</dt>
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
<a href="https://msdn.microsoft.com/library/windows/hardware/hh406248">USBD_CloseHandle</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh406258">Best Practices: Using URBs</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh450844">Allocating and Building URBs</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [usbref\buses]:%20USBD_CreateHandle routine%20 RELEASE:%20(11/3/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
