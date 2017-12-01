---
UID: NF.portcls.IPortWavePciStream.GetMapping
title: IPortWavePciStream::GetMapping
author: windows-driver-content
description: The GetMapping method obtains a mapping from the port driver and associates a tag with the mapping.
old-location: audio\iportwavepcistream_getmapping.htm
old-project: audio
ms.assetid: f0d4f266-6a43-4523-bf1d-3dda1fc9a5b8
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: IPortWavePciStream, GetMapping, IPortWavePciStream::GetMapping
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
req.alt-api: IPortWavePciStream.GetMapping
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
req.irql: <=DISPATCH_LEVEL
req.iface: IPortWavePciStream
---

# IPortWavePciStream::GetMapping method



## -description
<p>The <code>GetMapping</code> method obtains a mapping from the port driver and associates a tag with the mapping.</p>


## -syntax

````
NTSTATUS GetMapping(
  [in]  PVOID             Tag,
  [out] PPHYSICAL_ADDRESS PhysicalAddress,
  [out] PVOID             *VirtualAddress,
  [out] PULONG            ByteCount,
  [out] PULONG            Flags
);
````


## -parameters
<dl>

### -param <i>Tag</i> [in]

<dd>
<p>Specifies a tag value to associate with the mapping. The port driver can use this tag in a subsequent <a href="audio.iminiportwavepcistream_revokemappings">IMiniportWavePciStream::RevokeMappings</a> call to identify the mapping in the list of mappings to be revoked. The miniport driver uses the tag to identify the mapping in the <a href="audio.iportwavepcistream_releasemapping">IPortWavePciStream::ReleaseMapping</a> call that releases the mapping.</p>
</dd>

### -param <i>PhysicalAddress</i> [out]

<dd>
<p>Output pointer for the physical address. This parameter points to a caller-allocated pointer variable into which the method writes the physical address of the mapping. Specify a valid, non-NULL pointer value for this parameter.</p>
</dd>

### -param <i>VirtualAddress</i> [out]

<dd>
<p>Output pointer for the virtual address. This parameter points to a caller-allocated pointer variable into which the method writes the virtual address of the mapping. Specify a valid, non-NULL pointer value for this parameter.</p>
</dd>

### -param <i>ByteCount</i> [out]

<dd>
<p>Output pointer for the byte count. This parameter points to a caller-allocated ULONG variable into which the method writes the number of bytes in the mapping. Specify a valid, non-NULL pointer value for this parameter.</p>
</dd>

### -param <i>Flags</i> [out]

<dd>
<p>Output pointer for the status flag. This parameter points to a caller-allocated ULONG variable into which the method writes a status flag. Specify a valid, non-NULL pointer value for this parameter. A nonzero flag value indicates that the mapping acquired in this call is the last mapping in an I/O packet. This flag can be used to signal that the hardware should interrupt the miniport driver when it is done with this mapping. In response to the interrupt, the miniport driver can obtain new mappings to deliver to the hardware. The miniport driver is not obligated to use the flag in this way.</p>
</dd>
</dl>

## -returns
<p><code>GetMapping</code> returns STATUS_SUCCESS if the call was successful. Otherwise, the method returns an appropriate error code. The following table shows some of the possible return status codes.</p><dl>
<dt><b>STATUS_NOT_FOUND</b></dt>
</dl><p>A mapping is not immediately available, but the port driver will call <a href="audio.iminiportwavepcistream_mappingavailable">IMiniportWavePciStream::MappingAvailable</a> when a mapping does become available.</p>

<p> </p>

## -remarks
<p>Mappings obtained through the <code>GetMapping</code> method should be released by calling <a href="audio.iportwavepcistream_releasemapping">IPortWavePciStream::ReleaseMapping</a> unless they are revoked by the port driver. The port driver can revoke mappings by calling the stream's <a href="audio.iminiportwavepcistream_revokemappings">IMiniportWavePciStream::RevokeMappings</a> method.</p>

<p>The buffer storage for a stream that is played back through a miniport driver's rendering pin is attached to one or more IRPs. Each IRP contains a portion of the buffer storage for the stream. Each IRP's buffer storage is contiguous in virtual memory, but the memory pages that comprise the buffer do not in general map to contiguous locations in physical memory. Although a driver can use programmed I/O to access the buffer through its mapping into virtual memory, a DMA controller requires physical mappings instead.</p>

<p>The WavePci port driver uses the <code>GetMapping</code> method to expose the buffer to the miniport driver as a sequence of physical mappings. A typical mapping is one memory page or less in size, although a mapping can exceed the page size if two or more pages happen to occupy adjacent locations in physical memory.</p>

<p>The initial call to <code>GetMapping</code> outputs the mapping at the beginning of the buffer. Each successive call to <code>GetMapping</code> presents the next sequential mapping in the buffer. After reaching the end of the buffer, the next <code>GetMapping</code> call outputs the mapping at the beginning of the buffer and the mapping sequence repeats.</p>

<p>The kernel-mode virtual-memory address of the mapping is output through the <i>VirtualAddress</i> parameter. The miniport driver uses this address to access the mapping under direct program control. The page that contains the mapping is locked and no page fault can occur when the driver accesses the mapping. The audio device's bus-master DMA controller uses the address that is output through the <i>PhysicalAddress</i> parameter to access the mapping.</p>

<p>The <i>Tag</i> parameter is a PVOID value that the caller chooses to uniquely identify the mapping:</p>

<p>The port driver might use this tag to identify the mapping in a subsequent call to <b>IMiniportWavePciStream::RevokeMappings</b>.</p>

