---
UID: NF.portcls.IMiniportWavePciStream.RevokeMappings
title: IMiniportWavePciStream::RevokeMappings
author: windows-driver-content
description: The RevokeMappings method revokes mappings that were previously obtained through IPortWavePciStream::GetMapping.
old-location: audio\iminiportwavepcistream_revokemappings.htm
old-project: audio
ms.assetid: a6534917-5fe6-449b-8e85-398d26730f66
ms.author: windowsdriverdev
ms.date: 11/21/2017
ms.keywords: IMiniportWavePciStream, RevokeMappings, IMiniportWavePciStream::RevokeMappings
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: portcls.h
req.include-header: Portcls.h
req.target-type: Universal
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IMiniportWavePciStream.RevokeMappings
req.alt-loc: portcls.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: DISPATCH_LEVEL
req.iface: IMiniportWavePciStream
---

# IMiniportWavePciStream::RevokeMappings method



## -description
<p>The <code>RevokeMappings</code> method revokes mappings that were previously obtained through <a href="https://msdn.microsoft.com/library/windows/hardware/ff536909">IPortWavePciStream::GetMapping</a>.</p>


## -syntax

````
NTSTATUS RevokeMappings(
  [in]  PVOID  FirstTag,
  [in]  PVOID  LastTag,
  [out] PULONG MappingsRevoked
);
````


## -parameters
<dl>

### -param <i>FirstTag</i> [in]

<dd>
<p>Specifies the tag value that identifies the first mapping that is being revoked.</p>
</dd>

### -param <i>LastTag</i> [in]

<dd>
<p>Specifies the tag value that identifies the last mapping that is being revoked.</p>
</dd>

### -param <i>MappingsRevoked</i> [out]

<dd>
<p>Output pointer for the count of revoked mappings. This parameter points to a ULONG variable into which the method writes the number of mappings actually revoked by the call. This number excludes any mappings in the range <i>FirstTag</i> to <i>LastTag</i> that the miniport driver has already released. Due to synchronization issues, some of the mappings in the range might be released between the time that the port driver determines the list of mappings to be revoked and the call to <code>RevokeMappings</code>. For more information, see the following Remarks section.</p>
</dd>
</dl>

## -returns
<p><code>RevokeMappings</code> returns STATUS_SUCCESS if the call was successful. Otherwise, the method returns an appropriate error code.</p>

## -remarks
<p>The port driver calls <code>RevokeMappings</code> to revoke the stream's mappings when:</p>

<p>An I/O request (IRP) is canceled and the previously mapped memory might no longer be available.</p>

<p>The stream state changes to KSSTATE_STOP (see <a href="https://msdn.microsoft.com/library/windows/hardware/ff566856">KSSTATE</a>) and the device no longer has need for the mappings.</p>

<p>The miniport driver keeps track of the order in which it acquires its mappings from calls to <a href="https://msdn.microsoft.com/library/windows/hardware/ff536909">IPortWavePciStream::GetMapping</a>. The <code>RevokeMapping</code> method revokes all mappings in the sequence that begins with the mapping identified by <i>FirstTag</i> and ends with the mapping identified by <i>LastTag</i>. This includes the mappings identified by <i>FirstTag</i> and <i>LastTag</i> and all mappings in between. The miniport driver revokes each mapping by removing it from the list of available mappings.</p>

<p>The <code>RevokeMapping</code> method can be used to remove a single mapping by setting <i>FirstTag</i> and <i>LastTag</i> to the same value.</p>

<p>The port driver can call <code>RevokeMappings</code> asynchronously with respect to the miniport driver's maintenance operations on the DMA controller's scatter/gather transfer queue. Access to this queue needs to be protected by a synchronization primitive. For example, in the ac97 sample audio driver in the Microsoft Windows Driver Kit (WDK), this is done by surrounding critical code sections with <a href="https://msdn.microsoft.com/library/windows/hardware/ff551917">KeAcquireSpinLock</a> and <a href="https://msdn.microsoft.com/library/windows/hardware/ff553145">KeReleaseSpinLock</a> calls. Because the miniport driver can release mappings asynchronously with respect to the port driver's calls to <code>RevokeMappings</code>, the miniport driver might have previously released (see <a href="https://msdn.microsoft.com/library/windows/hardware/ff536911">IPortWavePciStream::ReleaseMapping</a>) one or more of the mappings specified in the <code>RevokeMappings</code> call.</p>

<p>For more information about mappings, see <a href="NULL">WavePci Latency</a>.</p>

<p>The port driver calls <code>RevokeMappings</code> to revoke the stream's mappings when:</p>

<p>An I/O request (IRP) is canceled and the previously mapped memory might no longer be available.</p>

<p>The stream state changes to KSSTATE_STOP (see <a href="https://msdn.microsoft.com/library/windows/hardware/ff566856">KSSTATE</a>) and the device no longer has need for the mappings.</p>

<p>The miniport driver keeps track of the order in which it acquires its mappings from calls to <a href="https://msdn.microsoft.com/library/windows/hardware/ff536909">IPortWavePciStream::GetMapping</a>. The <code>RevokeMapping</code> method revokes all mappings in the sequence that begins with the mapping identified by <i>FirstTag</i> and ends with the mapping identified by <i>LastTag</i>. This includes the mappings identified by <i>FirstTag</i> and <i>LastTag</i> and all mappings in between. The miniport driver revokes each mapping by removing it from the list of available mappings.</p>

<p>The <code>RevokeMapping</code> method can be used to remove a single mapping by setting <i>FirstTag</i> and <i>LastTag</i> to the same value.</p>

<p>The port driver can call <code>RevokeMappings</code> asynchronously with respect to the miniport driver's maintenance operations on the DMA controller's scatter/gather transfer queue. Access to this queue needs to be protected by a synchronization primitive. For example, in the ac97 sample audio driver in the Microsoft Windows Driver Kit (WDK), this is done by surrounding critical code sections with <a href="https://msdn.microsoft.com/library/windows/hardware/ff551917">KeAcquireSpinLock</a> and <a href="https://msdn.microsoft.com/library/windows/hardware/ff553145">KeReleaseSpinLock</a> calls. Because the miniport driver can release mappings asynchronously with respect to the port driver's calls to <code>RevokeMappings</code>, the miniport driver might have previously released (see <a href="https://msdn.microsoft.com/library/windows/hardware/ff536911">IPortWavePciStream::ReleaseMapping</a>) one or more of the mappings specified in the <code>RevokeMappings</code> call.</p>

<p>For more information about mappings, see <a href="NULL">WavePci Latency</a>.</p>

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
<p>IRQL</p>
</th>
<td width="70%">
<p>DISPATCH_LEVEL</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff536725">IMiniportWavePciStream</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff566856">KSSTATE</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff536909">IPortWavePciStream::GetMapping</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff536911">IPortWavePciStream::ReleaseMapping</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff553145">KeReleaseSpinLock</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff551917">KeAcquireSpinLock</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [audio\audio]:%20IMiniportWavePciStream::RevokeMappings method%20 RELEASE:%20(11/21/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
