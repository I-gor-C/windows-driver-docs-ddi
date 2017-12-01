---
UID: NF.dispmprt.DxgkInitialize
title: DxgkInitialize
author: windows-driver-content
description: The DxgkInitialize function loads and initializes the DirectX graphics kernel subsystem (Dxgkrnl.sys).
old-location: display\dxgkinitialize.htm
old-project: display
ms.assetid: 0eda4184-2852-4a31-b4da-1fbb99ed4670
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: DxgkInitialize
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: dispmprt.h
req.include-header: Dispmprt.h
req.target-type: Desktop
req.target-min-winverclnt: Available in Windows Vista and later versions of the Windows operating systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: DxgkInitialize
req.alt-loc: dispmprt.h
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
---

# DxgkInitialize function



## -description
<p>The <b>DxgkInitialize</b> function loads and initializes the DirectX graphics kernel subsystem (<i>Dxgkrnl.sys</i>).</p>


## -syntax

````
NTSTATUS DxgkInitialize(
  _In_ PDRIVER_OBJECT              DriverObject,
  _In_ PUNICODE_STRING             RegistryPath,
  _In_ PDRIVER_INITIALIZATION_DATA DriverInitializationData
);
````


## -parameters
<dl>

### -param <i>DriverObject</i> [in]

<dd>
<p>A pointer to a <a href="..\wdm\ns-wdm--driver-object.md">DRIVER_OBJECT</a> structure. The display miniport driver previously obtained this pointer in its <a href="display.driverentry_of_display_miniport_driver">DriverEntry</a> function.</p>
</dd>

### -param <i>RegistryPath</i> [in]

<dd>
<p>A pointer to a <a href="..\wudfwdm\ns-wudfwdm--unicode-string.md">UNICODE_STRING</a> structure that supplies the path to the driver's service registry key.  The display miniport driver previously obtained this pointer in its <a href="..\wdm\ns-wdm--driver-object.md">DRIVER_OBJECT</a> function.</p>
</dd>

### -param <i>DriverInitializationData</i> [in]

<dd>
<p>A pointer to a <a href="..\dispmprt\ns-dispmprt--driver-initialization-data.md">DRIVER_INITIALIZATION_DATA</a> structure that supplies the DirectX graphics kernel subsystem with pointers to functions implemented by the display miniport driver.</p>
</dd>
</dl>

## -returns
<p><b>DxgkInitialize</b>returns STATUS_SUCCESS if it succeeds; otherwise, it returns one of the error codes defined in <i>Ntstatus.h</i>.</p>

## -remarks
<p>The display miniport driver's <a href="display.driverentry_of_display_miniport_driver">DriverEntry</a> function calls <b>DxgkInitialize</b>.</p>

<p>The following code example shows an implementation of <a href="display.driverentry_of_display_miniport_driver">DriverEntry</a> in which <b>DxgkInitialize</b> is called.</p>

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
<p>Available in Windows Vista and later versions of the Windows operating systems.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Dispmprt.h (include Dispmprt.h)</dt>
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
<a href="display.driverentry_of_display_miniport_driver">DriverEntry of Display Miniport Driver</a>
</dt>
<dt>
<a href="..\dispmprt\ns-dispmprt--driver-initialization-data.md">DRIVER_INITIALIZATION_DATA</a>
</dt>
<dt>
<a href="..\wdm\ns-wdm--driver-object.md">DRIVER_OBJECT</a>
</dt>
<dt>
<a href="..\wudfwdm\ns-wudfwdm--unicode-string.md">UNICODE_STRING</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20DxgkInitialize function%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
