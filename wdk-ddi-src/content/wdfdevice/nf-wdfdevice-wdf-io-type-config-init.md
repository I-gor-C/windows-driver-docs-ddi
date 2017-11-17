---
UID: NF.wdfdevice.WDF_IO_TYPE_CONFIG_INIT
title: WDF_IO_TYPE_CONFIG_INIT
author: windows-driver-content
description: The WDF_IO_TYPE_CONFIG_INIT function initializes a driver's WDF_IO_TYPE_CONFIG structure.
old-location: wdf\wdf_io_type_config_init.htm
ms.assetid: 45D60409-EAE5-43A0-9E90-0B2F9FC31840
ms.author: windowsdriverdev
ms.date: 11/2/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: wdf
req.header: wdfdevice.h
req.include-header: Wdf.h
req.target-type: Universal
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 1.13
req.umdf-ver: 2.0
req.alt-api: WDF_IO_TYPE_CONFIG_INIT
req.alt-loc: wdfdevice.h
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
ms.keywords: WDF_IO_TYPE_CONFIG_INIT
req.iface: 
req.product: Windows 10 or later.
---

# WDF_IO_TYPE_CONFIG_INIT function



## -description
<p class="CCE_Message">[Applies to KMDF and UMDF]</p>
<p>The <b>WDF_IO_TYPE_CONFIG_INIT</b> function initializes a driver's <a href="https://msdn.microsoft.com/library/windows/hardware/dn265642">WDF_IO_TYPE_CONFIG</a> structure.</p>


## -syntax

````
void WDF_IO_TYPE_CONFIG_INIT(
  _Out_ PWDF_IO_TYPE_CONFIG IoTypeConfig
);
````


## -parameters
<dl>

### -param <i>IoTypeConfig</i> [out]

<dd>
<p>A pointer to a driver-allocated <a href="https://msdn.microsoft.com/library/windows/hardware/dn265642">WDF_IO_TYPE_CONFIG</a> structure.</p>
</dd>
</dl>

## -returns
<p>This function does not return a value.</p>

## -remarks
<p>The <b>WDF_IO_TYPE_CONFIG_INIT</b> function zeros the specified <a href="https://msdn.microsoft.com/library/windows/hardware/dn265642">WDF_IO_TYPE_CONFIG</a> structure and sets the  structure's <b>Size</b> member. It then sets the <b>ReadWriteIoType</b> member to <b>WdfDeviceIoBuffered</b>, and the <b>DeviceControlIoType</b> member to <b>WdfDeviceIoBuffered</b>.</p>

<p>For a code example that uses <b>WDF_IO_TYPE_CONFIG_INIT</b>, see <a href="https://msdn.microsoft.com/library/windows/hardware/dn265604">WdfDeviceInitSetIoTypeEx</a>.</p>

<p>The <b>WDF_IO_TYPE_CONFIG_INIT</b> function zeros the specified <a href="https://msdn.microsoft.com/library/windows/hardware/dn265642">WDF_IO_TYPE_CONFIG</a> structure and sets the  structure's <b>Size</b> member. It then sets the <b>ReadWriteIoType</b> member to <b>WdfDeviceIoBuffered</b>, and the <b>DeviceControlIoType</b> member to <b>WdfDeviceIoBuffered</b>.</p>

<p>For a code example that uses <b>WDF_IO_TYPE_CONFIG_INIT</b>, see <a href="https://msdn.microsoft.com/library/windows/hardware/dn265604">WdfDeviceInitSetIoTypeEx</a>.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Target platform</p>
</th>
<td width="70%">
<dl>
<dt><a href="http://go.microsoft.com/fwlink/p/?linkid=531356" target="_blank">Universal</a></dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Minimum KMDF version</p>
</th>
<td width="70%">
<p>1.13</p>
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
<dt>Wdfdevice.h (include Wdf.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/dn265642">WDF_IO_TYPE_CONFIG</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/dn265604">WdfDeviceInitSetIoTypeEx</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20WDF_IO_TYPE_CONFIG_INIT function%20 RELEASE:%20(11/2/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
