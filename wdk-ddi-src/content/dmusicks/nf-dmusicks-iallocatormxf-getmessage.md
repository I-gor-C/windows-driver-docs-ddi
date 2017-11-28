---
UID: NF.dmusicks.IAllocatorMXF.GetMessage
title: IAllocatorMXF::GetMessage
author: windows-driver-content
description: The GetMessage method serves as the retrieval point for any DirectMusic kernel-mode component that utilizes the port driver's allocator to reuse DMUS_KERNEL_EVENT structures.
old-location: audio\iallocatormxf_getmessage.htm
old-project: audio
ms.assetid: d5b56926-bcfb-4411-b24d-cc0758852510
ms.author: windowsdriverdev
ms.date: 11/21/2017
ms.keywords: IAllocatorMXF, GetMessage, IAllocatorMXF::GetMessage
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: dmusicks.h
req.include-header: Dmusicks.h
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IAllocatorMXF.GetMessage
req.alt-loc: dmusicks.h
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
req.iface: IAllocatorMXF
---

# IAllocatorMXF::GetMessage method



## -description
<p>The <code>GetMessage</code> method serves as the retrieval point for any DirectMusic kernel-mode component that utilizes the port driver's allocator to reuse <a href="https://msdn.microsoft.com/library/windows/hardware/ff536340">DMUS_KERNEL_EVENT</a> structures.</p>


## -syntax

````
NTSTATUS GetMessage(
  [out] PDMUS_KERNEL_EVENT *ppDMKEvt
);
````


## -parameters
<dl>

### -param <i>ppDMKEvt</i> [out]

<dd>
<p>Output pointer for the MIDI event. This parameter points to a caller-allocated pointer variable into which the method writes a pointer to the event structure being retrieved from the allocator. The structure itself is empty (zeroed by the allocator).</p>
</dd>
</dl>

## -returns
<p><code>GetMessage</code> returns S_OK if the call was successful. Otherwise, the method returns an appropriate error code.</p>

## -remarks
<p>The miniport driver uses the <code>GetMessage</code> method to retrieve event structures for MIDI rendering and capture. This method retrieves <a href="https://msdn.microsoft.com/library/windows/hardware/ff536340">DMUS_KERNEL_EVENT</a> structures from the same pool that <a href="https://msdn.microsoft.com/library/windows/hardware/ff536791">IMXF::PutMessage</a> puts them into when it discards them to the allocator.</p>

<p>In the case of a MIDI capture stream, the port driver retrieves capture events from the miniport driver when prompted by the usual Service DPC.</p>

<p>For more information about the allocator, see <a href="NULL">Allocator</a>.</p>

<p>The miniport driver uses the <code>GetMessage</code> method to retrieve event structures for MIDI rendering and capture. This method retrieves <a href="https://msdn.microsoft.com/library/windows/hardware/ff536340">DMUS_KERNEL_EVENT</a> structures from the same pool that <a href="https://msdn.microsoft.com/library/windows/hardware/ff536791">IMXF::PutMessage</a> puts them into when it discards them to the allocator.</p>

<p>In the case of a MIDI capture stream, the port driver retrieves capture events from the miniport driver when prompted by the usual Service DPC.</p>

<p>For more information about the allocator, see <a href="NULL">Allocator</a>.</p>

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
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Dmusicks.h (include Dmusicks.h)</dt>
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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff536491">IAllocatorMXF</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff536340">DMUS_KERNEL_EVENT</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff536791">IMXF::PutMessage</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [audio\audio]:%20IAllocatorMXF::GetMessage method%20 RELEASE:%20(11/21/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
