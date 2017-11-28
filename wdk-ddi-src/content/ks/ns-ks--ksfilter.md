---
UID: NS.ks._KSFILTER
title: KSFILTER
author: windows-driver-content
description: The KSFILTER structure describes an instantiated filter.
old-location: stream\ksfilter.htm
old-project: stream
ms.assetid: b9233f69-1ddf-4133-afd3-150aef5fc4a0
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: KSFILTER,
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: ks.h
req.include-header: Ks.h
req.target-type: Windows
req.target-min-winverclnt: Available in Microsoft Windows XP and later operating systems and in Microsoft DirectX 8.0 and later versions.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: KSFILTER
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
req.irql: 
req.iface: 
---

# KSFILTER structure



## -description
<p>The KSFILTER structure describes an instantiated filter.</p>


## -syntax

````
typedef struct _KSFILTER {
  const KSFILTER_DESCRIPTOR *Descriptor;
  KSOBJECT_BAG              Bag;
  PVOID                     Context;
} KSFILTER, *PKSFILTER;
````


## -struct-fields
<dl>

### -field <b>Descriptor</b>

<dd>
<p>A pointer to a <a href="https://msdn.microsoft.com/library/windows/hardware/ff562553">KSFILTER_DESCRIPTOR</a> structure that describes the characteristics of this particular filter.</p>
</dd>

### -field <b>Bag</b>

<dd>
<p>This member specifies the KSOBJECT_BAG (equivalent to type PVOID) associated with this filter instance. <a href="NULL">Object Bags</a> are structures used to associate dynamic memory with a specific AVStream object. Anything in the filter object bag is automatically cleaned up when the filter is deleted.</p>
</dd>

### -field <b>Context</b>

<dd>
<p>A pointer that is used by the client to associate context information with the specific filter instance. Typically, such context information is associated in the filter's <b>Create</b> member as defined in the KSFILTER_DISPATCH table for this filter instance. Any dynamically allocated context information should be placed in the object bag with <a href="https://msdn.microsoft.com/library/windows/hardware/ff560941">KsAddItemToObjectBag</a>. <b>Context</b> is initialized to the value of the <b>Context</b> member of the parent <a href="https://msdn.microsoft.com/library/windows/hardware/ff562530">KSFILTERFACTORY</a> at the time the filter is created. See <a href="NULL">AVStream Object Hierarchy</a>.</p>
</dd>
</dl>

## -remarks
<p>Drivers implementing software filters typically associate filter state with the KSFILTER structure. Software filters usually process data within the callback specified by the <b>Process</b> member of the corresponding <a href="https://msdn.microsoft.com/library/windows/hardware/ff562554">KSFILTER_DISPATCH</a> structure.</p>

<p>Hardware filters typically do not use KSFILTER because the focus of the hardware driver is the platform transition: the movement of data between the host and the external hardware. This transition is typically handled by code associated with an AVStream queue object.</p>

<p>Also see <a href="NULL">Object Bags</a>.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Available in Microsoft Windows XP and later operating systems and in Microsoft DirectX 8.0 and later versions.</p>
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
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff562553">KSFILTER_DESCRIPTOR</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff562554">KSFILTER_DISPATCH</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff561025">KsCompletePendingRequest</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff560941">KsAddItemToObjectBag</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [stream\stream]:%20KSFILTER structure%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
