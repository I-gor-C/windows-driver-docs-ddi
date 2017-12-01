---
UID: NE.wdfiotarget._WDF_IO_TARGET_OPEN_TYPE
title: WDF_IO_TARGET_OPEN_TYPE
author: windows-driver-content
description: The WDF_IO_TARGET_OPEN_TYPE enumeration specifies how a driver identifies a remote I/O target when the driver calls WdfIoTargetOpen.
old-location: wdf\wdf_io_target_open_type.htm
old-project: wdf
ms.assetid: 27aa5d78-03ce-4fc9-b1c8-d02a760e2787
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: WDF_IO_QUEUE_FORWARD_PROGRESS_POLICY, WDF_IO_QUEUE_FORWARD_PROGRESS_POLICY, *PWDF_IO_QUEUE_FORWARD_PROGRESS_POLICY
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: wdfiotarget.h
req.include-header: Wdf.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 1.0
req.umdf-ver: 2.0
req.alt-api: WDF_IO_TARGET_OPEN_TYPE
req.alt-loc: wdfiotarget.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: PASSIVE_LEVEL
req.iface: 
req.product: Windows 10 or later.
---

# WDF_IO_TARGET_OPEN_TYPE enumeration



## -description
<p class="CCE_Message">[Applies to KMDF and UMDF]</p>
<p>The <b>WDF_IO_TARGET_OPEN_TYPE</b> enumeration specifies how a driver identifies a remote I/O target when the driver calls <a href="..\wdfiotarget\nf-wdfiotarget-wdfiotargetopen.md">WdfIoTargetOpen</a>.</p>


## -syntax

````
typedef enum _WDF_IO_TARGET_OPEN_TYPE { 
  WdfIoTargetOpenUndefined          = 0,
  WdfIoTargetOpenUseExistingDevice  = 1,
  WdfIoTargetOpenByName             = 2,
  WdfIoTargetOpenReopen             = 3,
  WdfIoTargetOpenLocalTargetByFile  = 4
} WDF_IO_TARGET_OPEN_TYPE;
````


## -enum-fields
<dl>

### -field <a id="WdfIoTargetOpenUndefined"></a><a id="wdfiotargetopenundefined"></a><a id="WDFIOTARGETOPENUNDEFINED"></a><b>WdfIoTargetOpenUndefined</b>

<dd>
<p>Reserved for system use.</p>
</dd>

### -field <a id="WdfIoTargetOpenUseExistingDevice"></a><a id="wdfiotargetopenuseexistingdevice"></a><a id="WDFIOTARGETOPENUSEEXISTINGDEVICE"></a><b>WdfIoTargetOpenUseExistingDevice</b>

<dd>
<p>This value is supported by KMDF only.</p>
<p>The driver is identifying a remote I/O target by supplying a pointer to a Windows Driver Model (WDM) <a href="..\wdm\ns-wdm--device-object.md">DEVICE_OBJECT</a> structure.</p>
</dd>

### -field <a id="WdfIoTargetOpenByName"></a><a id="wdfiotargetopenbyname"></a><a id="WDFIOTARGETOPENBYNAME"></a><b>WdfIoTargetOpenByName</b>

<dd>
<p>The driver is opening a remote I/O target by supplying a Unicode name string that represents an <a href="https://msdn.microsoft.com/b30e7475-7f94-4993-b373-8e4a8b1bcb4c">object name</a>. This name can identify a device, file, or device interface.</p>
</dd>

### -field <a id="WdfIoTargetOpenReopen"></a><a id="wdfiotargetopenreopen"></a><a id="WDFIOTARGETOPENREOPEN"></a><b>WdfIoTargetOpenReopen</b>

<dd>
<p>The driver is reopening a remote I/O target after previously calling <a href="..\wdfiotarget\nf-wdfiotarget-wdfiotargetcloseforqueryremove.md">WdfIoTargetCloseForQueryRemove</a>. For more information, see the following Remarks section.</p>
</dd>

### -field <a id="WdfIoTargetOpenLocalTargetByFile"></a><a id="wdfiotargetopenlocaltargetbyfile"></a><a id="WDFIOTARGETOPENLOCALTARGETBYFILE"></a><b>WdfIoTargetOpenLocalTargetByFile</b>

<dd>
<p>This value is supported by UMDF only.</p>
<p><b>UMDF </b>The driver is opening a file handle that represents the lower stack (just like a local target), so that it can send a driver-created request down to the lower stack. A UMDF driver specifies this value when it calls <a href="..\wdfiotarget\nf-wdfiotarget-wdf-io-target-open-params-init-open-by-file.md">WDF_IO_TARGET_OPEN_PARAMS_INIT_OPEN_BY_FILE</a>.</p>
</dd>
</dl>

## -remarks
<p>The <b>WDF_IO_TARGET_OPEN_TYPE</b> enumeration is used in the <b>Type</b> member of the <a href="..\wdfiotarget\ns-wdfiotarget--wdf-io-target-open-params.md">WDF_IO_TARGET_OPEN_PARAMS</a> structure.</p>

<p>The driver can specify <b>WdfIoTargetOpenReopen</b> only if it specified <b>WdfIoTargetOpenByName</b> when it originally opened the remote I/O target.</p>

<p>If <b>WdfIoTargetOpenReopen</b> is set, the framework ignores all other members of the <a href="..\wdfiotarget\ns-wdfiotarget--wdf-io-target-open-params.md">WDF_IO_TARGET_OPEN_PARAMS</a> structure and uses the values that the driver specified when it originally called <a href="..\wdfiotarget\nf-wdfiotarget-wdfiotargetopen.md">WdfIoTargetOpen</a> to open a remote I/O target.</p>

<p>By default (unless the driver specifies <b>UmdfFileObjectPolicy</b>=<b>AllowNullAndUnknownFileObjects</b> in its INF file), UMDF doesn’t allow processing of I/O requests that are not associated with a file object. 
Also, some driver stacks, such as HIDclass-enumerated collection PDOs, fail requests that have no associated file object.</p>

<p>Unlike app-created requests, driver-created requests sent to a local I/O target have no associated file object.  As a result, the framework or the lower driver might fail those requests.</p>

<p>In this situation, you can use <b>WdfIoTargetOpenLocalTargetByFile</b> to cause driver-created requests sent to a local target to be associated with the file object corresponding to that target.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Minimum KMDF version</p>
</th>
<td width="70%">
<p>1.0</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Minimum UMDF version</p>
</th>
<td width="70%">
<p>2.0</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Wdfiotarget.h (include Wdf.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\wdm\ns-wdm--device-object.md">DEVICE_OBJECT</a>
</dt>
<dt>
<a href="..\wdfiotarget\ns-wdfiotarget--wdf-io-target-open-params.md">WDF_IO_TARGET_OPEN_PARAMS</a>
</dt>
<dt>
<a href="..\wdfiotarget\nf-wdfiotarget-wdf-io-target-open-params-init-open-by-file.md">WDF_IO_TARGET_OPEN_PARAMS_INIT_OPEN_BY_FILE</a>
</dt>
<dt>
<a href="..\wdfiotarget\nf-wdfiotarget-wdfiotargetcloseforqueryremove.md">WdfIoTargetCloseForQueryRemove</a>
</dt>
<dt>
<a href="..\wdfiotarget\nf-wdfiotarget-wdfiotargetopen.md">WdfIoTargetOpen</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20WDF_IO_TARGET_OPEN_TYPE enumeration%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
