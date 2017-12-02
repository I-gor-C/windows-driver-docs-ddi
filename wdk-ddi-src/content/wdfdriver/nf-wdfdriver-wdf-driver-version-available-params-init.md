---
UID: NF.wdfdriver.WDF_DRIVER_VERSION_AVAILABLE_PARAMS_INIT
title: WDF_DRIVER_VERSION_AVAILABLE_PARAMS_INIT
author: windows-driver-content
description: The WDF_DRIVER_VERSION_AVAILABLE_PARAMS_INIT function initializes a WDF_DRIVER_VERSION_AVAILABLE_PARAMS structure.
old-location: wdf\wdf_driver_version_available_params_init.htm
old-project: wdf
ms.assetid: aba3844e-745d-4d2c-9855-0535f53d7b0a
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: WDF_DRIVER_VERSION_AVAILABLE_PARAMS_INIT
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: wdfdriver.h
req.include-header: Wdf.h
req.target-type: Universal
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 1.0
req.umdf-ver: 2.0
req.alt-api: WDF_DRIVER_VERSION_AVAILABLE_PARAMS_INIT
req.alt-loc: wdfdriver.h
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

# WDF_DRIVER_VERSION_AVAILABLE_PARAMS_INIT function



## -description
<p class="CCE_Message">[Applies to KMDF and UMDF]</p>
<p>The WDF_DRIVER_VERSION_AVAILABLE_PARAMS_INIT function initializes a <a href="..\wdfdriver\ns-wdfdriver--wdf-driver-version-available-params.md">WDF_DRIVER_VERSION_AVAILABLE_PARAMS</a> structure.</p>


## -syntax

````
VOID WDF_DRIVER_VERSION_AVAILABLE_PARAMS_INIT(
  _Out_ PWDF_DRIVER_VERSION_AVAILABLE_PARAMS Params,
  _In_  ULONG                                MajorVersion,
  _In_  ULONG                                MinorVersion
);
````


## -parameters
<dl>

### -param Params [out]

<dd>
<p>A pointer to a <a href="..\wdfdriver\ns-wdfdriver--wdf-driver-version-available-params.md">WDF_DRIVER_VERSION_AVAILABLE_PARAMS</a> structure.</p>
</dd>

### -param MajorVersion [in]

<dd>
<p>A numeric value that represents the Kernel-Mode Driver Framework library's major version number.</p>
</dd>

### -param MinorVersion [in]

<dd>
<p>A numeric value that represents the Kernel-Mode Driver Framework library's minor version number.</p>
</dd>
</dl>

## -returns
<p>None</p>

## -remarks
<p>The WDF_DRIVER_VERSION_AVAILABLE_PARAMS_INIT function zeros the <a href="..\wdfdriver\ns-wdfdriver--wdf-driver-version-available-params.md">WDF_DRIVER_VERSION_AVAILABLE_PARAMS</a> structure that the <i>Params</i> parameter points to and sets the structure's <b>Size</b> member. Then, this function sets the structure's <b>MajorVersion</b> and <b>MinorVersion</b> members to the specified values.</p>

<p>For a code example that uses WDF_DRIVER_VERSION_AVAILABLE_PARAMS_INIT, see <a href="..\wdfdriver\nf-wdfdriver-wdfdriverisversionavailable.md">WdfDriverIsVersionAvailable</a>.</p>

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
<dt>Wdfdriver.h (include Wdf.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\wdfdriver\ns-wdfdriver--wdf-driver-version-available-params.md">WDF_DRIVER_VERSION_AVAILABLE_PARAMS</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20WDF_DRIVER_VERSION_AVAILABLE_PARAMS_INIT function%20 RELEASE:%20(11/30/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
