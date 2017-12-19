---
UID: NF.ks.KsPinGetDevice
title: KsPinGetDevice function
author: windows-driver-content
description: The KsPinGetDevice function returns the AVStream device to which Pin belongs.
old-location: stream\kspingetdevice.htm
old-project: stream
ms.assetid: 965aa806-90cc-4c82-a126-42ae433cba3b
ms.author: windowsdriverdev
ms.date: 12/14/2017
ms.keywords: KsPinGetDevice
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: ks.h
req.include-header: Ks.h
req.target-type: Desktop
req.target-min-winverclnt: Available in Microsoft Windows XP and later operating systems and DirectX 8.0 and later DirectX versions.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: KsPinGetDevice
req.alt-loc: ks.h
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
---

# KsPinGetDevice function



## -description
The<b> KsPinGetDevice </b>function returns the AVStream device to which <i>Pin</i> belongs.



## -syntax

````
PKSDEVICE __inline KsPinGetDevice(
  _In_ PKSPIN Pin
);
````


## -parameters

### -param Pin [in]

A pointer to a <a href="stream.kspin">KSPIN</a> structure representing the pin for which to return the owning AVStream device.


## -returns
<b>KsPinGetDevice </b>returns a pointer to a <a href="stream.ksdevice">KSDEVICE</a> structure representing the AVStream device to which <i>Pin</i> belongs.


## -remarks
This call is an inline function call to <a href="stream.ksgetdevice">KsGetDevice</a>.


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
Available in Microsoft Windows XP and later operating systems and DirectX 8.0 and later DirectX versions.

</td>
</tr>
<tr>
<th width="30%">
Header

</th>
<td width="70%">
<dl>
<dt>Ks.h (include Ks.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
IRQL

</th>
<td width="70%">
PASSIVE_LEVEL

</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="stream.kspin">KSPIN</a>
</dt>
<dt>
<a href="stream.ksdevice">KSDEVICE</a>
</dt>
<dt>
<a href="stream.ksgetdevice">KsGetDevice</a>
</dt>
<dt>
<a href="stream.ksdevice_descriptor">KSDEVICE_DESCRIPTOR</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [stream\stream]:%20KsPinGetDevice function%20 RELEASE:%20(12/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>

