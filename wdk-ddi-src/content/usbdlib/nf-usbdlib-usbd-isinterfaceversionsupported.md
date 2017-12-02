---
UID: NF.usbdlib.USBD_IsInterfaceVersionSupported
title: USBD_IsInterfaceVersionSupported
author: windows-driver-content
description: The USBD_IsInterfaceVersionSupported routine is called by a USB client driver to check whether the underlying USB driver stack supports a particular USBD interface version.
old-location: buses\usbd_isusbdinterfaceversionsupported.htm
old-project: usbref
ms.assetid: AEA5B6AA-8EEA-4D82-9991-1DE32BAE7DCE
ms.author: windowsdriverdev
ms.date: 11/20/2017
ms.keywords: USBD_IsInterfaceVersionSupported
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: usbdlib.h
req.include-header: 
req.target-type: Desktop
req.target-min-winverclnt: Requires WDK for Windows 8. Targets Windows Vista and later versions of the Windows operating system.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: USBD_IsInterfaceVersionSupported
req.alt-loc: Usbdex.lib,Usbdex.dll
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Usbdex.lib
req.dll: 
req.irql: PASSIVE_LEVEL
req.iface: 
req.product: Windows 10 or later.
---

# USBD_IsInterfaceVersionSupported function



## -description
<p>The <b>USBD_IsInterfaceVersionSupported</b> routine is called by a USB client driver to check whether the underlying USB driver stack supports a particular USBD interface version.</p>


## -syntax

````
BOOLEAN USBD_IsInterfaceVersionSupported(
  _In_ USBD_HANDLE USBDHandle,
  _In_ LONG        USBDInterfaceVersion
);
````


## -parameters
<dl>

### -param USBDHandle [in]

<dd>
<p>USBD handle that is retrieved by the client driver in a previous call to  the <a href="..\usbdlib\nf-usbdlib-usbd-createhandle.md">USBD_CreateHandle</a> routine.</p>
</dd>

### -param USBDInterfaceVersion [in]

<dd>
<p>A 	LONG value that represents the USBD interface version to check against the USB driver stack. Possible values include  USBD_INTERFACE_VERSION_602 or USBD_INTERFACE_VERSION_600. For more information, see Remarks.</p>
</dd>
</dl>

## -returns
<p><b>USBD_IsInterfaceVersionSupported</b> returns TRUE if the specified USBD interface version is supported by the USB driver stack; FALSE otherwise.  For more information, see Remarks.</p>

## -remarks
<p>The USB driver stack loaded for a device depends on the version of Windows, the host controller hardware, and the USB device. Windows 7  and earlier versions of Windows support USBD_INTERFACE_VERSION_600. The USBD interface versions, supported by the Windows 8 driver stack, are USBD_INTERFACE_VERSION_602 and USBD_INTERFACE_VERSION_600. A USB client driver rarely needs to know about the underlying driver stack's  interface version. In cases where such information is required, the client driver can call the <b>USBD_IsInterfaceVersionSupported</b> routine to check whether a particular interface version is supported by the underlying driver stack. For instance, the client driver calls <b>USBD_IsInterfaceVersionSupported</b> to determine whether the driver stack supports USBD_INTERFACE_VERSION_602. If it supports that version, the routine returns TRUE.</p>

<p>The routine requires a valid USBD handle (obtained in a previous call to <a href="..\usbdlib\nf-usbdlib-usbd-createhandle.md">USBD_CreateHandle</a>).  <b>USBD_IsInterfaceVersionSupported</b> can only  be called by client drivers that target Windows Vista and later versions of Windows. Those client drivers must get Windows Driver Kit (WDK) for Windows 8 in order to call the routines successfully.  <b>USBD_IsInterfaceVersionSupported</b> replaces the <a href="..\usbdlib\nf-usbdlib-usbd-getusbdiversion.md">USBD_GetUSBDIVersion</a>  routine. </p>

<p>The USBD interface version does not indicate the capabilities supported by the USB driver stack. For example just because the underlying driver stack supports  USBD_INTERFACE_VERSION_602, the client driver <i>must not</i> assume that the driver can use the static streams capability. That is because, even though the driver stack supports the capability, the host controller hardware or the USB device might not support streams. To determine whether the USB driver stack supports a certain capability, call <a href="buses.usbd_getcapability">USBD_QueryUsbCapability</a>.</p>

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
<dt>Usbdex.lib</dt>
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