<p>The miniport driver can use this tag to identify the mapping in a subsequent call to <b>IPortWavePciStream::ReleaseMapping</b>.</p>

<p>Although <i>Tag</i> is defined to be of type PVOID, the port driver never attempts to use this value as a pointer and does not require that it be a valid pointer.</p>

<p>A typical WavePci miniport driver maintains a record of each mapping that it receives. The tag might be a pointer to a record or an index into an array of records, for example, depending on the implementation. The only requirement for a tag is that it be a value that can be cast to type PVOID.</p>

<p>The <i>Flags</i> parameter indicates whether the call to <code>GetMapping</code> retrieved the final mapping in the portion of the audio data buffer that is attached to the current mapping IRP. When <i>Flags</i> indicates that a mapping is the last mapping in an IRP, a miniport driver can arm a hardware interrupt to fire when the miniport driver finishes playing that mapping. When the interrupt fires, this event informs the miniport driver that it needs to acquire more mappings to add to its DMA queue. The <i>Flags</i> parameter is typically used by a miniport driver that manages a single playback stream from the <a href="audio.kernel_mode_wdm_audio_components#kmixer_system_driver#kmixer_system_driver">KMixer system driver</a>. KMixer uses several mapping IRPs (a minimum of three in the current KMixer implementation) to buffer a single playback stream. Thus, if the miniport driver generates a hardware interrupt each time the DMA controller finishes with the final mapping in an IRP, interrupts should occur frequently enough to keep the DMA queue from starving.</p>

<p>The <i>Flags</i> parameter is typically ignored by miniport drivers that manage one or more DirectSound hardware-accelerated streams (see <a href="NULL">DirectSound Hardware Acceleration in WDM Audio</a>). In the case of a DirectSound buffer, the entire buffer can be attached to a single IRP. If the buffer is large and the miniport driver schedules a hardware interrupt only when it reaches the end of the buffer, interrupts will occur so far apart that the DMA queue might starve. In addition, if the driver is managing a large number of streams, scheduling a hardware interrupt each time the <i>Flags</i> parameter signals a final-mapping condition on a stream might generate so many interrupts that performance can be degraded. In these circumstances, the miniport driver should not rely on hardware interrupts to acquire mappings. Instead, it should schedule timer DPCs to occur at regular intervals to acquire mappings.</p>

<p>A miniport driver is most likely to call <code>GetMapping</code> during a call to the miniport stream object's <b>SetState</b>, <b>Service</b>, or <b>MappingAvailable</b> method (see <a href="..\portcls\nn-portcls-iminiportwavepcistream.md">IMiniportWavePciStream</a>).</p>

<p>To avoid potential deadlocks, the adapter driver must avoid holding a spin lock during its call to <code>GetMapping</code>. See the ac97 sample audio driver in the Microsoft Windows Driver Kit (WDK) for a code example that uses a spin lock to serialize accesses to shared data structures and peripherals in a multiprocessor system. The sample code calls <a href="..\wdm\nf-wdm-kereleasespinlock.md">KeReleaseSpinLock</a> before calling <code>GetMapping</code> and calls <a href="..\wdm\nf-wdm-keacquirespinlock.md">KeAcquireSpinLock</a> after calling <code>GetMapping</code>. Between the calls to release and acquire the spin lock, the driver thread must not assume that it has exclusive access to the data or peripherals that are guarded by the spin lock. The <a href="https://msdn.microsoft.com/library/windows/hardware/ff557262">Driver Verifier</a> tool checks for active spin locks during calls to <code>GetMapping</code>; if it detects one, it generates a 0xC4 (deadlock detection) bug check.</p>

<p>Although the size of a typical mapping is one memory page or less, a single mapping can exceed the page size if a portion of an audio buffer happens to occupy two or more contiguous pages in physical memory. Larger mappings can create problems for DMA hardware with design flaws that limit the block size. For example, if a DMA controller can handle a maximum block size of a single page, and <code>GetMapping</code> outputs a mapping that is larger than a page, the miniport driver must split the mapping into smaller blocks that the DMA hardware can handle. If the resulting number of blocks exceeds the number of available map registers in the DMA hardware, the driver cannot queue all of the blocks in a single scatter/gather DMA operation. When this occurs, the driver must keep track of the unqueued portion of the mapping and initiate DMA transfers of the remaining blocks at a later time when additional map registers become available.</p>

<p>In Windows 98/Me, Windows 2000, Windows XP, and Windows Server 2003, the <code>GetMapping</code> method never outputs a mapping that spans more than 16 pages. This limit might change in future Windows releases.</p>

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
<p>&lt;=DISPATCH_LEVEL</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\portcls\nn-portcls-iportwavepcistream.md">IPortWavePciStream</a>
</dt>
<dt>
<a href="audio.iminiportwavepcistream_mappingavailable">IMiniportWavePciStream::MappingAvailable</a>
</dt>
<dt>
<a href="audio.iminiportwavepcistream_revokemappings">IMiniportWavePciStream::RevokeMappings</a>
</dt>
<dt>
<a href="audio.iminiportwavepcistream_getallocatorframing">IMiniportWavePciStream::GetAllocatorFraming</a>
</dt>
<dt>
<a href="audio.iportwavepcistream_releasemapping">IPortWavePciStream::ReleaseMapping</a>
</dt>
<dt>
<a href="..\wdm\nf-wdm-kereleasespinlock.md">KeReleaseSpinLock</a>
</dt>
<dt>
<a href="..\wdm\nf-wdm-keacquirespinlock.md">KeAcquireSpinLock</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [audio\audio]:%20IPortWavePciStream::GetMapping method%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
