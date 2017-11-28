---
UID: NF.portcls.PcCreateContentMixed
title: PcCreateContentMixed
author: windows-driver-content
description: The PcCreateContentMixed function computes the DRM content rights for a composite stream containing mixed content from some number of KS audio streams.
old-location: audio\pccreatecontentmixed.htm
old-project: audio
ms.assetid: 9b916d43-26ab-4354-8537-2d4789c5fb52
ms.author: windowsdriverdev
ms.date: 11/21/2017
ms.keywords: PcCreateContentMixed
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: portcls.h
req.include-header: Portcls.h
req.target-type: Universal
req.target-min-winverclnt: The PortCls system driver implements the PcCreateContentMixed function in Microsoft Windows XP and later operating systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: PcCreateContentMixed
req.alt-loc: Portcls.lib,Portcls.dll
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Portcls.lib
req.dll: 
req.irql: 
req.iface: 
---

# PcCreateContentMixed function



## -description
<p>The <b>PcCreateContentMixed</b> function computes the DRM content rights for a composite stream containing mixed content from some number of KS audio streams. Note that this function call is identical in operation to the <a href="https://msdn.microsoft.com/library/windows/hardware/ff536348">DrmCreateContentMixed</a> function, and its parameter definitions and return value are also identical.</p>


## -syntax

````
PORTCLASSAPI NTSTATUS NTAPI  PcCreateContentMixed(void);
````


## -parameters


## -returns
<p>See return value definition in <a href="https://msdn.microsoft.com/library/windows/hardware/ff536348">DrmCreateContentMixed</a>.</p>

<p>See return value definition in <a href="https://msdn.microsoft.com/library/windows/hardware/ff536348">DrmCreateContentMixed</a>.</p>

<p>See return value definition in <a href="https://msdn.microsoft.com/library/windows/hardware/ff536348">DrmCreateContentMixed</a>.</p>

## -remarks
<p>For more information, see the comments in <a href="https://msdn.microsoft.com/library/windows/hardware/ff536348">DrmCreateContentMixed</a>.</p>

<p>For more information, see the comments in <a href="https://msdn.microsoft.com/library/windows/hardware/ff536348">DrmCreateContentMixed</a>.</p>

<p>For more information, see the comments in <a href="https://msdn.microsoft.com/library/windows/hardware/ff536348">DrmCreateContentMixed</a>.</p>

<p>For more information, see the comments in <a href="https://msdn.microsoft.com/library/windows/hardware/ff536348">DrmCreateContentMixed</a>.</p>

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
<p>Version</p>
</th>
<td width="70%">
<p>The PortCls system driver implements the PcCreateContentMixed function in Microsoft Windows XP and later operating systems.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Portcls.h (include Portcls.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Library</p>
</th>
<td width="70%">
<dl>
<dt>Portcls.lib</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff536348">DrmCreateContentMixed</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [audio\audio]:%20PcCreateContentMixed function%20 RELEASE:%20(11/21/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
