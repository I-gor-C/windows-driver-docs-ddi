---
UID: NE.wudfusb._WDF_USB_REQUEST_TYPE~r1
title: WDF_USB_REQUEST_TYPE
author: windows-driver-content
description: The WDF_USB_REQUEST_TYPE enumeration contains values that identify a type of USB request object.
old-location: wdf\wdf_usb_request_type_umdf.htm
old-project: wdf
ms.assetid: fb952527-a8df-41e7-8194-b4a82b7f550f
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: WUDF_INTERRUPT_CONFIG, WUDF_INTERRUPT_CONFIG, *PWUDF_INTERRUPT_CONFIG
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: wudfusb.h
req.include-header: Wudfusb.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: WDF_USB_REQUEST_TYPE
req.alt-loc: wudfusb.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: 
req.iface: 
req.product: Windows 10 or later.
---

# WDF_USB_REQUEST_TYPE enumeration



## -description
<p class="CCE_Message">[<b>Warning:</b> UMDF 2 is the latest version of UMDF and supersedes UMDF 1.  All new UMDF drivers should be written using UMDF 2.  No new features are being added to UMDF 1 and there is limited support for UMDF 1 on newer versions of Windows 10.  Universal Windows drivers must use UMDF 2.  For more info, see <a href="https://docs.microsoft.com/en-us/windows-hardware/drivers/wdf/getting-started-with-umdf-version-2">Getting Started with UMDF</a>.]</p>
<p>
      The <a href="https://msdn.microsoft.com/library/windows/hardware/ff553055">WDF_USB_REQUEST_TYPE</a> enumeration contains values that identify a type of USB request object.</p>


## -syntax

````
typedef enum _WDF_USB_REQUEST_TYPE { 
  WdfUsbRequestTypeInvalid                = 0,
  WdfUsbRequestTypeNoFormat               = ( WdfUsbRequestTypeInvalid + 1 ),
  WdfUsbRequestTypeDeviceControlTransfer  = ( WdfUsbRequestTypeNoFormat + 1 ),
  WdfUsbRequestTypePipeWrite              = ( WdfUsbRequestTypeDeviceControlTransfer + 1 ),
  WdfUsbRequestTypePipeRead               = ( WdfUsbRequestTypePipeWrite + 1 )
} WDF_USB_REQUEST_TYPE, *PWDF_USB_REQUEST_TYPE;
````


## -enum-fields
<dl>

### -field <a id="WdfUsbRequestTypeInvalid"></a><a id="wdfusbrequesttypeinvalid"></a><a id="WDFUSBREQUESTTYPEINVALID"></a><b>WdfUsbRequestTypeInvalid</b>

<dd>
<p>The type of the request object is invalid. </p>
</dd>

### -field <a id="WdfUsbRequestTypeNoFormat"></a><a id="wdfusbrequesttypenoformat"></a><a id="WDFUSBREQUESTTYPENOFORMAT"></a><b>WdfUsbRequestTypeNoFormat</b>

<dd>
<p>The request object is not formatted.</p>
</dd>

### -field <a id="WdfUsbRequestTypeDeviceControlTransfer"></a><a id="wdfusbrequesttypedevicecontroltransfer"></a><a id="WDFUSBREQUESTTYPEDEVICECONTROLTRANSFER"></a><b>WdfUsbRequestTypeDeviceControlTransfer</b>

<dd>
<p>The request object is sent when the application calls the Win32 <b>DeviceIoControl</b> function on the file object that is associated with the target device. </p>
</dd>

### -field <a id="WdfUsbRequestTypePipeWrite"></a><a id="wdfusbrequesttypepipewrite"></a><a id="WDFUSBREQUESTTYPEPIPEWRITE"></a><b>WdfUsbRequestTypePipeWrite</b>

<dd>
<p>The request object is sent when the application calls the Win32 <b>WriteFile</b> or <b>WriteFileEx</b> function on the file object that is associated with the target device. </p>
</dd>

### -field <a id="WdfUsbRequestTypePipeRead"></a><a id="wdfusbrequesttypepiperead"></a><a id="WDFUSBREQUESTTYPEPIPEREAD"></a><b>WdfUsbRequestTypePipeRead</b>

<dd>
<p>The request object is sent when the application calls the Win32 <b>ReadFile</b> or <b>ReadFileEx</b> function on the file object that is associated with the target device. </p>
</dd>
</dl>

## -remarks


## -requirements
<table>
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
</table>