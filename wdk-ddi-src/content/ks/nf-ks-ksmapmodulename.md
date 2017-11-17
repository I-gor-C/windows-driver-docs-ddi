---
UID: NF.ks.KsMapModuleName
title: KsMapModuleName
author: windows-driver-content
description: The KsMapModuleName function returns the image name and resource identifier that corresponds to the PhysicalDeviceObject and ModuleName parameters.
old-location: stream\ksmapmodulename.htm
ms.assetid: 3223a1bb-ab6c-45d7-9f9a-367a3aa7d465
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: stream
req.header: ks.h
req.include-header: Ks.h
req.target-type: Universal
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: KsMapModuleName
req.alt-loc: Ks.lib,Ks.dll
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Ks.lib
req.dll: 
req.irql: 
ms.keywords: KsMapModuleName
req.iface: 
---

# KsMapModuleName function



## -description
<p>The <b>KsMapModuleName</b> function returns the image name and resource identifier that corresponds to the <i>PhysicalDeviceObject </i>and<i> ModuleName </i>parameters. </p>


## -syntax

````
NTSTATUS KsMapModuleName(
  _In_  PDEVICE_OBJECT  PhysicalDeviceObject,
  _In_  PUNICODE_STRING ModuleName,
  _Out_ PUNICODE_STRING ImageName,
  _Out_ PULONG_PTR      ResourceId,
  _Out_ PULONG          ValueType
);
````


## -parameters
<dl>

### -param <i>PhysicalDeviceObject</i> [in]

<dd>
<p>Pointer to a DEVICE_OBJECT for which to return the requested information.</p>
</dd>

### -param <i>ModuleName</i> [in]

<dd>
<p>Pointer to a buffer that contains the module name for which to return the requested information.</p>
</dd>

### -param <i>ImageName</i> [out]

<dd>
<p>A caller-allocated buffer that receives the image name for the specified resource.</p>
</dd>

### -param <i>ResourceId</i> [out]

<dd>
<p>Pointer to a caller-supplied variable that receives the resource identifier.</p>
</dd>

### -param <i>ValueType</i> [out]

<dd>
<p>Pointer to a location into which the function returns the value type of the specified resource.</p>
</dd>
</dl>

## -returns
<p><b>KsMapModuleName</b> returns STATUS_SUCCESS if the requested values are found; otherwise, the routine returns an error code.</p>

## -remarks


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
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ks.h (include Ks.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Library</p>
</th>
<td width="70%">
<dl>
<dt>Ks.lib</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff562634">KsGetImageNameAndResourceId</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [stream\stream]:%20KsMapModuleName function%20 RELEASE:%20(10/25/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
