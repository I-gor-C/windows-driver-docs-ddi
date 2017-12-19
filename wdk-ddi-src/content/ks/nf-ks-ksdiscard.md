---
UID: NF.ks.KsDiscard
title: KsDiscard macro
author: windows-driver-content
description: The KsDiscard macro removes a given item from an object bag.
old-location: stream\ksdiscard.htm
old-project: stream
ms.assetid: cbd1cd9b-c3bd-4827-88e6-4b80d6ba7320
ms.author: windowsdriverdev
ms.date: 12/14/2017
ms.keywords: KsDiscard
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: macro
req.header: ks.h
req.include-header: Ks.h
req.target-type: Desktop
req.target-min-winverclnt: Available in Microsoft Windows XP and later operating systems and DirectX 8.0 and later DirectX versions.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: KsDiscard
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
req.irql: PASSIVE_LEVEL
---

# KsDiscard macro



## -description
The<b> KsDiscard </b>macro removes a given item from an object bag.



## -syntax

````
ULONG KsDiscard(
  _In_ KSxxx Object,
  _In_ PVOID Pointer
);
````


## -parameters

### -param Object [in]

The item pointed to by <i>Pointer</i> is removed from the object bag associated with this object. Can be of type <a href="stream.ksdevice">KSDEVICE</a>, <a href="stream.ksfilterfactory">KSFILTERFACTORY</a>, <a href="stream.ksfilter">KSFILTER</a>, or <a href="stream.kspin">KSPIN</a>.


### -param Pointer [in]

A pointer to the item to be removed from the requested object's bag.


## -remarks
This function is implemented as a C-style preprocessing macro in the <i>Ks.h</i> header.

<b>KsDiscard</b> calls <a href="stream.ksremoveitemfromobjectbag">KsRemoveItemFromObjectBag</a>, passing the object bag associated with <i>Object</i> (<i>Object -&gt; Bag</i>), the item specified by <i>Pointer</i>, and <b>TRUE</b> for the <i>Free</i> parameter. 


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
Library

</th>
<td width="70%">
<dl>
<dt>Ks.lib</dt>
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
<a href="stream.ksremoveitemfromobjectbag">KsRemoveItemFromObjectBag</a>
</dt>
<dt>
<a href="stream.ksdevice">KSDEVICE</a>
</dt>
<dt>
<a href="stream.ksfilterfactory">KSFILTERFACTORY</a>
</dt>
<dt>
<a href="stream.ksfilter">KSFILTER</a>
</dt>
<dt>
<a href="stream.kspin">KSPIN</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [stream\stream]:%20KsDiscard function%20 RELEASE:%20(12/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>

