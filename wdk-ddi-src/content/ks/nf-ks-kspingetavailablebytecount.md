---
UID: NF.ks.KsPinGetAvailableByteCount
title: KsPinGetAvailableByteCount
author: windows-driver-content
description: The KsPinGetAvailableByteCount routine outputs the number of bytes of input data ahead of the leading edge and the number of bytes of output buffer ahead of the leading edge, both for the queue of a caller-specified pin.
old-location: stream\kspingetavailablebytecount.htm
old-project: stream
ms.assetid: e3669f11-7284-4f65-b814-624337e7fa7f
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: KsPinGetAvailableByteCount
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: ks.h
req.include-header: Ks.h
req.target-type: Universal
req.target-min-winverclnt: Available in Microsoft Windows XP and later operating systems and DirectX 8.0 and later DirectX versions.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: KsPinGetAvailableByteCount
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
req.irql: 
req.iface: 
---

# KsPinGetAvailableByteCount function



## -description
<p>The<b> KsPinGetAvailableByteCount</b> routine outputs the number of bytes of input data ahead of the leading edge and the number of bytes of output buffer ahead of the leading edge, both for the queue of a caller-specified pin.</p>


## -syntax

````
NTSTATUS KsPinGetAvailableByteCount(
  _In_      PKSPIN Pin,
  _Out_opt_ PLONG  InputDataBytes,
  _Out_opt_ PLONG  OutputBufferBytes
);
````


## -parameters
<dl>

### -param Pin [in]

<dd>
<p>A pointer to a <a href="..\ks\ns-ks--kspin.md">KSPIN</a> structure for which to calculate these queue parameters.</p>
</dd>

### -param InputDataBytes [out, optional]

<dd>
<p>A pointer to a LONG value in which the routine returns the number of input data bytes ahead of the leading edge. Caller sets to <b>NULL</b> if this value is not requested.</p>
</dd>

### -param OutputBufferBytes [out, optional]

<dd>
<p>A pointer to  a LONG value in which the routine returns the number of output buffer bytes ahead of the leading edge. Caller sets to <b>NULL</b> if this value is not requested.</p>
</dd>
</dl>

## -returns
<p>Returns STATUS_SUCCESS if the requested count(s) have been retrieved. A nonsuccessful return status indicates that <i>Pin</i> does not have an associated queue.</p>

## -remarks
<p>Noninplace pins should use <i>InputDataBytes</i> for input pins and <i>OutputBufferBytes</i> for output pins.</p>

<p>The results of this call are not guaranteed to be safe unless either the processing mutex is held at call-time, or the caller has privately synchronized before calling the routine. To private synchronize, ensure that the pin does not transition from Acquire to Stop while the routine is executing. See <a href="https://msdn.microsoft.com/dd84fe3f-352e-4641-99d7-792ccecb0b40">Processing Mutex in AVStream</a>.</p>

<p>Also note that in-place transform can supply input and output counts.</p>

<p>In Windows XP and DirectX 8.0, the <i>InputDataBytes</i> count is not valid unless frames that the filter receives are full.</p>

<p>For additional information, see <a href="https://msdn.microsoft.com/73ab974f-8034-421f-980a-2393d84ec54c">Leading and Trailing Edge Stream Pointers</a>.</p>

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
</table>

## -see-also
<dl>
<dt>
<a href="..\ks\ns-ks--kspin-descriptor-ex.md">KSPIN_DESCRIPTOR_EX</a>
</dt>
<dt>
<a href="..\ks\nf-ks-kspingetleadingedgestreampointer.md">KsPinGetLeadingEdgeStreamPointer</a>
</dt>
<dt>
<a href="..\ks\nf-ks-kspingettrailingedgestreampointer.md">KsPinGetTrailingEdgeStreamPointer</a>
</dt>
<dt>
<a href="..\ks\ns-ks--ksstream-pointer.md">KSSTREAM_POINTER</a>
</dt>
<dt>
<a href="..\ks\ns-ks--kspin-dispatch.md">KSPIN_DISPATCH</a>
</dt>
<dt>
<a href="stream.avstrminipinprocess">AVStrMiniPinProcess</a>
</dt>
<dt>
<a href="..\ks\nf-ks-ksfilteracquireprocessingmutex.md">KsFilterAcquireProcessingMutex</a>
</dt>
<dt>
<a href="..\ks\nf-ks-kspinacquireprocessingmutex.md">KsPinAcquireProcessingMutex</a>
</dt>
<dt>
<a href="..\ks\nf-ks-ksfilterreleaseprocessingmutex.md">KsFilterReleaseProcessingMutex</a>
</dt>
<dt>
<a href="..\ks\nf-ks-kspinreleaseprocessingmutex.md">KsPinReleaseProcessingMutex</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [stream\stream]:%20KsPinGetAvailableByteCount routine%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
