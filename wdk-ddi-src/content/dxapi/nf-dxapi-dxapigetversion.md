---
UID: NF.dxapi.DxApiGetVersion
title: DxApiGetVersion
author: windows-driver-content
description: Do not use the DxApiGetVersion function; use the DxApi function along with the DD_DXAPI_GETVERSIONNUMBER function identifier instead.The DxApiGetVersion function returns a Direct Sound version number of 4.02.
old-location: display\dxapigetversion.htm
ms.assetid: f9d441a5-46b5-4da8-aa7e-f4f45eb733d4
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: display
req.header: dxapi.h
req.include-header: Dxapi.h
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: DxApiGetVersion
req.alt-loc: Dxapi.lib,Dxapi.dll
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Dxapi.lib
req.dll: 
req.irql: 
ms.keywords: DxApiGetVersion
req.iface: 
---

# DxApiGetVersion function



## -description
<p>Do not use the <b>DxApiGetVersion</b> function; use the <a href="https://msdn.microsoft.com/library/windows/hardware/ff557364">DxApi</a> function along with the <a href="https://msdn.microsoft.com/library/windows/hardware/ff550637">DD_DXAPI_GETVERSIONNUMBER</a> function identifier instead.</p>
<p>The <b>DxApiGetVersion</b> function returns a Direct Sound version number of 4.02.</p>


## -syntax

````
ULONG DxApiGetVersion(void);
````


## -parameters


## -returns
<p>Returns the major and minor version numbers of Direct Sound as 4 and 2 respectively.</p>

<p>Returns the major and minor version numbers of Direct Sound as 4 and 2 respectively.</p>

<p>Returns the major and minor version numbers of Direct Sound as 4 and 2 respectively.</p>

## -remarks


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
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Dxapi.h (include Dxapi.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Library</p>
</th>
<td width="70%">
<dl>
<dt>Dxapi.lib</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff550637">DD_DXAPI_GETVERSIONNUMBER</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff549530">DDGETVERSIONNUMBER</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff557364">DxApi</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20DxApiGetVersion function%20 RELEASE:%20(10/25/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
