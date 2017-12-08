---
UID: NF.wiamdef.WIAS_HRESULT
title: WIAS_HRESULT macro
author: windows-driver-content
description: The WIAS_HRESULT macro writes a diagnostic message to the Wiatrace.log file.
old-location: image\wias_hresult.htm
old-project: image
ms.assetid: e340eb98-34d4-49e7-92cd-4f57d8b6efb8
ms.author: windowsdriverdev
ms.date: 12/6/2017
ms.keywords: WIAS_HRESULT
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: macro
req.header: wiamdef.h
req.include-header: Wiamdef.h
req.target-type: Desktop
req.target-min-winverclnt: Available in Windows Vista and later versions of the operating system.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: WIAS_HRESULT
req.alt-loc: Wiamdef.h
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
req.product: Windows 10 or later.
---

# WIAS_HRESULT macro



## -description
The WIAS_HRESULT macro writes a diagnostic message to the <i>Wiatrace.log</i> file.


## -syntax

````
HRESULT WIAS_HRESULT(
   HINSTANCE hInstance,
   HRESULT   hr
);
````


## -parameters

### -param hInstance 

Handle to the calling driver. 

### -param hr 

Specifies the HRESULT value to be printed.

## -remarks
This macro is the recommended way to output HRESULTS on Windows Vista.

## -requirements
<table>
<tr>
<th width="30%">
Target platform
</th>
<td width="70%">
<dl>
<dt>Desktop</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
Version
</th>
<td width="70%">
Available in Windows Vista and later versions of the operating system.
</td>
</tr>
<tr>
<th width="30%">
Header
</th>
<td width="70%">
<dl>
<dt>Wiamdef.h (include Wiamdef.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="image.wias_assert">WIAS_ASSERT</a>
</dt>
<dt>
<a href="image.wias_error">WIAS_ERROR</a>
</dt>
<dt>
<a href="image.wias_trace">WIAS_TRACE</a>
</dt>
</dl>
 
 
<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [image\image]:%20WIAS_HRESULT macro%20 RELEASE:%20(12/6/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>
