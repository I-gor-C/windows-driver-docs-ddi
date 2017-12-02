---
UID: NF.ks.KsDiscard
title: KsDiscard
author: windows-driver-content
description: The KsDiscard macro removes a given item from an object bag.
old-location: stream\ksdiscard.htm
old-project: stream
ms.assetid: cbd1cd9b-c3bd-4827-88e6-4b80d6ba7320
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: KsDiscard
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
req.iface: 
---

# KsDiscard function



## -description
<p>The<b> KsDiscard </b>macro removes a given item from an object bag.</p>


## -syntax

````
ULONG KsDiscard(
  _In_ KSxxx Object,
  _In_ PVOID Pointer
);
````


## -parameters
<dl>

### -param Object [in]

<dd>
<p>The item pointed to by <i>Pointer</i> is removed from the object bag associated with this object. Can be of type <a href="..\ks\ns-ks--ksdevice.md">KSDEVICE</a>, <a href="..\ks\ns-ks--ksfilterfactory.md">KSFILTERFACTORY</a>, <a href="..\ks\ns-ks--ksfilter.md">KSFILTER</a>, or <a href="..\ks\ns-ks--kspin.md">KSPIN</a>.</p>
</dd>

### -param Pointer [in]

<dd>
<p>A pointer to the item to be removed from the requested object's bag.</p>
</dd>
</dl>

## -returns
<p>Returns the number of references on <i>Item</i>. A return value of zero indicates that the item pointed to by <i>Pointer</i> was not in the object bag of <i>Object</i> at call-time.</p>

<p>A return value of one indicates that the item was successfully removed from the object bag and that it was not in any other object bag. AVStream frees the item using either <a href="..\wdm\nf-wdm-exfreepool.md">ExFreePool</a> or the <i>Free</i> method specified at <a href="..\ks\nf-ks-ksadditemtoobjectbag.md">KsAddItemToObjectBag</a> call-time.</p>

<p>A return value greater than one indicates that the item is present in another object bag and that there are still references on it. In this case, AVStream removed the item from the object bag but did not free it.</p>

## -remarks
<p>This function is implemented as a C-style preprocessing macro in the <i>Ks.h</i> header.</p>

<p><b>KsDiscard</b> calls <a href="..\ks\nf-ks-ksremoveitemfromobjectbag.md">KsRemoveItemFromObjectBag</a>, passing the object bag associated with <i>Object</i> (<i>Object -&gt; Bag</i>), the item specified by <i>Pointer</i>, and <b>TRUE</b> for the <i>Free</i> parameter. </p>

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
<p>Library</p>
</th>
<td width="70%">
<dl>
<dt>Ks.lib</dt>
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
<a href="..\ks\nf-ks-ksremoveitemfromobjectbag.md">KsRemoveItemFromObjectBag</a>
</dt>
<dt>
<a href="..\ks\ns-ks--ksdevice.md">KSDEVICE</a>
</dt>
<dt>
<a href="..\ks\ns-ks--ksfilterfactory.md">KSFILTERFACTORY</a>
</dt>
<dt>
<a href="..\ks\ns-ks--ksfilter.md">KSFILTER</a>
</dt>
<dt>
<a href="..\ks\ns-ks--kspin.md">KSPIN</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [stream\stream]:%20KsDiscard function%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
