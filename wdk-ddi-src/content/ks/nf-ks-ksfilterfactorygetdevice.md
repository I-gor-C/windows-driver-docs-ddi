---
UID: NF.ks.KsFilterFactoryGetDevice
title: KsFilterFactoryGetDevice
author: windows-driver-content
description: The KsFilterFactoryGetDevice function returns the AVStream device to which FilterFactory belongs.
old-location: stream\ksfilterfactorygetdevice.htm
old-project: stream
ms.assetid: e5b7b014-3e06-49f2-8ccd-45d74592e349
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: KsFilterFactoryGetDevice
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
req.alt-api: KsFilterFactoryGetDevice
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
req.iface: 
---

# KsFilterFactoryGetDevice function



## -description
<p>The<b> KsFilterFactoryGetDevice </b>function returns the AVStream device to which <i>FilterFactory </i>belongs.</p>


## -syntax

````
PKSDEVICE __inline KsFilterFactoryGetDevice(
  _In_ PKSFILTERFACTORY FilterFactory
);
````


## -parameters
<dl>

### -param <i>FilterFactory</i> [in]

<dd>
<p>A pointer to a <a href="https://msdn.microsoft.com/library/windows/hardware/ff562530">KSFILTERFACTORY</a> structure for which to find the corresponding AVStream device.</p>
</dd>
</dl>

## -returns
<p>Returns a pointer to a <a href="https://msdn.microsoft.com/library/windows/hardware/ff561681">KSDEVICE</a> structure representing the AVStream device to which <i>FilterFactory</i> belongs.</p>

## -remarks
<p>This call is an inline function call to <a href="https://msdn.microsoft.com/library/windows/hardware/ff562615">KsGetDevice</a>.</p>

<p>For more information about the AVStream object hierarchy, see  <a href="NULL">AVStream Overview</a>.</p>

<p>This call is an inline function call to <a href="https://msdn.microsoft.com/library/windows/hardware/ff562615">KsGetDevice</a>.</p>

<p>For more information about the AVStream object hierarchy, see  <a href="NULL">AVStream Overview</a>.</p>

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
<p>Available in Microsoft Windows XP and later operating systems and DirectX 8.0 and later DirectX versions.</p>
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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff562530">KSFILTERFACTORY</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff561681">KSDEVICE</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff562615">KsGetDevice</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [stream\stream]:%20KsFilterFactoryGetDevice function%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
