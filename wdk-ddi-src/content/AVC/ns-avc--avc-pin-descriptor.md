---
UID: NS.avc._AVC_PIN_DESCRIPTOR
title: AVC_PIN_DESCRIPTOR
author: windows-driver-content
description: The AVC_PIN_DESCRIPTOR structure describes a pin on an AV/C subunit device.
old-location: stream\avc_pin_descriptor.htm
ms.assetid: 6d404c47-01ae-496c-8252-32f180cf0fd3
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: stream
req.header: avc.h
req.include-header: Avc.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: AVC_PIN_DESCRIPTOR
req.alt-loc: avc.h
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
ms.keywords: AVC_PIN_DESCRIPTOR, AVC_PIN_DESCRIPTOR, *PAVC_PIN_DESCRIPTOR
req.iface: 
---

# AVC_PIN_DESCRIPTOR structure



## -description
<p>The AVC_PIN_DESCRIPTOR structure describes a pin on an AV/C subunit device.</p>


## -syntax

````
typedef struct _AVC_PIN_DESCRIPTOR {
  ULONG                  PinId;
  KSPIN_DESCRIPTOR       PinDescriptor;
  PFNAVCINTERSECTHANDLER IntersectHandler;
  PVOID                  Context;
} AVC_PIN_DESCRIPTOR, *PAVC_PIN_DESCRIPTOR;
````


## -struct-fields
<dl>

### -field <b>PinId</b>

<dd>
<p>Specifies the offset (or ID) of the pin for which information is to be retrieved.</p>
</dd>

### -field <b>PinDescriptor</b>

<dd>
<p>Specifies a KSPIN_DESCRIPTOR structure. This structure is allocated in the nonpaged pool. The subunit driver must not free this pointer.</p>
</dd>

### -field <b>IntersectHandler</b>

<dd>
<p>An optional output parameter specifying a data range intersect handler associated with the <b>DataRanges</b> member of the <b>PinDescriptor</b> member.</p>
</dd>

### -field <b>Context</b>

<dd>
<p>An optional output parameter specifying a value to be passed to the <b>IntersectHandler</b> when it is called during format negotiation. For more information about what an intersect handler is, see <a href="https://msdn.microsoft.com/44281574-8258-47a3-857d-fd44bb949f17">DataRange Intersections in AVStream</a>.</p>
</dd>
</dl>

## -remarks
<p>This structure is used with the <a href="https://msdn.microsoft.com/library/windows/hardware/ff554160">AVC_FUNCTION_GET_PIN_DESCRIPTOR</a> function code.</p>

<p>This structure is used only as a member inside the AVC_MULTIFUNC_IRB structure. It is not used by itself.</p>

<p>See <a href="https://msdn.microsoft.com/3b4ec139-ff01-40bd-8e29-92f554180585">How to Use Avc.sys</a> For information about building and sending an AV/C command.</p>

<p>A description of the members of the <b>KSPIN_DESCRIPTOR</b> structure used in AVC_PIN_DESCRIPTOR follows:</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Avc.h (include Avc.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff556379">AV/C Intersect Handler</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff563533">KSPIN_DESCRIPTOR</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff554177">AVC_MULTIFUNC_IRB</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [stream\stream]:%20AVC_PIN_DESCRIPTOR structure%20 RELEASE:%20(10/25/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
