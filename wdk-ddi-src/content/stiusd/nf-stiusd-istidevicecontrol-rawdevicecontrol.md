---
UID: NF.stiusd.IStiDeviceControl.RawDeviceControl
title: IStiDeviceControl::RawDeviceControl
author: windows-driver-content
description: This topic describes the RawDeviceControl method.
old-location: image\istidevicecontrol_rawdevicecontrol.htm
old-project: image
ms.assetid: 107C7EB4-9C72-49CF-A330-7D517CC67F35
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: IStiDeviceControl, RawDeviceControl, IStiDeviceControl::RawDeviceControl
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: stiusd.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IStiDeviceControl.RawDeviceControl
req.alt-loc: Stiusd.h
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
req.iface: IStiDeviceControl
req.product: Windows 10 or later.
---

# IStiDeviceControl::RawDeviceControl method



## -description
<p>This topic describes the <b>RawDeviceControl</b> method.</p>


## -syntax

````
HRESULT RawDeviceControl(
   USD_CONTROL_CODE EscapeFunction,
   LPVOID           lpInData,
   DWORD            cbInDataSize,
   LPVOID           pOutData,
   DWORD            dwOutDataSize,
   LPDWORD          pdwActualData
);
````


## -parameters
<dl>

### -param <i>EscapeFunction</i> 

<dd>
<p>Defines the <b>USD_CONTROL_CODE</b> parameter <i>EscapeFunction.</i></p>
</dd>

### -param <i>lpInData</i> 

<dd>
<p>Defines the <b>LPVOID</b> parameter <i>lpInData.</i></p>
</dd>

### -param <i>cbInDataSize</i> 

<dd>
<p>Defines the <b>DWORD</b> parameter <i>cbInDataSize.</i></p>
</dd>

### -param <i>pOutData</i> 

<dd>
<p>Defines the <b>LPVOID</b> parameter <i>pOutData.</i></p>
</dd>

### -param <i>dwOutDataSize</i> 

<dd>
<p>Defines the <b>DWORD</b> parameter <i>dwOutDataSize.</i></p>
</dd>

### -param <i>pdwActualData</i> 

<dd>
<p>Defines the <b>LPDWORD</b> parameter <i>pdwActualData.</i></p>
</dd>
</dl>

## -returns
<p>Defines the <b>HRESULT</b> return value.</p>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Stiusd.h</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="image.istidevicecontrol">IStiDeviceControl</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [image\image]:%20IStiDeviceControl::RawDeviceControl method%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
