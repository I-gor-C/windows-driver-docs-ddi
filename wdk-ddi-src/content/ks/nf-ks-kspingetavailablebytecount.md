---
UID: NF.ks.KsPinGetAvailableByteCount
title: KsPinGetAvailableByteCount
author: windows-driver-content
description: The KsPinGetAvailableByteCount routine outputs the number of bytes of input data ahead of the leading edge and the number of bytes of output buffer ahead of the leading edge, both for the queue of a caller-specified pin.
old-location: stream\kspingetavailablebytecount.htm
ms.assetid: e3669f11-7284-4f65-b814-624337e7fa7f
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: stream
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
ms.keywords: KsPinGetAvailableByteCount
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

### -param <i>Pin</i> [in]

<dd>
<p>A pointer to a <a href="https://msdn.microsoft.com/library/windows/hardware/ff563483">KSPIN</a> structure for which to calculate these queue parameters.</p>
</dd>

### -param <i>InputDataBytes</i> [out, optional]

<dd>
<p>A pointer to a LONG value in which the routine returns the number of input data bytes ahead of the leading edge. Caller sets to <b>NULL</b> if this value is not requested.</p>
</dd>

### -param <i>OutputBufferBytes</i> [out, optional]

<dd>
<p>A pointer to  a LONG value in which the routine returns the number of output buffer bytes ahead of the leading edge. Caller sets to <b>NULL</b> if this value is not requested.</p>
</dd>
</dl>

## -returns
<p>Returns STATUS_SUCCESS if the requested count(s) have been retrieved. A nonsuccessful return status indicates that <i>Pin</i> does not have an associated queue.</p>

## -remarks
<p>Noninplace pins should use <i>InputDataBytes</i> for input pins and <i>OutputBufferBytes</i> for output pins.</p>

<p>The results of this call are not guaranteed to be safe unless either the processing mutex is held at call-time, or the caller has privately synchronized before calling the routine. To private synchronize, ensure that the pin does not transition from Acquire to Stop while the routine is executing. See <a href="NULL">Processing Mutex in AVStream</a>.</p>

<p>Also note that in-place transform can supply input and output counts.</p>

<p>In Windows XP and DirectX 8.0, the <i>InputDataBytes</i> count is not valid unless frames that the filter receives are full.</p>

<p>For additional information, see <a href="NULL">Leading and Trailing Edge Stream Pointers</a>.</p>

<p>Noninplace pins should use <i>InputDataBytes</i> for input pins and <i>OutputBufferBytes</i> for output pins.</p>

<p>The results of this call are not guaranteed to be safe unless either the processing mutex is held at call-time, or the caller has privately synchronized before calling the routine. To private synchronize, ensure that the pin does not transition from Acquire to Stop while the routine is executing. See <a href="NULL">Processing Mutex in AVStream</a>.</p>

<p>Also note that in-place transform can supply input and output counts.</p>

<p>In Windows XP and DirectX 8.0, the <i>InputDataBytes</i> count is not valid unless frames that the filter receives are full.</p>

<p>For additional information, see <a href="NULL">Leading and Trailing Edge Stream Pointers</a>.</p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff563534">KSPIN_DESCRIPTOR_EX</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff563513">KsPinGetLeadingEdgeStreamPointer</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff563518">KsPinGetTrailingEdgeStreamPointer</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff567139">KSSTREAM_POINTER</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff563535">KSPIN_DISPATCH</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff556351">AVStrMiniPinProcess</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff562524">KsFilterAcquireProcessingMutex</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff563488">KsPinAcquireProcessingMutex</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff562552">KsFilterReleaseProcessingMutex</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff563527">KsPinReleaseProcessingMutex</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [stream\stream]:%20KsPinGetAvailableByteCount routine%20 RELEASE:%20(10/25/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
